#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

# Define entry points in our package metadata. Keys should be fully qualified
# names of modules or (unbound) classes within PsychoPy (eg.
# 'psychopy.visual.Rect'). Values are used to specify which attributes of those
# objects to create or modify. For instance, our `get_area` function in the
# `psychopy_demo_plugin` module will be assigned as attribute `getArea` in the
# `psychopy.visual.Rect` class. After the plugin is loaded, any instances of
# `Rect` will have that method.

entry_points = {
    'psychopy.visual.Rect': ['getArea = psychopy_demo_plugin:get_area']}

# Run the setup function.
setup(
    name="psychopy-demo-plugin",  # this should match the project name
    version="0.1",  # put your plugin version here
    packages=['psychopy_demo_plugin'],
    package_data={"": ["*.txt", "*.md"]},
    author="Nobody",
    author_email="nobody@example.com",
    description="PsychoPy plugin to compute the area of a Rect stimuli.",
    url="https://github.com/mdcutone/psychopy-demo-plugin",
    classifiers=[
        "License :: OSI Approved :: MIT",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'],
    keywords="psychopy stimuli sample",
    entry_points=entry_points  # set our entry points in the package metadata
)