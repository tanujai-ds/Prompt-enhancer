"""Prompt Data Models"""
from pydantic import BaseModel, Field
from typing import Optional, List

class PromptRequest(BaseModel):
    """Request model for prompt improvement"""
    prompt: str = Field(..., min_length=1, max_length=5000, description="The prompt to improve")
    techniques: Optional[str] = Field(default="", description="Comma-separated enhancement techniques")
    
    class Config:
        schema_extra = {
            "example": {
                "prompt": "Write a story",
                "techniques": "Be specific, Give a role, Few-shot examples"
            }
        }

class PromptResponse(BaseModel):
    """Response model for improved prompt"""
    original_prompt: str
    improved_prompt: str
    techniques_used: List[str]
    status: str = "success"
    
    class Config:
        schema_extra = {
            "example": {
                "original_prompt": "Write a story",
                "improved_prompt": "Write a compelling sci-fi story...",
                "techniques_used": ["Be specific", "Give a role"],
                "status": "success"
            }
        }

class ErrorResponse(BaseModel):
    """Error response model"""
    status: str = "error"
    message: str
    error_code: Optional[str] = None
