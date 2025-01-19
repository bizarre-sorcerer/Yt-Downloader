import os
import json

def extractFormatData(formats):
  result = []
  
  for format in formats:
    result.append({
      "extension": format["ext"],
      "formatName": format["format"],
      "url": format["url"]
    })

  return result 


def removeDuplicateQualities(formats):
  encounteredResolutions = set()
  filteredFormats = []

  for format_ in formats:
      # Извлечение разрешения из formatName
      format_parts = format_["formatName"].split(' ')
      resolution = None

      # Убирает скобки лишние с строки формата
      for part in format_parts:
          if part.startswith('(') and part.endswith(')'):
              resolution = part[1:-1]  
              break

      # Если разрешение найдено и не встречалось ранее, формат добавляется в список фильтров
      if resolution and resolution not in encounteredResolutions:
        filteredFormats.append(format_)
        encounteredResolutions.add(resolution)

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

  return filteredFormats


def filterFormats(formats):
  filteredFormats = excludeFormats(formats)
  result = removeDuplicateQualities(filteredFormats)

  return result


def getVideoData(url):
  command = f"yt-dlp --dump-json {url}"
  output = os.popen(command).read()

  try:
    videoData = json.loads(output)
    
    formats = extractFormatData(videoData["formats"])
    filteredFormats = filterFormats(formats)
    
    title = videoData["title"]
    thumbnail = videoData["thumbnail"]
      
    return {
      "title": title, 
      "formats": filteredFormats,
      "thumbnail": thumbnail
    }
    
  except Exception as e: 
    return {
      "title": "", 
      "formats": "",
      "thumbnail": ""
    }


def extract(videoUrl):
    videoData = getVideoData(videoUrl)
    formats = videoData["formats"]
    thumbnail = videoData["thumbnail"]
    title = videoData['title']

    return {
       "title": title,
       "formats": formats,
       "thumbnail": thumbnail
    }