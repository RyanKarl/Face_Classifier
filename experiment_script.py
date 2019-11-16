from os import listdir
from os.path import isfile, join
import subprocess

#Collect the path
mypath = "/Users/ryankarl/Computer_Vision/course_project/Face_Classifier/examples/False/"

#Collect all image files
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#Run classifier for each image file
for i in onlyfiles:
    path = 'examples/False/' + i
    print subprocess.check_output(['python','recognize_faces_image.py', '--encodings','encodings.pickle','--image', path])
