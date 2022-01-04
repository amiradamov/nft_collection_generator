from PIL import Image 
from IPython.display import display 
import random
import json
import os

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

body = ["body1", "body2", "body3", "body4", "body5", "body6"] 
body_weights = [15, 10, 15, 5, 25, 30]

jacket = ["jacket1", "jacket2"] 
jacket_weights = [40, 50]

neck = ["neck1", "neck2", "neck3", "neck4", "neck5"] 
neck_weights = [70, 10, 5, 1, 14]

shorts = ['shorts', 'shorts1', 'shorts2']
shorts_weights = [30 , 34, 36]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name

body_files = {
    "body1": "body1",
    "body2": "body2",
    "body3": "body3",
    "body4": "body4",
    "body5": "body5",
    "body6": "body6"

}

jacket_files = {
    "jacket1": "jacket1",
    "jacket2": "jacket2"
}

neck_files = {
    "neck1": "neck1",
    "neck2": "neck2",
    "neck3": "neck3",
    "neck4": "neck4",
    "neck5": "neck5"
}

shorts_files = {
    "shorts": "shorts",
    "shorts1": "shorts1",
    "shorts2": "shorts2"
}

## Generate Traits

TOTAL_IMAGES = 50 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["body"] = random.choices(body, body_weights)[0]
    new_image ["jacket"] = random.choices(jacket, jacket_weights)[0]
    new_image ["neck"] = random.choices(neck, neck_weights)[0]
    new_image ["shorts"] = random.choices(shorts, shorts_weights)[0]
    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)


# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1
   
print(all_images)


# Get Trait Counts

body_count = {}
for item in body:
    body_count[item] = 0
    
jacket_count = {}
for item in jacket:
    jacket_count[item] = 0

neck_count = {}
for item in neck:
    neck_count[item] = 0
    
shorts_count = {}
for item in shorts:
    shorts_count[item] = 0

for image in all_images:
    body_count[image["body"]] += 1
    jacket_count[image["jacket"]] += 1
    neck_count[image["neck"]] += 1
    shorts_count[image["shorts"]] += 1
    
print(body_count)
print(jacket_count)
print(neck_count)
print(shorts_count)


#### Generate Images

os.mkdir(f'./images')

for item in all_images:

    im1 = Image.open(f'./1/{body_files[item["body"]]}.png').convert('RGBA')
    im2 = Image.open(f'./2/{jacket_files[item["jacket"]]}.png').convert('RGBA')
    im3 = Image.open(f'./3/{neck_files[item["neck"]]}.png').convert('RGBA')
    im4 = Image.open(f'./4/{shorts_files[item["shorts"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)

                     

    #Convert to RGB
    rgb_im = com3.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)