#!/bin/bash

# Install Python
PYTHON_VERSION="3.7"  # Replace with desired Python version

# Check if Python is already installed
if ! command -v python3 &>/dev/null; then
  echo "Installing Python $PYTHON_VERSION..."
  curl -sSL "https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer" | bash
  echo "export PATH=\"\$HOME/.pyenv/bin:\$PATH\"" >> ~/.bashrc
  echo "eval \"\$(pyenv init -)\"" >> ~/.bashrc
  echo "eval \"\$(pyenv virtualenv-init -)\"" >> ~/.bashrc
  source ~/.bashrc
  pyenv install "$PYTHON_VERSION"
  pyenv global "$PYTHON_VERSION"
else
  echo "Python is already installed."
fi

# Install colorama library
echo "Installing colorama library..."
pip install colorama

# Install humanize library
echo "Installing humanize library..."
pip install humanize

echo "Setup complete."
