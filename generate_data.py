# coding=utf-8
import os
import pandas as pd
import numpy as np

DATA_PATH = 'data'
img_path = os.path.join(DATA_PATH, 'AllDICOMs')
img_res_path = os.path.join(DATA_PATH, 'Pictures')
csv_path = os.path.join(DATA_PATH, 'INbreast.csv')

# 获取全名
#dcm_list = [dcm for dcm in os.listdir(img_path) if dcm.endswith('.dcm')]
# 1. 对所有dcm进行格式转换，并保存
#for dcm in dcm_list:
#    import dicom 
#    img_name = dcm.split('.dcm')[0]
#    content = dicom.read_file(os.path.join(img_path, dcm))
#    img = content.pixel_array
#    img = np.stack([img]*3, axis=-1)
#    import scipy
#    import scipy.misc
#    scipy.misc.imsave(os.path.join(img_res_path, img_name+'.jpg'), img)

print 'img exchange done.'
jpg_dict = {}
jpg_list = [jpg for jpg in os.listdir(img_res_path) if jpg.endswith('.jpg')]
for jpg in jpg_list:
    jpg_dict[jpg.split('_')[0]] = jpg
# 获取label
label_dict = {}
with open(os.path.join(img_path, 'label_zwt_10.txt')) as f:
    lines = f.readlines()
    for line in lines:
        img_name, label = line.split(' ')
        #print img_name, label
        label_dict[str(img_name)] = int(label)
#print label_dict, len(label_dict)
#print dcm_dict
train = pd.read_csv(csv_path, sep=';')
train['img_path'] = train['File Name'].map(lambda x: os.path.join(img_res_path, jpg_dict[str(x)]))
train['label'] = train['File Name'].map(lambda x: label_dict[str(x)])


train.to_csv(os.path.join(DATA_PATH, 'train.csv'), index=False)
