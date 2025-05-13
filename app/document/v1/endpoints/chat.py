from fastapi import APIRouter, Depends, Request

from app.core.chat import chat_core
from app.document.v1.dependencies import get_current_active_user
from app.models.user import User

router = APIRouter()


@router.get("/chat-history")
async def chat_history(request: Request, user: User = Depends(get_current_active_user)):
    db = request.state.db
    return chat_core.chat_history(db, user.id)


@router.post("/pdf-chat")
async def pdf_chat(
    message: str, file_id: str, user: User = Depends(get_current_active_user)
):
    return chat_core.pdf_chat(message, file_id, user.id)
