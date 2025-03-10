rray_like
        Input array.
    n : int, {1, 2}, optional
        Default is equal to 2.
    axis : int or None, default: None
        If an int, the axis of the input along which to compute the statistic.
        The statistic of each axis-slice (e.g. row) of the input will appear
        in a corresponding element of the output. If ``None``, the input will
        be raveled before computing the statistic.

    Returns
    -------
    kstatvar : float
        The `n` th k-statistic variance.

    See Also
    --------
    kstat : Returns the n-th k-statistic.
    moment : Returns the n-th central moment about the mean for a sample.

    Notes
    -----
    Unbiased estimators of the variances of the first two k-statistics are given by

    .. math::

        \mathrm{var}(k_1) &= \frac{k_2}{n}, \\
        \mathrm{var}(k_2) &= \frac{2k_2^2n + (n-1)k_4}{n(n - 1)}.

    References
    ----------
    .. [1] http://mathworld.wolfram.com/k-Statistic.html

    Nr|   r   r!   r^   T)ri   rz   Z_no_decor�   r{   zOnly n=1 or n=2 supported.)r   r	   r�   r�   r3   rT   )rW   ri   rz   r�   r�   Zk2Zk4r\   r\   r]   r4   D  s   ,

(r4   c           