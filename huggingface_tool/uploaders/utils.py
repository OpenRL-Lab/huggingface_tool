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