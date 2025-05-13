from app.config import settings
from google import genai


class LLMService:
    def __init__(self):
        pass

    def chat_with_llm(self, message: str, pdf_content: str):
        try:
            client = genai.Client(api_key=settings.GEMINI_API_KEY)
            formatted_content = (
                f"### User Query:\n{message}\n\n" f"### PDF Content:\n{pdf_content}"
            )
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=formatted_content
            )
            return response.text
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


llm_service = LLMService()
