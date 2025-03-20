import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/usdata/")
async def fetch_data():
    base_url = "https://data.sec.gov/submissions/"
    cik = "3110952"  # Example CIK for Apple Inc.
    url = f"{base_url}CIK{cik}.json"
    headers = {"User-Agent": "Your Name (your.email@example.com)"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        data = response.json()
        print(data)
        return data


@app.get("/items/")
async def fetch_with_error_handling():
    url = "https://catfact.ninja/fact"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()  # Raise an exception for 4XX/5XX errors
            return response.json()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
        except httpx.RequestError as e:
            print(f"Request error occurred: {e}")

@app.get("/companySearch/{company}")
async def fetch_with_error_handling(company: str):
    url = "https://catfact.ninja/fact"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()  # Raise an exception for 4XX/5XX errors
            return response.json()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
        except httpx.RequestError as e:
            print(f"Request error occurred: {e}")

# Run the async function
# asyncio.run(fetch_with_error_handling())
