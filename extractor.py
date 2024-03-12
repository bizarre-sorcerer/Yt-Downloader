import os
import json

videoUrl = "https://youtu.be/qYSWWGz9Z6s?si=Q8uQBHxQKypoNhCQ"

def extractFormatData(formatData):
  extension = formatData["ext"]
  formatName = formatData["format"]
  url = formatData["url"]

  return {
    "extension": extension,
    "formatName": formatName,
    "url": url
  }

def extractVideoData(url):
  # Получаем json данные на ютуб видео
  command = f"yt-dlp --dump-json {url}"
  output = os.popen(command).read()
  videoData = json.loads(output)

  # Нужные данные про видео вытаскиваю и сохраняю в переменные
  formats = videoData["formats"]
  formats = [extractFormatData(formatData) for formatData in formats] # Получает данные на все форматы
  title = videoData["title"]
  thumbnail = videoData["thumbnail"]
  
  return {
    "title": title, 
    "formats": formats,
    "thumbnail": thumbnail
  }

print(extractVideoData(videoUrl))