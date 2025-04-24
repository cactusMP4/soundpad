import keyboard
import sounddevice as sd
import soundfile as sf
import json


def playSound(soundIndex):
    config = json.load(open("conf.json"))

    filename = config["sounds"][str(soundIndex)]
    print(filename)
    if filename == None: return
    data, samplerate = sf.read("sounds/"+filename)

    sd.play(data, samplerate, device=config["deviceIndex"])

#for loop works strangly for some reason
keyboard.add_hotkey("alt+1", lambda: playSound(1))
keyboard.add_hotkey("alt+2", lambda: playSound(2))
keyboard.add_hotkey("alt+3", lambda: playSound(3))
keyboard.add_hotkey("alt+4", lambda: playSound(4))
keyboard.add_hotkey("alt+5", lambda: playSound(5))
keyboard.add_hotkey("alt+6", lambda: playSound(6))
keyboard.add_hotkey("alt+7", lambda: playSound(7))
keyboard.add_hotkey("alt+8", lambda: playSound(8))
keyboard.add_hotkey("alt+9", lambda: playSound(9))
keyboard.add_hotkey("alt+0", lambda: playSound(0))

keyboard.wait()