import requests

def get_weather(city_name, api_key):
    # Base URL for OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Temperature in Celsius
    }

    try:
        # Making the API request
        response = requests.get(base_url, params=params)

        # Debugging: Print detailed error if response code is not 200
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")
            return

        # Parse the response JSON if the request is successful
        data = response.json()
        city = data["name"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display the weather information
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    except requests.RequestException as e:
        print("Error connecting to the weather service:", e)

def main():
    print("--- Weather Checker for Cities ---")
    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    while True:
        # Prompt the user to enter a city name
        city_name = input("\nEnter the name of the city (or type 'exit' to quit): ")
        if city_name.lower() == "exit":
            print("Exiting the Weather Checker. Stay safe!")
            break
        get_weather(city_name, api_key)

if __name__ == "__main__":
    main()
