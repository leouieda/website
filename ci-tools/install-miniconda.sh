#!/bin/bash
# Check if miniconda is available in the cache, download it otherwise, and
# install.

mkdir -p download
echo -e "Cached in $HOME/download:"
ls -lh download

cd download

if [[ ! -f miniconda.sh ]]; then
    echo -e "Downloading miniconda installer"
    wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
else
    echo -e "Used cached miniconda installed"
fi

chmod +x miniconda.sh && ./miniconda.sh -b
