import numpy as np
import PIL
import os, os.path
from config.dicom_working_config import dicom_options as d_opt
from config.dicom_working_config import radiology_preset_options as rp_opt
from dicom_data_working.open_dicoms import extract_dicom_slices_from_folder
from dicom_data_working import convert_slices_to_preset
from dicom_data_working import normalize_slices_for_images


#extraction and coversion of preset
folder_path="/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/New folder/334/CT/20140113"
dicom_slices=extract_dicom_slices_from_folder(folder_path,0,0)
y=convert_slices_to_preset(dicom_slices,2)
type(x)




lungs_Masks = extract_Mask_slices_from_folder("/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/New folder/334/CT/20140113/files/Masks")


#extracting body
folder_body_mask = "/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/New folder/334/CT/20140113/files/body"
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
        
    return np.array(imgs_slices)

body_mask = extract_Mask_slices_from_folder(folder_body_mask)

len(x)
def body_in_mode(body,body_mask,folder_to_save):
    for i in range(len(body)):
        body_mask[i][body_mask[i]!=0] = 1
        b = np.multiply(body[i],body_mask[i])
        b = PIL.Image.fromarray(b)
        ct_image_path = os.path.join(folder_to_save,
                                     d_opt['filename_pattern'].format(i))
        b.save(ct_image_path)

folder_to_save = "/Users/Parth Gautam/Desktop/Python Scripts/Tomsk/New folder/334/CT/20140113/files/Body_final"
body_in_mode(y,body_mask,folder_to_save)
        