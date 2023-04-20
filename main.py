import numpy as np
import sklearn.metrics
from metric_utils import *


if __name__ == '__main__':
    output = np.random.randint(5, size=(15, 50))
    gt = np.random.randint(5, size=(15, 50))

    p, r, f1 = new_algorithm_precision_recall_f1score(output, gt)

    print("precision = {} \nrecall = {} \nf1_score = {}".format(p, r, f1))




