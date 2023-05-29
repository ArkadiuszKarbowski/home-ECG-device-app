########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################
"""
READ ME:
I made an extension of the QPushButton class to help make button
customization a animation easier
The QPushButton custom class is in custom_buttons.py, you can go
through it but only change it if youre sure of what youre doing

You can fully customize the buttons in the UI through the button_theme.json file.

Before you get started, please ensure that you fully understand 
the ICONIFY library, you can watch this video https://youtu.be/y9qQXn836K0 to help you understand.
These are the json keys supported(Please check the examples provided in the button_theme.json file)


name (the name of the button)
theme (theme number from 1 to 13)
customTheme (pass in your custom theme colors -color1 and color2- if the like the look of the available themes)
animateOn (the event that will trigger the button animation- hover or click- event)
animation (the part of the butttom you want to animate - border, background or both)
animationDuration (the time your animation should take playing)
animationEasingCurve (the easing curve for the anomation, google QT animation easing curve)
fallBackStyle (the style that should be applied to the button once the animation is done playing)
defaultStyle (the style that will be applied alongside the animation style)
iconify (pass in the iconify icon style:  
    name = name of the icon
    color = color of the icon
    size = size of the icon
    animateOn = event that should trigger icon animation (hover, click or all)
)

If no JSon value was passed for a particular button, the default stylesheet will be applied the button.

CHECK THE FOR-LOOP BELOW ON MAINWINDOW CLASS ON HOW TO APPLY STYLE FROM JSON FILE



You can also customize the buttons from inside your mainwindow class using the folowing statements:

Set theme
button.setObjectTheme(themeNumber)
Set custom theme
button.setObjectCustomTheme(color, color)
Set animation trigger event
button.setObjectAnimateOn("click" or "hover")
Pass the style that should be applied to the button once the animation is over
button.setObjectFallBackStyle(Stylesheet)
Set the style sheet that will be applied alongside the animation style and fallBack style
button.setObjectDefaultStyle(Stylesheet)
Set the animation easing curve
button._animation.setEasingCurve(QtCore easing curve)

IMPORTANT
If you need to apply the theme to the UI file generated by QT Designer, you should also import the custom_buttons to the UI, check ui_interface.py

Applying Iconfy from json is currently unstable, if you face problems then try applying the icons from within your py files 

"""
########################################################################
## IMPORTS
########################################################################
import sys
import iconify as ico
from iconify.qt import QtGui, QtWidgets, QtCore
from PySide2.QtCore import *

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT CUSTOM BUTTONS FILE
from custom_buttons import *
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()

        ######################################################################
        ## APPLY STYLE FROM JSON FILE
        ########################################################################
        # loadJsonStyle(self.ui.pushButton_2)
        for w in self.ui.widget.findChildren(QPushButton):
            # print(w.objectName())
            # load the stylesheet for button w from the json file
            loadJsonStyle(w)
            # check if the stylesheet was found 
            # if no style was found, apply the default style from the animation theme
            # if not w.wasThemed:
                # w is the button
                # 9 is the theme
                # applyAnimationThemeStyle(w, 2)
                # OR
                # Appply your own custom theme
                # applyCustomAnimationThemeStyle(w, "red", "yellow")
                # print(w)


        # Create new button
        # button = QPushButton("name")
        # button.setText("Login")
        # button.setObjectTheme(2)
        # self.ui.gridLayout.addWidget(button, 2, 1, 1, 1)

        # UNCOMMENT THE STATEMENTS NELOW TO SEE THEIR EFFECTS
        # self.ui.pushButton.setObjectTheme(1)
        # self.ui.pushButton_2.setObjectTheme(2)
        # self.ui.pushButton_3.setObjectTheme(3)
        # self.ui.pushButton_4.setObjectTheme(4)
        # self.ui.pushButton_5.setObjectTheme(5)
        # self.ui.pushButton_6.setObjectTheme(6)
        # self.ui.pushButton_7.setObjectTheme(11)
        # self.ui.pushButton_5.setObjectTheme(10)
        # self.ui.pushButton.setObjectCustomTheme("#fff", "#000")
        # self.ui.pushButton.setObjectAnimateOn("hover")
        # self.ui.pushButton_7.setObjectAnimateOn("click")
        # self.ui.pushButton._animation.setEasingCurve(QtCore.QEasingCurve.InOutElastic)

        # STYLE APPLIED AFTER THE ANIMATION IS COMPLETE
        # self.ui.pushButton.setObjectFallBackStyle("""
        # border-style: solid;
        # border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #FF4200, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);
        # border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #FF4200, stop:0.5 #FF4200, stop:0.6 #C0DB50, stop:1 #C0DB50);
        # border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF4200, stop:0.3 #FF4200, stop:0.7 #100E19, stop:1 #100E19);
        # border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);
        # border-width: 5px;
        # border-radius: 1px;
        # color: #d3dae3;
        # padding: 2px;
        # background-color: #100E19;
        # """)  

        # STYLE APPLIED ALONSIDE ANIMATION THEME STYLE AND FALLBACK STYLE
        # self.ui.pushButton.setObjectDefaultStyle(
        #     """
        #         border-radius:5px;
        #         border-width: 10px;
        #         color: #d3dae3;
        #         padding: 5px;
        #     """)   

        # Apply button icon
        # iconify(
            # self.ui.pushButton, 
            # icon = "font-awesome:solid:cloud-download-alt", 
            # color = "orange", 
            # size = 64, 
            # animation = "spin", 
            # animateOn = "click"
            # )

        # applyButtonShadow(
        #     self.ui.pushButton_4, 
        #     color= "#fff", 
        #     applyShadowOn= "hover", 
        #     animateShadow = True, 
        #     blurRadius = 100, 
        #     animateShadowDuration = 500,
        #     xOffset = 0,
        #     yOffset = 0
        #     )



########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  