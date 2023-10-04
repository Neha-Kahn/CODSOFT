import tkinter as tk
from tkinter import messagebox
import requests


def get_weather_data(city_name):
    # My OpenWeatherMap API key
    api_key = '08968e4bdd194898de89e79a95816747'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def display_weather():
    city_name = city_entry.get()

    if not city_name:
        messagebox.showerror("Error", "Please enter a city or zip code.")
        return

    weather_data = get_weather_data(city_name)

    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']

        result_heading = f"Weather in {weather_data['name']}:\n"
        result_text = f"Temperature: {temperature}°C\n"
        result_text += f"Humidity: {humidity}%\n"
        result_text += f"Description: {description.capitalize()}\n"
        result_text += f"Wind Speed: {wind_speed} m/s"

        heading_result_label.config(text=result_heading)
        result_label.config(text=result_text)
    else:
        messagebox.showerror("Error", "City not found, Please enter correct city name.")


# Creating the main window
root = tk.Tk()
root.title("Weather Forecast")
root.geometry("400x300")

# Creating GUI elements
label = tk.Label(root, text="Enter the name of a city or a zip code", font=("Arial", 12, "bold"), fg='blue')
label.place(x=60, y=30)

city_entry = tk.Entry(root, width=25, borderwidth=2)
city_entry.pack(pady=70)

search_button = tk.Button(root, text="Search", command=display_weather, borderwidth=2, font='bold',
                          fg='white', bg='blue')
search_button.place(x=165, y=100)

heading_result_label = tk.Label(root, text="", justify="left", font=('bold', 14))
heading_result_label.pack(pady=5)

result_label = tk.Label(root, text="", justify="left", font=14)
result_label.place(x=125, y=190)

root.mainloop()
