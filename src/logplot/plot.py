import os
import subprocess
import sys

import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, entries, special_entries, log_path, conf):
        self._entries = entries
        self._special_entries = special_entries
        self._log_path = log_path
        self._conf = conf
        self._initialise()
        plt.show()

    def _initialise(self):
        fig, ax = plt.subplots()
        fig.canvas.callbacks.connect("pick_event", self._data_point_click_callback)
        x, y = [], []
        default_style = self._conf.general.default_entry_style
        pick = self._conf.general.click_hit_tolerance

        for entry in self._entries:
            if entry.conf_entry.initial_state:
                ax.plot(x, y, default_style, picker=pick)
                x, y = [], []
            x.append(entry.line_number)
            y.append(entry.conf_entry.value)
        ax.plot(x, y, default_style, picker=pick)

        for entry in self._special_entries:
            style = entry.conf_entry.style or default_style
            ax.plot(entry.line_number, entry.conf_entry.value, style, picker=pick)

    def _data_point_click_callback(self, event):
        x_data, y_data = event.artist.get_data()
        x_val = np.take(x_data, event.ind)[0]
        self._open_log_viewer(line_number=x_val)

    def _open_log_viewer(self, line_number=None):
        cmd = self._conf.general.log_open_cmd
        if cmd:
            formatter = dict(path=self._log_path)
            if line_number and "line_number" in cmd:
                formatter.update(dict(line_number=line_number))
            cmd = cmd.format(**formatter)
            subprocess.Popen(cmd.split())
        else:  # Rely on the default program of the OS
            if sys.platform == "win32":
                os.startfile(self._log_path)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.Popen([opener, self._log_path])
