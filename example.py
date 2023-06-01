from main import caption_image
from io import BytesIO
import requests

print('Downloading image of cat...')
cat_image = BytesIO(requests.get('https://farm9.staticflickr.com/8237/8566763080_149842d963_z.jpg', stream=True).content)

print('Running captioning of image...')
print('Caption:', caption_image(cat_image))
print('Question answer:', caption_image(cat_image, 'Drink name is'))