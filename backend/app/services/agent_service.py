"""Agent Service for Prompt Improvement"""
from groq import Groq
from app.config import settings
from app.utils import build_system_prompt
from app.models import PromptRequest, PromptResponse

class AgentService:
    """Service for handling prompt improvement with Groq AI"""
    
    def __init__(self):
        """Initialize Groq client"""
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.MODEL
    
    def improve_prompt(self, request: PromptRequest) -> PromptResponse:
        """
        Improve a prompt using AI enhancement
        
        Args:
            request: PromptRequest containing prompt and techniques
            
        Returns:
            PromptResponse with improved prompt
            
        Raises:
            Exception: If API call fails
        """
        try:
            # Build system prompt with selected techniques
            system_prompt = build_system_prompt(request.techniques)
            
            # Call Groq API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": request.prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            improved_prompt = response.choices[0].message.content.strip()
            
            # Parse techniques
            techniques_list = [t.strip() for t in request.techniques.split(",") if t.strip()]
            
            return PromptResponse(
                original_prompt=request.prompt,
                improved_prompt=improved_prompt,
                techniques_used=techniques_list,
                status="success"
            )
        
        except Exception as e:
            raise Exception(f"Failed to improve prompt: {str(e)}")
