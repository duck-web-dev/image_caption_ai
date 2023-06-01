## Simple Image Captioning API for huggingface

This library is a small wrapper for the Hugging Face model `blip-image-captioning`. It provides an easy to use interface for generating natural language captions from images.

P.S.  This is for my personal use, so I wont make a big README 😅

### Installation Instructions

- Option 1 - Follow the steps below:
```bash
pip install --no-cache-dir -r requirements.txt

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu  # If you use GPU, see option 2 below

pip install 'transformers[torch]'

python3 main.py  # Run main.py for the first time to download model
```

- Option 2 - do it yourself:

  1. [Download huggingface library for python](https://huggingface.co/docs/transformers/installation)
   
  2. Install pytorch, see [their docs](https://pytorch.org/get-started/locally)

  3. ```pip install -r requirements.txt```

### Usage

To use the AI Image Captioning Library in your Python code, follow the steps below:

1. To get started, import ```caption_image``` function from this library.
   
2. Pass image to ```image_file``` arguement, image should be either path or bits buffer.

3. If you have a custom question (see ```example.py```), use ```condition``` argument. Leave it empty to just make a caption.

4. The function will return a natural language response for the given image.

#### Example:

```python
caption = caption_image('./cat.png', 'Animal name is')
```