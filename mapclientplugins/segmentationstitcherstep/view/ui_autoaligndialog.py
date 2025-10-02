# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autoaligndialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QFrame, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_auto_align_dialog(object):
    def setupUi(self, auto_align_dialog):
        if not auto_align_dialog.objectName():
            auto_align_dialog.setObjectName(u"auto_align_dialog")
        auto_align_dialog.resize(398, 209)
        auto_align_dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(auto_align_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.options_frame = QFrame(auto_align_dialog)
        self.options_frame.setObjectName(u"options_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.options_frame.sizePolicy().hasHeightForWidth())
        self.options_frame.setSizePolicy(sizePolicy)
        self.options_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.options_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.options_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.summary_label = QLabel(self.options_frame)
        self.summary_label.setObjectName(u"summary_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.summary_label.sizePolicy().hasHeightForWidth())
        self.summary_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.summary_label)

        self.align_gap_distance_frame = QFrame(self.options_frame)
        self.align_gap_distance_frame.setObjectName(u"align_gap_distance_frame")
        sizePolicy.setHeightForWidth(self.align_gap_distance_frame.sizePolicy().hasHeightForWidth())
        self.align_gap_distance_frame.setSizePolicy(sizePolicy)
        self.align_gap_distance_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.align_gap_distance_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.align_gap_distance_frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.phase_1_align_ends_checkBox = QCheckBox(self.align_gap_distance_frame)
        self.phase_1_align_ends_checkBox.setObjectName(u"phase_1_align_ends_checkBox")
        self.phase_1_align_ends_checkBox.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.phase_1_align_ends_checkBox)

        self.align_gap_distance_label = QLabel(self.align_gap_distance_frame)
        self.align_gap_distance_label.setObjectName(u"align_gap_distance_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.align_gap_distance_label)

        self.align_gap_distance_lineEdit = QLineEdit(self.align_gap_distance_frame)
        self.align_gap_distance_lineEdit.setObjectName(u"align_gap_distance_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.align_gap_distance_lineEdit)


        self.verticalLayout_2.addWidget(self.align_gap_distance_frame)

        self.phase_2_optimize_transformation_checkBox = QCheckBox(self.options_frame)
        self.phase_2_optimize_transformation_checkBox.setObjectName(u"phase_2_optimize_transformation_checkBox")
        self.phase_2_optimize_transformation_checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.phase_2_optimize_transformation_checkBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.options_frame)

        self.buttonBox = QDialogButtonBox(auto_align_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(auto_align_dialog)
        self.buttonBox.accepted.connect(auto_align_dialog.accept)
        self.buttonBox.rejected.connect(auto_align_dialog.reject)

        QMetaObject.connectSlotsByName(auto_align_dialog)
    # setupUi

    def retranslateUi(self, auto_align_dialog):
        auto_align_dialog.setWindowTitle(QCoreApplication.translate("auto_align_dialog", u"Dialog", None))
        self.summary_label.setText(QCoreApplication.translate("auto_align_dialog", u"Summary", None))
#if QT_CONFIG(tooltip)
        self.phase_1_align_ends_checkBox.setToolTip(QCoreApplication.translate("auto_align_dialog", u"<html><head/><body><p>Align mean end centroid and direction to fixed segment with gap distance.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.phase_1_align_ends_checkBox.setText(QCoreApplication.translate("auto_align_dialog", u"Phase 1: Align ends", None))
        self.align_gap_distance_label.setText(QCoreApplication.translate("auto_align_dialog", u"Align gap distance:", None))
#if QT_CONFIG(tooltip)
        self.align_gap_distance_lineEdit.setToolTip(QCoreApplication.translate("auto_align_dialog", u"<html><head/><body><p>Set gap distance to use when aligning ends. Can be negative to force overlap.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.align_gap_distance_lineEdit.setText(QCoreApplication.translate("auto_align_dialog", u"0", None))
#if QT_CONFIG(tooltip)
        self.phase_2_optimize_transformation_checkBox.setToolTip(QCoreApplication.translate("auto_align_dialog", u"<html><head/><body><p>Optimise rotation and translation in plane normal to end direction.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.phase_2_optimize_transformation_checkBox.setText(QCoreApplication.translate("auto_align_dialog", u"Phase 2: Optimize transformation", None))
    # retranslateUi

