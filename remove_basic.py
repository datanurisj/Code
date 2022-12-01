'''import'''
from multiprocessing.sharedctypes import Value
import pandas as pd 
import numpy as np
import json
import itertools

# 파일 경로
path_1 = 'C:\\Users\\이성재\\Desktop\\새 폴더\\dentistry_dataset_RP_1544.json'

with open(path_1, 'rt', encoding='UTF8') as j:
    content = json.load(j)
         
rp_info = content['info']
rp_image = content['images']
rp_annot = content['annotations']
rp_categ = content['categories']

rp = rp_info + rp_image
type(rp_info)
type(rp_image)
# segmentation 제거
rp_annot[4701]['segmentation'] = []
rp_annot[4701]


# 전체 적용
for i in range(len(rp_annot)):
    if rp_annot[i]['segmentation'] != []:
        rp_annot[i]['segmentation'] = []
    else:
        print("전부 끝났습니다.")
    
rp_annot

# json으로 추출
with open('Bbox.json', 'w', encoding="utf-8") as make_file:
    json.dump(rp_annot,make_file, ensure_ascii=False, indent="\t")
    