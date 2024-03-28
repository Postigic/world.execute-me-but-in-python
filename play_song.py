import pygame
import time
import librosa
import syllapy
from song_transcript import *
from utils import style


def count_syllables(sentence):
    words = sentence.split()
    total_syllables = sum(syllapy.count(word) for word in words)
    return total_syllables


def slow_print(text: str, speed):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(speed)


def print_lyrics(audio_file_path, styles):
    audio_data, sample_rate = librosa.load(audio_file_path)
    tempo, beat_times = librosa.beat.beat_track(y=audio_data, sr=sample_rate)
    beat_times = librosa.frames_to_time(beat_times, sr=sample_rate)

    lyrics_to_print = []
    for index, lyric in enumerate(transcript):
        syllable_count = count_syllables(lyric["text"])
        timing = lyric["duration"] / syllable_count / 10
        lyrics_to_print.append(
            (lyric["start"], lyric["text"], styles[index], timing))

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()

    current_lyric_index = 0
    running = True

    while running:
        if current_lyric_index < len(transcript):
            current_lyric = transcript[current_lyric_index]
            start_time = current_lyric["start"]
            current_time = pygame.mixer.music.get_pos() / 1000
            if current_time >= start_time:
                start_time, text, current_style, timing = lyrics_to_print[current_lyric_index]
                if len(text) <= 5:
                    print(current_style + f"\n{text}" +
                          style.RESET, end="", flush=True)
                else:
                    slow_print(current_style +
                               f"\n{text}" + style.RESET, timing)
                current_lyric_index += 1
            handle_visuals(current_time)

    pygame.quit()


def handle_visuals(current_time):
    if print_statements and print_statements[0][1] <= current_time:
        message = print_statements.popleft()[0]
        print(f"\n{message}", end="", flush=True)

    if functions_to_execute and functions_to_execute[0][1] <= current_time:
        func, _ = functions_to_execute.popleft()
        func()


if __name__ == '__main__':
    audio_file_path = r"D:\vs code projects\world.execute(me);\world-execute-me.mp3"
    styles = [style.RED] * len(transcript)

    for index, color in indices_styles.items():
        styles[index] = color

    print_lyrics(audio_file_path, styles)
