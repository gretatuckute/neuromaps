# -*- coding: utf-8 -*-
"""
Script to perform transforms. Specify via flags
"""
import os

vwfa = False
tom = False
glasser = True
lang_parcel_to_fsaverage = False
speech_parcel_to_fsaverage = False

from neuromaps import datasets
from neuromaps.transforms import *
import nibabel as nib
from nilearn import plotting
from matplotlib import pyplot as plt
from os.path import join

# Load MNI lang parcel
mni_lang_parcel = nib.load('/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/ROIs_Nov2020/Func_Lang_LHRH_SN220/allParcels_language.nii')

if vwfa:
    # ROI
    roi = nib.load('/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/vwfa/lvwfa.nii')

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

if tom:
    dir = '/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/tom/ToM_thresholded'

    # find all .img files
    rois = [f for f in os.listdir(dir) if f.endswith('.img')]

    # Load and transform
    for roi_name in rois:

        roi_name_no_ext = roi_name.split('.')[0]

        # Transform MNI to MNI
        roi_transformed_linear = mni152_to_mni152(img=join(dir, roi_name), # takes string instead of img, and opens it inside the function
                                target=mni_lang_parcel,
                                method='linear')

        roi_transformed_nearest = mni152_to_mni152(img=join(dir, roi_name),
                                target=mni_lang_parcel,
                                method='nearest')


        # Save
        nib.save(roi_transformed_linear, join(dir, f'{roi_name_no_ext}_MNI152_linear.nii'))
        nib.save(roi_transformed_nearest, join(dir, f'{roi_name_no_ext}_MNI152_nearest.nii'))

        # Plot transformed ROI and lang parcel
        plt.figure()
        plotting.plot_roi(mni_lang_parcel, title='Lang')
        plotting.plot_roi(roi_transformed_linear, title=f'{roi_name} linear')
        plotting.plot_roi(roi_transformed_nearest, title=f'{roi_name} nearest')
        plt.show()


if glasser:
    dir = '/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/glasser/from_original_source/'
    # From the original source: https://figshare.com/articles/dataset/HCP-MMP1_0_projected_on_MNI2009a_GM_volumetric_in_NIfTI_format/3501911

    fname_orig = 'HCPMMP1_on_MNI152_ICBM2009a_nlin.nii.gz'

    # Load and transform
    glasser = nib.load(join(dir, fname_orig))

    roi_transformed_nearest = mni152_to_mni152(img=glasser,
                            target=mni_lang_parcel,
                            method='nearest')

    # Unique values in the transformed ROI
    unique_vals = np.unique(roi_transformed_nearest.get_fdata())

    # Plot
    plt.figure()
    plotting.plot_roi(roi_transformed_nearest, title='Glasser nearest')
    plt.show()

    # Save
    nib.save(roi_transformed_nearest, join(dir, f'HCPMMP1_on_MNI152_ICBM2009a_nlin_MNI152_nearest.nii.gz'))











if lang_parcel_to_fsaverage:
    """
    Transform our MNI lang parcel in the volume to fsaverage
    """

    # '/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/ROIs_Nov2020/Func_Lang_LHRH_SN220/allParcels_language.nii'

    mni_lang_parcel_to_fsaverage_nearest = mni152_to_fsaverage(img=mni_lang_parcel,
                                                       method='nearest',
                                                       fsavg_density='164k')
    # Nearest is recommended for parcels

    # Save it as a gifti in the original dir # 'lh.parcels_language_fsaverage.gii'
    path = '/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/ROIs_Nov2020/Func_Lang_LHRH_SN220/'

    mni_lang_parcel_to_fsaverage_nearest[0].to_filename(os.path.join(path, 'lh.parcels_language_fsaverage.gii'))
    mni_lang_parcel_to_fsaverage_nearest[1].to_filename(os.path.join(path, 'rh.parcels_language_fsaverage.gii'))

if speech_parcel_to_fsaverage:
    """
    Transform our MNI speech parcel in the volume to fsaverage
    (from /om5/group/evlab/u/heesok/parcels/SpeechLoc/GSS_speechLoc_NT_n17_fROIs.nii)
    """

    mni_speech_parcel = nib.load('/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/ROIs_Nov2020/Func_Speech_NQ17/GSS_speechLoc_NT_n17_fROIs.nii')

    mni_speech_parcel_to_fsaverage_nearest = mni152_to_fsaverage(img=mni_speech_parcel,
                                                         method='nearest',
                                                         fsavg_density='164k')

    # Save it as a gifti in the original dir # 'lh.parcels_speech_fsaverage.gii'
    path = '/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/ROIs_Nov2020/Func_Speech_NQ17/'

    mni_speech_parcel_to_fsaverage_nearest[0].to_filename(os.path.join(path, 'lh.parcels_speech_fsaverage.gii'))
    mni_speech_parcel_to_fsaverage_nearest[1].to_filename(os.path.join(path, 'rh.parcels_speech_fsaverage.gii'))