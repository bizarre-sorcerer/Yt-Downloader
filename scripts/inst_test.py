import subprocess
import json

# Your Instagram username and password
username = 'username here'
password = 'password here'

# The URL of the Instagram video you want to download
url = 'https://www.instagram.com/p/C2hy6TUN3kU/'

# The command to run yt-dlp 
# yt-dlp -u 'username' -p 'password' --cookies 'cookies.txt' --write-info-json -o '%(title)s.%(ext)s' 'https://www.instagram.com/p/C2hy6TUN3kU/'
command = [
    'yt-dlp',
    '-u', username,
    '-p', password,
    '--cookies', 'cookies.txt',
    '--write-info-json',
    '-o', '%(title)s.%(ext)s',
    url
]

# Run the command and get the output
output = subprocess.run(command, capture_output=True, text=True)

# If there's an error, print it
if output.stderr:
    print(f'Error: {output.stderr}')

# If there's output, parse the JSON
if output.stdout:
    info = json.loads(output.stdout)
    print(info)