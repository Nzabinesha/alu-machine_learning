# 0x01. Plotting

## Description

This project covers the basics of plotting with `matplotlib`. Each task
completes a script that generates a specific type of plot: line graphs,
scatter plots, histograms, stacked bar graphs, and a combined figure made
up of several subplots.

## Requirements

* Ubuntu 16.04 LTS, `python3` (3.5)
* `numpy` 1.15, `matplotlib` 3.0
* Every file starts with `#!/usr/bin/env python3`, ends with a newline,
  is executable, and follows `pycodestyle` (2.5)
* Every module has documentation

## Files

| File | Description |
| --- | --- |
| `0-line.py` | Plots `y = x^3` as a solid red line |
| `1-scatter.py` | Scatter plot of men's height vs weight |
| `2-change_scale.py` | Line graph of C-14 decay with a logarithmic y-axis |
| `3-two.py` | Two line graphs comparing C-14 and Ra-226 decay |
| `4-frequency.py` | Histogram of student grades |
| `5-all_in_one.py` | Combines the five plots above into one 3x2 figure |
| `6-bars.py` | Stacked bar graph of fruit possessed per person |

## Usage

Each file can be run directly, e.g.:

```
./0-line.py
```

This opens a window displaying the corresponding plot. If running over
SSH, X11 forwarding must be enabled to view the plot locally.

## Author

Written as part of the ALU Machine Learning curriculum.