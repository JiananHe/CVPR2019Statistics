import csv
import re
from itertools import islice


def clsList(name, cls_num):
    cls_list = [" "] * cls_num

    if re.search(r'.*Classification.*', name, flags=re.IGNORECASE) is not None or re.search(r'.*Recognition.*', name, flags=re.IGNORECASE) is not None:
        cls_list[0] = 1
    if re.search(r'.*Detection.*', name, flags=re.IGNORECASE) is not None or re.search(r'.*Location.*', name, flags=re.IGNORECASE) is not None:
        cls_list[1] = 1
    if re.search(r'.*Segmentation.*', name, flags=re.IGNORECASE) is not None:
        cls_list[2] = 1
    if re.search(r'.*Tracking.*', name, flags=re.IGNORECASE) is not None:
        cls_list[3] = 1
    if re.search(r'.*Registration.*', name, flags=re.IGNORECASE) is not None or re.search(r'.*Stereo.*', name, flags=re.IGNORECASE) is not None:
        cls_list[4] = 1
    if re.search(r'.*Re-Identification.*', name, flags=re.IGNORECASE) is not None:
        cls_list[5] = 1
    if re.search(r'.*Pose.*Estimation.*', name, flags=re.IGNORECASE) is not None:
        cls_list[6] = 1
    if re.search(r'.*Text-to-Image.*', name, flags=re.IGNORECASE) is not None or re.search(r'.*Image Synthesis.*', name, flags=re.IGNORECASE) is not None\
            or re.search(r'.*Image Generation.*', name, flags=re.IGNORECASE) is not None or re.search(r'.*Image Completion.*', name, flags=re.IGNORECASE) is not None\
            or re.search(r'.*Image Inpainting.*', name, flags=re.IGNORECASE) is not None:
        cls_list[7] = 1
    if re.search(r'.*Super-Resolution.*', name, flags=re.IGNORECASE) is not None or re.search(r'.*Image-To-Image.*', name, flags=re.IGNORECASE) is not None \
            or re.search(r'.*Style Transfer.*', name, flags=re.IGNORECASE) is not None or re.search(r'.*Image Restoration.*', name, flags=re.IGNORECASE) is not None\
            or re.search(r'.*Image Rectification.*', name, flags=re.IGNORECASE) is not None or re.search(r'.*Image Deblurring.*', name, flags=re.IGNORECASE) is not None:
        cls_list[8] = 1
    if re.search(r'.*Image Retrieval.*', name, flags=re.IGNORECASE) is not None or re.search(r'.*Image Search.*', name, flags=re.IGNORECASE) is not None:
        cls_list[9] = 1
    if re.search(r'.*Question.*Answering.*', name, flags=re.IGNORECASE) is not None:
        cls_list[10] = 1
    if re.search(r'.*Point Cloud.*', name, flags=re.IGNORECASE) is not None or re.search(r'.*3D.*Reconstruction.*', name, flags=re.IGNORECASE) is not None \
            or re.search(r'.*SLAM.*', name, flags=re.IGNORECASE) is not None:
        cls_list[11] = 1

    return cls_list


if __name__ == "__main__":
    cls = ["分类/识别(Classification/Recognition)", "检测/定位(Detection/Location)",
           "分割(Segmentation)", "跟踪(Tracking)", "匹配(Registration/Stereo)",
           "重识别(Re-Identification)", "姿态估计(Pose Estimation)",
           "图像生成(生成原本不存在的图像或图像局部)(Text-to-Image/Image Synthesis/Image Generation/Image Completion/Image Inpainting)",
           "图像转换(基于已有图像进行变化)(Image-To-Image Translation/Style Transfer/Image Restoration/Image Rectification/Image Deblurring/Image Denosing/Super-Resolution)",
           "图像检索(Image Retrieval/Search)", "图像语义(Semantic Image/Visual Question Answering)",
           "三维场景相关(Point Clouds/3D Reconstruction/SLAM)", "Dataset/Benchmark",
           "学习策略相关（可用于改善样本空间、网络结构、训练过程、泛化能力等等的策略方法）",
           "网络结构相关（重点在于提出一种新的网络结构、或优化网络连接方法的论文，同时也应归类于该网络应用领域的topic）",
           "其他"
           ]
    cls_num = len(cls)

    file = open("CVPR2019.csv", 'r')

    csv_files = [open("CVPR2019_total.csv", 'w', newline=""),
                 open("1CVPR2019_sjr.csv", 'w', newline=""), open("2CVPR2019_ly.csv", 'w', newline=""),
                 open("3CVPR2019_xzm.csv", 'w', newline="")]

    reader = csv.reader(file)

    writers = []
    for i in range(4):
        writers.append(csv.writer(csv_files[i]))
        writers[i].writerow(["id", "name", "url"] + cls)

    for line in islice(reader, 1, None):
        id, name, url = line[:3]
        cls_list = clsList(name, cls_num)
        writers[0].writerow([id, name, url]+cls_list)
        if 325 <= int(id) < 649:
            writers[1].writerow([id, name, url]+cls_list)
        elif 649 <= int(id) < 972:
            writers[2].writerow([id, name, url]+cls_list)
        elif 972 <= int(id) < 1295:
            writers[3].writerow([id, name, url]+cls_list)



