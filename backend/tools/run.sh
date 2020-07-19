
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
pip3 install Flask gunicorn

python3 "${SRCPATH}/noplp.py" --datapath /home/ec2-user/noplp/backend/data
