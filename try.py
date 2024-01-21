# this is intended to be an add on to an earlier project where, I used open weather maps api, to generate weather data
# in this version the goal is to implement tkinter into the program
# tkinter will be used to create a window, as well as labels, buttons to make the window more user friendly
#

import tkinter as tk
import requests

window = tk.Tk()
window.geometry("600x600")
img = ""
window.config(background="lightblue")
window_2 = tk.Label(window, image=img)
window_2.pack(pady=5) 
window.title("weather display")

# defining gif files
rain_path = tk.PhotoImage(file="rain.gif")
snow_path = tk.PhotoImage(file="snow.gif")
#clouds_path = tk.PhotoImage(file="clouds.gif")
thunder_path = tk.PhotoImage(file="thunder.gif")
#mist_path = tk.PhotoImage(file="mist.webp")
shower_rain_path = tk.PhotoImage(file="rain_shower.gif")

# initializing the variable for future use
desc = ""

def get_weather(city, results_label):
    global desc
    api_key = "e0949efa5949b475cf6c15b5d682ec4a"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    answer = requests.get(url).json()

    if answer['cod'] == '404':
        results_label.config(text="Error, not able to retrieve weather data")
    else:
        temp = answer['main']['temp']
        temp = round((temp - 273.15) * 9/5 + 32)
        desc = answer['weather'][0]['description']

        results_label.config(text=f"The temperature in {city} is: {temp}°F\nThe weather in {city} is: {desc}")

        update_background_image()


def search():
    city = entry_field.get()
    result_label.config(text="searching")
    get_weather(city, result_label)


def update_background_image():
    global img
    if 'rain' in desc:
        img = rain_path
    elif 'snow' in desc:
        img = snow_path
    #elif 'clouds' in desc:
        #img = clouds_path
    elif 'thunder' in desc:
        img = thunder_path
    #elif 'mist' in desc:
        #img = mist_path
    elif 'shower rain' in desc:
        img = shower_rain_path

    window_2.config(image=img)  # Update the image displayed in the window_2 label


# entry label for the user
entry_label = tk.Label(text="Type in a city", font="helvetica 30", bg="lightblue")
entry_label.pack(pady=5)

# entry field
entry_field = tk.Entry(window, fg="black", background="grey", font="Helvetica 20")
entry_field.pack(pady=10)

# search button
search_button = tk.Button(window, font="helvetica 40", text="Search", command=search)
search_button.pack(pady=5)

# result label
result_label = tk.Label(window, font="Helvetica 30", fg="black", bg="lightblue")
result_label.pack(pady=5)

window.mainloop()

# currently the window is failing to place gif files as needed for the background
# if it does load the gifs, they are in the forms of images not gifs, apparently tkinter is not suited to handle gifs according to stack overflow
# However window is fully operational and uses tkinter as I intend, aside from the background
# temporarily, made the background light blue until it can be fixed
# when coming back, it would be better to use another library other than tkinter to execute the project as intended