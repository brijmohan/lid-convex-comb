# Convex combination of phonotactics

Code for paper
[Significance of neural phonotactic models for large-scale spoken language identification (IJCNN 2017)](https://www.researchgate.net/publication/313323989_Significance_of_neural_phonotactic_models_for_large-scale_spoken_language_identification)

This package lets you perform language identification over spoken utterances. Following steps explain how to setup the package, train the model and then test over unseen utterances. Please read the paper linked aboved for more details.

## Setup

The setup requires installation of RNNLM and SRILM. Please download and install them before proceeding to install this package.

* RNNLM: untar `src/rnnlm-0.4b.tgz` and run `make` inside the extracted folder to build the RNNLM package. Update the RNNLM path in `src/train_phonotactics.sh` and `src/test.sh`.
* SRILM: Follow the instructions at given [link](http://www.speech.sri.com/projects/srilm/download.html) to install.

Finally you must have have `ngram-count`, `ngram` and `rnnlm` in your PATH.

Next we need to setup python environment. Follow the commands to setup the environment.

```
cd lid-convex-comb
virtualenv venv
. venv/bin/activate
pip install -r src/requirements.txt
```

## Training

```
cd src
python train.py train.txt
```

`train.py` requires `train.txt` which has the following format:
```
audio_file_path_1 <tab> language_tag1
audio_file_path_2 <tab> language_tag1
audio_file_path_3 <tab> language_tag1
audio_file_path_4 <tab> language_tag2
audio_file_path_5 <tab> language_tag2
audio_file_path_6 <tab> language_tag2
.
.
.
```

Create another file named `test.txt` with similar format. After training is finished, make sure `data/langs` directory has a unique directory for each language for which you trained. Now run the following commands for testing on unseen data.
```
cd src
python test.py test.txt
```

## Troubleshooting

Please contact me for any issues at brijmohanlal.s [at] research [dot] iiit [dot] ac [dot] in.
