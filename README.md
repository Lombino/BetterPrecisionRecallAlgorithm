# MultiClass MultiOutput Precision Recall Algorithm
This code provides an implementation of the algorithm involved in the calculation of precision and recall for the multiclass multioutput scenarios.
Defining 
- $P_i$ as the output predicted for the $i$'th samples 
- $T_i$ as the ground truth for the $i$'th samples    
The formulas used to calculate the overall precision, recall and f1 score can be formuled as the following:

$$\begin{align}
P = \frac{\sum_i | P_i \cap T_i |}{\sum_i |P_i|} \\
R = \frac{\sum_i | P_i \cap T_i |}{\sum_i |T_i|} \\
F1 = \frac{2 * P * R}{P+R}
\end{align}$$


It also provide an implementation for the calculation of the class specific metrics. For each class the precision, recall and f1_score are defined by the well know formulas written below 

$$\begin{align}
p = \frac{TP}{TP+FP} \\
r = \frac{TP}{TP+FN} \\
f1 = \frac{2 * p * r}{p + r}
\end{align}$$
