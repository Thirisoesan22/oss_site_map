from fastapi import FastAPI, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/oss_site")
async def get_locations():
    try:
        with open("oss_site.geojson", "r") as geojson_file:
            geojson_data = geojson_file.read()
        return JSONResponse(content=geojson_data, media_type="application/json")
    except FileNotFoundError:
        return JSONResponse(content={"error": "GeoJSON file not found"}, status_code=404)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8003)