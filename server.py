from flask import Flask, render_template, request
from extractor import extractVideoData
from filter_formats import filterFormats
from reg import add_user

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


@app.route('/login', methods=['POST', 'GET'])
def login():
  if request.method == "GET":
    return render_template("login.html")
  
  elif request.method == "POST":
    username = request.form["login"]
    password = request.form['password']
    add_user(username, password)

  return render_template('login.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port='43345', debug=True)