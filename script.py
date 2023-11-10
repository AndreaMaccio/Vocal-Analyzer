import librosa
from pydub import AudioSegment
import numpy as np

def analyze_pitch_and_compare(file_user, file_original):
    # Converti da MP3 a WAV
    sound_user = AudioSegment.from_mp3(file_user)
    sound_original = AudioSegment.from_mp3(file_original)
    sound_user.export("user_recording.wav", format="wav")
    sound_original.export("original_song.wav", format="wav")

    # Carica gli audio con librosa
    y_user, sr_user = librosa.load("user_recording.wav")
    y_original, sr_original = librosa.load("original_song.wav")

    # Estrazione delle informazioni di pitch
    pitches_user, magnitudes_user = librosa.piptrack(y=y_user, sr=sr_user)
    pitches_original, magnitudes_original = librosa.piptrack(y=y_original, sr=sr_original)

    # Calcoliamo il pitch per ogni frame e poi prendiamo la media
    pitch_user = []
    for t in range(pitches_user.shape[1]):  # itera tra i frame
        index = magnitudes_user[:, t].argmax()
        pitch = pitches_user[index, t]
        if pitch > 0:  # consider only frames with a pitch
            pitch_user.append(pitch)
    
    pitch_original = []
    for t in range(pitches_original.shape[1]):  # itera tra i frame
        index = magnitudes_original[:, t].argmax()
        pitch = pitches_original[index, t]
        if pitch > 0: # considera solo i frame con un pitch
            pitch_original.append(pitch)

    # Calcoliamo la media dei pitch per entrambe le tracce
    pitch_user_mean = np.mean(pitch_user) if pitch_user else 0
    pitch_original_mean = np.mean(pitch_original) if pitch_original else 0

    # Confronto dei pitch e calcolo della differenza
    pitch_difference = np.abs(pitch_user_mean - pitch_original_mean)

    return pitch_difference

difference = analyze_pitch_and_compare('path_to_sang_mp3', 'path_to_original_mp3')
if 0<difference<5:
    print(f'La differenza di {difference} Hz è piccola! Ottima intonazione!')
elif 5<=difference<=20:
    print(f'La differenza di {difference} Hz è media! Leggermente fuori tono!')
else:
    print(f'La differenza di {difference} Hz è graande! Fuori tono!')