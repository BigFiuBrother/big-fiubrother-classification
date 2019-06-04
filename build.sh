#!/usr/bin/env bash

rm -rf build
rm -rf dist
rm -rf big_fiubrother_classification.egg-info
python3 setup.py bdist_wheel
