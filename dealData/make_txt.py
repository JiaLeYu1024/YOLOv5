import os, sys, zipfile
import json


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = box[0] + box[2] / 2.0
    y = box[1] + box[3] / 2.0
    w = box[2]
    h = box[3]

    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


# 打开标注文件
data = json.load(open('../datasets/UAVVaste/annotations/annotations.json', 'r'))

# 保存的路径
sum_txt_save_path = "../datasets/UAVVaste/labels/sum"


for img in data['images']:
    filename = img["file_name"]
    img_width = img["width"]
    img_height = img["height"]
    img_id = img["id"]
    ana_txt_name = filename.split(".")[0] + ".txt"  # 对应的txt名字，与jpg一致
    # print(ana_txt_name)
    f_txt = open(os.path.join(sum_txt_save_path, ana_txt_name), 'w')
    for ann in data['annotations']:
        if ann['image_id'] == img_id:
            box = convert((img_width, img_height), ann["bbox"])
            f_txt.write("%s %s %s %s %s\n" % (ann["category_id"], box[0], box[1], box[2], box[3]))
    f_txt.close()
