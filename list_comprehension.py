videos = [
    "Azure Computing Fundamentals",
    "Azure AI Fundamentals",
    "Engineering"
]

videos_without_spaces = [video for video in videos if " " not in video]
print(videos_without_spaces)  # Output: ['Engineering']