from flask import Flask, render_template, request
from extractor import extractVideoData

app = Flask(__name__)

@app.route('/')
def main_page():
  return render_template('index.html')

@app.route('/download', methods=["POST"])
def download():
  videoUrl = request.form["video_url"]
  videoData = extractVideoData(videoUrl)

  title = videoData["title"]
  formats = filterFormats(videoData["formats"])
  thumbnail = videoData["thumbnail"]

  return render_template(
    'download.html',
    title=title,
    formats=formats,
    thumbnail=thumbnail
  )


def filterFormats(formats):
  filteredFormats = excludeFormats(formats)
  result = removeDuplicateQualities(filteredFormats)

  return result

def removeDuplicateQualities(formats):
  encounteredResolutions = set()
  filteredFormats = []

  for format_ in formats:
      # Extract the resolution from the formatName
      format_parts = format_["formatName"].split(' ')
      resolution = None

      # Search for resolution enclosed in brackets
      for part in format_parts:
          if part.startswith('(') and part.endswith(')'):
              resolution = part[1:-1]  # Remove brackets
              break

      # If resolution found and not encountered before, add format to filtered list
      if resolution and resolution not in encounteredResolutions:
          filteredFormats.append(format_)
          encounteredResolutions.add(resolution)

  print("removeDuplicateQualities() result:")
  print(filteredFormats)

  return filteredFormats


def excludeFormats(formats):
  excludedFormats = ["storyboard", "ultralow"]
  filteredFormats = []

  for format_ in formats:
    excludeFlag = False

    for excludedFormat in excludedFormats:
      if excludedFormat in format_["formatName"]:
        excludeFlag = True 
        break
    
    if not excludeFlag:
      filteredFormats.append(format_)

  print("exludeFormats() result:")
  print(filteredFormats)

  return filteredFormats


if __name__ == '__main__':
  app.run(host='0.0.0.0', port='43345', debug=True)