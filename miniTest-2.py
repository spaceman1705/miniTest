import urllib.request
import json
import os
from datetime import datetime

def get_jakarta_forecast():
    api_key = os.environ.get("OPENWEATHER_API_KEY")

    if not api_key:
        print("API key tidak ditemukan!")
        return

    url = f"http://api.openweathermap.org/data/2.5/forecast?q=Jakarta&appid={api_key}&units=metric&cnt=40"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
    except Exception as e:
        print(f"Gagal mengambil data: {e}")
        return

    daily = {}
    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]
        time = item["dt_txt"].split(" ")[1]
        if date not in daily:
            daily[date] = item
        elif time == "12:00:00":
            daily[date] = item

    print("Weather Forecast:")
    for date, item in list(daily.items())[:5]:
        temp     = item["main"]["temp"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        day_str  = date_obj.strftime("%a, %d %b %Y")
        print(f"  {day_str}: {temp:.2f}°C")

if __name__ == "__main__":
    get_jakarta_forecast()