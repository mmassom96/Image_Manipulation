#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import torch
import matplotlib.pyplot as plt
from PIL import Image, ImageOps


# In[2]:


image_input = input('Select an image to turn into a Warhol masterpiece:\n' +
                '   input 1 for monroe.jpg\n' +
                '   input 2 for campbells.jpg\n' +
                '   input 3 for deadpool.jpg\n' +
                '   else default is python.jpg\n')
image_id = int(image_input)
if(image_id == 1):
    base_image = Image.open('monroe.jpg')
    threshold = 164
elif(image_id == 2):
    base_image = Image.open('campbells.jpg')
    threshold = 185
elif(image_id == 3):
    base_image = Image.open('deadpool.jpg')
    threshold = 164
else:
    base_image = Image.open('python.jpg')
    threshold = 128
base_array = numpy.array(base_image)
plt.imshow(base_array)
base_image.show()


# In[3]:


base_size = base_array.shape
#print('Height:', base_size[0])
#print('Width:', base_size[1])


# In[4]:


#Set grid size as a perfect square (i.e. input of 3 creates a 3x3=9 grid of images)
gridsize = 2
final_dimensions = (gridsize*base_size[0], gridsize*base_size[1], base_size[2])
final_array = numpy.zeros(final_dimensions)


# In[5]:


grayscale = ImageOps.grayscale(base_image)
grayscale_array = numpy.array(grayscale)
#plt.imshow(grayscale)


# In[6]:


red_array = numpy.zeros(base_array.shape)

for x in range(base_array.shape[0]):
    for y in range(base_array.shape[1]):
            red_array[x,y,0] = grayscale_array[x,y]
            red_array[x,y,1] = 0
            red_array[x,y,2] = 0
            
green_array = numpy.zeros(base_array.shape)

for x in range(base_array.shape[0]):
    for y in range(base_array.shape[1]):
            green_array[x,y,0] = 0
            green_array[x,y,1] = grayscale_array[x,y]
            green_array[x,y,2] = 0
            
blue_array = numpy.zeros(base_array.shape)

for x in range(base_array.shape[0]):
    for y in range(base_array.shape[1]):
            blue_array[x,y,0] = 0
            blue_array[x,y,1] = 0
            blue_array[x,y,2] = grayscale_array[x,y]
            
yellow_array = numpy.zeros(base_array.shape)

for x in range(base_array.shape[0]):
    for y in range(base_array.shape[1]):
            yellow_array[x,y,0] = grayscale_array[x,y]
            yellow_array[x,y,1] = grayscale_array[x,y]
            yellow_array[x,y,2] = 0
            
cyan_array = numpy.zeros(base_array.shape)

for x in range(base_array.shape[0]):
    for y in range(base_array.shape[1]):
            cyan_array[x,y,0] = 0
            cyan_array[x,y,1] = grayscale_array[x,y]
            cyan_array[x,y,2] = grayscale_array[x,y]

magenta_array = numpy.zeros(base_array.shape)

for x in range(base_array.shape[0]):
    for y in range(base_array.shape[1]):
            magenta_array[x,y,0] = grayscale_array[x,y]
            magenta_array[x,y,1] = 0
            magenta_array[x,y,2] = grayscale_array[x,y]
            
pink_array = numpy.zeros(base_array.shape)

for x in range(base_array.shape[0]):
    for y in range(base_array.shape[1]):
            pink_array[x,y,0] = grayscale_array[x,y]
            pink_array[x,y,1] = grayscale_array[x,y] * 0.75
            pink_array[x,y,2] = grayscale_array[x,y] * 0.8


# In[7]:


red = Image.fromarray(red_array.astype('uint8'))
plt.imshow(red)


# In[8]:


green = Image.fromarray(green_array.astype('uint8'))
plt.imshow(green)


# In[9]:


blue = Image.fromarray(blue_array.astype('uint8'))
plt.imshow(blue)


# In[10]:


yellow = Image.fromarray(yellow_array.astype('uint8'))
plt.imshow(yellow)


# In[11]:


