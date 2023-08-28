import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = '35bf50e9d28410391fbe6b67481b8c22'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.label_city = tk.Label(self.root, text="Enter city:")
        self.label_city.pack(pady=20)

        self.entry_city = tk.Entry(self.root)
        self.entry_city.pack(pady=10)

        self.button_fetch = tk.Button(self.root, text="Fetch Weather", command=self.fetch_weather)
        self.button_fetch.pack(pady=20)

        self.label_weather = tk.Label(self.root, font=('bold', 20))
        self.label_weather.pack(pady=20)

    def fetch_weather(self):
        city = self.entry_city.get()
        if not city:
            messagebox.showerror("Error", "City name cannot be empty!")
            return

        response = requests.get(BASE_URL.format(city, API_KEY))
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            weather = data['weather'][0]['description']
            self.label_weather.config(
                text=f"Weather in {city}:\nTemperature: {temperature}°C\nDescription: {weather.capitalize()}")
        else:
            print(response.content)  # This will print the error content
            self.label_weather.config(text="")
            messagebox.showerror("Error", f"Cannot fetch weather for {city}!")


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
