import keyboard
import sounddevice as sd
import soundfile as sf
import json

config = json.load(open("conf.json"))

def findDeviceIndex(name):
    devices = sd.query_devices()
    for index, device in enumerate(devices):
        if name in device["name"] and device["max_input_channels"] > 0:
            return index
    return None

def playSound(filename):
    data, samplerate = sf.read("sounds/"+filename)

    device = findDeviceIndex("CABLE Input (VB-Audio Virtual Cable), Windows DirectSound (0 in, 16 out)")

    sd.play(data, samplerate, device=device)
    sd.wait()

keyboard.add_hotkey("alt+1", lambda: playSound(config["sounds"]["1"]),)

keyboard.wait()