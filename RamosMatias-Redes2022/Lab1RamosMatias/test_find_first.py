from find_first_and_last import * 
import pytest

@pytest.mark.parametrize(
    "address, slash, expected",
    [
        ('10.15.120.3',     16, (('10.15.0.1', '10.15.255.254'),        '')),
        ('25.34.12.56',     8,  (('25.0.0.1', '25.255.255.254'),        '')),
        ('128.11.3.31',     16, (('128.11.0.1', '128.11.255.254'),      '')),
        ('192.168.32.14',   24, (('192.168.32.1', '192.168.32.254'),    '')),
        ('202.44.82.16',    26, (('202.44.82.1', '202.44.82.62'),       '')),
        ('156.1.128.200',   20, (('156.1.128.1', '156.1.143.254'),      '')),
        ('199.199.199.172', 26, (('199.199.199.129', '199.199.199.190'),'')),
        ('45.11.130.250',   19, (('45.11.128.1', '45.11.159.254'),      '')),
        ('45.208.245.222',  13, (('45.208.0.1', '45.215.255.254'),      '')),
        ('192.141.27.224',  27, (('192.141.27.225', '192.141.27.254'),  '')),
        ('172.20.7.160',    26, (('172.20.7.129', '172.20.7.190'),      ''))
    ]
)
def test_find_first_and_last(address, slash, expected):
    assert find_first_and_last(address, slash) == expected