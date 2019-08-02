import requests
from bs4 import BeautifulSoup
import xml
from lxml import html
import csv


def getUrlContent(url):
    paper_name = []
    paper_url = []

    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'lxml')

    for i in soup.find_all("dt"):
        paper_name.append(i.get_text())

    for i in soup.find_all("dd"):
        for a in i.find_all("a"):
            href = a.get('href')
            text = a.get_text()
            if href != None and text == "pdf":
                paper_url.append("http://openaccess.thecvf.com/" + href)

    assert len(paper_name) == len(paper_url) == 1294
    return paper_name, paper_url


if __name__ == "__main__":
    url = "http://openaccess.thecvf.com/CVPR2019.py"
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

    paper_name, paper_url = getUrlContent(url)

    with open("CVPR2019.csv", 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["id", "name", "url"] + cls)
        for i, name in enumerate(paper_name):
            writer.writerow([i+1, name, paper_url[i]] + [" "])
