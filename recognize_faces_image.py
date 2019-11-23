#This was inspired by the following articles:
#https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
#file:///Users/ryankarl/Downloads/Face%20recognition%20with%20OpenCV,%20Python,%20and%20deep%20learning%20-%20PyImageSearch.htm
#http://blog.dlib.net/2017/02/high-quality-face-recognition-with-deep.html

# python recognize_faces_image.py --encodings encodings.pickle --image examples/...

import face_recognition
import argparse
import pickle
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

#Load the faces and embeddings
print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

#Load the input image and convert it from BGR to RGB for dlib
image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Find the coordinates of the bounding boxes corresponding for each face in the input image, and compute the embeddings
print("[INFO] recognizing faces...")
boxes = face_recognition.face_locations(rgb,
	model=args["detection_method"])
encodings = face_recognition.face_encodings(rgb, boxes)

names = []

#Loop over the embeddings
for encoding in encodings:
	#Try to match each face in the input image to known encodings
	matches = face_recognition.compare_faces(data["encodings"],
		encoding)
	name = "Unknown"

	#Verify match
	if True in matches:
		#Find the matched faces and count the number of times each face was matched
		matchedIdxs = [i for (i, b) in enumerate(matches) if b]
		counts = {}

		#Count for each recognized face
		for i in matchedIdxs:
			name = data["names"][i]
			counts[name] = counts.get(name, 0) + 1

		#Find the face with the most votes 
		name = max(counts, key=counts.get)
	
	#Update the list of names
	names.append(name)

#Loop over the recognized faces
for ((top, right, bottom, left), name) in zip(boxes, names):
	#Write the name on the image
	cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
	y = top - 15 if top - 15 > 15 else top + 15
	cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
		0.75, (0, 255, 0), 2)

#Show the output 
cv2.imshow("Image", image)
cv2.waitKey(0)
