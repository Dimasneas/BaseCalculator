import basecalculator as bc


def test_add():
    assert bc.calculate('5+5') == '10'


def test_sub():
    assert bc.calculate('12-3') == '9'


def test_mult():
    assert bc.calculate('2*3') == '6'


def test_div():
    assert bc.calculate('4/5') == '0.8'


def test_bracket():
    assert bc.calculate('2*(2+2)') == '8'


def test_fackt():
    assert bc.calculate('1+((3-2)+(5-3))!!') == '721'


def test_num_sys():
    assert bc.calculate('bin587') == '1001001011'


def test_log():
    assert bc.calculate('log10') == '1'
