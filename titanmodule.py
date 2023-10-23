import cv2
import mediapipe as mp

def laydown(results):
    landmark_list=[]
    for id, lm in enumerate(results.pose_world_landmarks.landmark):

           landmark_list.append([id, lm.x, lm.y, lm.z])
        
    #create list with y,z position
    landmark_posy=[]
    landmark_posx=[]
    for landmark in landmark_list:
        landmark_posx.append(landmark[1])
        landmark_posy.append(landmark[2])
        
    #find laydown position
    laydown=False
    if max(landmark_posy)-min(landmark_posy) < (max(landmark_posx)-min(landmark_posx))*0.8:
        laydown=True
    print(landmark_posy)
    print(landmark_posx)
    print(laydown)
    print(max(landmark_posy)-min(landmark_posy))
    print(max(landmark_posx)-min(landmark_posx))
    return laydown

