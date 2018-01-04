import os
img_name = os.listdir("/Users/chenhai/Desktop/data/img")
print(img_name)
n = 0;
for temp in img_name:
    new_name = str(n).zfill(6)
    os.rename("/Users/chenhai/Desktop/data/img/"+temp,"/Users/chenhai/Desktop/data/img/"+new_name+".png")
    n+=1
