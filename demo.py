import faceSwap
import os
import cv2

# image1 = input("Enter the first image name: ")
# image2 = input("Enter the second image name: ")

image1 = "yony.jpg"
image2 = "kalise.jpg"

path = "images/original_images/"

image1path = os.path.join(path, image1)
image2path = os.path.join(path, image2)

img1 = cv2.imread(image1path)
img2 = cv2.imread(image2path)

faceSwap = faceSwap.FaceSwap()
faceSwap.faceSwap(img1, img2, mode="choose_largest_face",
                  showImages=True, saveSwappedImage=False)
