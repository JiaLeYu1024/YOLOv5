
# 拆分labels/train 到 val
import os
import shutil
import json

# path1：训练；path2：验证；path3：测试
def move_labels_imgs(path):

    # 打开标注文件
    data = json.load(open(path+'/annotations/train_val_test_distribution_file.json', 'r'))

    for file_name in data['train']:
        shutil.move(path+'/images/sum/' + file_name, path+'/images/train')
        shutil.move(path+'/labels/sum/' + file_name.split(".")[0] + ".txt", path+'/labels/train')

    for file_name in data['val']:
        shutil.move(path + '/images/sum/' + file_name, path + '/images/val')
        shutil.move(path + '/labels/sum/' + file_name.split(".")[0] + ".txt", path + '/labels/val')

    for file_name in data['test']:
        shutil.move(path + '/images/sum/' + file_name, path + '/images/test')
        shutil.move(path + '/labels/sum/' + file_name.split(".")[0] + ".txt", path + '/labels/test')

move_labels_imgs('../datasets/UAVVaste')
