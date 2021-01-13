#!/usr/bin/env python3

from sklearn_crfsuite import metrics

def evaluation(x_test, y_test, model, eval_classes):
    y_pred = model.predict(x_test)
    print(metrics.flat_classification_report(y_test, y_pred, labels=eval_classes))
