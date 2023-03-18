from scipy.stats import ttest_ind

def t_test(arr1, arr2):

    # Perform the t-test
    t, p = ttest_ind(arr1, arr2)

    # Print the results
    print("t-statistic: ", t)
    print("p-value: ", p)