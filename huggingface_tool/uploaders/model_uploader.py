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
import os

from pathlib import Path
from huggingface_tool.uploaders.base_uploader import BaseUploader
from huggingface_hub import HfApi
from huggingface_hub import ModelCard

def _huggingface_api_upload_file(api, path_or_fileobj, path_in_repo, repo_id, retry=5) -> bool:
    for retry_time in range(retry):
        try:
            api.upload_file(
                path_or_fileobj=path_or_fileobj,
                path_in_repo=path_in_repo,
                repo_id=repo_id,
                repo_type="model",
            )
            return True
        except:
            if retry_time == retry - 1:
                print(f"Can not upload the {path_or_fileobj} after {retry} times retry, please check your network connection.")
                return False

def _huggingface_api_upload_dir(api, folder_path, repo_id, retry=5) -> bool:
    for retry_time in range(retry):
        try:
            api.upload_folder(
                folder_path=folder_path,
                repo_id=repo_id,
                repo_type="model",
                ignore_patterns="README.md",
            )
            return True
        except:
            if retry_time == retry - 1:
                print(f"Can not upload the model after {retry} times retry, please check your network connection.")
                return False

class ModelUploader(BaseUploader):
    def __init__(self, file_or_dir: str, remote_name: str) -> None:
        super().__init__(file_or_dir, remote_name)
        self.model = None

    def check(self) -> bool:
        assert Path(self.file_or_dir).exists(), f"File or directory {self.file_or_dir} does not exist"
        return True

    def push_modelcard(self)->bool:
        card = ModelCard.load(os.path.join(self.file_or_dir,"README.md"))
        try:
            card.validate()
            card.push_to_hub(repo_id=self.remote_name)
        except:
            raise ValueError("model card info is invalid. please check.")
        return True

    def _push(self) -> bool:
        success = self.push_modelcard()

        if not success:
            print("Model card push failed.")
            return False

        api = HfApi()
        success = _huggingface_api_upload_dir(api, self.file_or_dir, self.remote_name)
        return success

    def _success_message(self):
        print(f"Model is uploaded to https://huggingface.co/{self.remote_name}")
