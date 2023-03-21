from Controller import *
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = controller()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
