import httpx
import time

# Wait for server to start
time.sleep(25)

base_url = "http://localhost:8000"

with httpx.Client(base_url=base_url, timeout=10.0) as client:
    try:
        resp = client.get("/")
        print("Root response:", resp.json())

        resp = client.get("/health")
        print("Health response:", resp.json())

        if resp.status_code == 200 and resp.json()["status"] == "ok":
            print("API test passed!")
        else:
            print("API test failed!")
            exit(1)
    except Exception as e:
        print("Client error:", e)
        exit(1)
