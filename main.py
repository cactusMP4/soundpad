import keyboard
import sounddevice as sd
import soundfile as sf

def play_audio(filename):
    data, samplerate = sf.read("sounds/"+filename)
    sd.play(data, samplerate, device=43)
    sd.wait()

keyboard.add_hotkey(
    "alt+1", lambda: play_audio("sfx_taunt.mp3")
)

keyboard.wait()