import click

from logplot import conf, log
from logplot.plot import Plot

import os

DEFAULT_CONF = os.path.join(os.path.dirname(__file__), "default_conf.yaml")


@click.command()
@click.argument("log-path", type=click.Path(exists=True))
@click.option(
    "--config-path",
    "-c",
    type=click.Path(exists=True),
    help="Path to a configuration file",
)
@click.version_option(None, "-v", "--version")
def log_plot(log_path, config_path):
    """Create an awesome plot of a log file"""
    user_conf = _select_user_config(config_path)
    config = conf.read(DEFAULT_CONF, user_conf)
    entries, special_entries = log.parse(log_path, config)
    Plot(
        entries=entries,
        special_entries=special_entries,
        log_path=os.path.abspath(log_path),
        conf=config,
    )


def _select_user_config(conf_path):
    if not conf_path:
        path = os.environ.get("LOGPLOT_CONFIG")
        if not path:
            raise ValueError(
                "Missing user config, give path to a configuration file "
                "as command line argument or define the path as "
                "LOGPLOT_CONFIG environment variable."
            )
    return os.path.abspath(conf_path)
