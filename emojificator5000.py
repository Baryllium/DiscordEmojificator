from pynput.keyboard import Controller, Key, Listener
import pyperclip
import time

def translate(message):
    output = ""
    numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    inEmote = False
    for c in message:
        if c == ":":
            inEmote = not inEmote
            if not inEmote: output += ":"
        if inEmote:
            output += c
        elif c.isalpha():
            output += ":regional_indicator_" + c.lower() + ":" + chr(8203)
        elif c.isnumeric():
            output += ":" + numbers[int(c)] + ":" + chr(8203)
        elif c == " ":
            output += "   "
    return output

def actions():
    # if you're on macos, change ctrl to cmd
    kb.press(Key.ctrl_l)
    kb.tap("a")
    kb.release(Key.ctrl_l)
    time.sleep(0.5)
    kb.press(Key.ctrl_l)
    kb.tap("c")
    kb.release(Key.ctrl_l)
    message = pyperclip.paste()
    output = translate(message)
    pyperclip.copy(output)
    kb.tap(Key.backspace)
    kb.press(Key.ctrl_l)
    kb.tap("v")
    kb.release(Key.ctrl_l)

def on_press(key):
    global readMode, buffer, message
    # you can change the key to whatever doesn't do anything on its own
    if key == Key.ctrl_r:
        actions()

readMode = False
buffer = ""
message = ""
kb = Controller()

listener = Listener(on_press=on_press)
listener.start()
