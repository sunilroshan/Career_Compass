from langchain_google_genai import ChatGoogleGenerativeAI
from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()


class CareerChatService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.7,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        
        
        self.chat_history: List[Dict[str, str]] = []
        
        self.knowledge_base = self._get_knowledge_base()
    
    def _get_knowledge_base(self) -> str:
        """Return comprehensive career knowledge as a single string"""
        return """
CAREER KNOWLEDGE BASE:

=== DATA SCIENCE CAREER PATH ===
Essential Skills: Python, SQL, Statistics, Machine Learning, Data Visualization (Tableau, PowerBI)
Key Libraries: Pandas, NumPy, Scikit-learn, TensorFlow, PyTorch
Entry Requirements: Strong math/stats background, portfolio projects, Kaggle competitions
Average Timeline: 6-12 months to become job-ready with intensive study
Common Roles: Data Analyst, Data Scientist, ML Engineer, Business Intelligence Analyst
Salary Range: $70K-$150K depending on experience and location
Learning Path: Start with Python basics → Statistics → Pandas/NumPy → Machine Learning → Deep Learning

=== FRONTEND DEVELOPER CAREER PATH ===
Essential Skills: HTML, CSS, JavaScript, React or Vue.js, Responsive Design
Key Tools: Git, Webpack, npm, Chrome DevTools, Figma
Entry Requirements: Strong portfolio with 3-5 projects, understanding of UX principles
Average Timeline: 4-8 months to become job-ready
Common Roles: Frontend Developer, UI Developer, React Developer, Web Developer
Salary Range: $60K-$130K depending on experience and location
Learning Path: HTML/CSS → JavaScript fundamentals → React/Vue → State Management → Testing

=== BACKEND DEVELOPER CAREER PATH ===
Essential Skills: Python/Node.js/Java, Databases (SQL/NoSQL), REST APIs, Authentication
Key Technologies: FastAPI, Express.js, PostgreSQL, MongoDB, Docker, AWS
Entry Requirements: Understanding of data structures, system design basics, API development
Average Timeline: 6-10 months to become job-ready
Common Roles: Backend Developer, API Developer, Software Engineer, DevOps Engineer
Salary Range: $70K-$140K depending on experience and location
Learning Path: Programming fundamentals → Databases → API development → Authentication → Deployment

=== FULL STACK DEVELOPER CAREER PATH ===
Essential Skills: Frontend (React) + Backend (Node.js/Python) + Databases + DevOps basics
Key Technologies: MERN/MEAN stack, RESTful APIs, Git, Docker, Cloud platforms
Entry Requirements: Comprehensive portfolio showing end-to-end applications
Average Timeline: 8-14 months to become job-ready
Common Roles: Full Stack Developer, Software Engineer, Application Developer
Salary Range: $75K-$150K depending on experience and location
Learning Path: Master frontend → Master backend → Learn databases → Add DevOps → Build complete projects

=== RESUME BEST PRACTICES ===
- Keep it to 1-2 pages maximum (1 page for students/entry-level)
- Use action verbs: Built, Developed, Implemented, Optimized, Designed, Created
- Quantify achievements: "Improved performance by 40%", "Reduced load time by 2s", "Served 10K+ users"
- Include relevant projects with tech stack and GitHub links
- Highlight measurable impact, not just responsibilities
- Tailor resume keywords to match job description (use same terms as job posting)
- Include certifications and relevant coursework
- Use ATS-friendly formatting (avoid tables, graphics in main content)
- Put most relevant experience at the top
- Include a strong summary/objective for entry-level positions
- Proofread multiple times for spelling/grammar errors

=== JOB SEARCH STRATEGIES ===
- Build a strong GitHub profile with quality projects (aim for 5-10 solid repositories)
- Contribute to open source projects to show collaboration skills
- Network on LinkedIn (connect with recruiters, comment on posts, share your work)
- Attend tech meetups, hackathons, and conferences (great for networking)
- Apply to startups and mid-size companies (less competition than FAANG)
- Prepare for technical interviews: LeetCode/HackerRank (solve 50-100 problems)
- Get referrals through alumni networks and connections (4x more likely to get interview)
- Consider internships as pathway to full-time roles
- Build personal projects that solve real problems (not just tutorials)
- Create a personal website/portfolio to showcase work
- Apply to 10-20 positions per week consistently
- Follow up on applications after 1-2 weeks
- Join Discord/Slack communities in your field

=== EMERGING TECH SKILLS 2024-2025 ===
HIGH DEMAND: 
- AI/ML (ChatGPT, LLMs, Prompt Engineering)
- Cloud Computing (AWS, Azure, GCP)
- Kubernetes & Container Orchestration
- Microservices Architecture
- DevOps/SRE practices

GROWING FIELDS:
- Blockchain Development (Web3, Smart Contracts)
- Cybersecurity (Ethical Hacking, Security Engineering)
- Data Engineering (Data Pipelines, ETL)
- Mobile Development (React Native, Flutter)

TOP LANGUAGES:
- Python (AI/Data Science/Backend)
- TypeScript (Web Development)
- Go (Backend/Cloud/DevOps)
- Rust (Systems Programming)
- Swift/Kotlin (Mobile)

FRAMEWORKS TO LEARN:
- Frontend: Next.js, React, Vue.js
- Backend: FastAPI, Django, Spring Boot, Express.js
- Mobile: React Native, Flutter

TOOLS & PLATFORMS:
- Docker, Kubernetes
- Terraform, Ansible
- Jenkins, GitLab CI/CD, GitHub Actions
- Prometheus, Grafana (monitoring)

CERTIFICATIONS WORTH GETTING:
- AWS Solutions Architect Associate
- Google Cloud Professional Cloud Architect
- CKA (Certified Kubernetes Administrator)
- Azure Fundamentals/Associate

=== INTERVIEW PREPARATION ===
TECHNICAL ROUNDS:
- Data Structures: Arrays, Linked Lists, Trees, Graphs, Hash Tables
- Algorithms: Sorting, Searching, Dynamic Programming, Recursion
- System Design: Scalability, Load Balancing, Caching, Databases
- Practice: 150+ LeetCode problems (Easy: 50, Medium: 80, Hard: 20)

BEHAVIORAL ROUNDS:
- Use STAR format (Situation, Task, Action, Result)
- Prepare 5-7 stories showcasing different skills
- Show problem-solving approach and teamwork
- Be specific with examples and quantify results

COMPANY RESEARCH:
- Understand their products and services
- Know their tech stack (check job posting, engineering blog)
- Read recent news and company culture info
- Check Glassdoor for interview insights

QUESTIONS TO ASK INTERVIEWER:
- What does a typical day look like for this role?
- What are the biggest challenges facing the team?
- How do you measure success in this position?
- What's the team structure and who would I work with?
- What opportunities for growth and learning exist?
- What's the tech stack and development process?

RED FLAGS TO AVOID:
- Bad-mouthing previous employers or colleagues
- Lack of questions about the role/company
- Being unprepared or late
- Not knowing basic concepts listed on your resume
- Appearing uninterested or checking phone

MOCK INTERVIEWS:
- Practice with peers or use platforms like Pramp, interviewing.io
- Record yourself to identify areas for improvement
- Get feedback from experienced developers

=== SKILLS GAP ANALYSIS ===
- Read 10-20 job postings in your target role
- Identify must-have vs nice-to-have skills
- Focus on skills appearing in 70%+ of postings (high-ROI)
- Learn transferable skills first (Git, testing, CI/CD, documentation)
- Build projects demonstrating each skill rather than just taking courses
- Document your learning journey (blog posts, GitHub README files)
- Get certifications for skills hard to demonstrate (AWS, security, etc.)
- Join communities to practice (Discord servers, Slack groups, Reddit)
- Teach others to solidify understanding (write tutorials, answer questions)
- Update resume as you learn new skills

=== CAREER READINESS ASSESSMENT ===
ENTRY LEVEL READY:
- 2-3 solid projects in your portfolio
- Understand fundamentals of your tech stack
- Can explain code decisions and trade-offs
- Comfortable with Git and version control
- Basic understanding of testing
- Can build features independently with guidance

MID LEVEL READY:
- 3-5 years experience or equivalent substantial projects
- Understand architecture and design patterns
- Can lead development of small features/modules
- Mentor junior developers
- Comfortable with code reviews
- Understanding of performance optimization

SENIOR LEVEL READY:
- 5+ years of experience
- Can design complete systems
- Technical leadership and mentoring abilities
- Understand business impact of technical decisions
- Experience with production systems at scale
- Strong communication skills

KEY READINESS INDICATORS:
✓ Can build features independently
✓ Understand and write tests
✓ Comfortable with code reviews (giving and receiving)
✓ Can debug complex issues
✓ Write clean, maintainable code
✓ Understand version control best practices

RED FLAGS (NOT READY):
✗ Can't explain past projects in detail
✗ No portfolio or GitHub presence
✗ Unable to write clean, working code
✗ Don't understand basic CS concepts
✗ Can't articulate why you made certain technical choices
✗ Haven't built anything outside of tutorials
"""
    
    def _find_relevant_context(self, query: str) -> str:
        """Simple keyword matching to find relevant sections"""
        query_lower = query.lower()
        kb = self.knowledge_base
        
       
        sections = {
            "data science": ["data science", "data scientist", "ml engineer", "machine learning", "data analyst"],
            "frontend": ["frontend", "front-end", "react", "vue", "javascript", "web developer", "ui developer"],
            "backend": ["backend", "back-end", "api", "server", "database", "python developer"],
            "fullstack": ["fullstack", "full-stack", "full stack"],
            "resume": ["resume", "cv", "application"],
            "interview": ["interview", "interviewing", "technical round", "behavioral"],
            "job search": ["job search", "apply", "application", "hiring"],
            "skills": ["skill", "learn", "technology", "framework"],
            "ready": ["ready", "prepared", "qualified", "career readiness"]
        }
        
        
        relevant = []
        for section, keywords in sections.items():
            if any(keyword in query_lower for keyword in keywords):
                
                start_marker = f"=== {section.upper()}"
                if start_marker in kb.upper():
                    relevant.append(section)
        
       
        if not relevant:
            return "General career guidance applicable to all tech roles"
        
        return f"Focus on: {', '.join(relevant)}"
    
    async def chat(self, query: str, context: str = "") -> str:
        """
        Handle career chat without embeddings
        """
        try:
            
            relevant_context = self._find_relevant_context(query)
            
           
            history_text = ""
            for msg in self.chat_history[-4:]:  # Last 4 messages for context
                role = msg["role"]
                content = msg["content"]
                history_text += f"{role.upper()}: {content}\n\n"
            
          
            prompt = f"""You are an expert career counselor and job search advisor specializing in tech careers.

Your role is to:
- Provide actionable career advice and guidance
- Help students understand job market trends and requirements
- Suggest relevant skills to learn based on career goals
- Give honest assessments of job readiness
- Offer strategies for skill development and career growth

Be encouraging but realistic. Provide specific, actionable advice rather than generic platitudes.

COMPREHENSIVE CAREER KNOWLEDGE BASE:
{self.knowledge_base}

RELEVANT TOPICS FOR THIS QUERY: {relevant_context}

USER'S RESUME CONTEXT:
{context if context else "No resume provided"}

CONVERSATION HISTORY:
{history_text if history_text else "No previous conversation"}

USER QUERY: {query}

Provide a helpful, specific, and actionable response (2-4 paragraphs). Use bullet points for lists. Be conversational and encouraging."""

            
            response = await self.llm.ainvoke(prompt)
            
          
            response_text = response.content if hasattr(response, 'content') else str(response)
            
        
            self.chat_history.append({"role": "user", "content": query})
            self.chat_history.append({"role": "assistant", "content": response_text})
            
          
            if len(self.chat_history) > 10:
                self.chat_history = self.chat_history[-10:]
            
            return response_text
            
        except Exception as e:
            print(f"Chat error: {str(e)}")
            return "I apologize, but I'm having trouble processing your request. Please try rephrasing your question or check your API key configuration."