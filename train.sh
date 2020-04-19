echo "Train model"
PYTHONPATH=gpt-2/src python gpt-2/train.py --dataset data/lyrics.npz
