import os
import cv2
from cv2 import imread


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame= cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
print(size)
out = cv2.VideoWriter('Sunset.mp4',cv2.VideoWriter_fourcc(*'mp4v'),5, size)

for i in range(count-1, 0, -1):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()
print("done")