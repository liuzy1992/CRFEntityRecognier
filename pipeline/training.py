#!/usr/bin/env python3

import scipy.stats
import sklearn_crfsuite
from sklearn_crfsuite import metrics
from sklearn.metrics import make_scorer
from sklearn.model_selection import RandomizedSearchCV
import joblib

def training(x_train, y_train, eval_classes, outdir, n_jobs):
    crf = sklearn_crfsuite.CRF(algorithm='lbfgs',
                               max_iterations=100,
                               all_possible_transitions=True)

    params_space = {'c1': scipy.stats.expon(scale=0.5), 'c2': scipy.stats.expon(scale=0.05),}

    # use the same metric for evaluation
    f1_scorer = make_scorer(metrics.flat_f1_score, average='weighted', labels=eval_classes)

    # search
    rs = RandomizedSearchCV(crf, 
                            params_space,
                            cv=5,
                            verbose=1,
                            n_jobs=n_jobs,
                            n_iter=50,
                            scoring=f1_scorer)

    rs.fit(x_train, y_train)
    print("CRF model training complete!")
    print("Best parameters:", rs.best_params_)
    print("Best CV score:", rs.best_score_)
    print()
    joblib.dump(value=rs.best_estimator_, filename=outdir + '/CRF.model', compress=True)
    print("CRF model saved to ==> " + outdir)


    return rs.best_estimator_
