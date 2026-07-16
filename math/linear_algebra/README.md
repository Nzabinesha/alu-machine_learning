# 0x00. Linear Algebra

## Description

This project covers the basics of linear algebra as used in machine
learning: slicing arrays and matrices, calculating shape, transposing,
element-wise operations, concatenation, and matrix multiplication —
first using plain Python lists, then using `numpy`.

## Requirements

* Ubuntu 16.04 LTS, `python3` (3.5)
* `numpy` 1.15
* Every file starts with `#!/usr/bin/env python3`, ends with a newline,
  is executable, and follows `pycodestyle` (2.5)
* Every module, class, and function has documentation
* No imports unless explicitly allowed by the task

## Files

| File | Description |
| --- | --- |
| `0-slice_me_up.py` | Slices an array in three different ways |
| `1-trim_me_down.py` | Extracts the middle two columns of a matrix |
| `2-size_me_please.py` | `matrix_shape` — calculates the shape of a matrix |
| `3-flip_me_over.py` | `matrix_transpose` — transposes a 2D matrix |
| `4-line_up.py` | `add_arrays` — adds two arrays element-wise |
| `5-across_the_planes.py` | `add_matrices2D` — adds two 2D matrices element-wise |
| `6-howdy_partner.py` | `cat_arrays` — concatenates two arrays |
| `7-gettin_cozy.py` | `cat_matrices2D` — concatenates two matrices along an axis |
| `8-ridin_bareback.py` | `mat_mul` — performs matrix multiplication |
| `9-let_the_butcher_slice_it.py` | Slices a numpy matrix in three different ways |
| `10-ill_use_my_scale.py` | `np_shape` — calculates the shape of a numpy.ndarray |
| `11-the_western_exchange.py` | `np_transpose` — transposes a numpy.ndarray |
| `12-bracin_the_elements.py` | `np_elementwise` — element-wise add/sub/mul/div |
| `13-cats_got_your_tongue.py` | `np_cat` — concatenates two numpy matrices along an axis |
| `14-saddle_up.py` | `np_matmul` — matrix multiplication with numpy |

## Usage

Standalone scripts (`0`, `1`, `9`) can be run directly:

```
./0-slice_me_up.py
```

Function-based tasks are imported and tested with a corresponding
`N-main.py` file, e.g.:

```
./2-main.py
```

## Author

Written as part of the ALU Machine Learning curriculum.
