import cv2
from PIL import Image
cap = cv2.VideoCapture(0)
import time

while True:
    ret, frame = cap.read()
    frame_cvt = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_blur = cv2.GaussianBlur(frame_cvt, (5, 5), 0)
    frame_edge = cv2.Canny(frame_blur, 30, 50)
    contours, _ = cv2.findContours(frame_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_contour)
        if cv2.contourArea(max_contour) > 5000:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
            object_only = frame[y:y+h, x:x+w]
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('s'):
                img_pil = Image.fromarray(object_only)
                time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
                img_pil.save(f"{time_str}.pdf")
                print('Save')