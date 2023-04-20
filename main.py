import numpy as np
import sklearn.metrics
from metric_utils import *


if __name__ == '__main__':
    output = np.random.randint(2, size=(15, 50))
    gt = np.random.randint(2, size=(15, 50))

    p, r, f1 = multiclass_multioutput_overall_precision_recall_f1score(output, gt)
    print("OVERALL precision = {} recall = {} f1_score = {}\n".format(p, r, f1))

    cp, cr, cf1 = multiclass_multioutput_class_specific_p_r_f1(output, gt)

    for i, (p, r, f1) in enumerate(zip(cp, cr, cf1)):
        print("CLASS {}:   precision = {} recall = {} f1_score = {}\n".format(i, p, r, f1))






