# -*- coding: utf-8 -*-
"""
Convert our standard MNI 152 to fsaverage surface. This is a testing script....
"""
test = True
from neuromaps import datasets
from neuromaps.transforms import *
import nibabel as nib
from nilearn import plotting
from matplotlib import pyplot as plt
from os.path import join

# Load MNI lang parcel
mni_lang_parcel = nib.load('/Users/gt/Documents/GitHub/fMRI_prep/data/ROIs/ROIs_Nov2020/Func_Lang_LHRH_SN220/allParcels_language.nii')

if test:
    # Transform mni_lang_parcel to fsaverage
    mni_lang_parcel_to_fsaverage = mni152_to_fsaverage(img=mni_lang_parcel,
                                                       method='linear',
                                                       fsavg_density='164k')

    mni_lang_parcel_to_fsaverage_nearest = mni152_to_fsaverage(img=mni_lang_parcel,
                                                       method='nearest',
                                                       fsavg_density='164k')

    # Save it as a gifti
    mni_lang_parcel_to_fsaverage[0].to_filename('lh.mni_lang_parcel_to_fsaverage_164k.gii')
    mni_lang_parcel_to_fsaverage[1].to_filename('rh.mni_lang_parcel_to_fsaverage_164k.gii')

    # save as gifti
    mni_lang_parcel_to_fsaverage_nearest[0].to_filename('lh.mni_lang_parcel_to_fsaverage_nearest_164k.nearest.gii')


    # mni_lang_parcel_to_fsaverage[0].darrays[0]

    # Save in current dir
    # nib.save(mni_lang_parcel_to_fsaverage, 'mni_lang_parcel_to_fsaverage_164k.nii')

    # Plot transformed ROI and lang parcel
    plt.figure()
    plotting.plot_roi(mni_lang_parcel, title='Lang')
    # mni_lang_parcel_to_fsaverage is a tuple with a gifti image in each element
    plotting.plot_roi(mni_lang_parcel_to_fsaverage[0], title='Lang to fsaverage')
    plt.show()
    plt.show()

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

if __name__ == '__main__':
    main()