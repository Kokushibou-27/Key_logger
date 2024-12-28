from pynput import keyboard

def press(key):
    try:
        print('{0}'.format(
            key.char))
    except AttributeError:
        print('{0}'.format(
            key))

def release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(
        on_press = press,
        on_release= release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press= press,
    on_release= release)
listener.start()