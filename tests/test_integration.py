from os import path as osp
from unittest.mock import patch

from click.testing import CliRunner
import pytest

from logplot.cli import log_plot

DATA_DIR = osp.join(osp.dirname(__file__), "data", "integration")
LOG = osp.join(DATA_DIR, "log.txt")
CONF = osp.join(DATA_DIR, "user_conf.yaml")


@pytest.fixture
def cli_runner():
    return CliRunner()


class TestPlotCreation:
    @patch("logplot.plot.plt.show")
    def test_it_plots(self, show_plot, cli_runner):
        res = cli_runner.invoke(log_plot, [LOG, "-c", CONF], catch_exceptions=False)
        assert not res.exception
        assert show_plot.call_count == 1
