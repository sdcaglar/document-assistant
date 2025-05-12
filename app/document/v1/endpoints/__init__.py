from fastapi import APIRouter

from app.document.v1.endpoints import auth, pdf

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(pdf.router, prefix="/pdf", tags=["pdf"])
