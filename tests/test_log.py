import json
from os import path as osp

import pytest

from logplot import log
from logplot.conf import General, ConfEntry, SpecialConfEntry, Conf


DATA_DIR = osp.join(osp.dirname(__file__), "data", "log")
LOG_PATH = osp.join(DATA_DIR, "log{}.txt")
CONF_PATH = osp.join(DATA_DIR, "conf{}.txt")
EXPECTED_JSON_PATH = osp.join(DATA_DIR, "expected_json_{}_{}.txt")


def conf_from_json_file(path):
    with open(path) as f:
        general, basics, specials = json.loads(f.read())
        entries = [ConfEntry(*e) for e in basics]
        special_entries = [SpecialConfEntry(*e) for e in specials]
        conf = Conf(General(*general), entries, special_entries)
        return conf


class TestParse:
    @pytest.mark.parametrize("log_case, conf_case", [(1, 1)])
    def test_it_parses(self, log_case, conf_case):
        conf = conf_from_json_file(CONF_PATH.format(conf_case))
        res = log.parse(LOG_PATH.format(log_case), conf)
        with open(EXPECTED_JSON_PATH.format(log_case, conf_case)) as expected_json:
            assert json.dumps(res) == expected_json.read()
