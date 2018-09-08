import os
import subprocess
import sys

import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, entries, special_entries, log_path, log_open_cmd):
        self._entries = entries
        self._special_entries = special_entries
        self._log_path = log_path
        self._log_open_cmd = log_open_cmd
        self._initialise()
        plt.show()

    def _initialise(self):
        x = [e.line_number for e in self._entries]
        y = [e.conf_entry.priority for e in self._entries]
        fig, ax = plt.subplots()  # TODO: configurability
        ax.plot(x, y, "-o", picker=5)  # TODO: configurability
        fig.canvas.callbacks.connect("pick_event", self._data_point_click_callback)

    def _data_point_click_callback(self, event):
        x_data, y_data = event.artist.get_data()
        x_val = np.take(x_data, event.ind)[0]
        self._open_log_viewer(line_number=x_val)

    def _open_log_viewer(self, line_number=None):
        if self._log_open_cmd:
            formatter = dict(path=self._log_path)
            if line_number and "line_number" in self._log_open_cmd:
                formatter.update(dict(line_number=line_number))
            cmd = self._log_open_cmd.format(**formatter)
            subprocess.Popen(cmd.split())
        else:  # Rely on the default program of the OS
            if sys.platform == "win32":
                os.startfile(self._log_path)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.Popen([opener, self._log_path])
