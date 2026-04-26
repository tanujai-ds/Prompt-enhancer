# 🚀 Prompt Improver AI

A professional-grade web application for enhancing and optimizing AI prompts using advanced techniques and the Groq AI API. Features a modern React frontend with a professional white/black design and a robust FastAPI backend.

## ✨ Features

- **AI-Powered Prompt Enhancement** - Improve your prompts using Groq's lightning-fast LLM
- **Multiple Enhancement Techniques:**
  - 📌 Be Specific - Add detailed constraints and context
  - 👤 Assign Role - Define AI's purpose and perspective
  - 📚 Few-Shot Examples - Provide reference examples
  - 🧠 Chain of Thought - Enable step-by-step reasoning
  - 📋 Define Format - Specify output structure
- **Professional UI** - Clean, modern white and black design
- **Smooth Animations** - Framer Motion for polished interactions
- **Copy to Clipboard** - One-click result copying
- **Real-time Processing** - Instant feedback with loading states
- **Fully Responsive** - Works on desktop, tablet, and mobile

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI library
- **Vite** - Fast build tool
- **Tailwind CSS** - Utility-first styling
- **Framer Motion** - Animation library
- **Axios** - HTTP client

### Backend
- **FastAPI** - Modern Python web framework
- **Groq API** - AI model inference
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## 📋 Prerequisites

- **Python 3.8+**
- **Node.js 16+**
- **npm or yarn**
- **Groq API Key** (get from [console.groq.com](https://console.groq.com))

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/prompt-improver.git
cd prompt-improver
```

### 2. Setup Backend

```bash
cd backend
python -m venv venv

# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file in the `backend` directory:
```env
OPENAI_API_KEY=your_groq_api_key_here
```

Start the backend:
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Backend runs at: **http://localhost:8000**

### 3. Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: **http://localhost:3000**

## 📖 API Documentation

Once the backend is running, visit **http://localhost:8000/docs** for interactive API documentation.

### Main Endpoint

**POST** `/api/v1/prompts/improve`

Request:
```json
{
  "prompt": "Write a story about space exploration",
  "techniques": "Be specific (add details and constraints), Give a role (assign AI a role)"
}
```

Response:
```json
{
  "original_prompt": "Write a story about space exploration",
  "improved_prompt": "As a creative science fiction author, write a compelling story...",
  "techniques_used": ["Be specific", "Give a role"],
  "status": "success"
}
```

## 📁 Project Structure

```
prompt-improver/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration settings
│   │   ├── main.py            # FastAPI app entry point
│   │   ├── models/            # Pydantic models
│   │   ├── routes/            # API routes
│   │   ├── services/          # Business logic
│   │   └── utils/             # Helper functions
│   ├── requirements.txt        # Python dependencies
│   ├── config.py
│   ├── main.py
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── pages/             # Page components
│   │   ├── hooks/             # Custom React hooks
│   │   ├── services/          # API client
│   │   ├── styles/            # Global styles
│   │   ├── animations/        # Framer Motion variants
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── tailwind.config.js     # Tailwind configuration
│   ├── vite.config.js         # Vite configuration
│   ├── index.html
│   └── Dockerfile
├── docker-compose.yml         # Docker orchestration
└── README.md
```

## 🐳 Docker Deployment

Build and run with Docker:

```bash
docker-compose up --build
```

This will:
- Start the FastAPI backend on port 8000
- Start the React frontend on port 3000

## 🔧 Configuration

### Backend Configuration
Edit `backend/app/config.py`:
```python
GROQ_API_KEY = os.getenv("OPENAI_API_KEY")  # Set via .env file
MODEL = "llama-3.3-70b-versatile"
CORS_ORIGINS = ["*"]
```

### Frontend Configuration
Edit `frontend/vite.config.js`:
```javascript
server: {
  port: 3000,
  proxy: {
    '/api': {
      target: 'http://127.0.0.1:8000',
      changeOrigin: true,
    }
  }
}
```

## 🎨 UI Customization

### Colors
Edit `frontend/tailwind.config.js` to customize the color scheme.

### Fonts
Fonts are loaded from Google Fonts in `frontend/index.html`.

### Animations
Modify animation variants in `frontend/src/animations/variants.js`.

## 🚀 Production Deployment

### Frontend Build
```bash
cd frontend
npm run build
npm run preview
```

### Backend Deployment
```bash
pip install gunicorn
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

## 🔐 Security

- ✅ CORS enabled for frontend-backend communication
- ✅ Input validation with Pydantic
- ✅ Environment variables for sensitive data
- ✅ Secure API key handling

## 📝 License

MIT License - Feel free to use this project for personal or commercial purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues and questions, please open an issue on GitHub.

---

**Made with ❤️ using React, FastAPI, and Groq AI**
