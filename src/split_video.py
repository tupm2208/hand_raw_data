import os
import cv2
import time
import librosa

def get_durations(audio_file):
    durations = librosa.get_duration(filename=audio_file)
    return durations

array = []

def count_frames(video_path):
    video = cv2.VideoCapture(video_path)
    c = 0
    while True:
        ret, frame = video.read()
        
        if not ret:
            break
        
        # en = cv2.imencode('.jpg', frame)
        # array.append(frame)

        c += 1
    
    return c

t1 = time.time()
video_path = "../datasets/Phát âm chuẩn - Anh ngữ đặc biệt - Saving Money (VOA)-Dfo-7GOtEY8.mkv"
c = count_frames(video_path)
durations = get_durations(video_path.replace('.mkv', '.f140.m4a'))
print("FPS: ", c/durations)
print(time.time() - t1)