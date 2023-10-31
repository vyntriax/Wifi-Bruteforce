import subprocess

def open_wifi_settings():
    try:
        # Open Android settings and navigate to Wi-Fi settings
        subprocess.run(['am', 'start', '-a', 'android.settings.SETTINGS'])
        subprocess.run(['input', 'keyevent', '20'])
        subprocess.run(['input', 'keyevent', '20'])
        subprocess.run(['input', 'keyevent', '66'])
        print('Wi-Fi settings opened successfully.')
    except Exception as e:
        print('Error:', e)

# Call the function to open Wi-Fi settings
open_wifi_settings()
