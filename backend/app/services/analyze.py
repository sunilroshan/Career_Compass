from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import List
import json
import os
import re
from dotenv import load_dotenv

load_dotenv()


# Output_Schema
class SkillGapModel(BaseModel):
    skill: str = Field(description="Missing skill name")
    importance: str = Field(description="Priority level: high or medium")
    suggestion: str = Field(description="Actionable suggestion to acquire the skill")


class AnalysisResultModel(BaseModel):
    match_score: float = Field(description="Match score from 0-10")
    match_level: str = Field(description="Match level description")
    skills_matched: List[str] = Field(description="List of matched skills")
    skills_gaps: List[SkillGapModel] = Field(description="List of skill gaps")
    strengths_found: List[str] = Field(description="Candidate's strengths")
    actionable_tip: str = Field(description="One specific actionable tip")


class JobMatchAnalyzer:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.3,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        
        self.analysis_prompt = PromptTemplate(
            input_variables=["job_description", "resume_text"],
            template="""You are an expert career counselor and technical recruiter with deep knowledge of job markets and skill requirements.

Analyze the following job description and candidate's resume to provide a comprehensive match analysis.

JOB DESCRIPTION:
{job_description}

CANDIDATE'S RESUME:
{resume_text}

Your task is to:
1. Calculate an accurate match score (0-10) based on skills alignment, experience, and qualifications
2. Identify all skills that match between the job requirements and resume
3. Identify critical skill gaps and provide actionable suggestions for each
4. Highlight the candidate's key strengths relevant to this role
5. Provide ONE specific, actionable tip to improve their application

Be thorough, accurate, and constructive. Focus on technical skills, soft skills, experience level, and cultural fit indicators.

IMPORTANT: Return ONLY a valid JSON object with this exact structure (no markdown, no code blocks, no explanations):

{{
  "match_score": 7.5,
  "match_level": "Good Match",
  "skills_matched": ["Python", "FastAPI", "React"],
  "skills_gaps": [
    {{
      "skill": "Docker",
      "importance": "high",
      "suggestion": "Learn containerization basics with Docker tutorials"
    }}
  ],
  "strengths_found": ["Strong programming foundation", "Relevant project experience"],
  "actionable_tip": "Emphasize your API development project in your cover letter"
}}

Return ONLY the JSON object above, nothing else."""
        )
    
    async def analyze(self, job_description: str, resume_text: str) -> dict:
        """
        Analyze job-resume match using LangChain
        """
        try:
           
            prompt_text = self.analysis_prompt.format(
                job_description=job_description,
                resume_text=resume_text
            )
            
        
            response = await self.llm.ainvoke(prompt_text)
            
           
            result_text = response.content if hasattr(response, 'content') else str(response)
         
            parsed_result = self._extract_json(result_text)
            
           
            if parsed_result:
                return self._validate_result(parsed_result)
            else:
                return self._get_default_result()
            
        except Exception as e:
            print(f"Analysis error: {str(e)}")
            return self._get_default_result()
    
    def _extract_json(self, text: str) -> dict:
        """Extract JSON from LLM response"""
        try:
           
            text = re.sub(r'```json\s*', '', text)
            text = re.sub(r'```\s*', '', text)
            
         
            start = text.find("{")
            end = text.rfind("}") + 1
            
            if start != -1 and end > start:
                json_str = text[start:end]
                data = json.loads(json_str)
                return data
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {str(e)}")
        except Exception as e:
            print(f"JSON extraction error: {str(e)}")
        
        return None
    
    def _validate_result(self, data: dict) -> dict:
        """Validate and normalize the result"""
        try:
           
            validated = {
                "match_score": float(data.get("match_score", 5.0)),
                "match_level": str(data.get("match_level", "Moderate Match")),
                "skills_matched": data.get("skills_matched", []),
                "skills_gaps": [],
                "strengths_found": data.get("strengths_found", []),
                "actionable_tip": str(data.get("actionable_tip", "Review the job requirements carefully"))
            }
            
            
            for gap in data.get("skills_gaps", []):
                if isinstance(gap, dict):
                    validated["skills_gaps"].append({
                        "skill": str(gap.get("skill", "Unknown")),
                        "importance": str(gap.get("importance", "medium")),
                        "suggestion": str(gap.get("suggestion", "Consider learning this skill"))
                    })
            
            
            validated["match_score"] = max(0.0, min(10.0, validated["match_score"]))
            
            return validated
            
        except Exception as e:
            print(f"Validation error: {str(e)}")
            return self._get_default_result()
    
    def _get_default_result(self) -> dict:
        """Return default result when analysis fails"""
        return {
            "match_score": 5.0,
            "match_level": "Analysis in progress - please try again",
            "skills_matched": [],
            "skills_gaps": [
                {
                    "skill": "Unable to analyze",
                    "importance": "medium",
                    "suggestion": "Please ensure both job description and resume are properly formatted with clear information"
                }
            ],
            "strengths_found": ["Analysis incomplete - please retry"],
            "actionable_tip": "Ensure your resume clearly highlights relevant skills and experience"
        }