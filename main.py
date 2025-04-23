import keyboard
import sounddevice as sd
import soundfile as sf
import json

def playSound(filename):
    data, samplerate = sf.read("sounds/"+filename)
    sd.play(data, samplerate, device=43)
    sd.wait()

sounds = json.load(open("conf.json"))
keyboard.add_hotkey(
    "alt+1", lambda: playSound(sounds["1"])
)

keyboard.wait()