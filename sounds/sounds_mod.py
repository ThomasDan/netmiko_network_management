# sound mod
from os import chdir
from playsound import playsound
from pathlib import Path


from pydub import AudioSegment
from pydub.playback import play

chdir(str(Path(__file__).parent))

def playsound_play(soundfile):
    playsound(soundfile)
    
def pydub_play_mp3(filename):
    song = AudioSegment.from_mp3(filename)
    play(song)
    
def pydub_play_wav(filename):
    song = AudioSegment.from_wav(filename)
    play(song)


play('notice.mp3')
pydub_play_mp3('notice.mp3')
pydub_play_wav('alert.wav')