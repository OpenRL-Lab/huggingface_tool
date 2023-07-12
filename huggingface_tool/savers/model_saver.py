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
import transformers

from huggingface_tool.savers.base_model_saver import BaseModelSaver

model_class_dict = {
    "AutoModelForSeq2SeqLM": transformers.AutoModelForSeq2SeqLM,
    "AutoModelForCausalLM": transformers.AutoModelForCausalLM,
    "AutoModelForSequenceClassification": transformers.AutoModelForSequenceClassification,
    "AutoModelForQuestionAnswering": transformers.AutoModelForQuestionAnswering,
    "AutoModelForTokenClassification": transformers.AutoModelForTokenClassification,
    "AutoModelForMultipleChoice": transformers.AutoModelForMultipleChoice,
    "AutoModelForNextSentencePrediction": transformers.AutoModelForNextSentencePrediction,
    "AutoModelForPreTraining": transformers.AutoModelForPreTraining,
    "AutoModelForMaskedLM": transformers.AutoModelForMaskedLM,
    "AutoModelForTableQuestionAnswering": transformers.AutoModelForTableQuestionAnswering,
}

class ModelSaver(BaseModelSaver):
    def __init__(self, model_class:str, name:str):
        super().__init__(name)
        self.model_class = model_class

    def _load(self,name):
        return model_class_dict[self.model_class].from_pretrained(name)