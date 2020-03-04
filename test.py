'''
Author: Javier Villegas Bravo
UIUC Department of Atmospheric Science


docs can be found here for h5py
http://docs.h5py.org/en/stable/quick.html
and here for the data
https://wiki.illinois.edu/wiki/display/~kindrtnk/Cloud+Detection+in+MODIS+Satellite+Images
HDFView can be downloaded here
https://www.hdfgroup.org/downloads/hdfview/
'''

import h5py

#define file path
home = '/Users/vllgsbr2/Desktop/MODIS_ML_data_sample/'
file_path = home + 'MODIS_MLData_Shape_64x64_2003019.1430_.hdf'

#grab h5py file object
hf_file = h5py.File(file_path, 'r')

#list the main groups; image number in this case
hf_keys = list(hf_file.keys())

#access all data within images; save into an array if you like
#automatically extracted as numpy arrays
for image_num in hf_keys:
    Classification_Accuracy = hf_file[image_num + '/ClassificationAccuracy'][()]
    Feature_Labels          = hf_file[image_num + '/FeatureLabels'][()]
    Image_Classification    = hf_file[image_num + '/ImageClassification'][()]
    Image_Features          = hf_file[image_num + '/ImageFeatures'][()]

#print(type(Image_Features[0,0,0]))
#print(Feature_Labels)

#get shape of data
Classification_Accuracy_shape = Classification_Accuracy.shape
Feature_Labels_shape          = Feature_Labels.shape
Image_Classification_shape    = Image_Classification.shape
Image_Features_shape          = Image_Features.shape

#print(Image_Features_shape)
