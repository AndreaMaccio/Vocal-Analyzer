# Vocal-Analyzer
 The Vocal Pitch Analyzer is designed to help singers and music enthusiasts compare their pitch to that of an original song. The script takes as input two audio files in MP3 format: a user recording and an original track. Calculates and returns the average pitch difference between the two tracks, providing useful pitch feedback.
# Installation
 ```pip install -r requirements.txt```
# Use
 To use the script, import the analyze_pitch_and_compare function from the script and pass the audio file paths as arguments:
```
from pitch_analyzer import analyze_pitch_and_compare
difference = analyze_pitch_and_compare('path_to_user_recording.mp3', 'path_to_original_track.mp3')
print(f"Differenza di pitch: {difference} Hz")
```
