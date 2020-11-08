
def collect_data():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import cv2
    from PIL import Image
    import PIL
    import os
    import shutil
    import datetime
    import time
    from threading import Thread
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(
        './haarcascade_frontalface_default.xml')
    count = 0
    name = input("enter name of person")
    Id = input(" enter unique id (aadhar card) ")
    Email_id = input("enter Email_id ")
    Phone_no=input("enter your phone number: ")
    from add_details_incsv import add_details
    # order add_details(Name,unique_id,email_id,phone_no)
    add_details(str(name),str(Id),str(Email_id),str(Phone_no))

    while(True):
        ret, frame = cap.read()
        if(ret == False):
            continue
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (51, 255, 51), 3)
            count += 1
            img_name_path = Id + '.' + str(count) + ".jpg"
            offset = 10
            if(count % 50 == 0):
                print(img_name_path)
            saving_image = gray[x:x+w, y:y+h]

            plt.imsave(img_name_path, gray[y:y+h, x:x+w], cmap='gray')
#            status=cv2.imwrite(img_name_path, saving_image, [cv2.IMWRITE_JPEG_QUALITY, 100])
            dest = './data_images'
            shutil.move(img_name_path, dest)

            cv2.imshow("frame", frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif(count > 200):
            break

    cap.release()
    cv2.destroyAllWindows()


def capture_data_details():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import cv2
    from PIL import Image
    import PIL
    import os
    import shutil
    import datetime
    import time
    from threading import Thread
    faces = []
    Ids = []
    for one in os.listdir('data_images'):
        new_path = os.path.join('data_images', one)
        img = Image.open(new_path).convert('L')
        img = np.array(img, 'uint8')
        curr_id = int(one.split('.')[0])
        Ids.append(curr_id)
        faces.append(img)
    return faces, Ids


def train_data():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import cv2
    from PIL import Image
    import PIL
    import os
    import shutil
    import datetime
    import time
    from threading import Thread
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    cap = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    face, Ids = capture_data_details()
    recognizer.train(face, np.array(Ids))
    try:
        recognizer.save("trained_model.yml")
        print("model trained successfully!")
    except:
        print("unable to train model")


def add_new_person():
    collect_data()
    print("collect data successfullt")
    print("model training start...")
    train_data()


add_new_person()
