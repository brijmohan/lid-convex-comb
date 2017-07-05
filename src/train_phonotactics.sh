#!/bin/bash

# Make sure you have RNNLM and SRILM installed on your system and paths have been set here
RNNLM_ROOT=/media/brij/SAARTHI/IIIT/SpeechLab/Projects/RNNLM/rnnlm-0.4b
DATA_ROOT=../data/langs

langname="$1"

# Train RNNLM
#"$RNNLM_ROOT"/rnnlm -train "$DATA_ROOT"/"$langname"/train.feats -rnnlm "$DATA_ROOT"/"$langname"/rnnlm.model -valid "$DATA_ROOT"/"$langname"/valid.feats -class 6 -min-improvement 1 -hidden 300 -rand-seed 1 -debug 2 -bptt 2 -bptt-block 10 -direct-order 3 -direct 2 -binary
"$RNNLM_ROOT"/rnnlm -train "$DATA_ROOT"/"$langname"/train.feats -rnnlm "$DATA_ROOT"/"$langname"/rnnlm.model -valid "$DATA_ROOT"/"$langname"/valid.feats -hidden 300 -rand-seed 1 -debug 2 -binary

# Train NGRAMS
cat "$DATA_ROOT"/"$langname"/train.feats "$DATA_ROOT"/"$langname"/valid.feats > "$DATA_ROOT"/"$langname"/train_valid.feats
ngram-count -text "$DATA_ROOT"/"$langname"/train_valid.feats -lm "$DATA_ROOT"/"$langname"/srilm.model -order 3