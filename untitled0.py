import numpy as np
import cv2
import pydicom as dicom
from matplotlib import pyplot as plt
img15=dicom.dcmread('IM15UD.dcm').pixel_array
plt.imshow(img15,cmap='gray')
plt.show()
#%%
#normalisation
#img15=cv2.equalizeHist(IMG15)

norm_img1 = cv2.normalize(img15, None, alpha=250, beta=100, norm_type=cv2.NORM_MINMAX)
norm_img2 = cv2.normalize(img15, None, alpha=0, beta=0, norm_type=cv2.NORM_MINMAX)
#cv2.imshow('original',img15)
norm_img1 = (255*norm_img1).astype(np.uint8)
#norm_img2 = np.clip(norm_img2, 0, 1)
norm_img2 = (255*norm_img2).astype(np.uint8)
dst = cv.equalizeHist(norm_img1)
plt.imshow(norm_img1,'gray')
plt.imshow(dst,'gray')

plt.imshow(norm_img1,cmap='gray')
plt.show()
#%%
plt.imshow(norm_img2,cmap='gray')
plt.show()
#%%
#Morphological
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15))
# Top Hat Transform
topHat = cv2.morphologyEx(img15, cv2.MORPH_TOPHAT, kernel)
# Black Hat Transform
blackHat = cv2.morphologyEx(img15, cv2.MORPH_BLACKHAT, kernel)
res = img15 + topHat - blackHat
plt.imshow(res,cmap='gray')
plt.show()

#%%
gray = np.array(img15, dtype=np.uint8)
I#MG15 = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
plt.show()
#%%
def BrightnessContrast(brightness=0):
    
    # getTrackbarPos returns the current position of the specified trackbar.
    brightness = 100
     
    contrast = 100
 
    effect = controller(img,brightness,contrast)
   
    # The function imshow displays an image in the specified window
    cv2.imshow('Effect', effect)
    #plt.imshow(effect)
 
def controller(img, brightness=255,contrast=127):
   
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
 
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
 
    if brightness != 0:
 
        if brightness > 0:
 
            shadow = brightness
 
            max = 255
 
        else:
 
            shadow = 0
            max = 255 + brightness
 
        al_pha = (max - shadow) / 255
        ga_mma = shadow
 
        # The function addWeighted calculates the weighted sum of two arrays
        cal = cv2.addWeighted(img, al_pha, img, 0, ga_mma)
 
    else:
        cal = img
 
    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)
 
        # The function addWeighted calculates the weighted sum of two arrays
        cal = cv2.addWeighted(cal, Alpha, cal, 0, Gamma)
 
    # putText renders the specified text string in the image.
    cv2.putText(cal, 'B:{},C:{}'.format(brightness,contrast), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return cal
 
if __name__ == '__main__':
    # The function imread loads an image from the specified file and returns it.
    original=dicom.dcmread('IM15UD.dcm').pixel_array

    # Making another copy of an image.
    img = original.copy()
 
    # The function namedWindow creates a window that can be used as a placeholder for images.
    cv2.namedWindow('Original Image 15')
 
    # The function imshow displays an image in the specified window.
    cv2.imshow('Original Image 15', original)
    #plt.imshow(original)           
 
    # createTrackbar(trackbarName,windowName, value, count, onChange)
    # Brightness range -255 to 255
    BrighgtnessContrast
     
    # Contrast range -127 to 127
    #cv2.createTrackbar('Contrast', 'Original Image 15',127, 2 * 127,BrightnessContrast) 
 
     
    #BrightnessContrast(0)
    #%%
    #img15_equalizeHist_cv = cv2.equalizeHist(img15)
    alpha = 3 # Contrast control (1.0-3.0)
    beta = 100 # Brightness control (0-100)
    adjusted = cv2.convertScaleAbs(img15, alpha=alpha, beta=beta)
    
    plt.imshow('original', img15)
    plt.imshow('adjusted', adjusted)
    #%%
    
   grayImage = cv2.cvtColor(img15, cv2.COLOR_BGR2GRAY)
   (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
   
