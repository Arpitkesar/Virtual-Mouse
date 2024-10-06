# step:1-The above code is used to open the camera
import cv2
import mediapipe as mp  # it is used to detect the face
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()  # it will increase the size of window camera
while True:
    isTrue, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # it is used to see the image in colour
    output = face_mesh.process(rgb_frame)
    landmark_point = output.multi_face_landmarks  # as this will determine the points occur in face like in eyes,teeth,chin,etc
    frame_h, frame_w, _ = frame.shape
    if landmark_point:
        landmarks = landmark_point[0].landmark
        # enumerate return the index of a range
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            # it will smaller the fraction of x axis and y axis which is less than 1
            if id == 1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)
        Left = [landmarks[145], landmarks[159]]
        for landmark in Left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if(Left[0].y - Left[1].y) < 0.004:  # it determine that eye is blinking and closed
            pyautogui.click()
            pyautogui.sleep(1)

    #  print(landmark_point)
    cv2.imshow("Eye Contolled Mouse", frame)
    cv2.waitKey(1)
# step-2:now we detect the face whether face is existing or not



