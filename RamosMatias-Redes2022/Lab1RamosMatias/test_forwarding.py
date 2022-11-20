from forwarding import *
import pytest

forward_table = [(('192.141.27.224',    27), 'm11'),
                 (('202.44.82.0',       26), 'm10'),
                 (('199.199.199.128',   26), 'm9'),
                 (('172.20.7.128',      26), 'm8'),
                 (('192.168.32.0',      24), 'm7'),
                 (('156.1.128.0',       20), 'm6'),
                 (('45.11.128.0',       19), 'm5'),
                 (('10.15.0.0',         16), 'm4'),
                 (('128.11.0.0',        16), 'm3'),
                 (('45.208.0.0',        13), 'm2'),
                 (('25.0.0.0',          8),  'm1'),
                 (('0.0.0.0',           0),  'm0'),
                ]
@pytest.mark.parametrize(
    "forward_table, address, expected",
    [
        (forward_table, '10.15.120.3',      'm4'),
        (forward_table, '192.168.32.10',    'm7'),
        (forward_table, '192.141.27.226',   'm11'),
        (forward_table, '202.44.82.66',     'm0'),
        (forward_table, '199.199.199.172',  'm9'),
        (forward_table, '172.20.7.160',     'm8'),
        (forward_table, '192.168.33.15',    'm0'),
        (forward_table, '156.1.128.200',    'm6'),
        (forward_table, '45.11.130.250',    'm5'),
        (forward_table, '10.15.10.120',     'm4'),
        (forward_table, '128.11.3.31',      'm3'),
        (forward_table, '45.208.245.222',   'm2'),
        (forward_table, '25.34.12.56',      'm1'),
    ]
)
def test_forwarding(forward_table, address, expected):
    assert forwarding(forward_table, address) == expected
