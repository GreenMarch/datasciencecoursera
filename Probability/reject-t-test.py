from scipy.stats import ttest_1samp
import numpy as np

mu, sigma = 0.2, 0.03 # mean and standard deviation
offer_complete_rate = np.random.normal(mu, sigma, 24) # track the last 24 weeks



print(offer_complete_rate)
offer_complete_rate_mean = np.mean(offer_complete_rate)
print(offer_complete_rate_mean)

# suppose in the first deployment we observe offer_complete_rate_first_deployment = 0.21

tset, pval = ttest_1samp(offer_complete_rate, 0.21)
print("p-values",pval)

# if pval < 0.05:    # alpha value is 0.05 or 5%
#     print("we are rejecting null hypothesis")
# else:
#     print("we are accepting null hypothesis")


pval_sum = 0
pval_reject_count = 0
round = 1000
for i in range(round):
    mu, sigma = 0.2, 0.03  # mean and standard deviation
    offer_complete_rate = np.random.normal(mu, sigma, 24)  # track the last 24 weeks

    tset, pval = ttest_1samp(offer_complete_rate, 0.22)
    pval_sum += pval
    pval_reject_count += int(pval < 0.05)
    print(i, pval, int(pval < 0.05))

print("p-values-avg", pval_sum/round)

print("p-values-reject_ratio", pval_reject_count / round)