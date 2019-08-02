#-*- coding:utf-8 -*-
import csv
from itertools import islice
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl


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
cls_abbr = ["分类/识别", "检测/定位",
       "分割", "跟踪", "匹配",
       "重识别", "姿态估计",
       "图像生成",
       "图像转换",
       "图像检索", "图像语义",
       "三维场景相关", "Dataset/Benchmark",
       "学习策略相关",
       "网络结构相关",
       "其他"
       ]

cls_num = len(cls)

res_file = open("CVPR2019_Result.csv", 'w', newline='')
writer = csv.writer(res_file)
writer.writerow(["id", "name", "url"] + cls)

csv_files = [open("0CVPR2019_hja(1).csv", 'r'),open("1CVPR2019_sjr(1).csv", 'r'),
             open("2CVPR2019_ly(1).csv", 'r'), open("3CVPR2019_xzm(1).csv", 'r')]

cls_list = [0] * cls_num
paper_sum = 0
for i in range(4):
    reader = csv.reader(csv_files[i])
    for line in islice(reader, 1, None):
        writer.writerow(line)

        line_cls = line[3:19]
        for idx, c in enumerate(line_cls):
            if str(c).find("1") != -1:
                cls_list[idx] += 1
        paper_sum += 1

assert paper_sum == 1294
cls_ratio = 100 * np.array(cls_list) / paper_sum

print("%d papers classification: \n " % paper_sum,
      " ".join("%s \n %d %.2f%%\n\n" % (cls[i], cls_list[i], cls_ratio[i]) for i in range(cls_num)))

print(np.sum(cls_list))
print(np.sum(cls_ratio))
writer.writerow([""])
writer.writerow([""])
writer.writerow(["", "Total", ""] + cls_list + ["Sum: " + str(np.sum(cls_list))])
writer.writerow(["", "Ratio", ""] + ['%.2f%%' % i for i in cls_ratio] + ["Sum: %.2f%%" % np.sum(cls_ratio)])

# draw bar picture
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# plt.figure()
x = np.arange(cls_num) + 1
y = cls_ratio
xticks = cls_abbr

plt.bar(x, y, width=0.7, align='center')
plt.xticks(x, xticks, size='small', rotation=30)
plt.xlabel('Paper Topic')
plt.ylabel('Paper Ratio(%)')
plt.title("CVPR2019 Papers Statistics")
for a, b in zip(x, y):
    plt.text(a, b+0.05, '%.2f%%' % b, ha='center', va='bottom', fontsize=9)
for a, b, c in zip(x, y, cls_list):
    plt.text(a, b+0.5, '%d' % c, ha='center', va='bottom', fontsize=9)

plt.ylim(0,18)
plt.show()



