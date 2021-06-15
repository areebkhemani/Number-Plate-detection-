import cv2

count = 0
frameWidth = 640
frameHeight = 480
minarea = 500
numPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

success, img = cap.read()
while success:

    imgGray = cv2.cvtColor(img, cv2.COLOR_BAYER_GR2GRAY)
    num_plates = numPlateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, width, height) in num_plates:
        area = width * height
        if area > minarea:
            cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 1.5)
            cv2.putText(img, "Number Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
            imgRoi = img[y: y + height, x: x + width]
            cv2.imshow("ROI", imgRoi)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("s"):
        cv2.imwrite("Resources/Scanned/NoPlate" + str(count) + ".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), 3, cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 255), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 255), 3)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1

"""
Press 'S' to take a snap shot of the plate and save it to the scanned folder located under Resources
"""