cyan = Image.fromarray(cyan_array.astype('uint8'))
plt.imshow(cyan)


# In[12]:


magenta = Image.fromarray(magenta_array.astype('uint8'))
plt.imshow(magenta)


# In[13]:


pink = Image.fromarray(pink_array.astype('uint8'))
plt.imshow(pink)


# In[14]:


for x in range(final_array.shape[0]):
    for y in range(final_array.shape[1]):
        if(x < base_array.shape[0]):
            if(y < base_array.shape[1]):
                final_array[x,y,0] = red_array[x,y,0]
                final_array[x,y,1] = red_array[x,y,1]
                final_array[x,y,2] = red_array[x,y,2]
            else:
                final_array[x,y,0] = green_array[x,y-base_array.shape[1],0]
                final_array[x,y,1] = green_array[x,y-base_array.shape[1],1]
                final_array[x,y,2] = green_array[x,y-base_array.shape[1],2]
        else:
            if(y < base_array.shape[1]):
                final_array[x,y,0] = yellow_array[x-base_array.shape[0],y,0]
                final_array[x,y,1] = yellow_array[x-base_array.shape[0],y,1]
                final_array[x,y,2] = yellow_array[x-base_array.shape[0],y,2]
            else:
                final_array[x,y,0] = blue_array[x-base_array.shape[0],y-base_array.shape[1],0]
                final_array[x,y,1] = blue_array[x-base_array.shape[0],y-base_array.shape[1],1]
                final_array[x,y,2] = blue_array[x-base_array.shape[0],y-base_array.shape[1],2]
        


# In[15]:


final_1 = Image.fromarray(final_array.astype('uint8'))
plt.imshow(final_1)
#final_1.show()


# In[16]:


for x in range(final_array.shape[0]):
    for y in range(final_array.shape[1]):
        if(x < base_array.shape[0]):
            if(y < base_array.shape[1]):
                final_array[x,y,0] = cyan_array[x,y,0]
                final_array[x,y,1] = cyan_array[x,y,1]
                final_array[x,y,2] = cyan_array[x,y,2]
            else:
                final_array[x,y,0] = magenta_array[x,y-base_array.shape[1],0]
                final_array[x,y,1] = magenta_array[x,y-base_array.shape[1],1]
                final_array[x,y,2] = magenta_array[x,y-base_array.shape[1],2]
        else:
            if(y < base_array.shape[1]):
                final_array[x,y,0] = pink_array[x-base_array.shape[0],y,0]
                final_array[x,y,1] = pink_array[x-base_array.shape[0],y,1]
                final_array[x,y,2] = pink_array[x-base_array.shape[0],y,2]
            else:
                final_array[x,y,0] = yellow_array[x-base_array.shape[0],y-base_array.shape[1],0]
                final_array[x,y,1] = yellow_array[x-base_array.shape[0],y-base_array.shape[1],1]
                final_array[x,y,2] = yellow_array[x-base_array.shape[0],y-base_array.shape[1],2]


# In[17]:


final_2 = Image.fromarray(final_array.astype('uint8'))
plt.imshow(final_2)
#final_2.show()


# In[18]:


pink_green = numpy.zeros(base_array.shape)

for x in range(base_array.shape[0]):
    for y in range(base_array.shape[1]):
        pixel = grayscale_array[x,y]
        if(pixel <= threshold):
            pink_green[x,y,0] = 1.2 * grayscale_array[x,y] * 0.01
            pink_green[x,y,1] = 1.2 * grayscale_array[x,y] * 0.85
            pink_green[x,y,2] = 1.2 * grayscale_array[x,y]
        else:
            pink_green[x,y,0] = 0
            pink_green[x,y,1] = grayscale_array[x,y]*.75
            pink_green[x,y,2] = 0

            
red_orange = numpy.zeros(base_array.shape)

