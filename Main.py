# Import the library
import face_recognition
import os
import numpy as np
from PIL import Image, ImageDraw
from IPython.display import display
import re

# Declare all the list
known_face_encodings = []
known_face_names = []
known_faces_filenames = []

# Walk in the folder to add every file name to known_faces_filenames
for (dirpath, dirnames, filenames) in os.walk('assets/img/users/bright/'):
    known_faces_filenames.extend(filenames)
    break

# Walk in the folder
for filename in known_faces_filenames:
    # Load each file
    face = face_recognition.load_image_file('assets/img/users/' + filename)
    # Extract the name of each employee and add it to known_face_names
    known_face_names.append(re.sub("[0-100]",'', filename[:-4]))
    # Encode de face of every employee
    known_face_encodings.append(face_recognition.face_encodings(face)[0])

print(known_face_names)

# Load an image with an unknown face
unknown_image = face_recognition.load_image_file("assets/img/test/test3.jpg")

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

print('Learned encoding for', len(known_face_encodings), 'images.')

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

collectname = []

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    # Or instead, use the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
    print(name)
    collectname.append(name)

# Remove the drawing library from memory as per the Pillow docs
del draw

print ('have',len(collectname),'people in this images.')

# Display the resulting image
display(pil_image)
