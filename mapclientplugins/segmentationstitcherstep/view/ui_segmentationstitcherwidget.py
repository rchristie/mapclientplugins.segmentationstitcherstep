# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'segmentationstitcherwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

from cmlibs.widgets.alignmentsceneviewerwidget import AlignmentSceneviewerWidget

class Ui_SegmentationStitcherWidget(object):
    def setupUi(self, SegmentationStitcherWidget):
        if not SegmentationStitcherWidget.objectName():
            SegmentationStitcherWidget.setObjectName(u"SegmentationStitcherWidget")
        SegmentationStitcherWidget.resize(1137, 878)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SegmentationStitcherWidget.sizePolicy().hasHeightForWidth())
        SegmentationStitcherWidget.setSizePolicy(sizePolicy)
        SegmentationStitcherWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(SegmentationStitcherWidget)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.dockWidget = QDockWidget(SegmentationStitcherWidget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.identifier_label = QLabel(self.dockWidgetContents)
        self.identifier_label.setObjectName(u"identifier_label")
        sizePolicy.setHeightForWidth(self.identifier_label.sizePolicy().hasHeightForWidth())
        self.identifier_label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.identifier_label)

        self.segments_groupBox = QGroupBox(self.dockWidgetContents)
        self.segments_groupBox.setObjectName(u"segments_groupBox")
        sizePolicy.setHeightForWidth(self.segments_groupBox.sizePolicy().hasHeightForWidth())
        self.segments_groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.segments_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.segments_listWidget = QListWidget(self.segments_groupBox)
        self.segments_listWidget.setObjectName(u"segments_listWidget")
        self.segments_listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.verticalLayout_2.addWidget(self.segments_listWidget)

        self.segmentData_groupBox = QGroupBox(self.segments_groupBox)
        self.segmentData_groupBox.setObjectName(u"segmentData_groupBox")
        sizePolicy.setHeightForWidth(self.segmentData_groupBox.sizePolicy().hasHeightForWidth())
        self.segmentData_groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.segmentData_groupBox)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.segmentTransformation_frame = QFrame(self.segmentData_groupBox)
        self.segmentTransformation_frame.setObjectName(u"segmentTransformation_frame")
        self.segmentTransformation_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.segmentTransformation_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.formLayout_6 = QFormLayout(self.segmentTransformation_frame)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setVerticalSpacing(3)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.segmentRotation_label = QLabel(self.segmentTransformation_frame)
        self.segmentRotation_label.setObjectName(u"segmentRotation_label")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.segmentRotation_label)

        self.segmentRotation_lineEdit = QLineEdit(self.segmentTransformation_frame)
        self.segmentRotation_lineEdit.setObjectName(u"segmentRotation_lineEdit")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.segmentRotation_lineEdit)

        self.segmentTranslation_label = QLabel(self.segmentTransformation_frame)
        self.segmentTranslation_label.setObjectName(u"segmentTranslation_label")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.segmentTranslation_label)

        self.segmentTranslation_lineEdit = QLineEdit(self.segmentTransformation_frame)
        self.segmentTranslation_lineEdit.setObjectName(u"segmentTranslation_lineEdit")

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.segmentTranslation_lineEdit)


        self.verticalLayout_3.addWidget(self.segmentTransformation_frame)

        self.segmentIgnoreOrientation_checkBox = QCheckBox(self.segmentData_groupBox)
        self.segmentIgnoreOrientation_checkBox.setObjectName(u"segmentIgnoreOrientation_checkBox")

        self.verticalLayout_3.addWidget(self.segmentIgnoreOrientation_checkBox)


        self.verticalLayout_2.addWidget(self.segmentData_groupBox)


        self.verticalLayout.addWidget(self.segments_groupBox)

        self.connections_groupBox = QGroupBox(self.dockWidgetContents)
        self.connections_groupBox.setObjectName(u"connections_groupBox")
        self.formLayout_3 = QFormLayout(self.connections_groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.connections_listWidget = QListWidget(self.connections_groupBox)
        self.connections_listWidget.setObjectName(u"connections_listWidget")
        self.connections_listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.connections_listWidget)


        self.verticalLayout.addWidget(self.connections_groupBox)

        self.controls_tabWidget = QTabWidget(self.dockWidgetContents)
        self.controls_tabWidget.setObjectName(u"controls_tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.controls_tabWidget.sizePolicy().hasHeightForWidth())
        self.controls_tabWidget.setSizePolicy(sizePolicy2)
        self.display_tab = QWidget()
        self.display_tab.setObjectName(u"display_tab")
        self.verticalLayout_7 = QVBoxLayout(self.display_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.displayMisc_frame = QFrame(self.display_tab)
        self.displayMisc_frame.setObjectName(u"displayMisc_frame")
        self.displayMisc_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.displayMisc_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.displayMisc_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.displayMisc_frame)

        self.displayMarker_frame = QFrame(self.display_tab)
        self.displayMarker_frame.setObjectName(u"displayMarker_frame")
        self.displayMarker_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.displayMarker_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout = QGridLayout(self.displayMarker_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.displayMarkerNames_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayMarkerNames_checkBox.setObjectName(u"displayMarkerNames_checkBox")

        self.gridLayout.addWidget(self.displayMarkerNames_checkBox, 3, 2, 1, 1)

        self.displayMarkerPoints_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayMarkerPoints_checkBox.setObjectName(u"displayMarkerPoints_checkBox")

        self.gridLayout.addWidget(self.displayMarkerPoints_checkBox, 3, 1, 1, 1)

        self.displayAxes_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayAxes_checkBox.setObjectName(u"displayAxes_checkBox")

        self.gridLayout.addWidget(self.displayAxes_checkBox, 3, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.displayMarker_frame)

        self.displayNode_frame = QFrame(self.display_tab)
        self.displayNode_frame.setObjectName(u"displayNode_frame")
        self.displayNode_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.displayNode_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.displayNode_frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.displayNodePoints_checkBox = QCheckBox(self.displayNode_frame)
        self.displayNodePoints_checkBox.setObjectName(u"displayNodePoints_checkBox")

        self.horizontalLayout_12.addWidget(self.displayNodePoints_checkBox)

        self.displayNodeNumbers_checkBox = QCheckBox(self.displayNode_frame)
        self.displayNodeNumbers_checkBox.setObjectName(u"displayNodeNumbers_checkBox")

        self.horizontalLayout_12.addWidget(self.displayNodeNumbers_checkBox)

        self.displayNodePointsScale_frame = QFrame(self.displayNode_frame)
        self.displayNodePointsScale_frame.setObjectName(u"displayNodePointsScale_frame")
        self.displayNodePointsScale_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.displayNodePointsScale_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.displayNodePointsScale_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.displayNodePointsScale_label = QLabel(self.displayNodePointsScale_frame)
        self.displayNodePointsScale_label.setObjectName(u"displayNodePointsScale_label")

        self.horizontalLayout_13.addWidget(self.displayNodePointsScale_label)

        self.displayNodePointsScale_lineEdit = QLineEdit(self.displayNodePointsScale_frame)
        self.displayNodePointsScale_lineEdit.setObjectName(u"displayNodePointsScale_lineEdit")

        self.horizontalLayout_13.addWidget(self.displayNodePointsScale_lineEdit)


        self.horizontalLayout_12.addWidget(self.displayNodePointsScale_frame)


        self.verticalLayout_7.addWidget(self.displayNode_frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.displayNodeGroup_frame = QFrame(self.display_tab)
        self.displayNodeGroup_frame.setObjectName(u"displayNodeGroup_frame")
        self.displayNodeGroup_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.displayNodeGroup_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.formLayout_5 = QFormLayout(self.displayNodeGroup_frame)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.displayNodeGroup_label = QLabel(self.displayNodeGroup_frame)
        self.displayNodeGroup_label.setObjectName(u"displayNodeGroup_label")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.displayNodeGroup_label)

        self.displayNodeGroup_comboBox = QComboBox(self.displayNodeGroup_frame)
        self.displayNodeGroup_comboBox.setObjectName(u"displayNodeGroup_comboBox")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.displayNodeGroup_comboBox)


        self.verticalLayout_7.addWidget(self.displayNodeGroup_frame)

        self.displayLineCategories_groupBox = QGroupBox(self.display_tab)
        self.displayLineCategories_groupBox.setObjectName(u"displayLineCategories_groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.displayLineCategories_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.displayLineGeneral_frame = QFrame(self.displayLineCategories_groupBox)
        self.displayLineGeneral_frame.setObjectName(u"displayLineGeneral_frame")
        self.displayLineGeneral_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.displayLineGeneral_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.displayLineGeneral_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.displayLineGeneral_checkBox = QCheckBox(self.displayLineGeneral_frame)
        self.displayLineGeneral_checkBox.setObjectName(u"displayLineGeneral_checkBox")

        self.horizontalLayout_9.addWidget(self.displayLineGeneral_checkBox)

        self.displayLineGeneralRadius_checkBox = QCheckBox(self.displayLineGeneral_frame)
        self.displayLineGeneralRadius_checkBox.setObjectName(u"displayLineGeneralRadius_checkBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.displayLineGeneralRadius_checkBox.sizePolicy().hasHeightForWidth())
        self.displayLineGeneralRadius_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.displayLineGeneralRadius_checkBox)

        self.displayLineGeneralTrans_checkBox = QCheckBox(self.displayLineGeneral_frame)
        self.displayLineGeneralTrans_checkBox.setObjectName(u"displayLineGeneralTrans_checkBox")

        self.horizontalLayout_9.addWidget(self.displayLineGeneralTrans_checkBox)


        self.verticalLayout_4.addWidget(self.displayLineGeneral_frame)

        self.displayIndepNetworks_frame = QFrame(self.displayLineCategories_groupBox)
        self.displayIndepNetworks_frame.setObjectName(u"displayIndepNetworks_frame")
        self.displayIndepNetworks_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.displayIndepNetworks_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.displayIndepNetworks_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.displayIndepNetworks_checkBox = QCheckBox(self.displayIndepNetworks_frame)
        self.displayIndepNetworks_checkBox.setObjectName(u"displayIndepNetworks_checkBox")

        self.horizontalLayout_10.addWidget(self.displayIndepNetworks_checkBox)

        self.displayIndepNetworksRadius_checkBox = QCheckBox(self.displayIndepNetworks_frame)
        self.displayIndepNetworksRadius_checkBox.setObjectName(u"displayIndepNetworksRadius_checkBox")

        self.horizontalLayout_10.addWidget(self.displayIndepNetworksRadius_checkBox)

        self.displayIndepNetworksTrans_checkBox = QCheckBox(self.displayIndepNetworks_frame)
        self.displayIndepNetworksTrans_checkBox.setObjectName(u"displayIndepNetworksTrans_checkBox")

        self.horizontalLayout_10.addWidget(self.displayIndepNetworksTrans_checkBox)


        self.verticalLayout_4.addWidget(self.displayIndepNetworks_frame)

        self.displayNetworkGroup1_frame = QFrame(self.displayLineCategories_groupBox)
        self.displayNetworkGroup1_frame.setObjectName(u"displayNetworkGroup1_frame")
        self.displayNetworkGroup1_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.displayNetworkGroup1_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.displayNetworkGroup1_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.displayNetworkGroup1_checkBox = QCheckBox(self.displayNetworkGroup1_frame)
        self.displayNetworkGroup1_checkBox.setObjectName(u"displayNetworkGroup1_checkBox")

        self.horizontalLayout_6.addWidget(self.displayNetworkGroup1_checkBox)

        self.displayNetworkGroup1Radius_checkBox = QCheckBox(self.displayNetworkGroup1_frame)
        self.displayNetworkGroup1Radius_checkBox.setObjectName(u"displayNetworkGroup1Radius_checkBox")
        sizePolicy3.setHeightForWidth(self.displayNetworkGroup1Radius_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNetworkGroup1Radius_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.displayNetworkGroup1Radius_checkBox)

        self.displayNetworkGroup1Trans_checkBox = QCheckBox(self.displayNetworkGroup1_frame)
        self.displayNetworkGroup1Trans_checkBox.setObjectName(u"displayNetworkGroup1Trans_checkBox")

        self.horizontalLayout_6.addWidget(self.displayNetworkGroup1Trans_checkBox)


        self.verticalLayout_4.addWidget(self.displayNetworkGroup1_frame)

        self.displayNetworkGroup2_frame = QFrame(self.displayLineCategories_groupBox)
        self.displayNetworkGroup2_frame.setObjectName(u"displayNetworkGroup2_frame")
        self.displayNetworkGroup2_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.displayNetworkGroup2_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.displayNetworkGroup2_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.displayNetworkGroup2_checkBox = QCheckBox(self.displayNetworkGroup2_frame)
        self.displayNetworkGroup2_checkBox.setObjectName(u"displayNetworkGroup2_checkBox")

        self.horizontalLayout_4.addWidget(self.displayNetworkGroup2_checkBox)

        self.displayNetworkGroup2Radius_checkBox = QCheckBox(self.displayNetworkGroup2_frame)
        self.displayNetworkGroup2Radius_checkBox.setObjectName(u"displayNetworkGroup2Radius_checkBox")
        sizePolicy3.setHeightForWidth(self.displayNetworkGroup2Radius_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNetworkGroup2Radius_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.displayNetworkGroup2Radius_checkBox)

        self.displayNetworkGroup2Trans_checkBox = QCheckBox(self.displayNetworkGroup2_frame)
        self.displayNetworkGroup2Trans_checkBox.setObjectName(u"displayNetworkGroup2Trans_checkBox")

        self.horizontalLayout_4.addWidget(self.displayNetworkGroup2Trans_checkBox)


        self.verticalLayout_4.addWidget(self.displayNetworkGroup2_frame)


        self.verticalLayout_7.addWidget(self.displayLineCategories_groupBox)

        self.displayEndPoint_groupBox = QGroupBox(self.display_tab)
        self.displayEndPoint_groupBox.setObjectName(u"displayEndPoint_groupBox")
        self.horizontalLayout_7 = QHBoxLayout(self.displayEndPoint_groupBox)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.displayEndPointBestFitLines_checkBox = QCheckBox(self.displayEndPoint_groupBox)
        self.displayEndPointBestFitLines_checkBox.setObjectName(u"displayEndPointBestFitLines_checkBox")

        self.horizontalLayout_7.addWidget(self.displayEndPointBestFitLines_checkBox)

        self.displayEndPointDirections_checkBox = QCheckBox(self.displayEndPoint_groupBox)
        self.displayEndPointDirections_checkBox.setObjectName(u"displayEndPointDirections_checkBox")
        sizePolicy3.setHeightForWidth(self.displayEndPointDirections_checkBox.sizePolicy().hasHeightForWidth())
        self.displayEndPointDirections_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.displayEndPointDirections_checkBox)

        self.displayEndPointRadius_checkBox = QCheckBox(self.displayEndPoint_groupBox)
        self.displayEndPointRadius_checkBox.setObjectName(u"displayEndPointRadius_checkBox")

        self.horizontalLayout_7.addWidget(self.displayEndPointRadius_checkBox)

        self.displayEndPointTrans_checkBox = QCheckBox(self.displayEndPoint_groupBox)
        self.displayEndPointTrans_checkBox.setObjectName(u"displayEndPointTrans_checkBox")

        self.horizontalLayout_7.addWidget(self.displayEndPointTrans_checkBox)


        self.verticalLayout_7.addWidget(self.displayEndPoint_groupBox)

        self.displayScale_frame = QFrame(self.display_tab)
        self.displayScale_frame.setObjectName(u"displayScale_frame")
        self.displayScale_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.displayScale_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.displayScale_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.displayRadiusScale_label = QLabel(self.displayScale_frame)
        self.displayRadiusScale_label.setObjectName(u"displayRadiusScale_label")

        self.horizontalLayout_3.addWidget(self.displayRadiusScale_label)

        self.displayRadiusScale_lineEdit = QLineEdit(self.displayScale_frame)
        self.displayRadiusScale_lineEdit.setObjectName(u"displayRadiusScale_lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.displayRadiusScale_lineEdit.sizePolicy().hasHeightForWidth())
        self.displayRadiusScale_lineEdit.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.displayRadiusScale_lineEdit)

        self.displayTheme_frame = QFrame(self.displayScale_frame)
        self.displayTheme_frame.setObjectName(u"displayTheme_frame")
        self.displayTheme_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.displayTheme_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.formLayout_4 = QFormLayout(self.displayTheme_frame)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.displayTheme_label = QLabel(self.displayTheme_frame)
        self.displayTheme_label.setObjectName(u"displayTheme_label")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.displayTheme_label)

        self.displayTheme_comboBox = QComboBox(self.displayTheme_frame)
        self.displayTheme_comboBox.addItem("")
        self.displayTheme_comboBox.addItem("")
        self.displayTheme_comboBox.setObjectName(u"displayTheme_comboBox")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.displayTheme_comboBox)


        self.horizontalLayout_3.addWidget(self.displayTheme_frame)


        self.verticalLayout_7.addWidget(self.displayScale_frame)

        self.controls_tabWidget.addTab(self.display_tab, "")
        self.annotations_tab = QWidget()
        self.annotations_tab.setObjectName(u"annotations_tab")
        self.verticalLayout_12 = QVBoxLayout(self.annotations_tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.annotations_group_frame = QFrame(self.annotations_tab)
        self.annotations_group_frame.setObjectName(u"annotations_group_frame")
        self.annotations_group_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.annotations_group_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.annotations_group_frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.annotationName_label = QLabel(self.annotations_group_frame)
        self.annotationName_label.setObjectName(u"annotationName_label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.annotationName_label)

        self.annotationTerm_label = QLabel(self.annotations_group_frame)
        self.annotationTerm_label.setObjectName(u"annotationTerm_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.annotationTerm_label)

        self.annotationTerm_lineEdit = QLineEdit(self.annotations_group_frame)
        self.annotationTerm_lineEdit.setObjectName(u"annotationTerm_lineEdit")
        self.annotationTerm_lineEdit.setEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.annotationTerm_lineEdit)

        self.annotationDimension_label = QLabel(self.annotations_group_frame)
        self.annotationDimension_label.setObjectName(u"annotationDimension_label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.annotationDimension_label)

        self.annotationDimension_lineEdit = QLineEdit(self.annotations_group_frame)
        self.annotationDimension_lineEdit.setObjectName(u"annotationDimension_lineEdit")
        self.annotationDimension_lineEdit.setEnabled(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.annotationDimension_lineEdit)

        self.annotationCategory_label = QLabel(self.annotations_group_frame)
        self.annotationCategory_label.setObjectName(u"annotationCategory_label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.annotationCategory_label)

        self.annotationCategory_comboBox = QComboBox(self.annotations_group_frame)
        self.annotationCategory_comboBox.setObjectName(u"annotationCategory_comboBox")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.annotationCategory_comboBox)

        self.annotationName_comboBox = QComboBox(self.annotations_group_frame)
        self.annotationName_comboBox.setObjectName(u"annotationName_comboBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.annotationName_comboBox)

        self.annotationAlignWeight_label = QLabel(self.annotations_group_frame)
        self.annotationAlignWeight_label.setObjectName(u"annotationAlignWeight_label")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.annotationAlignWeight_label)

        self.annotationAlignWeight_lineEdit = QLineEdit(self.annotations_group_frame)
        self.annotationAlignWeight_lineEdit.setObjectName(u"annotationAlignWeight_lineEdit")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.annotationAlignWeight_lineEdit)

        self.annotiationSetByCategory_checkBox = QCheckBox(self.annotations_group_frame)
        self.annotiationSetByCategory_checkBox.setObjectName(u"annotiationSetByCategory_checkBox")
        self.annotiationSetByCategory_checkBox.setChecked(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.annotiationSetByCategory_checkBox)


        self.verticalLayout_12.addWidget(self.annotations_group_frame)

        self.controls_tabWidget.addTab(self.annotations_tab, "")

        self.verticalLayout.addWidget(self.controls_tabWidget)

        self.bottom_frame = QFrame(self.dockWidgetContents)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.documentation_pushButton = QPushButton(self.bottom_frame)
        self.documentation_pushButton.setObjectName(u"documentation_pushButton")

        self.horizontalLayout_2.addWidget(self.documentation_pushButton)

        self.viewAll_pushButton = QPushButton(self.bottom_frame)
        self.viewAll_pushButton.setObjectName(u"viewAll_pushButton")

        self.horizontalLayout_2.addWidget(self.viewAll_pushButton)

        self.stdViews_pushButton = QPushButton(self.bottom_frame)
        self.stdViews_pushButton.setObjectName(u"stdViews_pushButton")

        self.horizontalLayout_2.addWidget(self.stdViews_pushButton)

        self.save_pushButton = QPushButton(self.bottom_frame)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.horizontalLayout_2.addWidget(self.save_pushButton)

        self.done_pushButton = QPushButton(self.bottom_frame)
        self.done_pushButton.setObjectName(u"done_pushButton")
        sizePolicy3.setHeightForWidth(self.done_pushButton.sizePolicy().hasHeightForWidth())
        self.done_pushButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.done_pushButton)


        self.verticalLayout.addWidget(self.bottom_frame)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.alignmentsceneviewerwidget = AlignmentSceneviewerWidget(SegmentationStitcherWidget)
        self.alignmentsceneviewerwidget.setObjectName(u"alignmentsceneviewerwidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.alignmentsceneviewerwidget.sizePolicy().hasHeightForWidth())
        self.alignmentsceneviewerwidget.setSizePolicy(sizePolicy5)
        self.alignmentsceneviewerwidget.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.alignmentsceneviewerwidget)


        self.retranslateUi(SegmentationStitcherWidget)

        self.controls_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SegmentationStitcherWidget)
    # setupUi

    def retranslateUi(self, SegmentationStitcherWidget):
        SegmentationStitcherWidget.setWindowTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Segmentation Stitcher", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Control Panel", None))
        self.identifier_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Identifier", None))
        self.segments_groupBox.setTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Segments:", None))
