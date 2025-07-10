import datetime, os, requests
from zoneinfo import ZoneInfo
from timezonefinder import TimezoneFinder
from google.adk.agents import Agent
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city: str) -> dict:
    """Fetches real-time weather data for a given city using OpenWeatherMap Current Weather API.

    Args:
        city (str): City name

    Returns:
        dict: status and weather report or error message
    """
    
    if not API_KEY:
        return {
            "status": "error",
            "error_message": "API key not found. Please set OPENWEATHER_API_KEY in your .env file.",
        }

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            return {
                "status": "error",
                "error_message": data.get("message", "Failed to fetch weather data."),
            }

        temp_c = data["main"]["temp"]
        temp_f = round(temp_c * 9 / 5 + 32, 2)
        desc = data["weather"][0]["description"].capitalize()

        return {
            "status": "success",
            "report": (
                f"The weather in {city.title()} is {desc} with a temperature of "
                f"{temp_c}°C ({temp_f}°F)."
            )
        }

    except Exception as e:
        return {"status": "error", "error_message": str(e)}


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city using coordinates and timezone.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    if not API_KEY:
        return {"status": "error", "error_message": "Missing API key in .env file"}

    try:
        # Step 1: Get coordinates from OpenWeatherMap Geocoding API
        geo_url = "http://api.openweathermap.org/geo/1.0/direct"
        geo_params = {
            "q": city,
            "limit": 1,
            "appid": API_KEY
        }
        geo_resp = requests.get(geo_url, params=geo_params)
        geo_data = geo_resp.json()

        if not geo_data:
            return {
                "status": "error",
                "error_message": f"City '{city}' not found.",
            }

        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']

        # Step 2: Determine time zone from coordinates
        tf = TimezoneFinder()
        tz_name = tf.timezone_at(lat=lat, lng=lon)

        if not tz_name:
            return {
                "status": "error",
                "error_message": f"Could not determine time zone for '{city}'."
            }

        # Step 3: Get current time in that timezone
        now = datetime.datetime.now(ZoneInfo(tz_name))
        report = f"The current time in {city.title()} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"

        return {"status": "success", "report": report}

    except Exception as e:
        return {"status": "error", "error_message": str(e)}


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)
