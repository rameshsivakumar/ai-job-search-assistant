import json

def call_gemini(prompt: str, temperature=0.0):
    from src.utils.mock_llm import mock_call_gemini
    return mock_call_gemini(prompt, temperature=temperature)
