from MainWindows import Ui_MainWindow
from addition import *
from PyQt5 import QtWidgets
from keras.models import load_model
from sklearn.datasets import load_files
import numpy as np
import cv2
from keras.preprocessing.image import img_to_array, load_img

class controller(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.connect_btn_event()
        self.image = None
        self.width_result_image = 200
        self.model = load_model('model.h5')

    def connect_btn_event(self):
        self.Ui.btn_input.clicked.connect(self.open_image)
        self.Ui.btn_output.clicked.connect(self.predict)

    def open_image(self):
        """
        __doc__
        Open Dialog to search the file image on local directory.
        """
        filename = select_file("Select Image", "../", "Image Files (*.jpeg *.jpg *.png *.gif *.bmg *.bmp)")
        self.image = read_image(filename)
        label_image = self.Ui.input
        image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        label_image.setPixmap(QtGui.QPixmap.fromImage(image))
        cv2.imwrite("/home/aji/Documents/metal surface/Ui/UI_class/Crazing/guest.bmp",self.image)

    def predict(self):
        test_dir = '/home/aji/Documents/metal surface/Ui/UI_class'
        def load_dataset(path):
            data = load_files(path)
            files = np.array(data['filenames'])
            targets = np.array(data['target'])
            target_labels = np.array(data['target_names'])
            return files, targets, target_labels

        x_test, y_test, target_labels = load_dataset(test_dir)

        def convert_image_to_array(files):
            images_as_array = []
            for file in files:
                # Convert to Numpy Array
                images_as_array.append(img_to_array(load_img(file)))
            return images_as_array

        x_test = np.array(convert_image_to_array(x_test))
        # print('Test set shape : ', x_test.shape)
        x_test = x_test.astype('float32') / 255
        y_pred = self.model.predict(x_test)

        for i, idx in enumerate(np.random.choice(x_test.shape[0], size=16)):
            pred_idx = np.argmax(y_pred[idx])
            # true_idx = np.argmax(y_test[idx])

            if str(pred_idx) == "0":
                self.Ui.output.setText("Crazing")
            elif str(pred_idx) == "1":
                self.Ui.output.setText("Inclusion")
            elif str(pred_idx) == "2":
                self.Ui.output.setText("Patches")
            elif str(pred_idx) == "3":
                self.Ui.output.setText("Pitted")
            elif str(pred_idx) == "4":
                self.Ui.output.setText("Rolled")
            elif str(pred_idx) == "5":
                self.Ui.output.setText("Scratches")
            else:
                self.Ui.output.setText("Not Defined")

def read_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("`{}` not cannot be loaded".format(image_path))
    else:
        pass
    return image
