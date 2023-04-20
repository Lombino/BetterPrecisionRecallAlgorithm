import numpy as np
import sklearn.metrics


def new_algorithm_precision_recall_f1score(y_true, y_pred):
    aus = np.logical_and(y_true, y_pred)
    p_intersec_target_ = np.sum(aus)  # cardinality
    p_ = np.sum(y_pred)  # cardinality
    t_ = np.sum(y_true)  # cardinality

    try:
        precision = round(p_intersec_target_ / p_, 4)
    except ZeroDivisionError:
        precision = 0
    try:
        recall = round(p_intersec_target_ / t_, 4)
    except ZeroDivisionError:
        recall = 0
    if precision + recall > 0:
        mul = precision * recall
        sum = precision + recall
        f1_score = round(2 * mul / sum, 4)
    else:
        f1_score = 0

    return precision, recall, f1_score


if __name__ == '__main__':
    output = np.random.randint(5, size=(15, 50))
    gt = np.random.randint(5, size=(15, 50))

    p, r, f1 = new_algorithm_precision_recall_f1score(output, gt)

    print("precision = {} \nrecall = {} \nf1_score = {}".format(p, r, f1))

    ps, rs, f1s, _ = sklearn.metrics.classification_report(y_true=gt, y_pred=output, zero_division=0)
    print("precision = {} \nrecall = {} \nf1_score = {}".format(ps, rs, f1s))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
