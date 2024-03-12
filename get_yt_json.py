import subprocess
import json
import sys
import os

def save_to_file(data, filename="yt_dlp_data.json"):
  directory = "jsonData"
  file_path = os.path.join(directory, filename)
  
  if not os.path.exists(directory):
    os.makedirs(directory)

  with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=2)


def get_yt_dlp_json(url):
  command = f'yt-dlp --dump-json "{url}"'
  output = os.popen(command).read()
  return output

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python save_yt_dlp_data.py <YouTube_URL>")
    sys.exit(1)

  yt_url = sys.argv[1]
  yt_dlp_data = get_yt_dlp_json(yt_url)

  if yt_dlp_data:
    print("JSON data saved to yt_dlp_data.json")
    save_to_file(yt_dlp_data)
  else:
    print("Failed to retrieve JSON data. Check the URL and make sure yt-dlp is installed.")