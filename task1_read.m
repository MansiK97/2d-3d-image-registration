info = dicominfo('IM15UD.dcm');
Y = dicomread(info);
figure
imshow(Y,[]);