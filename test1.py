#coding:utf-8

from PIL import Image,ImageFilter

kitten = Image.open(u"微信图片_20170716160123.png")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("test.png")
blurryKitten.show()

