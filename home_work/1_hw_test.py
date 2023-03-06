def test_first():
    assert ('home', 'work') == ('home', 'work')


def test_second():
    assert 'QC' == 'QC'


def test_third():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
