import uvicorn


if __name__ == "__main__":
    uvicorn.run("server.app:pjs_server", host="127.0.0.1", port=7000, reload=True)