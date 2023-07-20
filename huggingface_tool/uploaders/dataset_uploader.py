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

from pathlib import Path
from huggingface_tool.uploaders.base_uploader import BaseUploader
from datasets import load_from_disk


class DatasetUploader(BaseUploader):
    def __init__(self, file_or_dir: str, remote_name: str) -> None:
        super().__init__(file_or_dir, remote_name)
        self.dataset = None

    def check(self) -> bool:
        assert Path(self.file_or_dir).exists(), f"File or directory {self.file_or_dir} does not exist"
        try:
            self.dataset = load_from_disk(self.file_or_dir)
        except:
            print("Cannot load local dataset")
            return False
        return True

    def _push(self) -> bool:
        assert self.dataset is not None, "Dataset is not loaded"
        try:
            self.dataset.push_to_hub(self.remote_name)
        except:
            print("Cannot push to hub")
            return False
        return True

    def _success_message(self):
        print(f"Dataset is uploaded to https://huggingface.co/datasets/{self.remote_name}")
