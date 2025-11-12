import os
import sys
import time
import httpx

base_url = os.getenv("PINGGY_URL", "http://localhost:8000").strip()
if base_url and not base_url.startswith(("http://", "https://")):
    base_url = "https://" + base_url  # Serveo uses HTTPS

print(f"Testing API at: {base_url}")
time.sleep(3)  # Safety delay

with httpx.Client(base_url=base_url, timeout=15.0) as client:
    try:
        r1 = client.get("/")
        print("Root:", r1.json())

        r2 = client.get("/health")
        print("Health:", r2.json())

        if r2.status_code == 200 and r2.json().get("status") == "ok":
            print("API TEST PASSED")
            sys.exit(0)
        else:
            print("API TEST FAILED")
            sys.exit(1)
    except Exception as e:
        print(f"Client error: {e}")
        sys.exit(1)
