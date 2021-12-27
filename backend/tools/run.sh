#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    echo "USAGE $0 <ENV (local or prod)>"
    exit 1
fi

TOOLSPATH="$( cd "$(dirname "$0")" ; pwd -P )"
SRCPATH="$TOOLSPATH/../src"
VENV_PATH="${TOOLSPATH}/noplp-venv"

export PYTHONPATH=$PYTHONPATH':./lib'

echo "> Creating Python Virtual Environment"
if [ ! -d "$VENV_PATH" ]
then
    echo "virtualenv $VENV_PATH"
    python3 -m venv $VENV_PATH
else
    echo "Environment already exists"
fi

echo "> Activating environment"
echo "source ${VENV_PATH}/bin/activate"
source "${VENV_PATH}/bin/activate"

echo "> Installing requirements"
which pip3
pip3 install Flask gunicorn requests

if [[ $1 -eq "local" ]]; then
    BASE_PATH="/Users/fservais/Projects/personal/noplp"
    PORT="5000"
else
    BASE_PATH="/root/noplp"
    PORT="80"
fi

echo "Base path: $BASE_PATH"

python3 "${SRCPATH}/noplp.py" --datapath "$BASE_PATH/backend/data" --port "$PORT" --client_id=57832e0043e241839c8fb136b1689e0f --client_secret=91f25bceb8204bdcac15a3099499ab8d