#if QT_CONFIG(tooltip)
        self.segments_listWidget.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>Right-click for segments menu</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.segmentData_groupBox.setTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Segment data:", None))
        self.segmentRotation_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Rotation:", None))
#if QT_CONFIG(tooltip)
        self.segmentRotation_lineEdit.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>Euler angle rotations in degrees about z, y', x' for the selected segment above.</p><p>To set interactively: with the mouse pointer in the graphics area, hold down the A-key and left mouse button and drag to rotate the segment about the axis normal to the drag in the window plane. Translation will also be affected.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.segmentTranslation_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Translation:", None))
#if QT_CONFIG(tooltip)
        self.segmentTranslation_lineEdit.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>Translation in x, y, z for the selected segment above.</p><p>To set interactively: with the mouse points in the graphics area, hold down the A-key and middle mouse button and drag to translate.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.segmentIgnoreOrientation_checkBox.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>Tick this if the orientation data for this segment is incorrect. This puts it into the 'orientation ignore' annotation group so later workflow steps can ignore it.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.segmentIgnoreOrientation_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Ignore orientation data", None))
        self.connections_groupBox.setTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Connections:", None))
#if QT_CONFIG(tooltip)
        self.connections_listWidget.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>Right-click for connections menu</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.displayMarkerNames_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Marker names", None))
        self.displayMarkerPoints_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Marker points", None))
        self.displayAxes_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Axes", None))
        self.displayNodePoints_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Node points", None))
        self.displayNodeNumbers_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Node numbers", None))
        self.displayNodePointsScale_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Node scale:", None))
