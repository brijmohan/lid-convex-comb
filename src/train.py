import sys
import os
from os.path import join, isdir

import subprocess

from decoder_ps import decode

'''
Usage: python train.py train.txt
'''

args = sys.argv

train_txt = args[1]
lang_files = {}

# Read train.txt
with open(train_txt) as f:
    for line in f.read().splitlines():
        sp = line.split()
        lang = sp[1]
        if lang not in lang_files:
            lang_files[lang] = []
        lang_files.append(sp[0])

lang_dir = '../data/langs'
if not isdir(lang_dir):
    os.makedirs(lang_dir)

for l, lflist in lang_files.items():
    cldir = join(lang_dir, l)
    if not isdir(cldir):
        os.makedirs(cldir)

    # Create data to train phonotactic models
    nfiles = len(lflist)
    train_idx = round(nfiles * 0.8)
    with open(join(cldir, 'train.feats'), 'wb') as tfile,
         open(join(cldir, 'valid.feats'), 'wb') as vfile:
        for idx, aufile in enumerate(lflist):
            phone_string = decode(aufile)
            if idx < train_idx:
                tfile.write(phone_string)
            else:
                vfile.write(phone_string)

    # Train SRILM and RNNLM with training data
    subprocess.call(["bash", "train_phonotactics.sh", l])








