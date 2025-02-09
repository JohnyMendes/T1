
# Johny Silva Mendes
# Tasca 1 - Codi 

# mòduls necessaris per llegir, escriure i representar un fitxer .wav
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# crear i guardar a un fitxer un senyal sinusoidal
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)

# Per representar gràficament 5 períodes de senyal
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 

#reproduir el senyal directament des de python
import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                # Reproducció d'àudio

# Per analitzar el senyal fent servir la Transformada Discreta de Fourier
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

# representar el mòdul i la fase, en funció de la posició de cada valor 
k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics

## Proves i exercicis a fer i entregar
# 1.  frequencia: fx = 4kHz

T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=4000                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_f4k.wav', x, fm)

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()  

import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                # Reproducció d'àudio

from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics


# 2. senyal a analitzar: fitxer wav (x_r, fm = sf.read('nom_fitxer.wav')).

x_r, fm = sf.read('so_f4k.wav')
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()  

from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         
plt.subplot(211)                      
plt.plot(k,abs(X))                    
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                  
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))    
plt.xlabel('Index k')                 
plt.ylabel('$\phi_x[k]$')             
plt.show()    

# 3. Representar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en 0 a fm/2 en HzRepresentar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en 0 a fm/2 en Hz
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_prueba.wav', x, fm)

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()  

import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                # Reproducció d'àudio

from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤  k<N

modul = abs(X) 

moduldb = 20 * np.log10(modul/max(modul))
plt.figure(1)                         # Nova figura
plt.subplot(fm/2)                      # Espai per representar el mòdul
plt.plot(k,moduldb)                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()


# 4. Llegir un fitxer d'audio i comprovar: 
# Freqüència de mostratge.
# Nombre de mostres de senyal.
# Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.
# Representa la seva transformada en dB en funció de la freqüència, en el marge 
# Quines son les freqüències més importants del segment triat?

import numpy as np 
import soundfile as sf
import matplotlib.pyplot as plt 

# fitxer d'àudio que vull llegir 
fitxer = 'so_prueba.wav'
x_r, fm = sf.read('so_prueba.wav')

# Freqüència de mostratge:
print('Freqüència de mostreig:', fm)

# Nombre de mostres de senyal:
print('Nombre de mostres de senyal:', len(x_r))

# segmente de senyal de 25ms 
inici_t = 0    # segons
final_t = 0.025  # segons
inici = int(inici_t * fm)
final = int(final_t * fm)
segment = x_r[inici:final]
t = np.linspace(inici_t, final_t, len(segment))

# Visualitzar el segment 
plt.figure()
plt.plot(t, segment)
plt.xlabel('Temps (s)')
plt.ylabel('Amplitud')
plt.title('Segment de senyal de 25ms')
plt.show()

# Calcula la transformada de Fourier del segment de senyal i converteix a dB
freq_eix = np.fft.fftfreq(len(segment)) * fm
fft = np.abs(np.fft.fft(segment))
fft_db = 20 * np.log10(fft)

# Visualitzar la transformada en dB en funció de la freqüència
plt.figure()
plt.plot(freq_eix, fft_db)
plt.xlabel('Freqüència (Hz)')
plt.ylabel('Amplitud (dB)')
plt.title('Transformada de Fourier del segment de senyal')
plt.xlim(0, fm/2)
plt.show()

# freqüències més importants del segment de senyal
max_indices = np.argsort(fft)[::-1][:5] 
max_frequencies = freq_eix[max_indices]
print('Les freqüències més importants del segment de senyal són:', max_frequencies)



