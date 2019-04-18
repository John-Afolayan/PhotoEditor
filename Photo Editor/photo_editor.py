import sys  # get_image calls exit
from Cimpl import *
from filters import *
import random


def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img


if __name__ == "__main__":
    
        
    done = False
    while not done:
        answer = input("L)oad Image" + "\nB)lur" + "   E)dge detect" + "   P)osterize" + "   S)catter" + "   T)int sepia" + 
                       "\nW)eighted grayscale " + " X)treme contrast" + "\nQ)uit\n \n: ")
        
        
        try:
            
            if answer == 'L':
                img = get_image()
                done = False            
                            
            elif answer == "B":
                img = blur(img)
                show(img)
                
            elif answer == "E":
                value = int(input("Threshold? (0-256)"))
                img = detect_edges_better(img, value)
                show(img)
                
            elif answer == "P":
                img = posterize(img)
                show(img)
                
            elif answer == "S":
                img = scatter(img)
                show(img)
            
            elif answer == "T":
                img = sepia_tint(img)
                show(img)
                
            elif answer == "W":
                img = weighted_grayscale(img)
                show(img)
                
            elif answer == "X":
                img = extreme_contrast(img)
                show(img)
                            
            elif answer == "Q":
                print("\nTerminating Program\n")
                done = True
            
            else:  # The user typed a command other than Q or T or any of the above options
                print("No such command")
                
        except NameError:
            print('No image loaded')