from unittest.mock import MagicMock, patch
import pytest


from logplot.plot import Plot


@pytest.fixture
def mock_pyplot(monkeypatch):
    monkeypatch.setattr("logplot.plot.plt", MagicMock())


@pytest.fixture
def no_plot_initialise(monkeypatch):
    monkeypatch.setattr("logplot.plot.Plot._initialise", MagicMock())


@pytest.mark.usefixtures("mock_pyplot", "no_plot_initialise")
@patch("logplot.plot.sys")
class TestOpenLogViewer:
    # fmt: off
    @pytest.mark.parametrize(
        "open_cmd, shell, platform, log_path, expected",
        [
            ("", False, "linux", "foo/bar/log.txt", ["xdg-open", "foo/bar/log.txt"]),
            ("", False, "darwin", "foo/bar/log.txt", ["open", "foo/bar/log.txt"]),
            ("custom_cmd '{path}'", True, "darwin", "/foo/bar space/log.txt",
             ["custom_cmd", "/foo/bar space/log.txt"]),
            ("custom_cmd '{path}':{line_number} ", True, "win32", "somewhere/log.txt",
             ["custom_cmd", "somewhere/log.txt:99"])
        ]
    )
    # fmt: on
    @patch("logplot.plot.subprocess.Popen")
    def test_it_passes_correct_params_to_popen(
        self, popen, sys_mock, open_cmd, shell, platform, log_path, expected
    ):
        conf = MagicMock()
        conf.general.shell = shell
        conf.general.log_open_cmd = open_cmd
        sys_mock.platform = platform
        plot = Plot(entries=[], special_entries=[], log_path=log_path, conf=conf)

        plot._open_log_viewer(line_number=99)

        args, kwargs = popen.call_args
        assert args[0] == expected
        assert kwargs["shell"] == shell

    @patch("logplot.plot.os")
    def test_it_calls_startfile_on_windows_as_default(self, os_mock, sys_mock):
        conf = MagicMock()
        conf.general.log_open_cmd = ''
        sys_mock.platform = "win32"
        plot = Plot(entries=[], special_entries=[], log_path="foo", conf=conf)

        plot._open_log_viewer(line_number=99)
        os_mock.startfile.assert_called_with("foo")
