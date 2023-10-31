import subprocess

# Check if the termux-api package is installed
try:
    subprocess.run(['termux-api', 'wifi-enable'])
    print('Wi-Fi settings opened successfully.')
except FileNotFoundError:
    print('Error: termux-api package not found. Please install it using "pkg install termux-api".')
except Exception as e:
    print('Error:', e)
