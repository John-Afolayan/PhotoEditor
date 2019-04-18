from Cimpl import *
import random

def scatter(image):
    
    # Create an image that is a copy of the original.
    
    new_image = copy(image)
    
    # Visit all the pixels in new_image.
    
    for x, y, (r, g, b) in new_image:
        
        # Generate the row and column coordinates of a random pixel
        # in the original image. Repeat this step if either coordinate
        # is out of bounds.
        
        row_and_column_are_in_bounds = True
        while not row_and_column_are_in_bounds:
            
            # Generate two random numbers between -10 and 10, inclusive.
            
            rand1 = random.randint(-10, 10)
            rand2 = random.randint(-10, 10) 
            
            # Calculate the column and row coordinates of a
            # randomly-selected pixel in image.

            random_column = x + rand1
            random_row = y + rand2
            
            # Determine if the random coordinates are in bounds.

            if (x,y >= 0):
                row_and_column_are_in_bounds = True
                    
        # Get the color of the randomly-selected pixel.
        
        col = get_color(image, (x + rand1), (y + rand2))
        
        # Use that color to replace the color of the pixel we're visiting.
        
        set_color(new_image, x, y, col)
    
    return new_image
    # Return the scattered image.
    
image = load_image(choose_file())
new_image = scatter(image)
show(new_image)