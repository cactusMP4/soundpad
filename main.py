import keyboard
import sounddevice as sd
import soundfile as sf
import json


def playSound(soundIndex):
    config = json.load(open("conf.json"))

    filename = config["sounds"][str(soundIndex)]
    data, samplerate = sf.read("sounds/"+filename)

    sd.play(data, samplerate, device=config["deviceIndex"])

keyboard.add_hotkey("alt+1", lambda: playSound(1),)

keyboard.wait()