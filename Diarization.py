import torch
from pyannote.core import Segment, Annotation
from pyannote.metrics.diarization import DiarizationErrorRate

"""
Код для запуска pyannote-audio.
Указываем анализируемый файл, далее преобразуем его в формат rttm (лог выводов диаризации) и вывод в консоль результатов для наглядности.
"""

if __name__ == '__main__':
    pipeline = torch.hub.load('pyannote/pyannote-audio', 'dia_ami')
    diarization = pipeline({'audio': 'MultipleVoices_Sirena.wav'})
    with open('MultipleVoices_Sirena1.wav', 'w') as f:
        diarization.write_rttm(f)
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f'{turn.start:.1f}\t{turn.end:.1f}\tspeaker{speaker}')
