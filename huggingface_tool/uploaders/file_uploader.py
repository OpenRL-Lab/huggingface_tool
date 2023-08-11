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

from huggingface_hub import HfApi
from huggingface_tool.uploaders.base_api_uploader import BaseAPIUploader


class FileUploader(BaseAPIUploader):
    def _push(self) -> bool:
        try:
            api = HfApi()
            api.upload_file(
                path_or_fileobj=self.file_or_dir,
                path_in_repo=self.info["file_or_directory"],
                repo_id=self.info["repo_id"],
                repo_type=self.repo_type, )
        except:
            print("Cannot upload to hub")
            return False
        return True

    def _success_message(self):
        middle_type = "/datasets/" if self.repo_type == "dataset" else "/"
        print(
            f"File is uploaded to https://huggingface.co{middle_type}{self.info['repo_id']}"
        )

