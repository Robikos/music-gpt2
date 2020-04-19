echo "Move model files to source"
cp -R gpt-2/models gpt-2/src/models

echo "Evaluate unconditional samples"
PYTHONPATH=gpt-2/src python gpt-2/src/generate_unconditional_samples.py
