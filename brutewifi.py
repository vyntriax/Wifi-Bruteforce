import pyautogui
import time

def open_wifi_settings():
    try:
        # Open Android settings and navigate to Wi-Fi settings
        pyautogui.hotkey('ctrl', 'esc')  # Open settings (assuming it opens with the home button)
        time.sleep(1)  # Wait for settings to open
        pyautogui.press('tab', presses=2)  # Navigate to the Wi-Fi tab
        pyautogui.press('enter')  # Enter Wi-Fi settings
        print('Wi-Fi settings opened successfully.')
    except Exception as e:
        print('Error:', e)

# Call the function to open Wi-Fi settings
open_wifi_settings()
