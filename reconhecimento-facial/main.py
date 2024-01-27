import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
face_recognition = mp.solutions.face_detection
face_recognizer = face_recognition.FaceDetection()
draw = mp.solutions.drawing_utils

while True:
    checker, frame = webcam.read()

    if not checker:
        break

    list_face = face_recognizer.process(frame)

    if list_face.detections:
        for face in list_face.detections:
            draw.draw_detection(frame, face)

    cv2.imshow("Faces", frame)

    if cv2.waitKey(5) == 27:
        breakpoint()


webcam.release()
cv2.destroyAllWindows()
