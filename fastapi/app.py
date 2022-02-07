#!/usr/bin/env python3

import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.api:app", host="127.0.0.1", port=8081,  reload=True, log_level="info")