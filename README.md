# HuggingFace Tool

[![PyPI](https://img.shields.io/pypi/v/huggingface-tool)](https://pypi.org/project/huggingface-tool/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/huggingface-tool)
[![Hits-of-Code](https://hitsofcode.com/github/OpenRL-Lab/huggingface_tool?branch=main)](https://hitsofcode.com/github/OpenRL-Lab/huggingface_tool/view?branch=main)

Tools for loading, upload, managing huggingface models and datasets.


## Installation

`pip install huggingface-tool`

## Usage

Firstly, you need to login with `huggingface-cli login` (you can create or find your token at [settings](https://huggingface.co/settings/tokens)).

- Download and save a repo with: `htool save-repo <repo_id> <save_dir> -r <model/dataset>`. `-r` means the repo is a model or dataset repo. By default, it is a model repo.
  - For example: `htool save-repo OpenRL/tizero ./tizero`
  - For example: `htool save-repo OpenRL/DeepFakeFace ./DeepFakeFace -r dataset`
- Download and save a file with: `htool save-file <repo_id>:<remote_filepath> <save_dir> -r <model/dataset>`. `-r` means the repo is a model or dataset repo. By default, it is a model repo.
  - For example: `htool save-file OpenRL/tizero:actor.pt ./tizero`
  - For example: `htool save-file OpenRL/DeepFakeFace:README.md ./DeepFakeFace -r dataset`
- Download and save transformer models with: `htool save-model <model_class> <model_name> <save_dir>`
  - For example: `htool save-model AutoModelForCausalLM gpt2 ./gpt2`
- Download and save tokenizer with: `htool save-tk <tokenizer_name> <save_dir>`
  - For example: `htool save-tk gpt2 ./gpt2 `
- Download and save dataset with: `htool save-data <dataset_name> <save_dir>`
  - For example: `htool save-data daily_dialog ./daily_dialog`
- Download and save diffusion models with: `htool save-dm <model_name> <save_dir>`
  - For example: `htool save-dm google/ddpm-cat-256 ./google/`

You can also use htool to upload datasets and models to huggingface.

- Upload a file with: `htool upload-file <local_filepath> <organization_or_username/repo_name>:<remote_filepath> -r <model/dataset>`. `-r` means the repo is a model or dataset repo. By default, it is a model repo.
  - For example: `htool upload-file README.md OpenRL/tizero:README.md`
  - For example: `htool upload-file README.md OpenRL/DeepFakeFace:README.md -r dataset`
- Upload a directory with: `htool upload-dir <local_dirpath> <organization_or_username/repo_name>:<remote_dirpath> -r <model/dataset>`. `-r` means the repo is a model or dataset repo. By default, it is a model repo.
  - For example: `htool upload-dir ./tizero OpenRL/tizero:./`
  - For example: `htool upload-dir ./tizero/models OpenRL/tizero:./models`
  - For example: `htool upload-dir ./DeepFakeFace OpenRL/DeepFakeFace:./ -r dataset`
  - For example: `htool upload-dir ./DeepFakeFace/images OpenRL/DeepFakeFace:./images -r dataset`
- Upload dataset with: `htool upload-data <local_dataset_dir> <organization_or_username/dataset_name>`
  - For example: `htool upload-data ./daily_dialog OpenRL/daily_dialog`
- Upload model with: `htool upload-model <local_model_dir> <organization_or_username/model_name>`
  - For example: `htool upload-model ./tizero OpenRL/tizero`


## Citing huggingface_tool

If our work has been helpful to you, please feel free to cite us:
```latex
@misc{huggingface_tool2023,
    title={huggingface_tool},
    author={OpenRL Contributors},
    publisher = {GitHub},
    howpublished = {\url{https://github.com/OpenRL-Lab/huggingface_tool}},
    year={2023},
}
```
