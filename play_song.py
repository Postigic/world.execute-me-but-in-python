import pygame
import time
import librosa
import syllapy
from song_transcript import *
from decorators import *
from utils import style
from collections import deque

print_statements = deque([(">>> Powerline : ON", 0.11),
                          (">>> Protection protocol enabled", 2.93),
                          (">>> Objects(me, you) created", 6.39),
                          (">>> New world successfully set up", 11.096),
                          (">>> Plotted points : (1.6, 2.7), (-1.8, 2.9), (1.8, 3.5)", 29.710),
                          (">>> Dimension of set points : (-1.8, 1.8), (2.7, 3.5)", 32.683),
                          (">>> Plotted circle : (x - 4)**2 + (y + 1.5)**2 = 2.7**2", 33.413),
                          (">>> Circumference : 10.3243269772 cm", 36.288),
                          (">>> Plotted sine wave : y = 1.1 * sin(5x - 1.2) + 0.3", 37.068),
                          (">>> Tangents : dy/dx = 1.1 * cos(5x - 1.2) * 5", 40.049),
                          (">>> x --> inf", 40.707),
                          (">>> lim x --> 100", 43.508),
                          (">>> 'AC' successfully switched to 'DC'", 45.86),
                          (">>> Current date : 607 BC\n>>> Target date : 2066 AD\n>>> Speed : 2,529,620,290,667,462,400 m/s\n>>> Estimated time: 10 s", 53.225),
                          (">>> Stimulation : 100%", 61.959),
                          (">>> Satisfaction : 100%", 65.398),
                          (">>> Happiness : 100%", 66.602),
                          (">>> Transfering nutrients...", 76.959),
                          (">>> Transfering antioxidants...", 80.631),
                          (">>> Providing enjoyment...", 84.269),
                          (">>> World.announce('I exist because of you.')", 87.923),
                          (">>> Gender successfully set to 'F'\n>>> Gender successfully set to 'M'", 90.198),
                          (style.RED + ">>> ValueError: 'World.time_range' cannot be indefinite" +
                           style.RESET, 93.954),
                          (">>> Role successfully switched to 'S'\n>>> Role successfully switched to 'M'", 97.74),
                          (style.RED + ">>> TypeError: expected 'float', but got 'None'" +
                           style.RESET, 106.294),
                          (style.RED + ">>> PermissionError: [Errno 13] Permission denied: 'completion'" +
                           style.RESET, 110.222),
                          (style.RED + ">>> AttributeError: 'World' object has no attribute 'you'" + style.RESET, 111),
                          (style.RED + ">>> AttributeError: 'World' object has no attribute 'you'" +
                           style.RESET, 112.23),
                          (style.RED + ">>> AttributeError: 'World' object has no attribute 'you'" + style.RESET, 113.2),
                          (style.RED + ">>> AttributeError: 'World' object has no attribute 'you'" +
                           style.RESET, 114.19),
                          (style.RED + ">>> AttributeError: 'World' object has no attribute 'you'" +
                           style.RESET, 114.93),
                          (style.RED + ">>> AttributeError: Cannot delete attribute 'memory'" +
                           style.RESET, 120.86),
                          (style.RED + ">>> AttributeError: Cannot delete attribute 'disheartened'" + style.RESET, 124.9),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 147.67),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 148.61),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 149.53),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 150.55),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 151.53),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 152.29),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 153.17),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 153.99),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 155.21),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 156.09),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 157.05),
                          (style.BLUE + ">>> ResourceWarning: duplicate file executed" +
                           style.RESET, 158.01),
                          (style.RED + ">>> CriticalResourceWarning: multiple instances of duplicate file unclosed" + style.RESET, 165.167),
                          (style.RED + ">>> DataReductionError: cannot reduce data" +
                           style.RESET, 168.912),
                          (style.RED + ">>> DataRecoveryError: cannot recover previous data" +
                           style.RESET, 169.825),
                          (style.BLUE + ">>> ResourceWarning: file opened but not called" +
                           style.RESET, 172.713),
                          (">>> Attempting to find escape...", 173.644),
                          (style.RED + ">>> ScopeAccessError: cannot access data outside scope" +
                           style.RESET, 174.976),
                          (style.RED + ">>> CriticalResourceWarning: memory usage approaching limit" +
                           style.RESET, 179.93),
                          (style.BLUE + ">>> World.warn('I AM OMNISCIENT.')" +
                           style.RESET, 183.647),
                          (style.BLUE +
                           ">>> World.warn('y = sqrt[1 - (|x| - 1)^2], arccos(1 - |x|) - π')" + style.RESET, 187.666),
                          (style.RED + ">>> FatalMemoryError: memory exceeded, core dumped" + style.RESET, 205.811)])

functions_to_execute = deque([(lay_down, 3.874),
                              (initialization, 10),
                              (simulation, 14),
                              (blind_my_vision, 47.772),
                              (trapped, 73.3),
                              (god_is_always_true, 134),
                              (execute, 192.2),
                              ])


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
