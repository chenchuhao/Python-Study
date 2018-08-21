# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:04:46 2018

@author: lenovo
"""

import itchat
import os
import PIL.Image as Image
import math
#1-登录微信获取好友信息
##返回数据为列表，每个好友的用户名、昵称、备注、签名等信息为一个单独的元素，用户自己的为第一个
itchat.login()
friends = itchat.get_friends(update=True)
#print (friends)
print (1)

#2-创建文件夹用于保存好友头像
user = friends[0]['UserName']
os.mkdir(user)
print(2)

#3-保存好友头像
# a=''
k=0
# chars = a.maketrans('@#$%^&*~ﾍ()･_|{}[]?<> ','**********************')
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
#     j=i["NickName"].translate(chars).replace('*','')  
    fileImage = open(user + "/" + str(k) + ".jpg",'wb')
#     fileImage = open(user + "/" + j + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    k+=1
print(3)   
 
"""重命名
k = 0
for file in os.listdir(user):
    os.rename(user+"/"+file,user+"/test/"+str(k)+".jpg")
    k+=1
user = "@be23a623c15af56d94b465af3e2cfb20490293718910415d06d9504a567d4530/test"
"""
#4-头像按设定图像拼接并保存   
img=Image.open('im.bmp')
w=img.size[0]
h=img.size[1]
r=math.ceil(1040/w)
img = img.resize((int(w*r/100)*100, int(h*r/100)*100), Image.ANTIALIAS)
s=os.listdir(user)
c = len(s)
w=img.size[0]
h=img.size[1]
newim = Image.new('RGBA', (w, h))

k=0
x=0
y=0
for i in range(0,w,40):
    for j in range(0,h,40):
        p = img.getpixel((i, j))[2]
        if p!=255:
            try:
                im = Image.open(user + "/" +  str(k) + ".jpg")
            except:
                if k==c-1:
                    k=0
                else:
                    k+=1
            finally:
                im = Image.open(user + "/" +  str(k) + ".jpg")
                im = im.resize((40, 40), Image.ANTIALIAS)
                newim.paste(im, (i, j))
                if k==c-1:
                    k=0
                else:
                    k+=1
newim.save(user + ".bmp")
itchat.send_image(user + ".bmp", 'filehelper')
itchat.logout()






