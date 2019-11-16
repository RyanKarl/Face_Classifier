# python encode_faces.py --dataset dataset --encodings encodings.pickle
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
	help="path to input directory of faces + images")
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

#Find path to dataset images
print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images(args["dataset"]))

knownEncodings = []
knownNames = []

#Loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
	#Find the name of the individual
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]

	# Convert the image from BGR to dlib RGB
	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	#Find the coordinates of the bounding boxes for each face in the input image
	boxes = face_recognition.face_locations(rgb,
		model=args["detection_method"])

	#Compute the embedding for the face
	encodings = face_recognition.face_encodings(rgb, boxes)

	#Add each encoding and name to the set of known names and encodings
	for encoding in encodings:
		
		knownEncodings.append(encoding)
		knownNames.append(name)

#Save to disk
print("[INFO] serializing encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open(args["encodings"], "wb")
f.write(pickle.dumps(data))
f.close()
