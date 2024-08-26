from PIL import Image
import os
import re

images_path = r'/Users/yujeongjang/IdeaProjects/firebase/flutter_test/files/JSP프로그래밍'
image_list = []

list = sorted(os.listdir(images_path), key=lambda s: int(re.search(r'\d+', s).group()))

for i in list:
    print(i)
    img_path = 'files/JSP프로그래밍/' + i
    im_buf = Image.open(img_path)
    cvt_rgb = im_buf.convert('RGB')
    image_list.append(cvt_rgb)

image_list[0].save('files/JSP프로그래밍.pdf',  save_all=True, append_images=image_list[1:])

