# libraries
import cv2 as cv
import numpy as np
import glob
import random
import os


# augment images
class AugmentImages:

    # constructor to initialize range for rotation angle, brightness, and no of images to augment

    def __init__(self, rotation_range = 40, brightness_range = 50, no_of_Images = 100):

        self.rotation_range = rotation_range
        self.brightness_range = brightness_range
        self.no_of_Images = no_of_Images


    # rotate images
    def rotate_Image(self, img , rotate = 1):

        if rotate:
            h, w = img.shape[:2]
            angle = random.randint(0,self.rotation_range)
            rot_mat = cv.getRotationMatrix2D((w//2,h//2), angle,0.7)
            rotated_img = cv.warpAffine(img,rot_mat,(w,h))
            return rotated_img
        else:
            return img

    # increase or decrease brightness
    def change_Brightness(self, img , bright = 1):

        if bright:

            h, w = img.shape[:2]
            value = random.randint(0, self.brightness_range)
            brightness = np.ones(img.shape, dtype="uint8") * value

            choice = random.choice([0, 1])

            if choice :

                bright_img = cv.add(img, brightness)
                return bright_img

            else:

                bright_img = cv.subtract(img, brightness)
                return bright_img

        else:
            return img


    # flip images
    def flip_Image(self, img , flip):

        if flip:

            value = random.choice([-1,0,1])
            flipped_img = cv.flip(img,value)
            return flipped_img

        else:

            return img


    # Shape images
    def shapen_Image(self, img, sharp = 1):

        if sharp:
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            sharped_img = cv.filter2D(img, -1, kernel)
            return sharped_img

        else:
            return img

    #Zoom in or Zoom out images
    def zoom_Image(self, img , zoom =1):

        if zoom :

            choice = random.choice([0,1])

            if choice == 0:

                downScale = random.uniform(0.5, 1.0)
                scaledDown_Img = cv.resize(img, None, fx=downScale, fy=downScale, interpolation= cv.INTER_LINEAR)
                return scaledDown_Img
            else:

                upScale = random.uniform(0.0, 5.0)
                scaledUp_Img = cv.resize(img, None, fx=upScale * 3, fy=upScale * 3, interpolation=cv.INTER_LINEAR)
                return scaledUp_Img

        else:

            return img


    # augment images
    def augment_Image(self, img_path):

        # choose operations for image augmentation
        rotate =  random.choice([0,1])
        bright = random.choice([0,1])
        flip = random.choice([0,1])
        sharp = random.choice([0,1])
        zoom = random.choice([0,1])

        img = cv.imread(img_path)

        img = self.rotate_Image(img, rotate)
        img = self.change_Brightness(img, bright)
        img = self.flip_Image(img, flip)
        img = self.shapen_Image(img, sharp)
        img = self.zoom_Image(img, zoom)

        return img


if __name__ == "__main__":

    #Path to Images to Augment
    image_folder = "pics"

    # create directory to save augmented images
    if not os.path.exists("AugmentedImages"):
        os.mkdir("AugmentedImages")

    # track no of images augmented and used to name them
    image_num = 0

    # initialize contstructor of class
    aug_img = AugmentImages(rotation_range=40, brightness_range= 50, no_of_Images= 20)


    #loop to augemnt images
    while(image_num < aug_img.no_of_Images):

        print(image_num)

        for img_path in glob.glob(image_folder +"/*.jpg"):

            img = aug_img.augment_Image(img_path)

            cv.imwrite("AugmentedImages/" + str(image_num)+".jpg", img)
            image_num = image_num +1









