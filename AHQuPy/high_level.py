#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

from . import Debug
from .low_level import Mixer


class AHQuPy(Mixer):
    # user-friendly abstraction of class Mixer
    def __init__(self):
        Mixer.__init__(self)
