from pynput import keyboard

def press(key):
    try:
        print('{0}'.format(key.char), end="", flush=True)
    except AttributeError:
        print('{0}'.format(key), end="", flush=True)

def release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(
        on_press = press,
        on_release= release,
        suppress=True) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press= press,
    on_release= release,
    suppress= True)
listener.start()