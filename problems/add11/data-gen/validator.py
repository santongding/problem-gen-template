def validate(param, utils):
    getints = utils.getints
    lis = getints(2)
    n, k = lis[0], lis[1]
    assert 1 <= n <= 1e5
    assert 0 <= k <= 1e5
    if param.data_id < 8:
        assert n <= 1000 and k <= 1000
