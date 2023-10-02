import os
import cv2


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
frame = cv2.imread(images[81])
height,width,channels = frame.shape
vid = cv2.VideoWriter("sunset.avi",cv2.VideoWriter_fourcc(*"MPEG"),10,(width,height))
for i in range(0,count):
    frame = cv2.imread(images[i])
    vid.write(frame)
vid.release()
print("done")