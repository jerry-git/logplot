# LogPlot

[![Build Status](https://travis-ci.org/jerry-git/logplot.svg?branch=master)](https://travis-ci.org/jerry-git/logplot)
[![PyPI version](https://badge.fury.io/py/logplot.svg)](https://pypi.python.org/pypi/logplot/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/logplot.svg)](https://pypi.python.org/pypi/logplot/)
[![codecov](https://codecov.io/gh/jerry-git/logplot/branch/master/graph/badge.svg)](https://codecov.io/gh/jerry-git/logplot)
[![license](https://img.shields.io/github/license/jerry-git/logplot.svg)](https://github.com/jerry-git/logplot/blob/master/LICENSE)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


> WIP: hold your horses boi


## Installation
    $ pip3 install logplot
    
## Usage

### Configuration
> TODO

### Plotting logs

    $ logplot path/to/log -c path/to/conf/file
    
For example, this:

    $ logplot doc/examples/log.txt -c doc/examples/user_conf.yaml

yields this:

<p align="center">
  <img src="https://github.com/jerry-git/logplot/blob/master/doc/examples/plot.png" alt="example plot"/>
</p>

Clicking a data point in the plot opens the log file in the correct line number in the editor defined in the configuration file. If the `log_open_cmd` is not configured, the log will be opened with a default program defined by the OS.