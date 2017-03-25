# -*- coding: utf-8 -*-

from grout.core.scriptable import Scriptable
from grout.core.container import Container

from typing import Dict


class Environment(Scriptable):
    def __init__(self, scripts: Dict[str, str]=None):
        super().__init__(scripts)

    def setup(self, c: Container):
        self._run_script('setup', c)
