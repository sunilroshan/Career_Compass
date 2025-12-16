# 🧭 Career Compass - AI Job Match Assistant

An AI-powered career guidance platform that helps students analyze job-resume compatibility and get personalized career advice.

## ✨ Features

- **Job-Resume Match Analysis**: AI-powered scoring system (0-10 scale)
- **Skills Gap Analysis**: Identifies missing skills with actionable suggestions
- **File Upload Support**: Upload resume as PDF, DOCX, or TXT
- **Career Chat Assistant**: Interactive AI counselor for career guidance
- **Beautiful UI**: Modern, responsive interface with Tailwind CSS

## 🛠️ Tech Stack

**Frontend:**
- React.js
- Tailwind CSS
- Lucide React Icons
- Vite

**Backend:**
- FastAPI
- LangChain
- Google Gemini AI
- PyPDF2 (PDF parsing)
- python-docx (DOCX parsing)

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- Google Gemini API Key

## 🚀 Installation

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r req.txt
```

4. Create `.env` file:
```env
GOOGLE_API_KEY=your_google_api_key_here
```

5. Run backend:
```bash
python main.py
```

Backend runs on: **http://localhost:8000**

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run development server:
```bash
npm run dev
```

Frontend runs on: **http://localhost:5173**

## 🎯 Usage

1. **Start Backend**: Run FastAPI server on port 8000
2. **Start Frontend**: Run React app on port 5173
3. **Analyze Match**: 
   - Paste job description
   - Upload resume or paste text
   - Click "Analyze Match"
   - Get detailed analysis with scores and suggestions
4. **Career Chat**: Ask questions about career paths, skills, and job readiness

## 📁 Project Structure
```
career-compass/
├── backend/
│   ├── app/
│   │   └── services/
│   │       ├── analyze.py
│   │       ├── chat.py
│   │       └── resume_parser.py
│   ├── main.py
│   ├── req.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── index.html
└── README.md
```

## 🔑 API Endpoints

- `GET /` - API information
- `POST /api/analyze` - Analyze job-resume match
- `POST /api/chat` - Career counseling chat
- `POST /api/parse-resume` - Parse uploaded resume file

## 🎨 Screenshots

[Add screenshots of your application here]

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

This project is [MIT](LICENSE) licensed.

## 👨‍💻 Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Google Gemini AI for powering the analysis
- LangChain for AI framework
- FastAPI for backend framework
- React for frontend framework
