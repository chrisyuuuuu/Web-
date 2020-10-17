import pytesseract
from PIL import Image
from PIL import ImageEnhance

def shibie(filepath):
    img = Image.open(filepath)
    # img = img.convert('RGB')
    # enhancer = ImageEnhance.Color(img)
    # enhancer = enhancer.enhance(0)
    # enhancer = ImageEnhance.Brightness(enhancer)
    # enhancer = enhancer.enhance(2)
    # enhancer = ImageEnhance.Contrast(enhancer)
    # enhancer = enhancer.enhance(8)
    # enhancer = ImageEnhance.Sharpness(enhancer)
    # img = enhancer.enhance(20)

    # 转化为灰度图片
    img = img.convert('L')

    # 二值化处理
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = img.point(table, '1')

    return pytesseract.image_to_string(img)