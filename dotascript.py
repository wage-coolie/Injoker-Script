from pynput import keyboard
import pyautogui
# The key combination to check


# The key combination to check
COMBINATIONS = [
    {keyboard.KeyCode(char='1')},
    {keyboard.KeyCode(char='2')},
    {keyboard.KeyCode(char='3')},
    {keyboard.KeyCode(char='4')},
    {keyboard.KeyCode(char='5')},
    {keyboard.KeyCode(char='6')},
    {keyboard.KeyCode(char='7')},
    {keyboard.KeyCode(char='8')},
    {keyboard.KeyCode(char='9')},
    {keyboard.KeyCode(char='0')}
]

# The currently active modifiers
current = set()

def execute(key):
    if key==keyboard.KeyCode(char='1'):
        pyautogui.hotkey('q')
        pyautogui.hotkey('q')
        pyautogui.hotkey('q')
        pyautogui.hotkey('r')
        
    if key==keyboard.KeyCode(char='2'):
        pyautogui.hotkey('q')
        pyautogui.hotkey('q')
        pyautogui.hotkey('w')
        pyautogui.hotkey('r')
        
    if key==keyboard.KeyCode(char='3'):
        pyautogui.hotkey('q')
        pyautogui.hotkey('q')
        pyautogui.hotkey('e')
        pyautogui.hotkey('r')
        
    if key==keyboard.KeyCode(char='4'):
        pyautogui.hotkey('w')
        pyautogui.hotkey('w')
        pyautogui.hotkey('w')
        pyautogui.hotkey('r')

    if key==keyboard.KeyCode(char='5'):
        pyautogui.hotkey('w')
        pyautogui.hotkey('w')
        pyautogui.hotkey('q')
        pyautogui.hotkey('r')
        
    if key==keyboard.KeyCode(char='6'):
        pyautogui.hotkey('w')
        pyautogui.hotkey('w')
        pyautogui.hotkey('e')
        pyautogui.hotkey('r')
        
    if key==keyboard.KeyCode(char='7'):
        pyautogui.hotkey('q')
        pyautogui.hotkey('w')
        pyautogui.hotkey('e')
        pyautogui.hotkey('r') 

    if key==keyboard.KeyCode(char='8'):
        pyautogui.hotkey('e')
        pyautogui.hotkey('e')
        pyautogui.hotkey('e')
        pyautogui.hotkey('r')
        
    if key==keyboard.KeyCode(char='9'):
        pyautogui.hotkey('e')
        pyautogui.hotkey('e')
        pyautogui.hotkey('q')
        pyautogui.hotkey('r')
        
    if key==keyboard.KeyCode(char='0'):
        pyautogui.hotkey('e')
        pyautogui.hotkey('e')
        pyautogui.hotkey('w')
        pyautogui.hotkey('r')  
        
        

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        execute(key)

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