#if QT_CONFIG(tooltip)
        self.displayNodePointsScale_lineEdit.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>Set scale of node point sphere glyphs x 1/100 of mean segment length.</p><p>Value 0.0 sets fixed-size node point glyph.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.displayNodeGroup_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Node group:", None))
        self.displayLineCategories_groupBox.setTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Line Segmentations:", None))
        self.displayLineGeneral_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"General               ", None))
        self.displayLineGeneralRadius_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius", None))
        self.displayLineGeneralTrans_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Trans", None))
        self.displayIndepNetworks_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Indep. networks  ", None))
        self.displayIndepNetworksRadius_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius", None))
        self.displayIndepNetworksTrans_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Trans.", None))
        self.displayNetworkGroup1_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Network group 1", None))
        self.displayNetworkGroup1Radius_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius", None))
        self.displayNetworkGroup1Trans_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Trans.", None))
        self.displayNetworkGroup2_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Network group 2", None))
        self.displayNetworkGroup2Radius_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius", None))
        self.displayNetworkGroup2Trans_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Trans.", None))
        self.displayEndPoint_groupBox.setTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"End Points", None))
        self.displayEndPointBestFitLines_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Lines", None))
        self.displayEndPointDirections_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Tips", None))
        self.displayEndPointRadius_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius", None))
        self.displayEndPointTrans_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Trans.", None))
        self.displayRadiusScale_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius scale:", None))
