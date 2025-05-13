from app.models.base import ModelBase
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from datetime import datetime


class ChatHistory(ModelBase):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    message = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "message": self.message,
            "response": self.response,
            "timestamp": self.timestamp.isoformat(),
        }
