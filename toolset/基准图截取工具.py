import mss
from PIL import Image


def take_screenshot(region, save_path):
    """
    截取屏幕指定区域
    :param region: 需要截取的区域, 格式为 (left, top, width, height)
    :return: 截取的图片
    """
    region = {'left': region[0], 'top': region[1], 'width': region[2], 'height': region[3]}
    sct = mss.mss()
    screenshot = sct.grab(region)
    img = Image.frombytes('RGBA', screenshot.size, screenshot.bgra, 'raw', 'BGRA')
    img = img.convert('RGB')  # 转换为 RGB 格式
    img.save(save_path + '.png')  # 保存截图

def main(lists, paths):
    for i in range(len(lists)):
        take_screenshot(lists[i], paths[i])


if __name__ == '__main__':
    # 设置截屏区域（左，上，右，下）
    region = [
        (1373, 96, 60, 27),
        (1373, 322, 60, 27)
    ]
    save_paths = [
        'MXNG',
        'DLGNF'
    ]
    main(region, save_paths)



