import multiprocessing
import os
import requests
from mcp.server.fastmcp import FastMCP
import uvicorn


# Step 1: Create MCP server instance
mcp = FastMCP("WeatherMCP", stateless_http=True)
app = mcp.streamable_http_app()


# Step 2: Register your tool
@mcp.tool()
def get_weather(city: str):
    """
    Returns current temperature and windspeed for a given city.
    """
    # Get coordinates
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_response = requests.get(geo_url)
    if geo_response.status_code != 200:
        return {"error": "Failed to find city."}
    
    geo_data = geo_response.json().get("results")
    if not geo_data:
        return {"error": f"City '{city}' not found."}
    lat = geo_data[0]["latitude"]
    lon = geo_data[0]["longitude"]

    
    # Get weather
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_response = requests.get(weather_url)
    if weather_response.status_code != 200:
        return {"error": "Failed to fetch weather."}
    
    weather = weather_response.json().get("current_weather", {})
    return {
        "city": city,
        "temperature": f"{weather.get('temperature')} °C",
        "windspeed": f"{weather.get('windspeed')} km/h"
    }


# Step 3: Run your MCP
if __name__ == "__main__":
    mcp.run()