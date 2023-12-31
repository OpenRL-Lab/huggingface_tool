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


import click
from click.core import Context, Option
from termcolor import colored

from huggingface_tool import __AUTHOR__, __EMAIL__, __TITLE__, __VERSION__
from huggingface_tool.utils.util import get_system_info


def red(text: str):
    return colored(text, "red")


def print_version(
    ctx: Context,
    param: Option,
    value: bool,
) -> None:
    if not value or ctx.resilient_parsing:
        return
    click.secho(f"{__TITLE__.upper()} version: {red(__VERSION__)}")
    click.secho(f"Developed by {__AUTHOR__}, Email: {red(__EMAIL__)}")
    ctx.exit()


def print_system_info(
    ctx: Context,
    param: Option,
    value: bool,
) -> None:
    if not value or ctx.resilient_parsing:
        return
    info_dict = get_system_info()
    for key, value in info_dict.items():
        click.secho(f"- {key}: {red(value)}")
    ctx.exit()


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(invoke_without_command=True)
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Show package's version information.",
)
@click.option(
    "--system_info",
    is_flag=True,
    callback=print_system_info,
    expose_value=False,
    is_eager=True,
    help="Show system information.",
)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        pass
    else:
        pass
        # click.echo(f"I am about to invoke {ctx.invoked_subcommand}")


@cli.command()
@click.argument("model_name")
@click.argument("save_dir")
def save_dm(model_name, save_dir):
    from huggingface_tool.savers.diffusion_model_saver import DiffusionModelSaver

    saver = DiffusionModelSaver(model_name)
    if saver.load():
        saver.save(save_dir)
    else:
        saver.logger.info("Model not found")


@cli.command()
@click.argument("file_name")
@click.argument("save_dir")
@click.option(
    "--repo_type",
    "-r",
    type=click.Choice(
        [
            "model",
            "dataset",
        ]
    ),
    default="model",
    help="repo type",
)
def save_file(file_name, save_dir, repo_type):
    from huggingface_tool.savers.file_saver import FileSaver

    saver = FileSaver(file_name, repo_type)
    if saver.load():
        saver.save(save_dir)
    else:
        saver.logger.info("File not found")


@cli.command()
@click.argument("repo_name")
@click.argument("save_dir")
@click.option(
    "--repo_type",
    "-r",
    type=click.Choice(
        [
            "model",
            "dataset",
        ]
    ),
    default="model",
    help="repo type",
)
def save_repo(repo_name, save_dir, repo_type):
    from huggingface_tool.savers.repo_saver import RepoSaver

    saver = RepoSaver(repo_name, repo_type)
    if saver.load():
        saver.save(save_dir)
    else:
        saver.logger.info("Repo not found")


@cli.command()
@click.argument("tokenizer_name")
@click.argument("save_dir")
def save_tk(tokenizer_name, save_dir):
    from huggingface_tool.savers.tokenizer_saver import TokenizerSaver

    saver = TokenizerSaver(tokenizer_name)
    if saver.load():
        saver.save(save_dir)
    else:
        saver.logger.info("Tokenizer not found")


@cli.command()
@click.argument("dataset_name")
@click.argument("save_dir")
def save_data(dataset_name, save_dir):
    from huggingface_tool.savers.dataset_saver import DatasetSaver

    saver = DatasetSaver(dataset_name)
    if saver.load():
        saver.save(save_dir)
    else:
        saver.logger.info("Dataset not found")


@cli.command()
@click.argument("model_class")
@click.argument("model_name")
@click.argument("save_dir")
def save_model(model_class, model_name, save_dir):
    from huggingface_tool.savers.model_saver import ModelSaver

    saver = ModelSaver(model_class, model_name)
    if saver.load():
        saver.save(save_dir)
    else:
        saver.logger.info("Dataset not found")


@cli.command()
@click.argument("dataset_dir")
@click.argument("dataset_name")
def upload_data(dataset_dir, dataset_name):
    from huggingface_tool.uploaders.dataset_uploader import DatasetUploader

    uploader = DatasetUploader(dataset_dir, dataset_name)
    if uploader.check():
        uploader.push()
    else:
        uploader.logger.info("Dataset not valid")


@cli.command()
@click.argument("file_path")
@click.argument("remote_file_path")
@click.option(
    "--repo_type",
    "-r",
    type=click.Choice(
        [
            "model",
            "dataset",
        ]
    ),
    default="model",
    help="repo type",
)
def upload_file(file_path, remote_file_path, repo_type):
    from huggingface_tool.uploaders.file_uploader import FileUploader

    uploader = FileUploader(file_path, remote_file_path, repo_type)
    if uploader.check():
        uploader.push()
    else:
        uploader.logger.info("File not valid")


@cli.command()
@click.argument("dir_path")
@click.argument("remote_dir_path")
@click.option(
    "--repo_type",
    "-r",
    type=click.Choice(
        [
            "model",
            "dataset",
        ]
    ),
    default="model",
    help="repo type",
)
def upload_dir(dir_path, remote_dir_path, repo_type):
    from huggingface_tool.uploaders.dir_uploader import DirUploader

    uploader = DirUploader(dir_path, remote_dir_path, repo_type)
    if uploader.check():
        uploader.push()
    else:
        uploader.logger.info("Directory not valid")


@cli.command()
@click.argument("model_dir")
@click.argument("model_name")
def upload_model(model_dir, model_name):
    from huggingface_tool.uploaders.model_uploader import ModelUploader

    uploader = ModelUploader(model_dir, model_name)
    if uploader.check():
        uploader.push()
    else:
        uploader.logger.info("Model not valid")
