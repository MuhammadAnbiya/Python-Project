))``

    References
    ----------
    T.E. Oliphant, "A Bayesian perspective on estimating mean, variance, and
    standard-deviation from data", https://scholarsarchive.byu.edu/facpub/278,
    2006.

    Examples
    --------
    First a basic example to demonstrate the outputs:

    >>> from scipy import stats
    >>> data = [6, 9, 12, 7, 8, 8, 13]
    >>> mean, var, std = stats.bayes_mvs(data)
    >>> mean
    Mean(statistic=9.0, minmax=(7.103650222612533, 10.896349777387467))
    >>> var
    Variance(statistic=10.0, minmax=(3.176724206, 24.45910382))
    >>> std
    Std_dev(statistic=2.9724954732045084,
            minmax=(1.7823367265645143, 4.945614605014631))

    Now we generate some normally distributed random data, and get estimates of
    mean and standard deviation with 95% confidence intervals for those
    estimates:

    >>> n_samples = 100000
    >>> d