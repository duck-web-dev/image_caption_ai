__all__ = ['caption_image']

from pathlib import Path
from PIL import Image
import time

# Follow model installation instructions on README or:
# 1) https://huggingface.co/docs/transformers/installation
# 2) https://pytorch.org/get-started/locally/

print('Beginnned loading image-to-text model (up to 30 secs)...')
from transformers import BlipProcessor, BlipForConditionalGeneration
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
print('Done loading image-to-text model')


def caption_image(image_file: "str | bytes | Path", condition: "str | None" = None) -> str:
	raw_image = Image.open(image_file).convert('RGB')

	clock_start = time.time()

	if condition:
		# text = "a photography of"
		text = condition
		inputs = processor(raw_image, text, return_tensors="pt")
		out = model.generate(**inputs)
		result = processor.decode(out[0], skip_special_tokens=True)
	else:
		inputs = processor(raw_image, return_tensors="pt")
		out = model.generate(**inputs)
		result = processor.decode(out[0], skip_special_tokens=True)

	time_spent = (time.time() - clock_start) * 1000   # time spent (in milliseconds)
	print(f'Spent {time_spent}ms on "{result}"')

	return result