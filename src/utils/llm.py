from src.utils.mock_llm import mock_call_gemini

def call_gemini(prompt: str, temperature=0.0, max_tokens=512):
    return mock_call_gemini(prompt, temperature=temperature, max_tokens=max_tokens)

