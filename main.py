
import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

def detectImages(img, classifier):
  haarcascade = cv2.CascadeClassifier(classifier)
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  faces = haarcascade.detectMultiScale(gray) 
  for face in faces:
    x, y, w, h = face
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 5) #Buat bounding boxes yang masuk di ROI
  return img

def gaussianBlur(img, classifier):
  haarcascade = cv2.CascadeClassifier(classifier)
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  faces = haarcascade.detectMultiScale(gray) 
  for face in faces:
    x, y, w, h = face
    img[y:y+h, x:x+w] = cv2.GaussianBlur(img[y:y+h, x:x+w], (41,41), 0) #Blur pixels yang masuk dalam ROI
  return img

def mosaicBlur(img, classifier):
  haarcascade = cv2.CascadeClassifier(classifier)
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  faces = haarcascade.detectMultiScale(gray) 
  for face in faces:
    x, y, w, h = face
    
    steps_count = 8
    stepsX = np.linspace(x, x + w, steps_count + 1, dtype=np.int)
    stepsY = np.linspace(y, y + h, steps_count + 1, dtype=np.int)

    #Iterasi sesuai (steps_count x steps_count) kemudian membuat buat sensor bentuk rectangle dengan warna rata-rata pada tiap regionnya
    for directionX in range(steps_count):
      for directionY in range(steps_count):
        color = cv2.mean(
            img[
                stepsY[directionY] : stepsY[directionY + 1], 
                stepsX[directionX] : stepsX[directionX + 1]
                ]
            )
        cv2.rectangle(
            img, 
            (stepsX[directionX], stepsY[directionY]), 
            (stepsX[directionX + 1], stepsY[directionY + 1]), 
            color, 
            -1
            )
  return img

classifier = 'haarcascade_frontalface_default.xml'
img_path = sys.argv[1]

#Features
if sys.argv[2] == '1':
    img = cv2.imread(img_path)
    output1 = detectImages(img, classifier)
    plt.imshow(cv2.cvtColor(output1, cv2.COLOR_BGR2RGB))
    plt.title('Bounding Box')
    plt.grid(None) 
    plt.xticks([])
    plt.yticks([])
    lt.show()

elif sys.argv[2] == '2':
    img = cv2.imread(img_path)
    output2 = gaussianBlur(img, classifier)
    plt.imshow(cv2.cvtColor(output2, cv2.COLOR_BGR2RGB))
    plt.title('Gaussian Blur')
    plt.grid(None) 
    plt.xticks([])
    plt.yticks([])
    plt.show()

elif sys.argv[2] == '3':
    img = cv2.imread(img_path)
    output3 = mosaicBlur(img, classifier)
    plt.imshow(cv2.cvtColor(output3, cv2.COLOR_BGR2RGB))
    plt.title('Mosaic Blur')
    plt.grid(None) 
    plt.xticks([])
    plt.yticks([])
    plt.show()

else:
    img = cv2.imread(img_path)
    img1 = img.copy()
    img10 = img.copy()
    img11 = img.copy()
    output1 = detectImages(img1, classifier)
    output2 = gaussianBlur(img10, classifier)
    output3 = mosaicBlur(img11, classifier)
    output = [img, output1, output2, output3]
    titles = ['Original', 'Detected', 'Gaussian Blur', 'Mosaic Blur']

    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(cv2.cvtColor(output[i], cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.grid(None) 
        plt.xticks([])
        plt.yticks([])
    plt.rcParams["figure.figsize"] = (15,10)
    plt.show()