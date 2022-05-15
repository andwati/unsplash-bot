import os

from src.server import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 33507))
    app.run(host="0.0.0.0", port=port)
