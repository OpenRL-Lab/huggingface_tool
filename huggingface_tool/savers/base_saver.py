#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2023 The OpenRL Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""""""

from abc import ABC, abstractmethod

from huggingface_tool.utils.logger import Logger

class BaseSaver(ABC):
    def __init__(self, name:str):
        self.logger = Logger()
        self.name = name
        self.loaded_object = None



    def load(self) -> bool:
        try:
            self.loaded_object = self._load(self.name)
        except:
            self.logger.info(f"Could not load model from {self.name}")
            return False
        return True

    @abstractmethod
    def _load(self,name:str):
        raise NotImplementedError

    @abstractmethod
    def save(self,save_dir: str):
        raise NotImplementedError
