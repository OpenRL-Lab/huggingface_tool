# huggingface_tool

[![PyPI](https://img.shields.io/pypi/v/huggingface-tool)](https://pypi.org/project/huggingface-tool/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/huggingface-tool)
[![Hits-of-Code](https://hitsofcode.com/github/OpenRL-Lab/huggingface_tool?branch=main)](https://hitsofcode.com/github/OpenRL-Lab/huggingface_tool/view?branch=main)

Tools for loading, upload, managing huggingface models and datasets


## Installation

`pip install huggingface-tool`

## Usage

Firstly, you need to login with `huggingface-cli login` (you can create or find your token at [settings](https://huggingface.co/settings/tokens)).

- Download and save transformer models with: `htool save-model <model_class> <model_name> <save_dir>`
  - For example: `htool save-model AutoModelForCausalLM gpt2 ./gpt2`
- Download and save tokenizer with: `htool save-tk <tokenizer_name> <save_dir>`
  - For example: `htool save-tk gpt2 ./gpt2 `
- Download and save dataset with: `htool save-data <dataset_name> <save_dir>`
  - For example: `htool save-data daily_dialog ./daily_dialog`
- Download and save diffusion models with: `htool save-dm <model_name> <save_dir>`
  - For example: `htool save-dm google/ddpm-cat-256 ./google/`

You can also use htool to upload datasets and models to huggingface.

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