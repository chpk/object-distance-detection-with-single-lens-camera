import json
import os
import cv2
 	
font = cv2.FONT_HERSHEY_SIMPLEX
camdist=11.5
os.system('python flow --model cfg/yolo.cfg --load bin/yolo.weights')
os.system('python flow --imgdir sample_img/ --model cfg/yolo.cfg --load bin/yolo.weights --json')
with open('C:\\Users\\Premith Kumar\\Desktop\\object distance detection with single lens camera\\darkflow-master\\sample_img\\out\\zoom2.json') as f:
    data = json.load(f)
zdct0=data[0]['topleft']
zdct1=data[0]['bottomright']
with open('C:\\Users\\Premith Kumar\\Desktop\\object distance detection with single lens camera\\darkflow-master\\sample_img\\out\\originalimg2.json') as f:
    data = json.load(f)
odct0=data[0]['topleft']
odct1=data[0]['bottomright']
#############################################################################
d=float((odct1['y']-odct0['y'])/(zdct1['y']-zdct0['y']))
print(str((camdist/float(1-(d)))-5)+'cms')
#############################################################################
im=cv2.imread("C:\\Users\\Premith Kumar\\Desktop\\object distance detection with single lens camera\\darkflow-master\\sample_img\\originalimg2.jpg")
img = cv2.resize(im, (int(im.shape[1]/3), int(im.shape[0]/4)))
im=cv2.putText(img, str((camdist/float(1-(d)))-5)+"cm", (int(odct0['x']/3),int( odct0['y']/4)), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
img = cv2.rectangle(im, (int(odct0['x']/3),int( odct0['y']/4)), (int(odct1['x']/3),int( odct1['y']/4)), (0,0,255), 2)
cv2.imshow('Draw01',img)
cv2.waitKey(0)

################INSTRUCTIONS##############################
# 1)INSTALL DARKNET BEFORE RUNNING THIS JSONPARSE.PY.THE WEIGHTS AND CONFIGURATION FILES TO RUN YOLO ARE PLACES IN bin,cfg FOLDERS RESPECTIVELY
# 2)THE IMAGES TO BE TESTED ARE PRESENT IN sample_img FOLDER. SO ACCORDINLY CHANGE THE IMAGE PATH,NAMES TO RUN THE CODE
# 3)ASSIGN camdist=15(for originalimg,zoom IMAGES), 20(for originalimg1,zoom1 IMAGES), 11.5(for originalimg2,zoom2 IMAGES)
##################DESIRED DISTANCES#######################################
#actual distance:45 , 50, 46.5 

#**PROBLEMS ON INSTALLING YOLO REFER TO README.MD