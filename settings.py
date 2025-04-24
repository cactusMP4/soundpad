import json
import tkinter as tk
from tkinter import ttk
from sounddevice import query_devices


def getIndexFromItem(item: str):
    goingThroNumbers = False
    index = ""
    for char in item:
        if char == "]":
            return int(index)
        if goingThroNumbers:
            index += char
        if char == "[":
            goingThroNumbers = True


def select():
    selected_item = combo_box.get()

    jsonObj = json.load(open("conf.json"))
    jsonObj["deviceIndex"] = getIndexFromItem(selected_item)

    with open("conf.json", "w") as outfile:
        outfile.write(json.dumps(jsonObj))

root = tk.Tk()
root.resizable = True
root.title("Combobox Example")

label = tk.Label(root, text="Selected Item: ")
label.place(relx=0, rely=0, relwidth=1, relheight=0.2)
label.config(text="Select Device: ")

values = []
for device in query_devices():
    values.insert(len(values)+1, "["+str(device["index"])+"] "+device["name"])

combo_box = ttk.Combobox(root, values=values)
combo_box.pack(pady=5)
combo_box.place(relx=0, rely=0.2, relwidth=1)

combo_box.set("🎃")

combo_box.bind("<<ComboboxSelected>>", select)

root.mainloop()
