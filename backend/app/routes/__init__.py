"""API Routes"""
from fastapi import APIRouter
from .agent import router as agent_router

api_router = APIRouter()
api_router.include_router(agent_router, prefix="/api/v1/prompts", tags=["prompts"])

__all__ = ["api_router"]
