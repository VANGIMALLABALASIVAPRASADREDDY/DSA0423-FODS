import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

control_group = [50, 52, 48, 47, 51, 49, 53, 46, 50, 48]
treatment_group = [60, 62, 59, 63, 61, 58, 64, 60, 62, 59]

control = np.array(control_group)
treatment = np.array(treatment_group)

t_stat, p_value = stats.ttest_ind(treatment, control)

print("T-statistic:", t_stat)
print("P-value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("Reject Null Hypothesis")
    print("The new treatment has a statistically significant effect.")
else:
    print("Fail to Reject Null Hypothesis")
    print("No significant difference between treatment and placebo.")

plt.figure()
plt.boxplot([control, treatment])
plt.xticks([1, 2], ['Control Group', 'Treatment Group'])
plt.ylabel("Recovery Score")
plt.title("Clinical Trial Comparison")
plt.show()

plt.figure()
means = [np.mean(control), np.mean(treatment)]
plt.bar(['Control Mean', 'Treatment Mean'], means)
plt.ylabel("Average Recovery Score")
plt.title("Mean Comparison (p-value = {:.4f})".format(p_value))
plt.show()
