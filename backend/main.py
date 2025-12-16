from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

from app.services.analyze import JobMatchAnalyzer
from app.services.chat import CareerChatService
from app.services.resume_parser import parse_resume_file

app = FastAPI(
    title="Career Compass API",
    description="AI-Powered Job Match Analysis and Career Guidance",
    version="1.0.0"
)

#  CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize 
analyzer = JobMatchAnalyzer()
chat_service = CareerChatService()


# Request/Response 
class AnalyzeRequest(BaseModel):
    job_description: str
    resume_text: str


class SkillGap(BaseModel):
    skill: str
    importance: str
    suggestion: str


class AnalyzeResponse(BaseModel):
    match_score: float
    match_level: str
    skills_matched: List[str]
    skills_gaps: List[SkillGap]
    strengths_found: List[str]
    actionable_tip: str


class ChatRequest(BaseModel):
    query: str
    context: Optional[str] = ""


class ChatResponse(BaseModel):
    response: str


#Endpoints
@app.get("/")
async def root():
    return {
        "message": "Career Compass API",
        "version": "1.0.0",
        "endpoints": {
            "analyze": "/api/analyze",
            "chat": "/api/chat",
            "parse_resume": "/api/parse-resume"
        }
    }


@app.post("/api/analyze", response_model=AnalyzeResponse)
async def analyze_job_match(request: AnalyzeRequest):
    """
    Analyze job-resume match using AI
    """
    try:
        result = await analyzer.analyze(
            job_description=request.job_description,
            resume_text=request.resume_text
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/chat", response_model=ChatResponse)
async def career_chat(request: ChatRequest):
    """
    Chat with AI career assistant
    """
    try:
        response = await chat_service.chat(
            query=request.query,
            context=request.context
        )
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/parse-resume")
async def parse_resume(file: UploadFile = File(...)):
    """
    Parse uploaded resume file (PDF, DOCX, TXT)
    Returns extracted text from the file
    """
    try:
        # Validate_file
        allowed_types = [
            "application/pdf",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "text/plain"
        ]
        
        if file.content_type not in allowed_types:
            raise HTTPException(
                status_code=400,
                detail="Invalid file type. Please upload PDF, DOCX, or TXT file"
            )
        
        # Read_file
        content = await file.read()
        
        # Parse_file
        text = parse_resume_file(content, file.content_type)
        
        return {
            "text": text,
            "filename": file.filename,
            "content_type": file.content_type,
            "size": len(content)
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing file: {str(e)}")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)