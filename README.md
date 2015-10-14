# pyenvelope
[![Build Status](https://travis-ci.org/kaygorodov/pyenvelope.svg?branch=master)](https://travis-ci.org/kaygorodov/pyenvelope)

Pyenvelope helps you find an arbitrarily oriented minimum bounding rectangle of a set of points. Minimum bounding rectangle (MBR), also known as bounding box or envelope.

Currently, it calculates a bounding rectangle with minimum area (I am going to add the logic for minimum perimeter soon). It uses the rotating calipers method [https://en.wikipedia.org/wiki/Rotating_calipers](https://en.wikipedia.org/wiki/Rotating_calipers).

## Installation

You can use `pip`:

    $ pip install pyenvelope
    
## Usage

Use the `get_minimum_bounding_rectangle` function. It takes a set of points and returns coordinates of MBR vertices:

    >>> from pyenvelope import get_minimum_bounding_rectangle
    >>> get_minimum_bounding_rectangle([(1, 2), (2, 6), (3, 7), (2, 2)])
    [(1.94, 1.76), (3.2, 6.94), (2.29, 7.17), (1.00, 2.00), (1.94, 1.76)]