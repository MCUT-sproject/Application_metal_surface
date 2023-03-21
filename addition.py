import datetime
import os
from PyQt5 import QtWidgets, QtCore, QtGui
import cv2

def select_file(title, dir_path, file_filter):
    """
    Find the file path from the directory computer.

    Args:
        title: the title window of open dialog
        file_filter: determine the specific file want to search
        dir_path: Navigate to specific directory

    return:
        file_path:
    """
    options = QtWidgets.QFileDialog.DontUseNativeDialog
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, title, dir_path,
                                                         file_filter,
                                                         options=options)
    return file_path
