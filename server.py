from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")# server.py
import uvicorn
from fastapi import import FastAPI
import ssl

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # Create a quick self-signed cert for the runner
    import subprocess, os
    cert_file = "cert.pem"
    key_file  = "key.pem"
    if not os.path.exists(cert_file):
        subprocess.run([
            "openssl", "req", "-x509", "-newkey", "rsa:4096",
            "-keyout", key_file, "-out", cert_file,
            "-days", "1", "-nodes", "-subj", "/CN=localhost"
        ], check=True)

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile=cert_file, keyfile=key_file)

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        ssl=ssl_context,          # <-- HTTPS
        log_level="info"
    )
def health_check():
    return {"status": "ok"}
