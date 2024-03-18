import json
from tkinter import *
import requests

root = Tk()
root.title('Weather App')
root.geometry('600x100')
root.configure(background='lightblue')

def ziplookup():
    try:
        api_key = "1e95a19274b5dc630bc50c63be19aaa5"
        location = zip.get()
        uri = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        api = requests.get(uri).json()
        print(api)  # Print the entire API response

        if 'name' in api:
            location = api["name"]
            temperature = api["main"]["temp"]
            weather_description = api["weather"][0]["description"].capitalize()
            windspeed = api["wind"]["speed"]

            result_text = f"City: {location}\nTemperature: {temperature}°C\nWeather: {weather_description}\nWind Speed: {windspeed} m/s"
            myLabel = Label(root, text=result_text, font=('helvetica', 10), background='lightblue', justify=LEFT)
            myLabel.grid(row=2, column=0, columnspan=2)
        else:
            error_label = Label(root, text=f'Error: City "{location}" not found.', font=('helvetica', 10), background='lightblue')
            error_label.grid(row=2, column=0, columnspan=2)
    except Exception as e:
        error_label = Label(root, text='Error: ' + str(e), font=('helvetica', 10), background='lightblue')
        error_label.grid(row=2, column=0, columnspan=2)

zip = Entry(root)
zip.grid(row=4, column=5, padx=5, pady=5)
zipButton = Button(root, text='Lookup Zipcode', command=ziplookup)
zipButton.grid(row=4, column=6, padx=5, pady=5)

root.mainloop()