# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'postprocessing_layout.ui'
#
# Created: Fri Mar 10 10:39:40 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_postprocessing(object):
    def setupUi(self, postprocessing):
        postprocessing.setObjectName("postprocessing")
        postprocessing.setWindowModality(QtCore.Qt.NonModal)
        postprocessing.resize(1045, 595)
        self.verticalLayout_3 = QtGui.QVBoxLayout(postprocessing)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtGui.QLabel(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_rect = QtGui.QPushButton(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rect.sizePolicy().hasHeightForWidth())
        self.pushButton_rect.setSizePolicy(sizePolicy)
        self.pushButton_rect.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_rect.setCheckable(True)
        self.pushButton_rect.setObjectName("pushButton_rect")
        self.horizontalLayout_7.addWidget(self.pushButton_rect)
        self.pushButton_poly = QtGui.QPushButton(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_poly.sizePolicy().hasHeightForWidth())
        self.pushButton_poly.setSizePolicy(sizePolicy)
        self.pushButton_poly.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_poly.setCheckable(False)
        self.pushButton_poly.setObjectName("pushButton_poly")
        self.horizontalLayout_7.addWidget(self.pushButton_poly)
        self.pushButton_undo = QtGui.QPushButton(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_undo.sizePolicy().hasHeightForWidth())
        self.pushButton_undo.setSizePolicy(sizePolicy)
        self.pushButton_undo.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_undo.setCheckable(False)
        self.pushButton_undo.setObjectName("pushButton_undo")
        self.horizontalLayout_7.addWidget(self.pushButton_undo)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.line = QtGui.QFrame(postprocessing)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtGui.QLabel(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_plot = QtGui.QPushButton(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_plot.sizePolicy().hasHeightForWidth())
        self.pushButton_plot.setSizePolicy(sizePolicy)
        self.pushButton_plot.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_plot.setCheckable(False)
        self.pushButton_plot.setDefault(False)
        self.pushButton_plot.setFlat(False)
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.horizontalLayout_6.addWidget(self.pushButton_plot)
        self.pushButton_delete = QtGui.QPushButton(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout_6.addWidget(self.pushButton_delete)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtGui.QLabel(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 20))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.max_figures = QtGui.QSpinBox(postprocessing)
        self.max_figures.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.max_figures.setMinimum(2)
        self.max_figures.setMaximum(100)
        self.max_figures.setProperty("value", 20)
        self.max_figures.setObjectName("max_figures")
        self.verticalLayout.addWidget(self.max_figures)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_snr = QtGui.QPushButton(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_snr.sizePolicy().hasHeightForWidth())
        self.pushButton_snr.setSizePolicy(sizePolicy)
        self.pushButton_snr.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_snr.setObjectName("pushButton_snr")
        self.horizontalLayout_5.addWidget(self.pushButton_snr)
        self.pushButton_pe = QtGui.QPushButton(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_pe.sizePolicy().hasHeightForWidth())
        self.pushButton_pe.setSizePolicy(sizePolicy)
        self.pushButton_pe.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_pe.setObjectName("pushButton_pe")
        self.horizontalLayout_5.addWidget(self.pushButton_pe)
        self.pushButton_spe = QtGui.QPushButton(postprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_spe.sizePolicy().hasHeightForWidth())
        self.pushButton_spe.setSizePolicy(sizePolicy)
        self.pushButton_spe.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_spe.setObjectName("pushButton_spe")
        self.horizontalLayout_5.addWidget(self.pushButton_spe)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_plot = QtGui.QVBoxLayout()
        self.verticalLayout_plot.setObjectName("verticalLayout_plot")
        self.verticalLayout_3.addLayout(self.verticalLayout_plot)
        self.buttonBox = QtGui.QDialogButtonBox(postprocessing)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(postprocessing)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), postprocessing.close)
        QtCore.QMetaObject.connectSlotsByName(postprocessing)

    def retranslateUi(self, postprocessing):
        postprocessing.setWindowTitle(QtGui.QApplication.translate("postprocessing", "Plot of all picks", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("postprocessing", "Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_rect.setText(QtGui.QApplication.translate("postprocessing", "Rectangle", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_poly.setText(QtGui.QApplication.translate("postprocessing", "Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_undo.setText(QtGui.QApplication.translate("postprocessing", "Clear selection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("postprocessing", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_plot.setText(QtGui.QApplication.translate("postprocessing", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setText(QtGui.QApplication.translate("postprocessing", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("postprocessing", "Max. Figures:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("postprocessing", "Refresh plot (and color by):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_snr.setText(QtGui.QApplication.translate("postprocessing", "SNR", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_pe.setText(QtGui.QApplication.translate("postprocessing", "PE", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_spe.setText(QtGui.QApplication.translate("postprocessing", "SPE", None, QtGui.QApplication.UnicodeUTF8))

