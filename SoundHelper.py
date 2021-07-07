from pydub import AudioSegment

"""
Объединение записей.
Параметры:
 -путь к изначальному файлу
 -пути к файлам, которые нужно присединить
 -имя файла результата
"""

def audio_join(start_sound, join_sounds, export_name):
    start = AudioSegment.from_file(start_sound, format="mp3")
    result = start
    for sound in join_sounds:
        curr_sound = AudioSegment.from_file(sound, format="mp3")
        result += curr_sound
    result.export(export_name, format="mp3")

"""
Форматирование из mp3 в wav формат.
Параметры:
 -путь к файлу
 -имя файла результата
"""

def mp3_to_wav(audio, export_name):
    aud = AudioSegment.from_file(audio, format="mp3")
    aud.export(export_name, format="wav")

"""
Добавление фона.
Параметры:
 -путь к начальному файлу
 -путь к файлу, который будем накладывать
 -с какого момента времени накладывать (1 секунда = 1000)
 -громкость файла фона (1 Дб = 1)
 -длительность записи, которую будем накладывать (1 секунда = 1000)
 -имя файла результата
"""

def add_background(original_file, background_file, position, loud_background, duration, export_name):
    orig = AudioSegment.from_file(original_file, format="wav")
    background_full = AudioSegment.from_file(background_file, format="wav")
    loud = background_full + loud_background
    background = loud[:duration]
    result = orig.overlay(background, position=position)
    result.export(export_name, format="wav")
    
"""
Повторение записи.
Параметры:
 -путь к файлу
 -сколько раз повторить
 -громкость (1 Дб = 1)
 -имя файла результата
"""
    
def multiple(original_file, times, loud, export_name):
    song = AudioSegment.from_wav(original_file)
    result_background = song * times
    louder = result_background + loud
    louder.export(export_name, format="wav")


PATH = ["clips/common_voice_ru_20149587.mp3",
        "clips/common_voice_ru_20149588.mp3"]

if __name__ == '__main__':

    # audio_join("Sirena.mp3", PATH, "Sirena1.mp3")
    # mp3_to_wav("Background1.mp3", "Background.wav")
    # add_background("SimpleTest.wav", "Background_White_Noise.wav", 0, 0, 100000, "SimpleTest_White_Noise.wav")