for x in range(base_array.shape[0]):
    for y in range(base_array.shape[1]):
        pixel = grayscale_array[x,y]
        if(pixel <= threshold):
            red_orange[x,y,0] = 1.3 * grayscale_array[x,y]
            red_orange[x,y,1] = 0
            red_orange[x,y,2] = 0
        else:
            red_orange[x,y,0] = grayscale_array[x,y]
            red_orange[x,y,1] = grayscale_array[x,y] * 0.7
            red_orange[x,y,2] = 0

blue_yellow = numpy.zeros(base_array.shape)

for x in range(base_array.shape[0]):
    for y in range(base_array.shape[1]):
        pixel = grayscale_array[x,y]
        if(pixel <= threshold):
            blue_yellow[x,y,0] = 0
            blue_yellow[x,y,1] = 0
            blue_yellow[x,y,2] = 1.5 * grayscale_array[x,y]
        else:
            blue_yellow[x,y,0] = grayscale_array[x,y]
            blue_yellow[x,y,1] = grayscale_array[x,y]
            blue_yellow[x,y,2] = 0
            
turqoise_magenta = numpy.zeros(base_array.shape)

for x in range(base_array.shape[0]):
    for y in range(base_array.shape[1]):
        pixel = grayscale_array[x,y]
        if(pixel >= threshold):
            turqoise_magenta[x,y,0] = 0.85 * grayscale_array[x,y] * 0.61
            turqoise_magenta[x,y,1] = 0.85 * grayscale_array[x,y] * 0.93
            turqoise_magenta[x,y,2] = 0.85 * grayscale_array[x,y] * 0.85
        else:
            turqoise_magenta[x,y,0] = 1.5 * grayscale_array[x,y]
            turqoise_magenta[x,y,1] = 0
            turqoise_magenta[x,y,2] = 1.5 * grayscale_array[x,y]


# In[19]:


pink_green_img = Image.fromarray(pink_green.astype('uint8'))
plt.imshow(pink_green_img)


# In[20]:


red_orange_img = Image.fromarray(red_orange.astype('uint8'))
plt.imshow(red_orange_img)


# In[21]:


blue_yellow_img = Image.fromarray(blue_yellow.astype('uint8'))
plt.imshow(blue_yellow_img)


# In[22]:


turqoise_magenta_img = Image.fromarray(turqoise_magenta.astype('uint8'))
plt.imshow(turqoise_magenta_img)


# In[23]:


for x in range(final_array.shape[0]):
    for y in range(final_array.shape[1]):
        if(x < base_array.shape[0]):
            if(y < base_array.shape[1]):
                final_array[x,y,0] = pink_green[x,y,0]
                final_array[x,y,1] = pink_green[x,y,1]
                final_array[x,y,2] = pink_green[x,y,2]
            else:
                final_array[x,y,0] = turqoise_magenta[x,y-base_array.shape[1],0]
                final_array[x,y,1] = turqoise_magenta[x,y-base_array.shape[1],1]
                final_array[x,y,2] = turqoise_magenta[x,y-base_array.shape[1],2]
        else:
            if(y < base_array.shape[1]):
                final_array[x,y,0] = blue_yellow[x-base_array.shape[0],y,0]
                final_array[x,y,1] = blue_yellow[x-base_array.shape[0],y,1]
                final_array[x,y,2] = blue_yellow[x-base_array.shape[0],y,2]
            else:
                final_array[x,y,0] = red_orange[x-base_array.shape[0],y-base_array.shape[1],0]
                final_array[x,y,1] = red_orange[x-base_array.shape[0],y-base_array.shape[1],1]
                final_array[x,y,2] = red_orange[x-base_array.shape[0],y-base_array.shape[1],2]


# In[24]:


final_two_tone = Image.fromarray(final_array.astype('uint8'))
plt.imshow(final_two_tone)
final_two_tone.show()


# In[25]:


if(image_id == 1):
    final_two_tone.save('monroe_warhol.jpg')
elif(image_id == 2):
    final_two_tone.save('campbells_warhol.jpg')
elif(image_id == 3):
    final_two_tone.save('deadpool_warhol.jpg')
else:
    final_two_tone.save('python_warhol.jpg')


# In[ ]:




