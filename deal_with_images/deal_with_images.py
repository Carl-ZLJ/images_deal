from PIL import Image


def fill_image(file_path):
    img = Image.open(file_path)
    width, height = img.size
    # 选取长和宽中较大值作为新图片的
    new_image_length = width if width > height else height
    # 生成新图片[白底]
    new_image = Image.new(img.mode, (new_image_length, new_image_length), color='white')
    # 将之前的图粘贴在新图上，居中 if width > height:#原图宽大于高，则填充图片的竖直维度
    # (x,y)二元组表示粘贴上图相对下图的起始位置
    if height < width:
        new_image.paste(img, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(img, (int((new_image_length - width) / 2), 0))
    return new_image


# 切图
# 行m 列n
def cut_image(file_path, m, n):
    img = Image.open(file_path)
    width, height = img.size
    item_width = int(width / n)
    item_height = int(height / m)
    box_list = []
    # crop 参数 (left, upper, right, lower)
    for i in range(0, m):
        for j in range(0, n):
            box = (j*item_width, i*item_height, (j+1)*item_width, (i+1)*item_height)
            box_list.append(box)
    img_list = [img.crop(box) for box in box_list]
    return img_list


# 保存
def save_images(img_list):
    index = 1
    for img in img_list:
        img.save('./result'+str(index) + '.png', 'PNG')
        index += 1


# 行m 列n
def show_images(img_lst, m, n):
    width, height = img_lst[0].size
    gap = 10
    new_image = Image.new(img_lst[0].mode, (int(width*n + (n-1)*gap), \
                          int(height*m + (m-1)*gap)), color='white')
    # new_image.show()
    for i in range(0, m):
        for j in range(0, n):
            new_image.paste(img_lst[i*m + j], (j*width + j*gap, i*height + i*gap))
    return new_image
