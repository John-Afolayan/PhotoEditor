import sys  # get_image calls exit
from Cimpl import *
from photo_editor import *
import random

def blur(image):
      
    target = copy(image)
    
        
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(image, x, y - 1)
            left_red, left_green, left_blue = get_color(image, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            center_red, center_green, center_blue = get_color(image, x, y)
            top_right_red,top_right_green,top_right_blue = get_color(image, x+1, y+1)
            bottom_right_red,bottom_right_green,bottom_right_blue = get_color(image, x+1, y-1)
            bottom_left_red,bottom_left_green,bottom_left_blue = get_color(image, x-1, y-1)
            top_left_red,top_left_green,top_left_blue = get_color(image, x-1, y+1)            
            
            
            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red + top_right_red + 
                       bottom_right_red + bottom_left_red + top_left_red) // 5

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green + top_right_green + 
                       bottom_right_green + bottom_left_green + top_left_green) // 5

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue + top_right_blue + 
                       bottom_right_blue + bottom_left_blue + top_left_blue) // 5

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target



def detect_edges(image, threshold):
   
    new_image = copy(image)
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):
            
            top_red, top_green, top_blue = get_color(image, x, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            
            top_brightness = (top_red + top_green + top_blue) // 3
            bttm_brightness = (bottom_red + bottom_green + bottom_blue) // 3
            abs_val = abs(top_brightness - bttm_brightness)
                      
            if abs_val > threshold:
                r, g, b = (0, 0, 0)
            else:
                r, g, b = (255, 255, 255)
            
            set_color(new_image, x, y, create_color(r,g,b))
    
    return new_image


def detect_edges_better(image, threshold):
    
    new_image = copy(image)
    for y in range(1, get_height(image) - 2):
        for x in range(1, get_width(image) - 1):
            
            top_red, top_green, top_blue = get_color(image, x, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            
            top_brightness = (top_red + top_green + top_blue) // 3
            bttm_brightness = (bottom_red + bottom_green + bottom_blue) // 3
            abs_val = abs(top_brightness - bttm_brightness)
                      
            if abs_val > threshold:
                r, g, b = (0, 0, 0)
            else:
                r, g, b = (125, 125, 125)
            
            set_color(new_image, x, y, create_color(r,g,b))
    
    return new_image


def _adjust_component(amount):
    """add-on function for posterize"""
    amount = int(amount)
    if amount > 0 and amount < 63:
        amount = 31
    elif amount > 64 and amount < 127:
        amount = 95
    elif amount > 128 and amount < 191:
        amount = 159
    elif amount > 192 and amount < 255:
        amount = 223
    return (amount)


def posterize(image):
      
    new_image = copy(image)
    for (x, y, (r, g, b)) in new_image:
        setRed = _adjust_component(r)
        setGreen = _adjust_component(g)
        setBlue = _adjust_component(b)
        newCol = create_color(setRed, setGreen, setBlue)
        set_color(new_image, x, y, newCol)
    return (new_image)



def scatter(original):
   
    # Create an image that is a copy of the original.
    
    scattered = copy(original)
    
    # Visit all the pixels in new_image.
    
    for x, y, (r, g, b) in scattered:
        
        row_and_column_are_in_bounds = False
        while not row_and_column_are_in_bounds:
            
            rand1 = random.randint(-10, 10)
            rand2 = random.randint(-10, 10) 
            

            random_column = x + rand1
            random_row = y + rand2
            
            # Determine if the random coordinates are in bounds.

            if ( random_column in range (get_width(original))) and ( random_row in range (get_height(original))):
                row_and_column_are_in_bounds = True
                    
        # Get the color of the randomly-selected pixel.
        
        col = get_color(original, random_column, random_row)
        
        # Use that color to replace the color of the pixel we're visiting.
        
        set_color(scattered, x, y, col)
    
    # Return the scattered image.

    return scattered


def extreme_contrast(image): 
  
    new_image = copy(image) 
    for x, y, (r, g, b) in image: 
        if r <= 127: 
            r = 0            
        else: 
            r = 255
            
        if g <= 127: 
            g = 0            
        else: 
            g = 255
        
        if b <= 127: 
            b = 0            
        else: 
            b = 255
        
        contrast = create_color(r, g, b)
        set_color(new_image, x, y, contrast)
    
    return new_image

def grayscale(image):

    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image


def weighted_grayscale(image):
   
    new_image = copy(image)
    for x, y, (r, g, b) in new_image:
        brightness = r*0.299 + g*0.587 + b*0.114
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image



def sepia_tint(image):
    
    sepia = weighted_grayscale(image)
    for x, y, (r, g, b) in sepia:
        if r<63:
            b = b*0.9
            r = r*1.1
          
        elif r<191:
            b = b*0.85
            r = r*1.15
        
        else:
            b = b*0.93
            r = r*1.08
            
        colour = create_color(r,g,b)
        set_color(sepia, x, y, colour)
 
    return sepia

