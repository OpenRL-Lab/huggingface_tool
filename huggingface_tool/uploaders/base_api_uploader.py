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
from typing import Dict
from abc import ABC, abstractmethod

from pathlib import Path
from huggingface_tool.uploaders.base_uploader import BaseUploader


class BaseAPIUploader(BaseUploader, ABC):
    def __init__(self, file_or_dir: str, remote_path: str, repo_type: str):
        super().__init__(file_or_dir,remote_path)
        self.info = self.get_info(remote_path)
        self.repo_type = repo_type

    def get_info(self, remote_path: str) -> Dict[str, str]:
        split_string = remote_path.split(":")
        assert len(split_string) == 2
        repo_id = split_string[0]
        file_or_directory = split_string[1]
        return {"repo_id": repo_id, "file_or_directory": file_or_directory}

    def check(self) -> bool:
        assert Path(
            self.file_or_dir
        ).exists(), f"File or directory {self.file_or_dir} does not exist"
        return True

