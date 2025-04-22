import keyboard

def playSound(a):
    print(a)

keyboard.add_hotkey(
    "alt+1", lambda: playSound("abs")
)

keyboard.wait()