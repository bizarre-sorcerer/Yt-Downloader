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
