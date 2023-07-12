# huggingface_tool

[![PyPI](https://img.shields.io/pypi/v/huggingface-tool)](https://pypi.org/project/huggingface-tool/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/huggingface-tool)
[![Hits-of-Code](https://hitsofcode.com/github/OpenRL-Lab/huggingface_tool?branch=main)](https://hitsofcode.com/github/OpenRL-Lab/huggingface_tool/view?branch=main)

Tools for loading, upload, managing huggingface models and datasets


## Installation

`pip install huggingface-tool`

## Usage

- Download and save transformer models with: `htool save-model <model_class> <model_name> <save_dir>`
  - For example: `htool save-model AutoModelForCausalLM gpt2 ./gpt2`
- Download and save tokenizer with: `htool save-tk <tokenizer_name> <save_dir>`
  - For example: `htool save-tk gpt2 ./gpt2 `
- Download and save dataset with: `htool save-data <dataset_name> <save_dir>`
  - For example: `htool save-data daily_dialog ./daily_dialog`
- Download and save diffusion models with: `htool save-dm <model_name> <save_dir>`
  - For example: `htool save-dm google/ddpm-cat-256 ./google/`


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