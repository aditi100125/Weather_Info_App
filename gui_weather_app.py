import tkinter as tk
from tkinter import messagebox
import requests
from config import API_KEY

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].title()
        return f"📍 City: {data['name']}\n🌡️ Temperature: {temp} °C\n☁️ Weather: {weather}"
    else:
        return None

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    result = fetch_weather(city)
    if result:
        result_label.config(text=result)
    else:
        result_label.config(text="❌ Unable to fetch weather. Check city name or API key.")

# --- GUI Setup ---
root = tk.Tk()
root.title("🌤 Weather App")
root.geometry("350x250")
root.resizable(False, False)

# --- UI Elements ---
title_label = tk.Label(root, text="Weather Info", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 12), width=25, justify='center')
city_entry.pack()

get_btn = tk.Button(root, text="Get Weather 🔍", command=show_weather, font=("Helvetica", 12))
get_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=10)

# --- Start App ---
root.mainloop()
