from collections import defaultdict, OrderedDict
import os
import pkg_resources
import shlex
import subprocess
import sys

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

from .colors import next_colour


TEMP_COLOR = "black"


class Plot:
    def __init__(self, entries, special_entries, log_path, conf):
        self._entries = entries
        self._special_entries = special_entries
        self._log_path = log_path
        self._conf = conf
        self._legend_mapping = {}
        self._initialise()
        plt.show()

    def _initialise(self):
        self._fig, self._ax = plt.subplots()
        self._fig.canvas.callbacks.connect("pick_event", self._click_callback)
        x, y = [], []
        trend_mapping = defaultdict(list)

        def add_line():
            nonlocal x, y
            if x and y:
                line = self._ax.plot(
                    x,
                    y,
                    self._conf.general.default_entry_style,
                    picker=self._conf.general.click_hit_tolerance,
                    zorder=-32,
                    color=TEMP_COLOR,
                )[0]
                trend_mapping[str(y)].append(line)
                x, y = [], []

        for entry in self._entries:
            if entry.conf_entry.initial_state:
                add_line()
            x.append(entry.line_number)
            y.append(entry.conf_entry.value)

        # last line
        add_line()

        self._add_special_entries()
        self._create_legend(trend_mapping)
        self._add_naming()

    def _add_special_entries(self):
        for entry in self._special_entries:
            style = entry.conf_entry.style or self._conf.general.default_entry_style
            self._ax.plot(
                entry.line_number,
                entry.conf_entry.value,
                style,
                picker=self._conf.general.click_hit_tolerance,
            )

    def _create_legend(self, trend_mapping):
        # shrink the plot area a bit to fit the legend outside
        box = self._ax.get_position()
        self._ax.set_position([box.x0, box.y0, box.width * 0.95, box.height])

        # sort based on lines count in trends
        # to have the trends in nice order in the legend
        sorted_trend_items = sorted(
            trend_mapping.items(), key=lambda item: len(item[1]), reverse=True
        )
        sorted_mapping = OrderedDict(sorted_trend_items)
        legend_dummy_lines = []
        legend_labels = []

        for lines in sorted_mapping.values():
            color = next_colour()
            for line in lines:
                line.set_color(color)

            legend_line = Line2D([0], [0], color=color, lw=4)
            legend_labels.append("{}x".format(len(lines)))
            legend_dummy_lines.append(legend_line)

        self._legend = self._ax.legend(
            legend_dummy_lines,
            legend_labels,
            title="trends",
            loc="center left",
            bbox_to_anchor=(1, 0.5),
        )

        for legend_line, lines in zip(
            self._legend.get_lines(), sorted_mapping.values()
        ):
            legend_line.set_picker(5)
            self._legend_mapping[legend_line] = lines

    def _add_naming(self):
        self._fig.suptitle(self._conf.general.plot_title)
        plt.xlabel(self._conf.general.y_axis_name)
        plt.ylabel(self._conf.general.x_axis_name)
        version = pkg_resources.get_distribution("logplot").version
        plt.gcf().canvas.set_window_title("logplot {}".format(version))

    def _click_callback(self, event):
        if event.artist in self._legend_mapping:  # click in legend
            visible = not self._legend_mapping[event.artist][0].get_visible()
            for line in self._legend_mapping[event.artist]:
                # toggle visibility
                line.set_visible(visible)

            event.artist.set_alpha(1 if visible else 0.2)
            self._fig.canvas.draw()

        elif event.artist.get_visible():  # click in plot
            x_data, y_data = event.artist.get_data()
            x_val = np.take(x_data, event.ind)[0]
            # y_val = np.take(y_data, event.ind)[0]
            self._open_log_viewer(line_number=x_val)

    def _open_log_viewer(self, line_number=None):
        cmd = self._conf.general.log_open_cmd
        shell = self._conf.general.shell
        if cmd:
            cmd = cmd.format(line_number=line_number, path=self._log_path)
            subprocess.Popen(shlex.split(cmd), shell=shell)
        else:  # Rely on the default program of the OS
            if sys.platform == "win32":
                os.startfile(self._log_path)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.Popen([opener, self._log_path], shell=shell)
