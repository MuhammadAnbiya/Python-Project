  r1   �   s"   7"
r1   c                 C  �   | S �Nr\   �rh   r\   r\   r]   �<lambda>�   �    rr   c                 C  �   | fS rp   r\   rq   r\   r\   r]   rr   �   �    )�result_to_tuple�	n_outputs�default_axisr^   ��axisc                  s�  t ��������|dks|dk rtd��t|�}� du r%���d��d� �j�  }dg� ��fdd�td|d �D � }|dkrI|d d	 | S |d
kr_||d
  |d d  ||d	   S |dkr�d
|d d  d| |d  |d
   || |d   ||d	  |d   S |dkr�d|d d  d| |d d
  |d
   d| |d	  |d
 d
   d| |d  |d  |d   || |d  |d   ||d	  |d  |d   S td��)a7	  
    Return the `n` th k-statistic ( ``1<=n<=4`` so far).

    The `n` th k-statistic ``k_n`` is the unique symmetric unbiased estimator of the
    `n` th cumulant :math:`\kappa_n` [1]_ [2]_.

    Parameters
    ----------
    data : array_like
        Input array.
    n : int, {1, 2, 3, 4}, optional
        Default is equal to 2.
    axis : int or None, default: None
        If an int, the axis of the input along which