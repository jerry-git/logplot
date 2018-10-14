# LogPlot

[![Build Status](https://travis-ci.org/jerry-git/logplot.svg?branch=master)](https://travis-ci.org/jerry-git/logplot)
[![PyPI version](https://badge.fury.io/py/logplot.svg)](https://pypi.python.org/pypi/logplot/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/logplot.svg)](https://pypi.python.org/pypi/logplot/)
[![codecov](https://codecov.io/gh/jerry-git/logplot/branch/master/graph/badge.svg)](https://codecov.io/gh/jerry-git/logplot)
[![license](https://img.shields.io/github/license/jerry-git/logplot.svg)](https://github.com/jerry-git/logplot/blob/master/LICENSE)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


<p align="center">
  <img src="https://github.com/jerry-git/logplot/blob/master/doc/examples/example.gif" alt="example gif"/>
</p>


## Installation
    $ pip3 install logplot
    
## Usage

### Configuration
In order to plot interesting graphs from custom logs, `logplot` needs to know what log entries are considered interesting. 
This can be done by defining `entries` and `special_entries` sections in the config file. 
The main purpose of `entries` is to plot trends, i.e. connected points. This is useful e.g. for plotting state machine states. 
`special_entries` is for plotting single, unconnected points, such as errors.

Each entry in `entries` and `special_entries` should have the following:
* `identifier`: string to be searched from log entries
* `value`: y-axis value in the plot

Ideally, one entry in `entries` should have `initial_state: true`. This is used for separating plotted series from each other.

You can define specific marker style for each entry in `special_entries`, refer to [`matplotlib` docs](https://matplotlib.org/api/markers_api.html) for available options.


In addition to the `entries` and `special-entries` sections, user can override default settings (see src/logplot/default_conf.yaml) in `general` section. 
For example, it's the place where you can define the command to be used for opening the log in your favorite editor. 
   
See doc/example/user_conf.yaml and corresponding log file (doc/example/log.txt) for full example.

### Plotting logs

    $ logplot path/to/log -c path/to/conf/file
    
For example, this:

    $ logplot doc/examples/log.txt -c doc/examples/user_conf.yaml

yields this:

<p align="center">
  <img src="https://github.com/jerry-git/logplot/blob/master/doc/examples/plot.png" alt="example plot"/>
</p>

Clicking a data point in the plot opens the log file in the correct line number in the editor defined in the configuration file.
If the `log_open_cmd` is not configured, the log will be opened with a default program defined by the OS. 
Note that `log_open_cmd` has to configured to be able to open the log in the correct line number.

`logplot` will automatically identify different trends in the plotted entries. 
You can toggle the visibility of these trends by clicking items in the legend.

Here's an example of a bit bigger log which contains 100k entries, 13 different states, and 15 different trends.

	$ logplot doc/examples/log_huge.txt -c doc/examples/user_conf_huge.yaml

<p align="center">
  <img src="https://github.com/jerry-git/logplot/blob/master/doc/examples/plot_huge.png" alt="example plot huge"/>
</p>

And the same with three most occuring trends filtered out.

<p align="center">
  <img src="https://github.com/jerry-git/logplot/blob/master/doc/examples/plot_huge_filtered.png" alt="example plot huge filtered"/>
</p>



