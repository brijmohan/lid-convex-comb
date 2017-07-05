import os
from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

import sox

# Replace with your own model directory
MODELDIR = "../venv/lib/python2.7/site-packages/pocketsphinx/model"
#DATADIR = "../venv/lib/python2.7/site-packages/pocketsphinx/data"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us'))
config.set_string('-jsgf', 'phone.gram')
config.set_string('-dict', 'phone.dic')
decoder = Decoder(config)

# Decode streaming data.
decoder = Decoder(config)

def transform_audio(ifpath, ofpath):
    tfm = sox.Transformer()
    tfm.convert(samplerate=16000.0, n_channels=1, bitdepth=16)
    tfm.norm()
    tfm.build(ifpath, ofpath)

def decode(fpath):
    # Convert audio to required format
    ofpath = 'tmp.wav'
    transform_audio(fpath, ofpath)

    decoder.start_utt()
    stream = open(ofpath, 'rb')
    while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
    else:
        break
    decoder.end_utt()
    os.remove(ofpath)

    return ' '.join([seg.word for seg in decoder.seg() if 'NULL' not in seg.word])

