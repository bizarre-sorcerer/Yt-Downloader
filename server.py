from flask import Flask, render_template, redirect, url_for, request
from extractor import extractVideoData
from filter_formats import filterFormats
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# app.config['SECRET_KEY'] = 'secret-key'
# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)

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


if __name__ == '__main__':
  app.run(host='0.0.0.0', port='43345', debug=True)