# https://blog.dominodatalab.com/imbalanced-datasets/
def bootstrap(X, n = None, iterations = 1):
     if n == None:
        n = len(X)
    X_resampled = np.random.choice(X, size = (iterations, n), replace = True)
    return X_resampled
