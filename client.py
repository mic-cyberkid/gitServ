import os
import sys
import time
import httpx

# ngrok free gives HTTPS URL, but we forward HTTP → use HTTPS but allow HTTP content
base_url = os.getenv("NGROK_URL")
if not base_url:
    base_url = "http://localhost:8000"
else:
    # ngrok gives https://..., keep it
    pass

print(f"Testing API at: {base_url}")
time.sleep(8)  # wait for server + tunnel

with httpx.Client(base_url=base_url, timeout=15.0, verify=False) as client:
    try:
        r1 = client.get("/")
        print("Root response:", r1.json())

        r2 = client.get("/health")
        print("Health response:", r2.json())

        if r2.status_code == 200 and r2.json().get("status") == "ok":
            print("API TEST PASSED")
            sys.exit(0)
        else:
            print("API TEST FAILED")
            sys.exit(1)
    except Exception as e:
        print(f"Client error: {e}")
        sys.exit(1)
