import pyautogui
import time

def open_wifi_settings():
    try:
        # Open Android settings and navigate to Wi-Fi settings
        pyautogui.hotkey('ctrl', 'esc')  # Open recent apps (assuming it opens with the home button)
        time.sleep(1)  # Wait for recent apps to open
        pyautogui.press('esc')  # Close recent apps (if necessary)
        pyautogui.press('win')  # Open app drawer (assuming it opens with the home button)
        time.sleep(1)  # Wait for app drawer to open
        pyautogui.typewrite('Settings')  # Type 'Settings' to search for the Settings app
        time.sleep(1)  # Wait for search results to appear
        pyautogui.press('enter')  # Open the Settings app
        time.sleep(1)  # Wait for the Settings app to open
        pyautogui.press('tab', presses=4)  # Navigate to the Wi-Fi tab (adjust the number of tab presses as needed)
        pyautogui.press('enter')  # Enter Wi-Fi settings
        print('Wi-Fi settings opened successfully.')
    except Exception as e:
        print('Error:', e)

# Call the function to open Wi-Fi settings
open_wifi_settings()
