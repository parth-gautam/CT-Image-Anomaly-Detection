import numpy as np
import sys
from PIL import Image
import os, os.path
import scipy
from skimage import morphology
from skimage import measure
from config import lungs_segmentation as ls_conf
from config.dicom_working_config import dicom_options as d_opt

sys.path.insert(0, "/Users/Parth Gautam/Desktop/CT_Project/tpuctanalysis-segmentation-and-classification-d1c0df68cbfc/dicom_data_working")

from config.dicom_working_config import dicom_options as d_opt
from config.dicom_working_config import radiology_preset_options as rp_opt
from open_dicoms import extract_dicom_slices_from_folder
from dicom_data_working import convert_slices_to_preset
from dicom_data_working import normalize_slices_for_images


#extraction and coversion of preset
folder_path="/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/clinical_records_20180410_170435_70/clinical_records_20180410_170435_70/70/CT/20110902"
dicom_slices=extract_dicom_slices_from_folder(folder_path,0,0)
x=convert_slices_to_preset(dicom_slices,4)
type(dicom_slices)

#Creating lung Masks
from segment_ct_slices import main
folder_path_save = "/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/clinical_records_20180410_170435_70/clinical_records_20180410_170435_70/70/CT/Masks"
folder_path="/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/clinical_records_20180410_170435_70/clinical_records_20180410_170435_70/70/CT/20110902"
main(folder_path,'bone',0,0,folder_path_save)


def extract_Mask_slices_from_folder(folder_path):
    """
    Creates a Mask slices pixel data array in a certain radiology preset
    from a set of Mask-files stored in the folder
    :param folder_path: Path to the directory contained dicom-files
    :param except_from_start: A number of slices to except from the start
    :param except_from_end: A number of slices to except from the end
    :return: An array of Mask slices pixel data in a certain radiology preset
    """
    
    imgs_slices = []
    path = folder_path
    valid_images = ".png"
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs_slices.append(np.array(Image.open(os.path.join(path,f))))
        
    return imgs_slices

import cv2 as cv
#extrct masks in lung mode
lungs_Masks = extract_Mask_slices_from_folder("/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/New folder/334/CT/20140113/files/Masks")
d = PIL.Image.fromarray(lungs_Masks[50])
d
ret,thresh2 = cv.threshold(lungs_Masks[50],0,100,cv.THRESH_BINARY)
d = PIL.Image.fromarray(x[32])
d
#exmpl slices
def process_lyr(lung,body):
    k = []
    for i in range(len(lung)):
        #joining lung masks and body
        u = lung[i]+body[i]
        u[u!=0] = 255
        
        #applying erosion filter
        ef_size = ls_conf['erosion_filter_size']
        eroded_slice = morphology.erosion(u, np.ones([ef_size, ef_size]))
        #applying median filter
        
        medfilt_slice = (scipy.signal.medfilt(eroded_slice, kernel_size=[5,5])).astype(np.uint8)
        k.append(medfilt_slice)
    return k

#getting processed
f = np.asarray(process_lyr(lungs_Masks,x))


#Extracting body masks
def extract_body_masks(fp,folder_path):
    k=0
    for i in range(len(f)):
        #finding contours
        im2,contours,hierarchy = cv2.findContours(f[i], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        f[i].fill(0)    
        c = max(contours, key = cv2.contourArea)
        body_mask = cv2.fillConvexPoly(f[i], c, color = 255)
        body_mask = PIL.Image.fromarray(body_mask)
        ct_image_path = os.path.join(folder_path,
                                     d_opt['filename_pattern'].format(i))
        body_mask.save(ct_image_path)

extract_body_masks(f,"/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/New folder/334/CT/20140113/files/body")


