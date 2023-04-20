import numpy as np


def multiclass_multioutput_overall_precision_recall_f1score(y_true, y_pred, zero_division=0):
    """

    :param y_true: Ground truth. Expecting a [n,m] shaped np.array
    :param y_pred: Output predicted. Expecting a [n,m] shaped np.array
    :param zero_division: What result should be returned in case of 0 division
    :return: multiclass multioutput OVERALL precision, recall and f1_score
    """
    aus = np.logical_and(y_true, y_pred)
    # aus is an [n,m] shaped tensor where
    # the (i,j) element is 1 if the j'th output of the i'th input is correctly classified
    p_intersec_target_ = np.sum(aus)
    # p_intersec_target_ is the cardinality of the set |P intersect T|  (look the readme for the formulas)
    p_ = np.sum(y_pred)
    # p_ is the cardinality |P|
    t_ = np.sum(y_true)
    # t_ is the cardinality |T|

    try:
        precision = round(p_intersec_target_ / p_, 4)
    except ZeroDivisionError:
        precision = zero_division
    try:
        recall = round(p_intersec_target_ / t_, 4)
    except ZeroDivisionError:
        recall = zero_division
    if precision + recall > 0:
        mul = precision * recall
        sum = precision + recall
        f1_score = round(2 * mul / sum, 4)
    else:
        f1_score = zero_division

    return precision, recall, f1_score


def multiclass_multioutput_class_specific_p_r_f1(y_true, y_pred):
    """
    :param y_true: Ground truth. Expecting a [n,m] shaped np.array
    :param y_pred: Output predicted. Expecting a [n,m] shaped np.array
    :return: 3 [n] shaped arrays containing the precision, recall and f1 score of each class
    """
    aus = np.logical_and(y_true, y_pred)
    # aus is an [n,m] shaped tensor where
    # the (i,j) element is 1 if the j'th output of the i'th input is correctly classified
    class_specific_tp = np.sum(aus, axis=1)
    tp_plus_fp = np.sum(y_pred, axis=1)
    tp_plus_fn = np.sum(y_true, axis=1)
    class_specific_p = np.round(class_specific_tp / tp_plus_fp, decimals=4)
    class_specific_r = np.round(class_specific_tp / tp_plus_fn, decimals=4)
    class_specific_f1 = 2 * (class_specific_p * class_specific_r)/(class_specific_p + class_specific_r)
    class_specific_f1 = np.round(class_specific_f1, decimals=4)
    return class_specific_p, class_specific_r, class_specific_f1