"""
Script contains code for an image manipulation program that retrieves user input to perform requested
commands. Its functionality includes, saving JPEG images to PNG, image rotation, apply contrast 
(black and white shades) to an image. etc

Images that that will undergo some form of manipulation cannot just be showed using the "show() method.
This is because, the user has to determine which image to apply effects to.
Therefore, the program displays image(s) chosen by user. All images should be stored as variable and
made know to the user. The image should be accessed based on the variable the user inputs - input 
should be used to display image.
"""
#Importing the image module from the the pillow library
# and the os module
from PIL import Image, ImageFilter
import os

#OPENING IMAGES - using path.
#The normal way of accessing images via their url will not work in this code.
#This is because the images are in a folder where the main file (CODE.PY) does not exist.
#Even if the file is dragged and dropped into the folder it does not work.
#To make it work, you must take all the images out of the image_JPEG folder, with the main code inside
#a folder. Then will it work. However, we need to be organised and not get our work dirty.
#Therefore second solution is to access the image through its path. This is the method used in this script.

#MULTI-STRUCTURAL ARRAY
#To prevent the values of display from popping up like a slide show the name of image will be saved in
#the display key without the "show()" method. Image will then be accessed as seen in the example below:
#if store == "one":
#   gallery[display][0].show()  - JAVASCRIPT STYLE.


#gallery["display"]

#CODE SIMPLIFIED AFTER PLAYING AROUND WITH COMPLEXITY - AND IT WORKS.

#DISPLAY
effects = f"""
EFFECTS ON SCRIPT
1) Rotate  2) png              5) Size
3) Blur   4) Black and White   6) Crop
"""
print(effects)
print("Images are labeled 0 to 9.\nInput any of those number to access an image.\nOpen specific folders containing the effects, to view them.")

#PROLOGUE OF CODE
num_effs = int(input("How many effects would you like to apply? "))
#Creating an empty list of chosen effects.
chosen_eff = []
#Using for loops and other method to ask for effects a specific number of times.
for i in range(num_effs):
    #Retrieve names of effects and store as list.
    effs_name = input("List the effects: ").lower()
    data = effs_name
#Storing effects in empty list.
#There should also be FUNCTIONS to access chosen effects.
    chosen_eff.append(data)
print(chosen_eff)


#FUNCTION THAT ROTATES.
#There should be functions for each effect - making code clean.
#Image has been displayed. Create functions of each effect and apply LIST of effects to image chosen
#TRY ADDING CODE THAT ASKS USER IF THEY WANT TO ROTATE AND SAVE AN PNG OR JPEG
def rote():
    #Ask user the file type they would like to save it as after the effects have been applied.
    degree = int(input("Rotation degree: "))
    #Line that handles error when degree is not a number.
    #Sets degree to 90, by default. 
    #Create variable called default.
    type = input("Image format (png/jpg): ").lower()
    if type == "png":
        img_eff.rotate(degree).save(f"Rotation/{select}.png")
        img_eff.show()
    elif type == "jpg":
        img_eff.rotate(degree).save(f"Rotation/{select}.jpg")
        img_eff.show()
    else:
        print("Unsupported file format.")

#FUNCTION THAT SAVES AS PNG.
def format():
    img_eff.save(f"Saved_PNG/{select}.png")
    img_eff.show()

#FUNCTION FOR VALUE.
def blk_wte():
    img_eff.convert(mode="L").save(f"Black & White/{select}.jpg")
    img_eff.show()
    
#FUNCTION FOR BLUR.
def opacity():
    #Amount of blur.
    bl_amt = int(input("Blur amount: "))
    img_eff.filter(ImageFilter.GaussianBlur(bl_amt)).save(f"Blur/{select}.png")
    img_eff.show()
    #MUST WORK ON UNTIL IT WORKS.
    #Works now! I just had to make use syntax was right. 
    #Thus, from PIL import "Image, ImageFilter", instead of "from PIL import Image,ImageFilter"

