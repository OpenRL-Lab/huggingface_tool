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
import datasets

from huggingface_tool.savers.base_saver import BaseSaver

class DatasetSaver(BaseSaver):
    def _load(self,name:str):
        return datasets.load_dataset(name)

    def save(self, save_dir: str):
        if self.loaded_object is None:
            self.logger.info("No dataset loaded, cannot save")
            return
        self.loaded_object.save_to_disk(save_dir)

