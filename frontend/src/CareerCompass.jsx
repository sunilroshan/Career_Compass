import React, { useState, useRef } from 'react';
import { Upload, FileText, Briefcase, TrendingUp, Sparkles, Target, Zap, AlertCircle, CheckCircle, ArrowRight, MessageSquare, Send, Loader2, File, X } 
from 'lucide-react';

const CareerCompass = () => {
  
  const [jobDesc, setJobDesc] = useState('');
  const [resume, setResume] = useState('');
  const [resumeFile, setResumeFile] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('analyze');
  const [chatQuery, setChatQuery] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [chatLoading, setChatLoading] = useState(false);
  const [uploadMode, setUploadMode] = useState('text');
  const fileInputRef = useRef(null);

  const API_URL = 'http://localhost:8000';


  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;


    const validTypes = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'text/plain'];
    if (!validTypes.includes(file.type)) {
      alert('Please upload a PDF, DOCX, or TXT file');
      return;
    }

    if (file.size > 5 * 1024 * 1024) {
      alert('File size must be less than 5MB');
      return;
    }

    setResumeFile(file);
    setResume('');
  };

  const removeFile = () => {
    setResumeFile(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  
  const analyzeMatch = async () => {

    if (!jobDesc.trim()) {
      alert('Please provide a job description');
      return;
    }

    if (!resume.trim() && !resumeFile) {
      alert('Please provide your resume (text or file)');
      return;
    }

    setLoading(true);
    setAnalysis(null);
    
    try {
      let resumeText = resume;

      
      if (resumeFile) {
        const formData = new FormData();
        formData.append('file', resumeFile);

        const uploadResponse = await fetch(`${API_URL}/api/parse-resume`, {
          method: 'POST',
          body: formData
        });

        if (!uploadResponse.ok) {
          throw new Error('Failed to parse resume file');
        }
        
        const { text } = await uploadResponse.json();
        resumeText = text;
      }

     
      const response = await fetch(`${API_URL}/api/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          job_description: jobDesc,
          resume_text: resumeText
        })
      });

      if (!response.ok) {
        throw new Error('Analysis failed');
      }
      
      const data = await response.json();
      setAnalysis(data);
    } catch (error) {
      alert('Error analyzing match. Make sure backend is running on port 8000.');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };


  const handleChat = async () => {
    if (!chatQuery.trim()) return;

    const userMessage = { role: 'user', content: chatQuery };
    setChatHistory(prev => [...prev, userMessage]);
    setChatQuery('');
    setChatLoading(true);

    try {
      let contextText = resume;

 
      if (resumeFile && !resume) {
        const formData = new FormData();
        formData.append('file', resumeFile);

        const uploadResponse = await fetch(`${API_URL}/api/parse-resume`, {
          method: 'POST',
          body: formData
        });

        if (uploadResponse.ok) {
          const { text } = await uploadResponse.json();
          contextText = text;
        }
      }

      const response = await fetch(`${API_URL}/api/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: userMessage.content,
          context: contextText || ''
        })
      });

      if (!response.ok) {
        throw new Error('Chat failed');
      }
      
      const data = await response.json();
      setChatHistory(prev => [...prev, { role: 'assistant', content: data.response }]);
    } catch (error) {
      alert('Error in chat. Make sure backend is running.');
      console.error(error);
    } finally {
      setChatLoading(false);
    }
  };

  
  const getScoreColor = (score) => {
    if (score >= 8) return 'from-emerald-500 to-teal-500';
    if (score >= 6) return 'from-blue-500 to-cyan-500';
    if (score >= 4) return 'from-amber-500 to-orange-500';
    return 'from-red-500 to-pink-500';
  };

  const getScoreText = (score) => {
    if (score >= 8) return 'Excellent Match';
    if (score >= 6) return 'Good Match';
    if (score >= 4) return 'Moderate Match';
    return 'Needs Improvement';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50">

      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-purple-100 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 py-4">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4">

            {/* Logo and Title */}
            <div className="flex items-center space-x-3">
              <div className="bg-gradient-to-br from-purple-500 to-pink-500 p-2 rounded-xl">
                <Briefcase className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                  Career Compass
                </h1>
                <p className="text-sm text-gray-500">AI-Powered Job Match Assistant</p>
              </div>
            </div>
            
            {/* Navigation Tabs */}
            <div className="flex space-x-2">
              <button
                onClick={() => setActiveTab('analyze')}
                className={`px-4 py-2 rounded-lg font-medium transition-all ${
                  activeTab === 'analyze'
                    ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg'
                    : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                }`}
              >
                <Target className="w-4 h-4 inline mr-2" />
                Analyze Match
              </button>
              <button
                onClick={() => setActiveTab('chat')}
                className={`px-4 py-2 rounded-lg font-medium transition-all ${
                  activeTab === 'chat'
                    ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg'
                    : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                }`}
              >
                <MessageSquare className="w-4 h-4 inline mr-2" />
                Career Chat
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 py-8">
        {activeTab === 'analyze' ? (

          // Analysis Tab
          <div className="grid lg:grid-cols-2 gap-6">

            {/* Input Section */}
            <div className="space-y-6">
              
              {/* Job Description Input */}
              <div className="bg-white rounded-2xl shadow-xl p-6 border border-purple-100">
                <div className="flex items-center space-x-3 mb-4">
                  <div className="bg-gradient-to-br from-blue-500 to-cyan-500 p-2 rounded-lg">
                    <FileText className="w-5 h-5 text-white" />
                  </div>
                  <h2 className="text-xl font-bold text-gray-800">Job Description</h2>
                </div>
                <textarea
                  value={jobDesc}
                  onChange={(e) => setJobDesc(e.target.value)}
                  placeholder="Paste the job description here...&#10;&#10;Example:&#10;We're looking for a Full Stack Developer with:&#10;- 2+ years experience with React & Node.js&#10;- Strong knowledge of Python & FastAPI&#10;- Experience with Docker & AWS..."
                  className="w-full h-64 p-4 border-2 border-gray-200 rounded-xl focus:border-purple-400 focus:ring-4 focus:ring-purple-100 transition-all resize-none text-gray-700"
                />
              </div>

              {/* Resume Input */}
              <div className="bg-white rounded-2xl shadow-xl p-6 border border-purple-100">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center space-x-3">
                    <div className="bg-gradient-to-br from-purple-500 to-pink-500 p-2 rounded-lg">
                      <Upload className="w-5 h-5 text-white" />
                    </div>
                    <h2 className="text-xl font-bold text-gray-800">Your Resume</h2>
                  </div>
                 
                  <div className="flex space-x-2">
                    <button
                      onClick={() => setUploadMode('text')}
                      className={`px-3 py-1 text-sm rounded-lg transition-all ${
                        uploadMode === 'text'
                          ? 'bg-purple-100 text-purple-700 font-medium'
                          : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                      }`}
                    >
                      Text
                    </button>
                    <button
                      onClick={() => setUploadMode('file')}
                      className={`px-3 py-1 text-sm rounded-lg transition-all ${
                        uploadMode === 'file'
                          ? 'bg-purple-100 text-purple-700 font-medium'
                          : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                      }`}
                    >
                      Upload
                    </button>
                  </div>
                </div>

                {uploadMode === 'text' ? (
                
                  <textarea
                    value={resume}
                    onChange={(e) => setResume(e.target.value)}
                    placeholder="Paste your resume text here...&#10;&#10;Include:&#10;- Skills (Python, JavaScript, React, etc.)&#10;- Experience & Projects&#10;- Education&#10;- Certifications"
                    className="w-full h-64 p-4 border-2 border-gray-200 rounded-xl focus:border-purple-400 focus:ring-4 focus:ring-purple-100 transition-all resize-none text-gray-700"
                  />
                ) : (
                  
                  <div className="space-y-4">
                    {!resumeFile ? (
                      <label className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed border-gray-300 rounded-xl cursor-pointer hover:border-purple-400 transition-all bg-gray-50 hover:bg-purple-50">
                        <div className="flex flex-col items-center justify-center pt-5 pb-6">
                          <Upload className="w-12 h-12 text-gray-400 mb-3" />
                          <p className="mb-2 text-sm text-gray-600">
                            <span className="font-semibold">Click to upload</span> or drag and drop
                          </p>
                          <p className="text-xs text-gray-500">PDF, DOCX, or TXT (max 5MB)</p>
                        </div>
                        <input
                          ref={fileInputRef}
                          type="file"
                          className="hidden"
                          accept=".pdf,.docx,.txt"
                          onChange={handleFileUpload}
                        />
                      </label>
                    ) : (
                      
                      <div className="flex items-center justify-between p-4 bg-gradient-to-r from-purple-50 to-pink-50 border-2 border-purple-200 rounded-xl">
                        <div className="flex items-center space-x-3">
                          <div className="bg-purple-500 p-2 rounded-lg">
                            <File className="w-5 h-5 text-white" />
                          </div>
                          <div>
                            <p className="font-medium text-gray-800">{resumeFile.name}</p>
                            <p className="text-sm text-gray-500">
                              {(resumeFile.size / 1024).toFixed(1)} KB
                            </p>
                          </div>
                        </div>
                        <button
                          onClick={removeFile}
                          className="p-2 hover:bg-red-100 rounded-lg transition-all"
                        >
                          <X className="w-5 h-5 text-red-500" />
                        </button>
                      </div>
                    )}
                    <p className="text-sm text-gray-500 text-center">
                      Supported formats: PDF, DOCX, TXT
                    </p>
                  </div>
                )}
              </div>

             
              <button
                onClick={analyzeMatch}
                disabled={loading}
                className="w-full bg-gradient-to-r from-purple-500 to-pink-500 text-white py-4 rounded-xl font-bold text-lg shadow-lg hover:shadow-xl transform hover:scale-105 transition-all disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
              >
                {loading ? (
                  <span className="flex items-center justify-center">
                    <Loader2 className="w-5 h-5 mr-2 animate-spin" />
                    Analyzing...
                  </span>
                ) : (
                  <span className="flex items-center justify-center">
                    <Sparkles className="w-5 h-5 mr-2" />
                    Analyze Match
                  </span>
                )}
              </button>
            </div>

            <div className="space-y-6">
              {analysis ? (
                <>
                  
                  <div className="bg-white rounded-2xl shadow-xl p-8 border border-purple-100">
                    <div className="text-center">
                      <div className={`inline-block bg-gradient-to-r ${getScoreColor(analysis.match_score)} p-1 rounded-full mb-4`}>
                        <div className="bg-white rounded-full px-8 py-4">
                          <div className="text-5xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                            {analysis.match_score}/10
                          </div>
                        </div>
                      </div>
                      <h3 className="text-2xl font-bold text-gray-800 mb-2">
                        {getScoreText(analysis.match_score)}
                      </h3>
                      <p className="text-gray-600">{analysis.match_level}</p>
                    </div>
                  </div>

                  <div className="bg-white rounded-2xl shadow-xl p-6 border border-purple-100">
                    <div className="flex items-center space-x-2 mb-4">
                      <CheckCircle className="w-5 h-5 text-green-500" />
                      <h3 className="text-lg font-bold text-gray-800">Matched Skills</h3>
                    </div>
                    <div className="flex flex-wrap gap-2">
                      {analysis.skills_matched.map((skill, idx) => (
                        <span
                          key={idx}
                          className="px-4 py-2 bg-gradient-to-r from-green-50 to-emerald-50 text-green-700 rounded-lg border border-green-200 font-medium"
                        >
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>

              
                  {analysis.skills_gaps && analysis.skills_gaps.length > 0 && (
                    <div className="bg-white rounded-2xl shadow-xl p-6 border border-purple-100">
                      <div className="flex items-center space-x-2 mb-4">
                        <AlertCircle className="w-5 h-5 text-orange-500" />
                        <h3 className="text-lg font-bold text-gray-800">Skills to Develop</h3>
                      </div>
                      <div className="space-y-3">
                        {analysis.skills_gaps.map((gap, idx) => (
                          <div
                            key={idx}
                            className="p-4 bg-gradient-to-r from-orange-50 to-amber-50 rounded-lg border border-orange-200"
                          >
                            <div className="flex items-center justify-between mb-2">
                              <span className="font-bold text-orange-700">{gap.skill}</span>
                              <span className={`text-xs px-2 py-1 rounded-full ${
                                gap.importance === 'high' 
                                  ? 'bg-red-100 text-red-700'
                                  : 'bg-yellow-100 text-yellow-700'
                              }`}>
                                {gap.importance} priority
                              </span>
                            </div>
                            <p className="text-sm text-gray-600">{gap.suggestion}</p>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  <div className="bg-white rounded-2xl shadow-xl p-6 border border-purple-100">
                    <div className="flex items-center space-x-2 mb-4">
                      <TrendingUp className="w-5 h-5 text-blue-500" />
                      <h3 className="text-lg font-bold text-gray-800">Your Strengths</h3>
                    </div>
                    <ul className="space-y-2">
                      {analysis.strengths_found.map((strength, idx) => (
                        <li key={idx} className="flex items-start space-x-2">
                          <ArrowRight className="w-5 h-5 text-blue-500 flex-shrink-0 mt-0.5" />
                          <span className="text-gray-700">{strength}</span>
                        </li>
                      ))}
                    </ul>
                  </div>

              
                  <div className="bg-gradient-to-r from-purple-500 to-pink-500 rounded-2xl shadow-xl p-6 text-white">
                    <div className="flex items-center space-x-2 mb-3">
                      <Zap className="w-5 h-5" />
                      <h3 className="text-lg font-bold">Actionable Tip</h3>
                    </div>
                    <p className="text-purple-50 leading-relaxed">{analysis.actionable_tip}</p>
                  </div>
                </>
              ) : (
                
                <div className="bg-white rounded-2xl shadow-xl p-12 border border-purple-100 text-center">
                  <div className="bg-gradient-to-br from-purple-100 to-pink-100 w-24 h-24 rounded-full flex items-center justify-center mx-auto mb-4">
                    <Target className="w-12 h-12 text-purple-500" />
                  </div>
                  <h3 className="text-xl font-bold text-gray-800 mb-2">
                    Ready to Analyze
                  </h3>
                  <p className="text-gray-600">
                    Enter a job description and your resume (text or file), then click "Analyze Match"
                  </p>
                </div>
              )}
            </div>
          </div>
        ) : (
         
          <div className="max-w-4xl mx-auto">
            <div className="bg-white rounded-2xl shadow-xl border border-purple-100 overflow-hidden">
              
              <div className="bg-gradient-to-r from-purple-500 to-pink-500 p-6 text-white">
                <h2 className="text-2xl font-bold mb-2">Career Assistant Chat</h2>
                <p className="text-purple-100">Ask me anything about your career path, skills, or job search!</p>
              </div>

              
              <div className="h-96 overflow-y-auto p-6 space-y-4 bg-gray-50">
                {chatHistory.length === 0 ? (
                 
                  <div className="text-center py-12">
                    <div className="bg-gradient-to-br from-purple-100 to-pink-100 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-4">
                      <MessageSquare className="w-10 h-10 text-purple-500" />
                    </div>
                    <h3 className="text-lg font-bold text-gray-800 mb-2">Start a Conversation</h3>
                    <p className="text-gray-600 mb-4">Try asking:</p>
                    <div className="space-y-2">
                      {[
                        "What skills should I learn for data science roles?",
                        "Am I ready for frontend developer positions?",
                        "How can I improve my resume for tech jobs?"
                      ].map((suggestion, idx) => (
                        <button
                          key={idx}
                          onClick={() => setChatQuery(suggestion)}
                          className="block w-full max-w-md mx-auto px-4 py-2 bg-white border-2 border-purple-200 rounded-lg text-gray-700 hover:border-purple-400 transition-all text-left"
                        >
                          {suggestion}
                        </button>
                      ))}
                    </div>
                  </div>
                ) : (
                  
                  <>
                    {chatHistory.map((msg, idx) => (
                      <div
                        key={idx}
                        className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
                      >
                        <div
                          className={`max-w-2xl px-4 py-3 rounded-2xl whitespace-pre-wrap ${
                            msg.role === 'user'
                              ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white'
                              : 'bg-white border border-gray-200 text-gray-800'
                          }`}
                        >
                          {msg.content}
                        </div>
                      </div>
                    ))}
                    {chatLoading && (
                      <div className="flex justify-start">
                        <div className="bg-white border border-gray-200 px-4 py-3 rounded-2xl">
                          <Loader2 className="w-5 h-5 animate-spin text-purple-500" />
                        </div>
                      </div>
                    )}
                  </>
                )}
              </div>

         
              <div className="p-4 bg-white border-t border-gray-200">
                <div className="flex space-x-2">
                  <input
                    type="text"
                    value={chatQuery}
                    onChange={(e) => setChatQuery(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && !chatLoading && handleChat()}
                    placeholder="Ask about skills, career paths, job readiness..."
                    className="flex-1 px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-purple-400 focus:ring-4 focus:ring-purple-100 transition-all"
                    disabled={chatLoading}
                  />
                  <button
                    onClick={handleChat}
                    disabled={chatLoading || !chatQuery.trim()}
                    className="px-6 py-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-xl font-medium hover:shadow-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    <Send className="w-5 h-5" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
};

export default CareerCompass;