#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module containing objects to export to PsychoPy. These objects are
referenced in the package metadata which also instructs where to put them in
PsychoPy's namespace."""


def get_area(self):
    """Compute the area of a `Rect` stimulus in `units`.

    Returns
    -------
    float
        Area in units^2.

    """
    return self.size[0] * self.size[1]