def thumbnail():
    #Variable of opened image selected by user.
    img_eff 
    print(img_eff.size)
    #Inputs for dimensions.
    d_one = int(input("Enter first dimension: "))
    d_two = int(input("Enter second dimension: "))
    #siz = (d_one, d_two)
    new_siz = img_eff.resize((d_one, d_two))
    new_siz.save(f"Size/{select}.png")
    new_siz.show()

def crop():
    print("By default the crop effect has two methods.\nSelect one.")
    #Cropping out pixels from the bottom of image,
    #based on user's option.
    #FUNCTION FOR CROPPING PIXELS OFF THE BOTTOM.
    def crp_bottom():
        pxl = int(input("Enter amount of pixel to crop: "))
        x1 = 0
        y1 = 0
        x2 = img_eff.width
        y2 = img_eff.height - pxl
        cropped = img_eff.crop((x1, y1, x2, y2))
        cropped.show()
        cropped.save(f"CROP/bottom/{select}.png")

    #FUNCTION THAT CROPS EVERYTHING OUTSIDE OF THE PICTURE AT THE CENTER.
    #NOT NECESSARILY THE CENTER, BUT BASED ON USER'S INPUT
    def crp_out():
        print("Recommendation:\n use the number 2\n or input location desired.\n Using 2 makes the focus be on the center.")
        #ASK USER IF THEY WOULD LIKE TO GO WITH DEFAULT SETTINGS OR USE THEIR OWN, THEN GRANT USER REQUEST.
        dault = input("Would you like to apply the default settings?(yes/no) ").lower()
        if dault == "yes":
            xcenter = img_eff.width/2
            ycenter = img_eff.height/2
        elif dault == "no":
            #ASK USER OF X AND Y COORDINATES OF SECTION THEY WOULD LIKE TO FOCUS ON.
            cor_x = int(input("X-coordinate: "))
            cor_y = int(input("Y-coordinate: "))
            xcenter = img_eff.width/cor_x
            ycenter = img_eff.height/cor_y
        
        
        x1 = xcenter - 100
        y1 = ycenter - 100
        x2 = xcenter + 100
        y2 = ycenter + 100
        cropped = img_eff.crop((x1, y1, x2, y2))
        cropped.show()
        #IF STATEMENT TO SAVE TO THE REQUIRED FOLDER, BASED ON USER'S OPTION ABOVE.
        if dault == "yes":
            cropped.save(f"CROP/outside_default/{select}.png")
        elif dault == "no":
            cropped.save(f"CROP/outside_user/{select}.png")

    #ASKS USER WHICH OF THE CROP METHOD THE WOULD LIKE TO USE.
    crop_option = input("Would you like to crop image from bottom or crop everything\n outside a specific point chosen?(crop out/ crop bottom) ")
    if crop_option.lower() == "crop out":
        crp_out()
    elif crop_option.lower() == "crop bottom":
        crp_bottom()

#USER-IMAGE-ACCESS
#Retrieves data from user regarding image chosen.
#select = input("Which image would you like to access? ").lower()
select = int(input("Which image would you like to access? "))
#Image.open(f"Images_JPEG/{select}.jpg").show()
img_eff = Image.open(f"Images_JPEG/{select}.jpg")

#USE IF STATEMENT TO APPLY THE EFFECTS IN THE LIST.
if "rotate" in chosen_eff:
    rote()
if "png" in chosen_eff:
    format()
if "black and white" in chosen_eff:
    blk_wte()
if "blur" in chosen_eff:
    opacity()
if "size" in chosen_eff:
    thumbnail()
if "crop" in chosen_eff:
    crop()

    
"""
CONCLUSION:
Everything works as expected. The focus should be placed on creating folders using the os module in the near future.
"""

#def blur():
    #gallery["display"][0].filter(ImageFilter.GaussianBlur()).save("Images_JPEG/xiamen.jpg")
    #pass




 
"""
Applying effects in the list to chosen image.
example list = [rotate, blur]
if list[0] == True:
    #Function rotate.
    rotate()
"""