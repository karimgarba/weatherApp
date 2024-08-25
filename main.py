from dotenv import load_dotenv
import os
import requests
import tkinter as tk

load_dotenv()

def getWeather(location):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":location}
    
    headers = {
    	"x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
    	"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    weatherInfo = response.json()

    locationName = weatherInfo['location']['name']
    temperature = weatherInfo['current']['temp_c']
    condition = weatherInfo['current']['condition']['text']

    print(response.json())
    print(f"{locationName}: Temperature {temperature}°C, Condition: {condition}")

    return f"{locationName}: Temperature {temperature}°C, Condition: {condition}"

def displayWeather(locationEntry, resultLabel, imageLabel):
    location = locationEntry.get()
    weatherInfo = getWeather(location)
    resultLabel.config(text=weatherInfo)

    icon_url = "https:" + weatherInfo['current']['condition']['icon']
    icon_response = requests.get(icon_url)
    icon = tk.PhotoImage(data=icon_response.content)

def main():
    root = tk.Tk()
    root.title("Weather App")

    locationEntry = tk.Entry(root)
    locationEntry.pack()

    imageLabel = tk.Label(root)
    imageLabel.pack()  
    
    resultLabel = tk.Label(root, text="Weather will be displayed here") 
    resultLabel.pack()

    # Use lambda to correctly pass arguments to getWeather when the button is clicked
    fetchButton = tk.Button(root, text="Fetch Weather", command=lambda: displayWeather(locationEntry, resultLabel, imageLabel))
    fetchButton.pack()

    root.mainloop()

if __name__ == "__main__":
    main()