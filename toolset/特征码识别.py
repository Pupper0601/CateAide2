import cv2
import matplotlib
import matplotlib.pyplot as plt
from mss import mss
from PIL import Image
import numpy as np

# 设置支持中文的字体（假设你已经安装相应的中文字体）
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置为黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

def take_screenshot(region, save_path):
    """截取屏幕区域并保存为图片"""
    region = {'left': region[0], 'top': region[1], 'width': region[2], 'height': region[3]}
    sct = mss()
    screenshot = sct.grab(region)

    img = Image.frombytes('RGBA', screenshot.size, screenshot.bgra, 'raw', 'BGRA')
    img = img.convert('RGB')  # 转换为 RGB 格式（如果需要保存为 JPEG 或 PNG）
    img.save(save_path + ".png")  # 保存截图
    return np.array(img)

def image_visualization(image1, image2):
    # 读取图像
    img1 = cv2.imread(image1)
    # img2 = cv2.imread(image2)
    img2 = image2

    # 转换为灰度图
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    # gray1 = cv2.GaussianBlur(gray1, (5, 5), 0)  # 高斯模糊
    # gray1 = cv2.equalizeHist(gray1) # 直方图均衡化

    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # gray2 = cv2.GaussianBlur(gray2, (5, 5), 0)  # 高斯模糊
    # gray2 = cv2.equalizeHist(gray2)  # 直方图均衡化

    # 创建SIFT检测器
    sift = cv2.SIFT_create()

    # 检测特征点和计算描述符
    keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

    # 创建BFMatcher对象
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    # 匹配描述符
    matches = bf.match(descriptors1, descriptors2)

    # 根据匹配结果进行排序
    matches = sorted(matches, key=lambda x: x.distance)

    # 计算相似度
    similarity = 0.0
    if len(keypoints1) > 0:
        matched_count = len(matches)  # 图2中包含的图1特征点数量
        similarity = matched_count / len(keypoints1)  # 图1特征点数量作为分母
        print(f"两个图像的相似度: {similarity:.2f}")
    else:
        print("图1没有检测到特征点，无法计算相似度。")

    return img1, img2, gray1, gray2, keypoints1, keypoints2, matches, similarity


def plot_image_matches(image1, image2):
    img1, img2, gray1, gray2, keypoints1, keypoints2, matches, similarity = image_visualization(image1, image2)
    # 可视化匹配
    img_matches_1 = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:10], None)
    img_matches_2 = cv2.drawMatches(gray1, keypoints1, gray2, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # 使用matplotlib显示匹配结果
    plt.figure(figsize=(5, 5))

    plt.subplot(2, 1, 1)  # 两行一列，第一个子图
    plt.imshow(cv2.cvtColor(img_matches_1, cv2.COLOR_BGR2RGB))
    plt.title(f'相似度: {similarity:.2f}')
    plt.axis('off')  # 不显示坐标轴

    plt.subplot(2, 1, 2)    # 两行一列，第二个子图
    plt.imshow(cv2.cvtColor(img_matches_2, cv2.COLOR_BGR2RGB))
    plt.title(f'相似度: {similarity:.2f}')
    plt.axis('off')  # 不显示坐标轴
    plt.show()


if __name__ == '__main__':
    img_1 = r"F:\Object\GitHub\CateAide2\basis_images\1920_1080\pose\zhan.png"
    img_2 = take_screenshot([709, 990, 30, 32], 'screenshot')
    # img_2 = r"F:\Object\GitHub\CateAide2\test\test1\screenshot.png"
    plot_image_matches(img_1, img_2)
