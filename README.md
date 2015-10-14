# pyenvelope
[![Build Status](https://travis-ci.org/kaygorodov/pyenvelope.svg?branch=master)](https://travis-ci.org/kaygorodov/pyenvelope)

Pyenvelope helps you find an arbitrarily oriented minimum bounding rectangle of a set of points. Minimum bounding rectangle (MBR), also known as bounding box or envelope.

Currently, it calculates a bounding rectangle with minimum area (I am going to add the logic for minimum perimeter soon). It uses the rotating calipers method [https://en.wikipedia.org/wiki/Rotating_calipers](https://en.wikipedia.org/wiki/Rotating_calipers).

## Installation

You can use `pip`:

    $ pip install pyenvelope