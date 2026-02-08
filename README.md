# American Sign Language Text Convertor

A computer-vision prototype that converts ASL hand signs into text using a CNN-based model. Includes training notebooks and a real-time webcam demo.

## Overview
- `Main.ipynb`: training and evaluation
- `create_data.ipynb`: dataset preparation
- `app2.py`: real-time ASL to text demo
- `camera.py`: webcam capture utility
- `model/`: trained model artifacts

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the Demo
```bash
python app2.py
```
The demo will open a webcam window and display predicted letters/words.

## Dataset
See `Dataset link` for the source of the ASL dataset.

## Notes
- On macOS, you may need to install enchant dictionaries for `pyenchant`.
- Model artifacts are loaded from the `model/` directory.
