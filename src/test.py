from os import listdir
from os.path import join
import operator

from subprocess import check_output

from decoder_ps import decode

import sys
args = sys.argv

test_txt = args[1]

langs_dir = '../data/langs'
langs = listdir(langs_dir)

correct = 0
total = 0

with open(test_txt) as f:
    for line in f.read().splitlines():
        total += 1
        sp = line.split()
        gt = sp[1]
        aufile = sp[0]

        phone_string = decode(aufile)

        testfile = 'tmp.txt'
        with open(testfile, 'wb') as testf:
            testf.write(phone_string)

        scores = []
        sum_scores = 0.0
        for l in langs:
            sc = float(check_output(["bash", "test.sh", l, testfile]))
            scores.append(sc)
            sum_scores += sc

        scores = [1.0 - (s/sum_scores) for s in scores]
        index, value = max(enumerate(scores), key=operator.itemgetter(1))

        pred = langs[index]
        print "Ground truth: {}, Predicted: {}".format(gt, pred)

        if gt == pred:
            correct += 1

print "Accuracy: ", float(correct) * 100.0 / total



