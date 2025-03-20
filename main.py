import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/usdata/")
async def fetch_data():
    base_url = "https://data.sec.gov/submissions/"
    cik = "0000320193"  # Example CIK for Apple Inc.
    url = f"{base_url}CIK{cik}.json"
    headers = {"User-Agent": "ghomevenet"}
    print(url)
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for 4XX/5XX errors
            data = response.json()
            print(data)
            return data
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=str(e))
        except ValueError as e:
            raise HTTPException(status_code=500, detail="Invalid JSON response")


@app.get("/items/")
async def fetch_with_error_handling():
    url = "https://catfact.ninja/fact"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()  # Raise an exception for 4XX/5XX errors
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=str(e))
