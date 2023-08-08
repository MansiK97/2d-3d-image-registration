import cv2 as cv
import pydicom as dicom
import matplotlib.pyplot as plt
from skimage import exposure

#IM15UD
ds = dicom.dcmread('IM15UD.dcm',0)

img1 = ds.pixel_array

plt.imshow(img1,'gray')
plt.show()
cv.imwrite('dcm.png', img1)
img1.shape
#%%
sd.PixelData = img1.tobytes()
#dicom.write_file('out.dcm',img1)
dicom.dcmwrite('out.dcm',sd,write_like_original=True)
#%%
img=cv.imread('dcm.png',0)
plt.imshow(img)
#%%
print(img1.dtype)
#%%
src = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
plt.imshow(src,'gray')
#%%
dst = cv.equalizeHist(img1)
plt.imshow(src)
plt.imshow(dst)
cv.waitKey()
#%%
img1_equalise_adapthist=exposure.equalize_adapthist(img1)
plt.imshow(img1_equalise_adapthist,'gray')
plt.show()
#%%
img1_equalize_hist=exposure.equalize_hist(img1)
plt.imshow(img1_equalize_hist,'gray')
plt.show()

#%%

#IM19UD
ds = dicom.dcmread('IM19UD.dcm')
img2 = ds.pixel_array
plt.imshow(img2,'gray')
plt.show()

#%%
img2_equalise_adapthist=exposure.equalize_adapthist(img2)
plt.imshow(img2_equalise_adapthist,'gray')
plt.show()
#%%
img2_equalize_hist=exposure.equalize_hist(img2)
plt.imshow(img2_equalize_hist,'gray')

plt.show()

#%%

#IMG21UD
ds = dicom.dcmread('IMG21UD.dcm')
img3 = ds.pixel_array
plt.imshow(img3,'gray')
plt.show()

#%%
img3_equalise_adapthist=exposure.equalize_adapthist(img3)
plt.imshow(img3_equalise_adapthist,'gray')
plt.show()
#%%
img3_equalize_hist=exposure.equalize_hist(img3)
plt.imshow(img3_equalize_hist,'gray')
plt.show()

#%%

#IM25UD
ds = dicom.dcmread('IM25UD.dcm')
img4 = ds.pixel_array
plt.imshow(img4,'gray')
plt.show()

#%%
img4_equalise_adapthist=exposure.equalize_adapthist(img4)
plt.imshow(img4_equalise_adapthist,'gray')
plt.show()
#%%
img4_equalize_hist=exposure.equalize_hist(img4)
plt.imshow(img4_equalize_hist,'gray')
plt.show()

#%%

#IM31UD
ds = dicom.dcmread('IM31UD.dcm')
img5 = ds.pixel_array
plt.imshow(img5,'gray')
plt.show()

#%%
img5_equalise_adapthist=exposure.equalize_adapthist(img5)
plt.imshow(img5_equalise_adapthist,'gray')
plt.show()
#%%
img5_equalize_hist=exposure.equalize_hist(img5)
plt.imshow(img5_equalize_hist,'gray')
plt.show()

#%%

#IM39UD
ds = dicom.dcmread('IM39UD.dcm')
img6 = ds.pixel_array
plt.imshow(img6,'gray')
plt.show()

#%%
img6_equalise_adapthist=exposure.equalize_adapthist(img6)
plt.imshow(img6_equalise_adapthist,'gray')
plt.show()
#%%
img6_equalize_hist=exposure.equalize_hist(img6)
plt.imshow(img6_equalize_hist,'gray')
plt.show()


