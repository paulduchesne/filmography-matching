#!/usr/bin/env python3
# coding: utf-8

import filmographymatching
import pathlib

if __name__ == "__main__":

    # define inputs and outputs. 

    a = pathlib.Path.cwd() / 'data-1.csv'
    b = pathlib.Path.cwd() / 'data-2.csv'
    output = pathlib.Path.cwd() / 'results.csv'

    filmographymatching.match(a, b, output)