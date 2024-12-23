import tkinter as tk
import requests
import time

def getWeather(event=None):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=2779a9e7a14f07c64c5b5c3dd3586a40"
    try:
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info = condition + "\n" + str(temp) + "°C"
        final_data = (
            f"Max Temp: {max_temp}°C\n"
            f"Min Temp: {min_temp}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}"
        )

        label1.config(text=final_info)
        label2.config(text=final_data)
    except Exception as e:
        label1.config(text="Error fetching data")
        label2.config(text="Please check the city name or try again.")

# Initialize the main canvas
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.configure(bg="#ADD8E6")  # Light blue background

# Fonts
f = ("poppins", 15, "bold")  # Bold for additional data
t = ("poppins", 35, "bold")  # Bold for main info

# Entry field for city input
textfield = tk.Entry(canvas, font=t, justify="center", bg="white", fg="black", relief="flat", highlightbackground="#ffffff", highlightthickness=2)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

# Labels to display weather information
label1 = tk.Label(canvas, font=t, bg="#ADD8E6", fg="white", wraplength=500, justify="center")
label1.pack(pady=(10, 20))

label2 = tk.Label(canvas, font=f, bg="#ADD8E6", fg="white", wraplength=500, justify="center")
label2.pack()

# Run the main loop
canvas.mainloop()
