#!/bin/bash

# Make sure SRILM and RNNLM are installed

# Usage: bash test.sh <lang_name> <test_file>
# lang_name must be a folder in ../data/langs/

RNNLM_ROOT=/media/brij/SAARTHI/IIIT/SpeechLab/Projects/RNNLM/rnnlm-0.4b
DATA_ROOT=../data/langs

# Get input parameters
testlang="$1"
testfile="$2"

ngram -lm "$DATA_ROOT"/"$testlang"/srilm.model -ppl "$testfile" -debug 2 > temp.ppl

"$RNNLM_ROOT"/convert < temp.ppl > srilm.txt

"$RNNLM_ROOT"/rnnlm -rnnlm "$DATA_ROOT"/"$testlang"/rnnlm.model -test "$testfile" -lm-prob srilm.txt -lambda 0.5 | grep -Po 'PPL combine:\s\K[0-9.]*'
