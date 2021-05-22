import cv2
import time

start_program=time.time()
print(start_program)

happy_time = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
nose_cascade = cv2.CascadeClassifier('nose.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cv2.namedWindow("Webcam")
cap = cv2.VideoCapture(0)

if cap.isOpened(): # try to get the first frame
    #_, img = cap.read()
    rval, frame = cap.read()
else:
    rval = False

while rval:
    cv2.imshow("Webcam", frame)
    rval, frame = cap.read()

    _, img = cap.read()
    rval, frame = cap.read()

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # viteza de redare 1.2
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)  # 4=vecini (mean)
    for (x, y, width, height) in faces:
        cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 2)

        if width>100:
            cv2.putText(img, "big head", (x-200, y + 30), cv2.FONT_ITALIC, 2, (255, 255, 255), 3, cv2.LINE_AA)
            cap_mare = 1
        else :
            cv2.putText(img, "small head", (x-200, y + 30), cv2.FONT_ITALIC, 2, (255, 255, 255), 3, cv2.LINE_AA)
            cap_mare = 0

    roi_gray = gray[y:y + height, x:x + width]
    roi_color = img[y:y + height, x:x + width]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # nose = nose_cascade.detectMultiScale(roi_gray)
    # for (nx, ny, nw, nh) in nose:
    #     cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (255, 255, 0), 2)



    smile = smile_cascade.detectMultiScale(roi_gray)
    for (sx, sy, sw, sh) in smile:
        if sw > 85  and sh > 30 :
            start_time_if1=time.time()
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (255, 0, 255), 2)
            cv2.putText(img, "you are smiling", (x-200, y+100), cv2.FONT_ITALIC, 2, (255, 255, 255), 3, cv2.LINE_AA)
            #happy_time = happy_time + 1
            end_time_if1 = time.time()
            happy_time = happy_time + (end_time_if1-start_time_if1)
        elif cap_mare == 0:
            start_time_if2 = time.time()
            cv2.putText(img, "you are smiling", (x - 200, y + 100), cv2.FONT_ITALIC, 2, (255, 255, 255), 3, cv2.LINE_AA)
            end_time_if2 = time.time()
            #happy_time = happy_time + 1
            happy_time = happy_time + (end_time_if2-start_time_if2)

    cv2.putText(img, "Happiness calculator", (x-250 , y - 200), cv2.FONT_ITALIC, 1, (255, 255, 255), 2, cv2.LINE_AA)

    end_program=time.time()
    real_time=end_program-start_program
    procent_program = happy_time * 100 / real_time

    if (procent_program < 0.05 and end_program > start_program+10):
        cv2.putText(img, "Smile more :)!", (x - 300, y - 100), cv2.FONT_ITALIC, 1, (0, 0, 255), 2, cv2.LINE_AA)

    procent_program = "{:.2f}".format(procent_program)

    cv2.putText(img, str(procent_program), (x + 100, y - 200), cv2.FONT_ITALIC, 1, (255, 255, 255), 2, cv2.LINE_AA)
    float(procent_program)
    cv2.putText(img, "%", (x + 170, y - 200), cv2.FONT_ITALIC, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Face detection', img)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("Webcam")


# start_program=time.time()
# start_time_if1=time.time()
# end_time_if2=time.time()
# happy_time=happy_time+start_time_if1-end_time_if2
#
# procent_program=happy_time*100/start_program
#
# if procent<30:
#     cv2.putText(img, "atentie persoana e depresiva!", (x - 200, y + 100), cv2.FONT_ITALIC, 2, (255, 255, 255), 3, cv2.LINE_AA)





