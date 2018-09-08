import json
from os import path as osp

import pytest

from logplot import conf


DATA_DIR = osp.join(osp.dirname(__file__), "data", "conf")
DEFAULT_PATH = osp.join(DATA_DIR, "default{}.yaml")
USER_PATH = osp.join(DATA_DIR, "user{}.yaml")
EXPECTED_JSON_PATH = osp.join(DATA_DIR, "expected_json_{}_{}.txt")


class TestRead:
    @pytest.mark.parametrize("default_case, user_case", [(1, 1), (1, 2)])
    def test_it_reads(self, default_case, user_case):
        res = conf.read(DEFAULT_PATH.format(default_case), USER_PATH.format(user_case))
        with open(EXPECTED_JSON_PATH.format(default_case, user_case)) as expected_json:
            assert json.dumps(res) == expected_json.read()
