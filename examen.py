import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

#4168

frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)

wave770_ = frecuencia770.make_wave(duration=0.5, start=0, framerate=44100)
wave1209_ = frecuencia1209.make_wave(duration=0.5, start=0, framerate=44100)

frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)

wave697 = frecuencia697.make_wave(duration=0.5, start=0.5, framerate=44100)
wave1209 = frecuencia1209.make_wave(duration=0.5, start=0.5, framerate=44100)

frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)

wave770 = frecuencia770.make_wave(duration=0.5, start=1, framerate=44100)
wave1477 = frecuencia1477.make_wave(duration=0.5, start=1, framerate=44100)

frecuencia852 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1209, amp=1, offset=0)

wave852 = frecuencia852.make_wave(duration=0.5, start=1.5, framerate=44100)
wave1336 = frecuencia1209.make_wave(duration=0.5, start=1.5, framerate=44100)

wavesonido1 = wave770_ + wave1209_
wavesonido2 = wave697 + wave1209
wavesonido3 = wave770 + wave1477
wavesonido4 = wave852 + wave1336


wave_sum = wavesonido1 + wavesonido2 + wavesonido3 + wavesonido4 

wave_sum.write("sonido_resultante.wav")