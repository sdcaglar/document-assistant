import openai
from app.config import settings
from typing import Any, Dict

openai.api_key = settings.OPENAI_API_KEY


class LLMService:
    def __init__(self):
        pass

    @staticmethod
    def chat_with_llm(message: str, pdf_content: str) -> Dict[str, Any]:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an assistant that has access to the following PDF content.",
                    },
                    {"role": "user", "content": pdf_content},
                    {"role": "user", "content": message},
                ],
            )
            return {"response": response["choices"][0]["message"]["content"]}
        except Exception as e:
            return {"error": str(e)}


llm_service = LLMService()
