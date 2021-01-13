#!/usr/bin/env python3

import sys
import time
from pipeline import *

def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def main(infile, outdir, n_jobs):
    print()
    print(get_time() + " Loading and transforming data to features ...")
    x_train, x_test, y_train, y_test, eval_classes = preprocess(infile)
    print()
    print(get_time() + " Start training CRF model ...")
    crf = training(x_train, y_train, eval_classes, outdir, n_jobs)
    print()
    print(get_time() + " Evaluating model on test set ...")
    evaluation(x_test, y_test, crf, eval_classes)

main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
