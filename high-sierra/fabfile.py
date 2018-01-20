#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import fabric.contrib.files
from fabric.api import env, sudo, execute, run, put


def dotfiles():
    """ dotfiles を適当な箇所に置く """

    put("dotfiles/inputrc", "~/.inputrc")
    # put("dotfiles/tmux.conf", "~/.tmux.conf")
    # put("dotfiles/vimrc", "~/.vimrc")
    put("dotfiles/bashrc", "~/.bashrc")


def brew():
    """ brew, brew cask と brew.txt, cask.txt 中のパッケージをインストールする """

    url = "https://raw.githubusercontent.com/Homebrew/install/master/install"
    run(" ".join([
        "ruby", "-e",
        "\"$(curl -fsSL {})\"".format(url)
    ]))
    run(" ".join([
        "brew", "tap", "caskroom/cask"
    ]))
    run(" ".join([
        "brew", "update"
    ]))

    brew_pkgs_file = "./brew/brew.txt"
    if os.path.exists(brew_pkgs_file):
        with open(brew_pkgs_file) as fi:
            for line in fi:
                pkg = line.rstrip()
                run(" ".join(["brew", "install", pkg]))

    cask_pkgs_file = "./brew/cask.txt"
    if os.path.exists(cask_pkgs_file):
        with open(cask_pkgs_file) as fi:
            for line in fi:
                pkg = line.rstrip()
                run(" ".join(["brew", "cask", "install", pkg]))


def sshfs():
    """ sshfs をインストールする """

    run(" ".join([
        "brew", "cask", "install", "osxfuse"
    ]))
    run(" ".join([
        "brew", "install", "sshfs"
    ]))


def bashit():
    """ bash-it をインストールする """

    bashit_plugins_file = "./bashit/plugins.txt"
    bashit_completion_file = "./bashit/completion.txt"
    bashit_aliases_file = "./bashit/aliases.txt"

    if not fabric.contrib.files.exists("~/.bash-it"):
        run(" ".join([
            "git", "clone", "--depth=1",
            "https://github.com/Bash-it/bash-it.git",
            "~/.bash-it"
        ]))

        run(" ".join([
            "~/.bash-it/install.sh", "--silent"
        ]))

    run(" ".join([
        "source", "~/.bashrc"
    ]))

    with open(bashit_plugins_file) as fi:
        plugins = " ".join([line.strip() for line in fi])
        run(" ".join([
            "bash-it", "enable", "plugin", plugins
        ]))

    with open(bashit_completion_file) as fi:
        completions = " ".join([line.strip() for line in fi])
        run(" ".join([
            "bash-it", "enable", "completion", completions
        ]))

    with open(bashit_aliases_file) as fi:
        aliases = " ".join([line.strip() for line in fi])
        run(" ".join([
            "bash-it", "enable", "alias", aliases
        ]))


def volt():
    """ volt をインストールする """

    run(" ".join([
        "go", "get", "github.com/vim-volt/volt"
    ]))


def solarized():
    """ solarized をインストールする """

    run(" ".join([
        "git", "clone",
        "https://github.com/altercation/solarized",
        "~/.colors/solarized"
    ]))

    # setup vim colorscheme
    if not fabric.contrib.files.exists("~/.vim/colors"):
        run(" ".join(["mkdir", "-p", "~/.vim/colors"]))

    run(" ".join([
        "cp",
        "~/.colors/solarized/vim-colors-solarized/colors/solarized.vim",
        "~/.vim/colors/"
    ]))


def python2_environment():
    """ python2 にpep8系, ipythonをインストールする """

    run(" ".join([
        "pip2", "install", "pep8"
    ]))

    run(" ".join([
        "pip2", "install", "autopep8"
    ]))

    run(" ".join([
        "pip2", "install", "flake8"
    ]))

    run(" ".join([
        "pip2", "install", "ipython"
    ]))


def python_environment():
    """ python3 にpep8系, ipythonをインストールする """

    run(" ".join([
        "pip3", "install", "pep8"
    ]))

    run(" ".join([
        "pip3", "install", "autopep8"
    ]))

    run(" ".join([
        "pip3", "install", "flake8"
    ]))

    run(" ".join([
        "pip3", "install", "ipython"
    ]))
