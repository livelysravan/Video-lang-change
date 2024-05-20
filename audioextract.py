from moviepy.editor import VideoFileClip

def extract_audio(video_path, audio_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    video_clip.close()
video_path = "sravann.mp4"
audio_path = "path_to_save_extracted_audio_file.mp3"
extract_audio(video_path, audio_path)
print("Audio extracted successfully!")
