#   STEP 1 CREATE DATA FOR TRAINING THE MODEL
#Create Training Data
import numpy as np
import cv2

# load haarcascade face classifier
face_classifier = cv2.CascadeClassifier(  cv2.data.haarcascades +"haarcascade_frontalface_default.xml" )
 
# Load functions
def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces is () :
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]
        
    return cropped_face




# Collect 100 samples of your face from webcam input
def collect_samples(path, count):
    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        
            # Save file in specified directory with unique name
            file_name_path = path + str(count) + '.jpg'
            cv2.imwrite(file_name_path, face)
        
            # Put count on images and display live count
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Cropper', face)
        
        else:
            print("Face not found")
            pass
        if cv2.waitKey(1) == 13 or count == 100: #13 is the Enter Key
            break
        
    cap.release()
    cv2.destroyAllWindows()      
    print("Collecting Samples Complete")


i =0 
j=0

print("Collecting Samples Absar Qureshi")
collect_samples("C:/Users/ABSAR/OneDrive/Pictures/faces/user1/", i)

print("Collecting Samples Of Friend")
collect_samples("C:/Users/ABSAR/OneDrive/Pictures/faces/user2/", j)
