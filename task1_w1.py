import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import pydicom as dicom
import imutils
import SimpleITK as sitk
%matplotlib inline

#IM15UD

image_path='IM15UD.dcm'
ds = dicom.dcmread(image_path)
img1 = ds.pixel_array
plt.imshow(img1,'gray')


#%%

blur1 = cv.GaussianBlur(img1,(21,21),0)

fig, ((ax1),(ax2))=plt.subplots(1,2,figsize=(9,12),constrained_layout=True)
ax1.imshow(img1,'gray')
ax2.imshow(blur1,'gray')
#Saving image as dicom image
img15=sitk.GetImageFromArray(blur1)
sitk.WriteImage(img15,"img15_blur.dcm")
#%%
#Rotation
Rotated_image1 = imutils.rotate(img1, angle=45)

#cv.imshow(Rotated_image)
plt.imshow(Rotated_image1),plt.title('Rotated')

Rotated_image2 = imutils.rotate(img1, angle=60)
plt.imshow(Rotated_image2,'gray'),plt.title('Rotated')

Rotated_image3 = imutils.rotate(blur1, angle=60)
plt.imshow(Rotated_image3,'gray'),plt.title('Rotated')

fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=(9,12),constrained_layout=True)
ax1.imshow(img1,'gray')
ax2.imshow(Rotated_image1,'gray')
ax3.imshow(Rotated_image2,'gray')
ax4.imshow(Rotated_image3,'gray')

#%%
#IM19UD

image_path='IM19UD.dcm'
ds = dicom.dcmread(image_path)

img2 = ds.pixel_array
blur2 = cv.GaussianBlur(img2,(5,5),0)

ig, ((ax1),(ax2))=plt.subplots(1,2,figsize=(9,12),constrained_layout=True)
ax1.imshow(img2,'gray')
ax2.imshow(blur2,'gray')
#%%
#Rotation
Rotated_image1 = imutils.rotate(img2, angle=45)

#cv.imshow(Rotated_image)
plt.imshow(Rotated_image1),plt.title('Rotated')

Rotated_image2 = imutils.rotate(img2, angle=60)
plt.imshow(Rotated_image2,'gray'),plt.title('Rotated)
                                            
                                    
Rotated_image3 = imutils.rotate(blur2, angle=60)
plt.imshow(Rotated_image3,'gray'),plt.title('Rotated by 60 degrees')

#%%
fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=(9,12),constrained_layout=True)
ax1.imshow(img2,'gray')
ax2.imshow(Rotated_image1,'gray')
ax3.imshow(Rotated_image2,'gray')
ax4.imshow(Rotated_image3,'gray')

#%%
#IM21UD

image_path='IM21UD.dcm'
ds = dicom.dcmread(image_path)

img3 = ds.pixel_array
blur3 = cv.GaussianBlur(img3,(5,5),0)

ig, ((ax1),(ax2))=plt.subplots(1,2,figsize=(9,12),constrained_layout=True)
ax1.imshow(img3,'gray')
ax2.imshow(blur3,'gray')
#%%
#Rotation
Rotated_image1 = imutils.rotate(img3, angle=45)

#cv.imshow(Rotated_image)
plt.imshow(Rotated_image1),plt.title('Rotated')

Rotated_image2 = imutils.rotate(img3, angle=60)
plt.imshow(Rotated_image2,'gray'),plt.title('Rotated')

Rotated_image3 = imutils.rotate(blur3, angle=60)
plt.imshow(Rotated_image3,'gray'),plt.title('Rotated')

fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=(9,12),constrained_layout=True)
ax1.imshow(img3,'gray')
ax2.imshow(Rotated_image1,'gray')
ax3.imshow(Rotated_image2,'gray')
ax4.imshow(Rotated_image3,'gray')

 #%%
 #IM25UD

 image_path='IM25UD.dcm'
 ds = dicom.dcmread(image_path)

 img4 = ds.pixel_array
 blur4 = cv.GaussianBlur(img4,(5,5),0)

 ig, ((ax1),(ax2))=plt.subplots(1,2,figsize=(9,12),constrained_layout=True)
 ax1.imshow(img4,'gray')
 ax2.imshow(blur4,'gray')
 #%%
 #Rotation
 Rotated_image1 = imutils.rotate(img4, angle=45)

 #cv.imshow(Rotated_image)
 plt.imshow(Rotated_image1),plt.title('Rotated')

 Rotated_image2 = imutils.rotate(img4, angle=60)
 plt.imshow(Rotated_image2,'gray'),plt.title('Rotated')

 Rotated_image3 = imutils.rotate(blur4, angle=60)
 plt.imshow(Rotated_image3,'gray'),plt.title('Rotated')

 fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=(9,12),constrained_layout=True)
 ax1.imshow(img4,'gray')
 ax2.imshow(Rotated_image1,'gray')
 ax3.imshow(Rotated_image2,'gray')
 ax4.imshow(Rotated_image3,'gray')
 
 #%%
 #IM31UD

 image_path='IM31UD.dcm'
 ds = dicom.dcmread(image_path)

 img5 = ds.pixel_array
 blur5 = cv.GaussianBlur(img5,(1,11),0)
 plt.imshow(blur5,'gray')
 #%%

 ig, ((ax1),(ax2))=plt.subplots(1,2,figsize=(9,12),constrained_layout=True)
 ax1.imshow(img5,'gray')
 ax2.imshow(blur5,'gray')
 #%%
 #Rotation
 Rotated_image1 = imutils.rotate(img5, angle=45)

 #cv.imshow(Rotated_image)
 plt.imshow(Rotated_image1),plt.title('Rotated')

 Rotated_image2 = imutils.rotate(img5, angle=60)
 plt.imshow(Rotated_image2,'gray'),plt.title('Rotated')

 Rotated_image3 = imutils.rotate(blur5, angle=60)
 plt.imshow(Rotated_image3,'gray'),plt.title('Rotated')

 fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=(9,12),constrained_layout=True)
 ax1.imshow(img5,'gray')
 ax2.imshow(Rotated_image1,'gray')
 ax3.imshow(Rotated_image2,'gray')
 ax4.imshow(Rotated_image3,'gray')
 
 #%%
 #IM39UD

 image_path='IM39UD.dcm'
 ds = dicom.dcmread(image_path)

 img6 = ds.pixel_array
 blur6 = cv.GaussianBlur(img6,(5,5),0)

 ig, ((ax1),(ax2))=plt.subplots(1,2,figsize=(9,12),constrained_layout=True)
 ax1.imshow(img6,'gray')
 ax2.imshow(blur6,'gray')
 #%%
 #Rotation
 Rotated_image1 = imutils.rotate(img6, angle=45)

 #cv.imshow(Rotated_image)
 plt.imshow(Rotated_image1),plt.title('Rotated')

 Rotated_image2 = imutils.rotate(img6, angle=60)
 plt.imshow(Rotated_image2,'gray'),plt.title('Rotated')

 Rotated_image3 = imutils.rotate(blur6, angle=60)
 plt.imshow(Rotated_image3,'gray'),plt.title('Rotated')

 fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=(9,12),constrained_layout=True)
 ax1.imshow(img6,'gray')
 ax2.imshow(Rotated_image1,'gray')
 ax3.imshow(Rotated_image2,'gray')
 ax4.imshow(Rotated_image3,'gray')
 
 