# Face_Classifier

It is suggested users run the following pip command to download key packages:

  pip install dlib imutils face_recognition

To run the Feature Extractor run the following command (quit with SPACE):

  python encode_faces.py --dataset dataset --encodings encodings.pickle

To run the Face Classifier run the following command (quit with SPACE):

  python recognize_faces_image.py --encodings encodings.pickle --image examples/True/IMG_1907.jpg

The best way to run the LBP Face Classifier is via iPython Jupyter Notebook (this can be installed via pip or conda).

Once Jupyter is installed, navigate to the lbp directory and start the notebook with the command: (note the iPython kernel is version 3)

  jupyter notebook lbp_work.ipynb

The features have already been extracted, and the model saved, so pickle files are provided for the sake of efficiency and convenience.

Below is the Python Environment to run the CNN based Face Classifier:

absl-py==0.8.1

anytree==2.7.0

astor==0.8.0

backports.functools-lru-cache==1.5

backports.weakref==1.0.post1

beautifulsoup4==4.8.1

cachetools==3.1.1

certifi==2019.9.11

chardet==3.0.4

Click==7.0

cloudpickle==1.2.2

cmake==3.15.3

cycler==0.10.0

decorator==4.4.0

dlib==19.18.0

enum34==1.1.6

face-recognition==1.2.3

face-recognition-models==0.3.0

funcsigs==1.0.2

functools32==3.2.3.post2

futures==3.3.0

gast==0.2.2

google-auth==1.7.1

google-auth-oauthlib==0.4.1

google-pasta==0.1.8

graphviz==0.13

grpcio==1.25.0

h5py==2.10.0

idna==2.8

imutils==0.5.3

Keras==2.3.1

Keras-Applications==1.0.8

Keras-Preprocessing==1.1.0

keras-vggface==0.6

kiwisolver==1.1.0

lxml==4.4.1

Markdown==3.1.1

matplotlib==2.2.4

mock==3.0.5

networkx==2.2

numpy==1.16.5

oauthlib==3.1.0

opt-einsum==2.3.2

pandas==0.24.2

Pillow==6.2.0

protobuf==3.10.0

pyasn1==0.4.7

pyasn1-modules==0.2.7

pybaseball==1.0.8

pyparsing==2.4.2

python-dateutil==2.8.0

pytz==2019.2

PyWavelets==1.0.3

PyYAML==5.1.2

requests==2.22.0

requests-oauthlib==1.3.0

rsa==4.0

scikit-image==0.14.5

scikit-learn==0.20.4

scipy==1.2.2

seaborn==0.9.0

six==1.12.0

sklearn==0.0

soupsieve==1.9.4

subprocess32==3.5.4

tensorboard==2.0.1

tensorflow==2.0.0

tensorflow-estimator==2.0.1

termcolor==1.1.0

urllib3==1.25.6

Werkzeug==0.16.0

wrapt==1.11.2

Below is the Python Environment to run the LBP-based Face Classifier:

absl-py==0.7.1
astor==0.8.0
certifi==2019.6.16
chardet==3.0.4
Click==7.0
cycler==0.10.0
decorator==4.4.1
dlib==19.17.0
easydict==1.9
face-recognition==1.2.3
face-recognition-models==0.3.0
ffmpeg==1.4
gast==0.2.2
google-pasta==0.1.7
grpcio==1.22.0
h5py==2.9.0
idna==2.8
imageio==2.6.1
imutils==0.5.2
joblib==0.13.2
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.0
kiwisolver==1.1.0
Markdown==3.1.1
matplotlib==3.1.1
networkx==2.4
numpy==1.17.1
opencv-contrib-python==4.1.1.26
opencv-python==4.1.0.25
pandas==0.25.0
Pillow==6.0.0
protobuf==3.9.0
pyparsing==2.4.2
python-dateutil==2.8.0
pytz==2019.2
PyWavelets==1.1.1
PyYAML==5.1.2
requests==2.22.0
scikit-image==0.16.2
scikit-learn==0.15.0
scipy==1.3.1
six==1.12.0
sklearn==0.0
tensorboard==1.14.0
tensorflow==1.14.0
tensorflow-estimator==1.14.0
termcolor==1.1.0
urllib3==1.25.3
Werkzeug==0.15.5
wrapt==1.11.2

