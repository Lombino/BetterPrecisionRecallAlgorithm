# BetterPrecisionRecallAlgorithm
This code provides an other (maybe better) implementation of the algorithm involved in the calculation of precision and recall

$$\begin{align}
hP = \frac{\sum_i | \hat{P_i} \cap \hat{T_i} |}{\sum_i |\hat{P_i}|} \\
hR = \frac{\sum_i | \hat{P_i} \cap \hat{T_i} |}{\sum_i |\hat{T_i}|} \\
hF1 = \frac{2*hP*hR}{hP+hR}
\end{align}$$
