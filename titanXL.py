import requests
import cv2
import mediapipe as mp
import titanmodule
import time

token = 'urenBIzfvtrk7HMbr61QGPLqmrff7BJoD3EqkLfoHeC'
url = 'https://notify-api.line.me/api/notify'
headers = {'content-type' : 'application/x-www-form-urlencoded', 'Authorization' : 'Bearer ' + token}
session = requests.Session()
data={'message': 'Alert! someone falling'}
told = False

# initialize Pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# create capture object
cap = cv2.VideoCapture(0)
consist=0
while cap.isOpened():
    # read frame from capture object
    _, frame = cap.read()
    time.sleep(0.033)
    
    try:
     # convert the frame to RGB format
        RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # process the RGB frame to get the result
        results = pose.process(RGB)
        if titanmodule.laydown(results):
           consist+=1
        elif consist>0:
           consist-=1
        if consist>=150:
           consist=70
           if told == False:
              told = True
              session.post(url,headers=headers,data=data) 
        if consist <= 5:
           told = False

        # draw detected skeleton on the frame
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        # show the final output
        cv2.imshow('Output', frame)
    except:
        cv2.imshow('Output', frame)
        pass
    if cv2.waitKey(1) == ord('q'):
     break
cap.release()
cv2.destroyAllWindows()