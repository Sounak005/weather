import requests

def get_current_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"] - 273.15  # Convert from Kelvin to Celsius
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_data = data["weather"]
        description = weather_data[0]["description"]
        return {
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity,
            "description": description,
        }
    else:
        return None

# Replace YOUR_API_KEY with your actual API key
api_key = "d9f05fc1bcfa6ca1ec3711beefcc419b"
city = input("Enter the city name: ")
weather_data = get_current_weather(city, api_key)
if weather_data is not None:
    print(f"Temperature: {weather_data['temperature']:.1f}°C")
    print(f"Atmospheric pressure: {weather_data['pressure']} hPa")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Description: {weather_data['description']}")
else:
    print("City not found")