#if QT_CONFIG(tooltip)
        self.displayRadiusScale_lineEdit.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>Set scale of radius shown e.g. 0.5 shows graphics at half the true radius.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.displayTheme_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Theme:", None))
        self.displayTheme_comboBox.setItemText(0, QCoreApplication.translate("SegmentationStitcherWidget", u"Dark", None))
        self.displayTheme_comboBox.setItemText(1, QCoreApplication.translate("SegmentationStitcherWidget", u"Light", None))

#if QT_CONFIG(tooltip)
        self.displayTheme_comboBox.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>Switch between black/white background theme with other colours changed for contrast.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.controls_tabWidget.setTabText(self.controls_tabWidget.indexOf(self.display_tab), QCoreApplication.translate("SegmentationStitcherWidget", u"Display", None))
        self.annotationName_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Name:", None))
        self.annotationTerm_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Term:", None))
        self.annotationDimension_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Dimension:", None))
        self.annotationCategory_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Category:", None))
#if QT_CONFIG(tooltip)
        self.annotationCategory_comboBox.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>Set the category controlling how features with this annotation term are interpreted:</p><p>* EXCLUDE: exclude from output.</p><p>* GENERAL: include but do not stitch.</p><p>* INDEPENDENT_NETWORK: include and allow stitching with itself only.</p><p>* NETWORK_GROUP_1: include and allow stitching between anything in this group.</p><p>* NETWORK_GROUP_2: include and allow stitching between anything in this group.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.annotationAlignWeight_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Align Weight:", None))
#if QT_CONFIG(tooltip)
        self.annotationAlignWeight_lineEdit.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p><br/>Weight &gt;= 0.0 applied to this annotation/category when optimizing alignment.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.annotiationSetByCategory_checkBox.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>If checked, the values entered in the following are set for all annotations in the current category.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.annotiationSetByCategory_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Set by category:", None))
        self.controls_tabWidget.setTabText(self.controls_tabWidget.indexOf(self.annotations_tab), QCoreApplication.translate("SegmentationStitcherWidget", u"Annotations", None))
        self.documentation_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Online Documentation", None))
        self.viewAll_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"View All", None))
        self.stdViews_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Std. Views", None))
#if QT_CONFIG(tooltip)
        self.save_pushButton.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>Save stitcher and display settings without leaving.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.save_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Save...", None))
        self.done_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Done", None))
    # retranslateUi

