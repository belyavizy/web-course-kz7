import cv2
import face_recognition
import datetime

video_capture = cv2.VideoCapture(0)
time = []
while True:
    start = datetime.datetime.now()
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_locations = face_recognition.face_locations(gray)
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    finish = datetime.datetime.now()
    print('Время работы: ' + str((finish - start)))
    time.append((finish - start).microseconds)


print(sum(time) / len(time))

video_capture.release()
cv2.destroyAllWindows()
