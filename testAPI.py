# Import the required libraries
from tkinter import *
import requests
import json

# Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")
win.title("Cat Fact API ")

# Create a text box to display the response body
text = Text(win, height=10, width=50, wrap="word")
text.config(font="Arial, 12")

# Create a label widget
label = Label(win, text="Cat Facts")
label.config(font="Calibri, 14")

# Add the API URL
api_url = "https://catfact.ninja/fact"

# Define a function to retrieve the response
# and text attribute from the JSON response
def get_zen():
   response = requests.get(api_url).text
   response_info = json.loads(response)
   Fact = response_info["fact"]
   text.delete('1.0', END)
   text.insert(END, Fact)

# Create Next and Exit Button
b1 = Button(win, text="Next", command=get_zen)
b2 = Button(win, text="Exit", command=win.destroy)

label.pack()
text.pack()
b1.pack()
b2.pack()

get_zen()

win.mainloop()