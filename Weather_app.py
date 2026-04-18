# Weather App — Fetch real-time weather using OpenWeatherMap API
import requests

api_key = "YOUR_API_KEY_HERE"

while True:
    city = input("Enter city name or quit: ")
    if city.lower() == "quit":
        print("---Bye Bye---")
        break

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        city = data.get("name")
        country = data.get("sys").get("country")
        temperature = data.get("main").get("temp")
        feels_like = data.get("main").get("feels_like")
        humidity = data.get("main").get("humidity")
        weather = data["weather"][0]["description"]
        wind_speed = data.get("wind").get("speed")

        print(f"City: {city}")
        print(f"Country: {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found. Please try again.")