# (Ongoing) Zero-shot TTS based on VITS
[VITS](https://arxiv.org/abs/2106.06103): Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech

## Note
0. This repository aims to implement a VITS-based zero-shot TTS system varying with diverse style/speaker conditioning methods.
0. To remove the secondary elements, we simply extract a style representation by jointly training a reference encoder from [StyleSpeech](https://arxiv.org/abs/2106.03153). In detail, 1. we do not utilize pretrained models (e.g., [Link1](https://arxiv.org/abs/2009.14153), [Link2](https://arxiv.org/abs/2006.11477)) as the reference encoder, 2. we do not apply meta-learning or speaker verification loss during training.
0. [LibriTTS]((https://research.google/tools/datasets/libri-tts/)) dataset (train-clean-100 and train-clean-360) is used for training.

|Model|Text Encoder|Flow|Posterior Encoder|Vocoder|
|------|-----|-----|-----|-----|
|`master`([YourTTS](https://arxiv.org/abs/2112.02418))|Output addition|Global conditioning|Global conditioning|Input addition
|`s1`(Proposed)|SC-CNN|SC-CNN|SC-CNN|TBD|


## Pre-requisites
0. Python >= 3.6
0. Clone this repository
0. Install python requirements. Please refer [requirements.txt](requirements.txt)
    1. You may need to install espeak first: `apt-get install espeak`
0. Download datasets
    1. Download and extract the LJ Speech dataset, then rename or create a link to the dataset folder: `ln -s /path/to/LJSpeech-1.1/wavs DUMMY1`
    1. For mult-speaker setting, download and extract the VCTK dataset, and downsample wav files to 22050 Hz. Then rename or create a link to the dataset folder: `ln -s /path/to/VCTK-Corpus/downsampled_wavs DUMMY2`
0. Build Monotonic Alignment Search and run preprocessing if you use your own datasets.
```sh
# Cython-version Monotonoic Alignment Search
cd monotonic_align
python setup.py build_ext --inplace
```

```
## Training Exmaple
python train_zs.py -c configs/libritts_base.json -m libritts_base
```


## Inference Example
See [inference.ipynb](inference.ipynb)
