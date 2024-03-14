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

  print(formats)

  return render_template(
    'download.html',
    title=title,
    formats=formats,
    thumbnail=thumbnail
  )

def filterFormats(formats):
  excludedFormats = ["storyboard"]
  filteredFormats = []

  for format in formats:
    excludeFlag = False

    for excludedFormat in excludedFormats:
      if excludedFormat in format["formatName"]:
        excludeFlag = True 
        break
    
    if not excludeFlag:
      filteredFormats.append(format)
  
  return filteredFormats

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='43345', debug=True)