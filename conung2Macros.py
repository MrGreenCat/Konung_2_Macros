from pynput import keyboard, mouse
import time
import threading

keyboard_controller = keyboard.Controller()
mouse_controller = mouse.Controller()

def heal_macro(): #quick application of healing through the context menu of the main character
    
    keyboard_controller.press(keyboard.Key.ctrl)
    time.sleep(0.2)  

    mouse_controller.position = (66, 83)
    mouse_controller.click(mouse.Button.left, 2)
    time.sleep(0.1) 

    keyboard_controller.release(keyboard.Key.ctrl)
    time.sleep(0.2)  

    mouse_controller.position = (216, 301)
    mouse_controller.click(mouse.Button.left, 1)

def load_macro(): #fast loading from the top of the save list
    
    keyboard_controller.press(keyboard.Key.esc)
    keyboard_controller.release(keyboard.Key.esc)
    time.sleep(0.2)  

    mouse_controller.position = (494, 340)
    mouse_controller.click(mouse.Button.left, 1)
    time.sleep(0.2)  

    mouse_controller.position = (407, 226)
    mouse_controller.click(mouse.Button.left, 1)

double_click_in_progress = False
def double_click(x, y): #double-click when scrolling the mouse wheel to speed up character movement
    global double_click_in_progress
    if not double_click_in_progress:
        double_click_in_progress = True
        mouse_controller.position = (x, y)
        mouse_controller.click(mouse.Button.left, 2)
        time.sleep(0.1)  
        double_click_in_progress = False

def on_scroll(x, y, dx, dy):
    if dy > 0:  
        threading.Thread(target=double_click, args=(x, y)).start()

def on_press(key):
    try:
        if key.char == '6': 
            heal_macro()
        elif key.char == '4':
            load_macro()
    except AttributeError:
        pass

keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

mouse_listener = mouse.Listener(on_scroll=on_scroll)
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()

