"""

API Diagnostic Tester
Checks connectivity, latency and response integrity from an API endpoint.

"""
import requests
import time

#Public mock API endpoint
url = "https://jsonplaceholder.typicode.com/todos/1"

print("=== API Diagnostic Test ===")

try:
    start = time.time()

    # Send request
    response = requests.get(url, timeout=5)

    # Calculate latency
    latency = round((time.time() - start) * 1000, 2)

    # Output results
    print(f"Status Code: {response.status_code}")
    print(f"Latency: {latency} ms")
    print("Response Body:", response.json())

    # Basic health check
    if response.status_code == 200:
        print("\nAPI is reachable and responding normally.")
    else:
        print("\nAPI responded but returned an unexpected status code.")

except requests.exceptions.Timeout:
    print("Timeout: API did not respond within 5 seconds.")
except requests.exceptions.ConnectionError:
    print("Connection error: Cannot reach endpoint.")
except Exception as e:
    print("Unexpected error:", e)

print("==========================")