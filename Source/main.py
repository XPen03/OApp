import utils
import mouth_detection
import os

known_names, known_faces_encoding = utils.create_database('../Images/database/group3')

unknown_names, unknown_faces_encoding = utils.create_database('../Images/test_face/group4')

known_names.append('unknown')

index = [utils.recognize_face(unknown_face_encoding, known_faces_encoding) for unknown_face_encoding in unknown_faces_encoding]

names = [known_names[i] for i in index]

print((utils.compare_result(unknown_names[0],names[0])))

if utils.compare_result(unknown_names[0],names[0]):
    filepath = '../Images/test_mouth/'
    predictor_path = './shape_predictor_68_face_landmarks.dat'

    paths = utils.load_paths(filepath)
    image_paths = [os.path.join(filepath,f) for f in paths]
    #for image_path in image_paths:
    for i in range(len(image_paths)):
        image_path = image_paths[i]
        image_name = paths[i]
        mouth_detection.mouth_location(image_path,image_name, predictor_path)

# to save the mouth part of a person in a certain file
#save_path = '../Images/save_path/'
#save_name = 'xxx.jpg'
#image_path = os.path.join(save_path,save_name)

