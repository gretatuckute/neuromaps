# -*- coding: utf-8 -*-
"""
Try transforms
"""



from neuromaps import datasets
from neuromaps.transforms import *
import nibabel as nib
from nilearn import plotting
from matplotlib import pyplot as plt

# Load MNI lang parcel
mni_lang_parcel = nib.load('/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/ROIs_Nov2020/Func_Lang_LHRH_SN220/allParcels_language.nii')

# ROI
roi = nib.load('/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/vWFA/lvwfa.nii')

# Transform MNI to MNI
roi_transformed_linear = mni152_to_mni152(img=roi,
                        target=mni_lang_parcel,
                        method='linear')

roi_transformed_nearest = mni152_to_mni152(img=roi,
                        target=mni_lang_parcel,
                        method='nearest')


# Save
nib.save(roi_transformed_linear, '/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/vWFA/lvwfa_MNI152_linear.nii')
nib.save(roi_transformed_nearest, '/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/vWFA/lvwfa_MNI152_nearest.nii')

# Plot transformed ROI and lang parcel
plt.figure()
plotting.plot_roi(mni_lang_parcel, title='Lang')
plotting.plot_roi(roi_transformed_linear, title='vWFA linear')
plotting.plot_roi(roi_transformed_nearest, title='vWFA nearest')
plt.show()



