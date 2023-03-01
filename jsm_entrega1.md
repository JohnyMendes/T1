Primera tasca APA 2023: Anàlisi fitxer de so
============================================

## Nom i cognoms: Johny Silva Mendes

Proves i exercicis a fer i entregar
-----------------------------------
# 1.  frequencia: fx = 4kHz, fx = 9kHz, fx = 2kHz 

fent servir diferents freqüències per la sinusoide podem observar en una mateixa gràfica els diferents períodes de les diferents senyals i en una altre gràfica els diferents mòduls i fases en funció dels valors. 

# 2.
Resultat gràfic de 5 períodes de senyal: 

<img src="img/sinusoide2.png" width="480" align="center">

Representació del mòdul i la fase, en funció de la posició de cada valor: 

<img src="img/TF2.png" width="480" align="center">

# 3. Representar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en 0 a fm/2 en Hz

# moduldb = 20 * math.log10(abs(X)/max(abs(X)))


# 4. 

x_r, fm = sf.read('so_f4k.wav')