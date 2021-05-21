img = Image.open('/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/clinical_records_20180410_170435_70/clinical_records_20180410_170435_70/70/CT/Masks/046.png')
imgr = np.array(img)
ret,thresh2 = cv.threshold(imgr,254,255,cv.THRESH_BINARY)
i = PIL.Image.fromarray(thresh2)
i
df_size = ls_conf['dilation_filter_size']
dilated_slice = morphology.dilation(thresh2, np.ones([3,3]))
i = PIL.Image.fromarray(dilated_slice)
i

eroded_slice = morphology.erosion(dilated_slice, np.ones([3, 3]))

i = PIL.Image.fromarray(eroded_slice)
i

medfilt_slice = (scipy.signal.medfilt(eroded_slice, kernel_size=[5,5])).astype(np.uint8)
i = PIL.Image.fromarray(medfilt_slice)
i

