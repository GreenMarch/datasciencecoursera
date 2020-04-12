import numpy as np
"""
def rmse(predictions, targets):
    differences = predictions - targets
    differences_squared = differences ** 2
    mean_of_differences_squared = differences_squared.mean()
    rmse_val = np.sqrt(mean_of_differences_squared)
    return rmse_val


y_hat = np.array([0.000, 0.166, 0.333])
y_true = np.array([0.000, 0.254, 0.998])

print("d is: " + str(["%.8f" % elem for elem in y_hat]))
print("p is: " + str(["%.8f" % elem for elem in y_true]))
rmse_val = rmse(y_hat, y_true)
print("rms error is: " + str(rmse_val))
"""

def my_rmse(y, yhat):
    """
    :param y: list of target
    :param yhat: list of calculated outcome
    :return: float number to eval errors
    """
    # if not (y and yhat):
    #     return -1
    if len(y) != len(yhat):
        return -1
    sse = 0
    for i in range(len(y)):
        sse += (y[i] - yhat[i]) ** 2
    return np.sqrt(sse/len(y))

def my_mae(y, yhat):
    """
    :param y: list of target
    :param yhat: list of calculated outcome
    :return: float number to eval errors
    """
    # if not (y and yhat):
    #     return -1
    if len(y) != len(yhat):
        return -1
    error_sum = 0
    for i in range(len(y)):
        error_sum += np.absolute(y[i] - yhat[i])
    return error_sum/len(y)


def my_mbe(y, yhat):
    if len(y) != len(yhat):
        return -1
    error_sum = 0
    for i in range(len(y)):
        error_sum += (y[i] - yhat[i])
    return error_sum/len(y)



y_hat = np.array([0.000, 0.166, 0.333, 0.666])
y_true = np.array([0.000, 0.254, 0.998, 0.333])

print("d is: " + str(["%.8f" % elem for elem in y_hat]))
print("p is: " + str(["%.8f" % elem for elem in y_true]))
rmse_val = my_rmse(y_hat, y_true)
print("new rmse is: " + str(rmse_val))

mae_val = my_mae(y_hat, y_true)
print("new mae error is: " + str(mae_val))

mbe_val = my_mbe(y_hat, y_true)
print("new mbe error is: " + str(mbe_val))