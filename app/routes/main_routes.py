from flask import render_template, request, Blueprint
from services.main_service import *

main_routes = Blueprint('main_routes', __name__, template_folder="../templates")

@main_routes.route('/')
def main_page():
    return render_template('index.html')

@main_routes.route('/download', methods=["POST"])
def download():
    videoUrl = request.form["video_url"]    
    
    videoData = extract(videoUrl)

    return render_template(
        'download.html',
        title=videoData['title'],
        formats=videoData['formats'],
        thumbnail=videoData['thumbnail']
    )
