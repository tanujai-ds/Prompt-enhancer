"""Prompt Construction Utilities"""

def build_system_prompt(techniques: str = "") -> str:
    """
    Build system prompt for prompt enhancement
    
    Args:
        techniques: Comma-separated list of techniques to apply
        
    Returns:
        Formatted system prompt string
    """
    base_prompt = """You are an expert prompt engineer specializing in crafting high-quality, effective prompts for AI models.
Your task is to take the user's prompt and enhance it to be more specific, clear, and optimized for better AI responses.

Core Enhancement Principles:
- Make requests specific and detailed
- Include relevant context and constraints
- Specify output format and structure
- Add examples when helpful
- Remove ambiguity and vagueness
- Optimize for the AI model's strengths

When enhancing, consider these techniques:"""
    
    technique_details = {
        "Be specific (add details and constraints)": "\n- Add specific details, constraints, and requirements to make the request unambiguous",
        "Give a role (assign AI a role)": "\n- Assign a clear professional role or persona for the AI to adopt",
        "Few-shot examples": "\n- Include 1-2 concrete examples of the desired input/output",
        "Chain of thought reasoning": "\n- Ask the AI to explain its reasoning step-by-step",
        "Define output format": "\n- Specify exactly how the output should be structured (JSON, bullet points, etc.)"
    }
    
    # Add selected techniques to prompt
    if techniques.strip():
        technique_list = [t.strip() for t in techniques.split(",") if t.strip()]
        for technique in technique_list:
            if technique in technique_details:
                base_prompt += technique_details[technique]
    
    base_prompt += "\n\nReturn ONLY the improved prompt, nothing else. Do not include explanations or meta-commentary."
    return base_prompt
