from app.core.pdf import pdf_core
from app.integration.llm_service import llm_service
from app.repository.chat import chat_history_repository


class ChatCore:
    def __init__(self):
        pass

    def chat_history(self, db, user_id):
        chat_history = chat_history_repository.get_all_chat_history(db, user_id)
        return {"history": [entry.to_dict() for entry in chat_history]}

    def pdf_chat(self, message, file_id, user_id):
        parsed_data = pdf_core.extract_text_from_pdf(file_id, user_id)
        return llm_service.chat_with_llm(message, parsed_data.get("text"))


chat_core = ChatCore()
