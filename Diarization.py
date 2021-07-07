import torch
from pyannote.core import Segment, Annotation
from pyannote.metrics.diarization import DiarizationErrorRate

"""
Код для запуска pyannote-audio.
Указываем анализируемый файл, далее преобразуем его в формат rttm (лог выводов диаризации) и вывод в консоль результатов для наглядности.

pyAudioAnalysis запускается через консоль строкой:
python3 audioAnalysis.py speakerDiarization -i path/to/dirizationFile.wav --num 0 
num - количество кластеров(спикеров), на которые алгоритм должен разбить запись. Если 0, то происходит диаризация файла.
"""

if __name__ == '__main__':
    pipeline = torch.hub.load('pyannote/pyannote-audio', 'dia_ami')
    diarization = pipeline({'audio': 'MultipleVoices_Sirena.wav'})
    with open('MultipleVoices_Sirena1.wav', 'w') as f:
        diarization.write_rttm(f)
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f'{turn.start:.1f}\t{turn.end:.1f}\tspeaker{speaker}')

    metric = DiarizationErrorRate()

    hypothesis = Annotation()
    hypothesis[Segment(1, 12)] = "A"
    hypothesis[Segment(13, 33)] = "B"
    hypothesis[Segment(22, 42)] = "A"
    hypothesis[Segment(33, 47)] = "C"
    hypothesis[Segment(47, 72)] = "D"
    hypothesis[Segment(72, 91)] = "B"
    hypothesis[Segment(91, 112)] = "A"
    hypothesis[Segment(112, 133)] = "C"

"""
Подсчёт значения метрики. Гипотетическую разметку (то, что мы приблизительно хотим видеть) задаём сами, а практический результат находится в переменной diarization (алгоритм возвращает переменную типа Annotation)
"""

    value = metric(diarization, hypothesis)

