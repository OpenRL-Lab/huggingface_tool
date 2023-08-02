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

from huggingface_hub import hf_hub_download

from huggingface_tool.savers.base_api_saver import BaseAPISaver


class FileSaver(BaseAPISaver):
    def _load(self, name: str):
        split_string = name.split(":")
        assert len(split_string) == 2
        repo_id = split_string[0]
        file = split_string[1]
        repo_type = self.repo_type if self.repo_type == "dataset" else None
        return {"repo_id": repo_id, "file": file, "repo_type": repo_type}

    def save(self, name):
        local_dir = Path(name)
        local_dir.mkdir(parents=True, exist_ok=True)
        hf_hub_download(
            repo_id=self.loaded_object["repo_id"],
            filename=self.loaded_object["file"],
            repo_type=self.loaded_object["repo_type"],
            local_dir=local_dir,
        )
