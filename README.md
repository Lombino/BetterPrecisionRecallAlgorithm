# MultiClass MultiOutput Precision Recall Algorithm
This code provides an implementation of the algorithm involved in the calculation of precision and recall for the multiclass multioutput scenarios

$$\begin{align}
hP = \frac{\sum_i | \hat{P_i} \cap \hat{T_i} |}{\sum_i |\hat{P_i}|} \\
hR = \frac{\sum_i | \hat{P_i} \cap \hat{T_i} |}{\sum_i |\hat{T_i}|} \\
hF1 = \frac{2*hP*hR}{hP+hR}
\end{align}$$
