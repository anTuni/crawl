import cv2
import os
import os.path

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_casecade = cv2.CascadeClassifier('./haarcascade_eye.xml')

candidates = ['유재석', '안철수', '제니', '박지성', '엄홍길', '김택진', '기안84', '데니스홍']

for candidate in candidates:
    path = 'D:/sources/crawl/crwaledimage/images/'+candidate
    i = 1
    while True:
        img = cv2.imread(path + '/' + str(i) +'.jpg')
        print(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3,5)
        imgNum  = 0
        
        for (x,y,w,h) in faces:
            print('for'+str(imgNum))
            try:
                if not os.path.exists(path+"/cropped"):
                    os.makedirs(path+"/cropped")
                cropped = img[y - int(h / 10):y + h + int(h / 10), x - int(w / 10):x + w + int(w / 10)]
                cv2.imwrite(path + "/cropped" + str(i)+"_"+ str(imgNum) + ".png", cropped)
            except:
                continue
            imgNum += 1
        i = i+1