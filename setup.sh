echo "Clone nshepperd/gpt-2"
git clone git@github.com:nshepperd/gpt-2.git

echo "Install pip dependecies"
pip install -r requirements.txt

echo "Download GPT-2 model"
PYTHONPATH=gpt-2/src python gpt-2/download_model.py 117M

echo "Create directories"
mkdir data
mkdir models

echo "Download artist songs"
python fetch_songs.py '$1'

echo "Encode lyrics"
PYTHONPATH=gpt-2/src python gpt-2/encode.py data/lyrics.txt data/lyrics.npz
