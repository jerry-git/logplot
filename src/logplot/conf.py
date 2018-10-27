from collections import namedtuple
from itertools import combinations
import logging

import yaml

logger = logging.getLogger(__name__)


General = namedtuple(
    "General",
    [
        "log_open_cmd",
        "default_entry_style",
        "click_hit_tolerance",
        "shell",
        "plot_title",
        "x_axis_name",
        "y_axis_name",
        "legend_title",
    ],
)
General.__new__.__defaults__ = (None,) * len(General._fields)

ConfEntry = namedtuple("ConfEntry", ["identifier", "value", "label", "initial_state"])
# stuff after value are optional
ConfEntry.__new__.__defaults__ = (None, None)

SpecialConfEntry = namedtuple(
    "SpecialConfEntry", ["identifier", "value", "label", "regex", "style"]
)
# stuff after value are optional
SpecialConfEntry.__new__.__defaults__ = (None, None, None)

Conf = namedtuple("Conf", ["general", "entries", "special_entries"])


def _loag_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def read(default_path, user_path):
    default = _loag_yaml(default_path)
    user = _loag_yaml(user_path)
    # General settings from default and then override by user defined
    general = default.get("general", {})
    general.update(user.get("general", {}))
    general = General(**general)
    # Log entry specific settings only from user
    basics = [ConfEntry(**e) for e in user["entries"]]

    for e1, e2 in combinations(basics, 2):
        if e1.identifier in e2.identifier or e2.identifier in e1.identifier:
            logger.warning(
                "Colliding identifiers: {} {}".format(e1.identifier, e2.identifier)
            )

    specials = [SpecialConfEntry(**e) for e in user.get("special-entries", [])]
    return Conf(general, basics, specials)
