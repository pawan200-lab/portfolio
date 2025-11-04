def get_weather(city, api_key):
    if not api_key:
        print("API key is missing. Please provide one.")
        return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
