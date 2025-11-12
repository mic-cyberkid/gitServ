import httpx
import time
import sys
import os

# Get ngrok URL from env var (set in workflow)
base_url = os.environ.get("NGROK_URL", "http://localhost:8000")
if not base_url.startswith(("http://", "https://")):
    base_url = "https://" + base_url  # ngrok provides HTTPS

print(f"Using base URL: {base_url}")

# Wait for server to start (increased for ngrok setup)
time.sleep(10)

with httpx.Client(base_url=base_url, timeout=30.0) as client:
    try:
        resp = client.get("/")
        print("Root response:", resp.json())

        resp = client.get("/health")
        print("Health response:", resp.json())

        if resp.status_code == 200 and resp.json()["status"] == "ok":
            print("API test passed!")
        else:
            print("API test failed!")
            sys.exit(1)
    except Exception as e:
        print("Client error:", e)
        sys.exit(1)
