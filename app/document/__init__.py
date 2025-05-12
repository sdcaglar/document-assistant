import traceback

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi_pagination import add_pagination
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.config import settings
from app.db.database import SessionLocal
from app.document.v1.endpoints import api_router

document = FastAPI(
    title="Document Assistant",
    version=f"{settings.APP_VERSION}-{settings.RELEASE_NO}",
    openapi_url="/openapi.json" if settings.DEVELOPER_MODE else None,
)


document.include_router(api_router)

add_pagination(document)


@document.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    if isinstance(exc.detail, str):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error_code": exc.status_code, "error_message": exc.detail},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"error_code": exc.detail.value, "error_message": exc.detail.phrase},
    )


@document.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        request.state.db = SessionLocal()
        return await call_next(request)
    except Exception:
        if settings.DEVELOPER_MODE:
            traceback.print_exc()
        request.state._exception = traceback.format_exc()
        return JSONResponse(
            status_code=500,
            content={"error_code": 500, "error_message": "Internal server error"},
        )
    finally:
        request.state.db.close()


@document.middleware("http")
async def add_all_headers(request: Request, call_next):
    headers = request.headers
    client_ip = "127.0.0.1"
    client_user_agent = "local"
    if "X-Forwarded-For" in headers:
        client_ip = headers["X-Forwarded-For"]
    elif "x-forward-for" in headers:
        client_ip = headers["x-forward-for"]
    elif "x-real-ip" in headers:
        client_ip = headers["x-real-ip"]
    elif "CLIENT-IP" in headers:
        client_ip = headers["CLIENT-IP"]
    elif "X-User-Ip" in headers:
        client_ip = headers["X-User-Ip"]
    elif "x-user-ip" in headers:
        client_ip = headers["x-user-ip"]

    if len(client_ip.split(",")) > 0:
        client_ip = client_ip.split(",")[0].strip()

    if "CLIENT-USER-AGENT" in headers:
        client_user_agent = headers["CLIENT-USER-AGENT"]
    elif "user-agent" in headers:
        client_user_agent = headers["user-agent"]

    request.state.client_ip = client_ip
    request.state.client_user_agent = client_user_agent
    return await call_next(request)


@document.get("/health", response_class=HTMLResponse)
def health():
    return """
    <html>
        <head>
            <title>OK</title>
        </head>
        <body>
            <p>OK</p>
        </body>
    </html>
    """
