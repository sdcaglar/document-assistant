import uvicorn


if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000, proxy_headers=True)
    # uvicorn.run("run:app", host="0.0.0.0", port=8000, reload=True)
    uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)
