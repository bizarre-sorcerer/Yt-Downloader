import subprocess
import json
import sys

def get_yt_dlp_json(url):
  try:
    # Run yt-dlp command to get JSON data
    result = subprocess.run(["yt-dlp", "--dump-json", url], capture_output=True, text=True)
    if result.returncode == 0:
        return json.loads(result.stdout)
    else:
        print(f"Error running yt-dlp: {result.stderr}")
        return None
  except Exception as e:
    print(f"An error occurred: {e}")
    return None

def save_to_file(data, filename="yt_dlp_data.json"):
  with open(filename, "w") as json_file:
    json.dump(data, json_file, indent=2)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python save_yt_dlp_data.py <YouTube_URL>")
    sys.exit(1)

  yt_url = sys.argv[1]
  yt_dlp_data = get_yt_dlp_json(yt_url)

  if yt_dlp_data:
    save_to_file(yt_dlp_data)
    print("JSON data saved to yt_dlp_data.json")
  else:
    print("Failed to retrieve JSON data. Check the URL and make sure yt-dlp is installed.")