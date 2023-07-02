#!/usr/bin/env bash
VENV_NAME="venv-music-gen"
echo "Setting up environment in .${VENV_NAME} ..."
if [ ! -d ".${VENV_NAME}" ]; then \
  virtualenv --system-site-packages .${VENV_NAME}
fi
export BUILD_SPLIT_CUDA=ON
source "./.${VENV_NAME}/bin/activate"
echo "Welcome to Music Gen CLI Shell."
echo "You are in a virtual env. Please Run "pip install . --user" to install non-nix dependencies"
echo "See music-gen-cli --help"
