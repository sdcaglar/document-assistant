from app.models.chat import ChatHistory


class ChatHistoryRepository:
    def __init__(self):
        pass

    def get_all_chat_history(self, db, user_id):
        return db.query(ChatHistory).filter(ChatHistory.user_id == user_id).all()


chat_history_repository = ChatHistoryRepository()
