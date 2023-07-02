#!/usr/bin/env python
import sys
import os
import argparse as ap
import sounddevice as sd
import soundfile as sf
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write


MAX_SECONDS = 30
VALID_MODELS = [ "small", "medium", "melody", "large" ];
DEFAULT_MODEL = "small"

parser = ap.ArgumentParser(
    prog = "musicgen",
    description = "Generates music based on keywords",
    epilog="Buy me a coffee",
)
parser.add_argument('-k', '--keyword', nargs='+', help="<Required> prompt keyword", required=True)
parser.add_argument('-f', '--fileprefix', type=str, help="<Required> output file prefix", required=True)
parser.add_argument('-p', '--play', action='store_true', help="<Required> output file prefix" )
parser.add_argument('-s', '--seconds', type=int, help="<Optional> Seconds to record - defaults to 5s. Capped at 30s", default=5 )
parser.add_argument('-m', '--modelname', type=str, help="<Optional> Model to use: small(30M), medium | meldoy (1.5B), large (3.3B). Default to small", default=DEFAULT_MODEL )
args = parser.parse_args()


def play_audio(output_file):
    # Extract data and sampling rate from file
    data, fs = sf.read(output_file, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing

def gen_music(model, descriptions, seconds):
    model.set_generation_params(duration=seconds) #seconds
    #wav = model.generate_unconditional(2) #no idea
    return model.generate(descriptions)

def write_music(sample_rate, file_prefix, wav_model):
    for idx, one_wav in enumerate(wav_model):
        audio_write(f'{idx}_{file_prefix}', one_wav.cpu(), sample_rate, strategy="loudness")

def get_duration(seconds):
    if seconds > MAX_SECONDS:
        print(f'Capping at {MAX_SECONDS} seconds', file=sys.stderr)
        return MAX_SECONDS
    else:
        return seconds

def validate_model(model_name):
    if not model_name in VALID_MODELS:
        print(f'{model_name} not in valid. Defaulting to {DEFAULT_MODEL}.', file=sys.stderr)
        return DEFAULT_MODEL
    return model_name

file_prefix = args.fileprefix
descriptions = args.keyword
seconds = get_duration(args.seconds)
model_name = validate_model(args.modelname)

# Load model
model = MusicGen.get_pretrained(model_name)

# Generate music
wav_model = gen_music(model, descriptions, seconds)
write_music(model.sample_rate, file_prefix, wav_model)
os.replace(f'0_{file_prefix}.wav', f'{file_prefix}.wav')

if args.play:
    play_audio(f'{file_prefix}.wav')
