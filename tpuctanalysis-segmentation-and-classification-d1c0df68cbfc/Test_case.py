img = Image.open('/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/New folder/334/CT/20140113/files/Body_final/026.png')
img
imgr = np.array(img)
ret,thresh2 = cv.threshold(imgr,0.00000000000001,255,cv.THRESH_BINARY_INV)
body_m = Image.open('/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/New folder/334/CT/20140113/files/body/026.png')
imgrm = np.array(body_m)
imgrm[imgrm!=0]=1
mult = np.multiply(thresh2,imgrm)




img[img!=0]=1
i = PIL.Image.fromarray(mult)
i
df_size = ls_conf['dilation_filter_size']
dilated_slice = morphology.dilation(mult, np.ones([5,5]))
i = PIL.Image.fromarray(dilated_slice)
i

eroded_slice = morphology.erosion(dilated_slice, np.ones([7, 7]))

i = PIL.Image.fromarray(eroded_slice)
i

medfilt_slice = (scipy.signal.medfilt(eroded_slice, kernel_size=[7,7])).astype(np.uint8)
i = PIL.Image.fromarray(medfilt_slice)
i






