#!/usr/bin/env python
import os
import argparse as ap
import sounddevice as sd
import soundfile as sf
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

parser = ap.ArgumentParser(
    prog = "musicgen",
    description = "Generates music based on keywords",
    epilog="Buy me a coffee",
)
parser.add_argument('-k', '--keyword', nargs='+', help="<Required> prompt keyword", required=True)
parser.add_argument('-f', '--fileprefix', type=str, help="<Required> output file prefix", required=True)
parser.add_argument('-p', '--play', action='store_true', help="<Required> output file prefix" )
args = parser.parse_args()


def play_audio(output_file):
    # Extract data and sampling rate from file
    data, fs = sf.read(output_file, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing

def gen_music(model, descriptions):
    model.set_generation_params(duration=5) #seconds
    #wav = model.generate_unconditional(2) #no idea
    return model.generate(descriptions)

def write_music(sample_rate, file_prefix, wav_model):
    for idx, one_wav in enumerate(wav_model):
        audio_write(f'{idx}_{file_prefix}', one_wav.cpu(), sample_rate, strategy="loudness")

file_prefix = args.fileprefix
descriptions = args.keyword
model = MusicGen.get_pretrained('small')
wav_model = gen_music(model, descriptions)
write_music(model.sample_rate, file_prefix, wav_model)
os.replace(f'0_{file_prefix}.wav', f'{file_prefix}.wav')

if args.play:
    play_audio(f'{file_prefix}.wav')
