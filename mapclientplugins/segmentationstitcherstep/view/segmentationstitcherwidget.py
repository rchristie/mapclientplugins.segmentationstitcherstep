"""
Dialog/UI for interacting with SegmentationStitcherModel.
"""
import webbrowser

from PySide6 import QtCore, QtWidgets

from cmlibs.maths.vectorops import dot, magnitude, mult, normalize, sub
from cmlibs.widgets.utils import parse_real_non_negative, parse_vector

from mapclientplugins.segmentationstitcherstep.view.autoaligndialog import AutoAlignDialog
from mapclientplugins.segmentationstitcherstep.view.newconnectiondialog import NewConnectionDialog
from mapclientplugins.segmentationstitcherstep.view.ui_segmentationstitcherwidget import Ui_SegmentationStitcherWidget
from segmentationstitcher.annotation import AnnotationCategory


class SegmentationStitcherWidget(QtWidgets.QWidget):

    def __init__(self, model, parent=None):
        super(SegmentationStitcherWidget, self).__init__(parent)
        self._ui = Ui_SegmentationStitcherWidget()
        self._ui.setupUi(self)
        self._model = model
        self._ui.alignmentsceneviewerwidget.setContext(model.get_context())
        self._ui.alignmentsceneviewerwidget.setModel(model)
        # self._model.registerTransformationChangeCallback(self._transformationChanged)
        self._done_callback = None
        self._build_segments_list()
        self._build_annotationName_comboBox()
        self._build_annotationCategory_comboBox()
        self._build_connections_list()
        self._make_connections()
        self._refresh_options()
        self._model.set_segment_data_change_callback(self._segment_data_changed)

    def _segment_data_changed(self, segment):
        if segment == self._model.get_current_segment():
            self._refresh_segment_data()

    def _graphics_initialized(self):
        """
        Callback for when SceneviewerWidget is initialised.
        Set custom scene from model.
        """
        sceneviewer = self._ui.alignmentsceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            scene = self._model.get_root_region().getScene()
            self._ui.alignmentsceneviewerwidget.setScene(scene)
            self._set_display_theme_background()
            # self._ui.alignmentsceneviewerwidget.setSelectModeAll()
            sceneviewer.setLookatParametersNonSkew([2.0, -2.0, 1.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0])
            sceneviewer.setTransparencyMode(sceneviewer.TRANSPARENCY_MODE_SLOW)
            self._viewAll_buttonClicked()

    def _set_display_theme_background(self):
        sceneviewer = self._ui.alignmentsceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            theme_name = self._model.get_display_theme()
            background_colour_rgb = [1.0, 1.0, 1.0] if (theme_name == 'Light') else [0.0, 0.0, 0.0]
            sceneviewer.setBackgroundColourRGB(background_colour_rgb)

    def _transformation_changed(self):
        # self._ui.segmentRotation_lineEdit.setText(self._model.getRotationText())
        # self._ui.segmentTranslation_lineEdit.setText(self._model.getTranslationText())
        pass

    def _make_connections(self):
        self._ui.alignmentsceneviewerwidget.graphicsInitialized.connect(self._graphics_initialized)
        self._ui.documentation_pushButton.clicked.connect(self._documentation_buttonClicked)
        self._ui.done_pushButton.clicked.connect(self._done_buttonClicked)
        self._ui.save_pushButton.clicked.connect(self._save_buttonClicked)
        self._ui.stdViews_pushButton.clicked.connect(self._stdViews_buttonClicked)
        self._ui.viewAll_pushButton.clicked.connect(self._viewAll_buttonClicked)
        self._ui.segments_listWidget.customContextMenuRequested.connect(self._segments_listWidget_contextMenu)
        self._ui.segmentRotation_lineEdit.editingFinished.connect(self._segmentRotation_lineEditChanged)
        self._ui.segmentTranslation_lineEdit.editingFinished.connect(self._segmentTranslation_lineEditChanged)

        self._ui.connections_listWidget.customContextMenuRequested.connect(self._connections_listWidget_contextMenu)

        self._ui.displayAxes_checkBox.clicked.connect(self._displayAxes_clicked)
        self._ui.displayMarkerPoints_checkBox.clicked.connect(self._displayMarkerPoints_clicked)
        self._ui.displayMarkerNames_checkBox.clicked.connect(self._displayMarkerNames_clicked)
        self._ui.displayNodePoints_checkBox.clicked.connect(self._displayNodePoints_clicked)
        self._ui.displayNodeNumbers_checkBox.clicked.connect(self._displayNodeNumbers_clicked)
        self._ui.displayNodePointsScale_lineEdit.editingFinished.connect(self._displayNodePointsScale_entered)
        self._ui.displayNodeGroup_comboBox.currentIndexChanged.connect(self._displayNodeGroupChanged)

        self._ui.displayLineGeneral_checkBox.clicked.connect(self._displayLineGeneral_clicked)
        self._ui.displayLineGeneralRadius_checkBox.clicked.connect(self._displayLineGeneralRadius_clicked)
        self._ui.displayLineGeneralTrans_checkBox.clicked.connect(self._displayLineGeneralTrans_clicked)
        self._ui.displayIndepNetworks_checkBox.clicked.connect(self._displayIndepNetworks_clicked)
        self._ui.displayIndepNetworksRadius_checkBox.clicked.connect(self._displayIndepNetworksRadius_clicked)
        self._ui.displayIndepNetworksTrans_checkBox.clicked.connect(self._displayIndepNetworksTrans_clicked)
        self._ui.displayNetworkGroup1_checkBox.clicked.connect(self._displayNetworkGroup1_clicked)
        self._ui.displayNetworkGroup1Radius_checkBox.clicked.connect(self._displayNetworkGroup1Radius_clicked)
        self._ui.displayNetworkGroup1Trans_checkBox.clicked.connect(self._displayNetworkGroup1Trans_clicked)
        self._ui.displayNetworkGroup2_checkBox.clicked.connect(self._displayNetworkGroup2_clicked)
        self._ui.displayNetworkGroup2Radius_checkBox.clicked.connect(self._displayNetworkGroup2Radius_clicked)
        self._ui.displayNetworkGroup2Trans_checkBox.clicked.connect(self._displayNetworkGroup2Trans_clicked)

        self._ui.displayEndPointDirections_checkBox.clicked.connect(self._displayEndPointDirections_clicked)
        self._ui.displayEndPointBestFitLines_checkBox.clicked.connect(self._displayEndPointBestFitLines_clicked)
        self._ui.displayEndPointRadius_checkBox.clicked.connect(self._displayEndPointRadius_clicked)
        self._ui.displayEndPointTrans_checkBox.clicked.connect(self._displayEndPointTrans_clicked)
        self._ui.displayRadiusScale_lineEdit.editingFinished.connect(self._displayRadiusScale_entered)
        self._ui.displayTheme_comboBox.currentIndexChanged.connect(self._display_theme_changed)

        self._ui.annotationName_comboBox.currentIndexChanged.connect(self._annotationName_changed)
        self._ui.annotationCategory_comboBox.currentIndexChanged.connect(self._annotationCategory_changed)
        self._ui.annotationAlignWeight_lineEdit.editingFinished.connect(self._annotationAlignWeight_entered)

    def _set_combo_box_items(self, combo_box, names, current_name):
        """
        Set list of all names and currently selected name in combo box.
        :param combo_box: QComboBox
        :param names: List of all valid names of which 0 index is the default/None text.
        :param current_name: Name in combo box tests or None for first/default item.
        """
        combo_box.blockSignals(True)
        combo_box.addItems(names)
        if current_name:
            index = combo_box.findText(current_name)
        else:
            index = 0
        combo_box.setCurrentIndex(index)
        combo_box.blockSignals(False)

    def _refresh_options(self):
        self._ui.identifier_label.setText('Identifier:  ' + self._model.get_step_identifier())
        self._ui.displayAxes_checkBox.setChecked(self._model.is_display_axes())
        self._ui.displayMarkerPoints_checkBox.setChecked(self._model.is_display_marker_points())
        self._ui.displayMarkerNames_checkBox.setChecked(self._model.is_display_marker_names())
        self._ui.displayNodePoints_checkBox.setChecked(self._model.is_display_node_points())
        self._ui.displayNodeNumbers_checkBox.setChecked(self._model.is_display_node_numbers())
        self._refresh_node_points_scale()
        group_names = self._model.get_raw_group_names()
        self._set_combo_box_items(
            self._ui.displayNodeGroup_comboBox, ["<all>"] + group_names, self._model.get_display_node_group_name())

        self._ui.displayLineGeneral_checkBox.setChecked(self._model.is_display_line_general())
        self._ui.displayLineGeneralRadius_checkBox.setChecked(self._model.is_display_line_general_radius())
        self._ui.displayLineGeneralTrans_checkBox.setChecked(self._model.is_display_line_general_trans())
        self._ui.displayIndepNetworks_checkBox.setChecked(self._model.is_display_line_independent_network())
        self._ui.displayIndepNetworksRadius_checkBox.setChecked(
            self._model.is_display_line_independent_network_radius())
        self._ui.displayIndepNetworksTrans_checkBox.setChecked(self._model.is_display_line_independent_network_trans())
        self._ui.displayNetworkGroup1_checkBox.setChecked(self._model.is_display_line_network_group_1())
        self._ui.displayNetworkGroup1Radius_checkBox.setChecked(self._model.is_display_line_network_group_1_radius())
        self._ui.displayNetworkGroup1Trans_checkBox.setChecked(self._model.is_display_line_network_group_1_trans())
        self._ui.displayNetworkGroup2_checkBox.setChecked(self._model.is_display_line_network_group_2())
        self._ui.displayNetworkGroup2Radius_checkBox.setChecked(self._model.is_display_line_network_group_2_radius())
        self._ui.displayNetworkGroup2Trans_checkBox.setChecked(self._model.is_display_line_network_group_2_trans())

        self._refresh_radius_scale()
        self._ui.displayEndPointDirections_checkBox.setChecked(self._model.is_display_end_point_directions())
        self._ui.displayEndPointBestFitLines_checkBox.setChecked(self._model.is_display_end_point_best_fit_lines())
        self._ui.displayEndPointRadius_checkBox.setChecked(self._model.is_display_end_point_radius())
        self._ui.displayEndPointTrans_checkBox.setChecked(self._model.is_display_end_point_trans())
        index = self._ui.displayTheme_comboBox.findText(self._model.get_display_theme())
        self._ui.displayTheme_comboBox.blockSignals(True)
        self._ui.displayTheme_comboBox.setCurrentIndex(index)
        self._ui.displayTheme_comboBox.blockSignals(False)

        self._refresh_segment_data()
        self._refresh_current_annotation_settings()
        self._ui.done_pushButton.setEnabled(True)

    @staticmethod
    def _refresh_comboBox_names(comboBox, names, current_name):
        comboBox.blockSignals(True)
        comboBox.clear()
        current_index = 0
        index = 0
        for name in names:
            comboBox.addItem(name)
            if name == current_name:
                current_index = index
            index += 1
        comboBox.setCurrentIndex(current_index)
        comboBox.blockSignals(False)

    @staticmethod
    def _select_comboBox_item(comboBox, names, current_name):
        """
        Don't build combobox, just show the current annotation or None.
        :param comboBox:
        :param names: List of all valid names, optionally including '-' for None.
        :param current_name: Item name, including '-' for None if allowed.
        """
        current_index = names.index(current_name)
        comboBox.setCurrentIndex(current_index)

    def _build_annotationName_comboBox(self):
        annotations = self._model.get_stitcher().get_annotations()
        current_annotation = self._model.get_current_annotation()
        self._refresh_comboBox_names(
            self._ui.annotationName_comboBox,
            ['-'] + [annotation.get_name() for annotation in annotations],
            current_annotation.get_name() if current_annotation else '-')

    def _select_current_annotation(self):
        annotations = self._model.get_stitcher().get_annotations()
        names = ['-'] + [annotation.get_name() for annotation in annotations]
        current_annotation = self._model.get_current_annotation()
        self._select_comboBox_item(
            self._ui.annotationName_comboBox, names, current_annotation.get_name() if current_annotation else '-')

    def _build_annotationCategory_comboBox(self):
        self._refresh_comboBox_names(
            self._ui.annotationCategory_comboBox,
            [category.name for category in AnnotationCategory],
            AnnotationCategory.EXCLUDE.name)

    def _refresh_current_annotation_settings(self):
        """
        Display current annotation settings.
        """
        current_annotation = self._model.get_current_annotation()
        enabled = current_annotation is not None
        self._ui.annotationName_comboBox.setEnabled(True)
        self._ui.annotationTerm_lineEdit.setText(
            current_annotation.get_term() if current_annotation else '')
        self._ui.annotationTerm_lineEdit.setEnabled(enabled)
        self._ui.annotationDimension_lineEdit.setText(
            str(current_annotation.get_dimension()) if current_annotation else '')
        self._ui.annotationDimension_lineEdit.setEnabled(enabled)
        if current_annotation:
            names = [category.name for category in AnnotationCategory]
            self._select_comboBox_item(
                self._ui.annotationCategory_comboBox, names, current_annotation.get_category().name)
            index = 0
            current_category_name = current_annotation.get_category().name
            for category in AnnotationCategory:
                if category.name == current_category_name:
                    self._ui.annotationCategory_comboBox.setCurrentIndex(index)
                index += 1
        self._ui.annotationCategory_comboBox.setEnabled(enabled)
        realFormat = "{:.4g}"
        self._ui.annotationAlignWeight_lineEdit.setText(
            realFormat.format(current_annotation.get_align_weight()) if current_annotation else "")

    def _annotationName_changed(self, index):
        annotation_name = self._ui.annotationName_comboBox.itemText(index)
        self._model.set_current_annotation_by_name(annotation_name)
        self._refresh_current_annotation_settings()

    def _annotationCategory_changed(self, index):
        annotation_category_name = self._ui.annotationCategory_comboBox.itemText(index)
        self._model.set_current_annotation_category_by_name(annotation_category_name)

    def _annotationAlignWeight_entered(self):
        align_weight = parse_real_non_negative(self._ui.annotationAlignWeight_lineEdit)
        if align_weight >= 0.0:
            set_by_category = self._ui.annotiationSetByCategory_checkBox.isChecked()
            self._model.set_current_annotation_align_weight(align_weight, set_by_category)
        self._refresh_current_annotation_settings()

    def get_model(self):
        return self._model

    def _documentation_buttonClicked(self):
        webbrowser.open("https://abi-mapping-tools.readthedocs.io/en/latest/mapclientplugins.segmentationstitcherstep/docs/index.html")

    def register_done_callback(self, done_callback):
        self._done_callback = done_callback

    def _done_buttonClicked(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self._ui.dockWidget.setFloating(False)
        self._model.done()
        self._model = None
        self._done_callback()
        QtWidgets.QApplication.restoreOverrideCursor()

    def _save_buttonClicked(self):
        # Create a QMessageBox instance
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Save settings confirmation")
        msg_box.setText("Save/overwrite settings?")
        msg_box.setIcon(QtWidgets.QMessageBox.Question)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
        ret = msg_box.exec()
        if ret == QtWidgets.QMessageBox.Yes:
            self._model.save()

    def _stdViews_buttonClicked(self):
        sceneviewer = self._ui.alignmentsceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            result, eyePosition, lookatPosition, upVector = sceneviewer.getLookatParameters()
            upVector = normalize(upVector)
            viewVector = sub(lookatPosition, eyePosition)
            viewDistance = magnitude(viewVector)
            viewVector = normalize(viewVector)
            # viewX = dot(viewVector, [1.0, 0.0, 0.0])
            viewY = dot(viewVector, [0.0, 1.0, 0.0])
            viewZ = dot(viewVector, [0.0, 0.0, 1.0])
            # upX = dot(upVector, [1.0, 0.0, 0.0])
            upY = dot(upVector, [0.0, 1.0, 0.0])
            upZ = dot(upVector, [0.0, 0.0, 1.0])
            if (viewZ < -0.999) and (upY > 0.999):
                # XY -> XZ
                viewVector = [0.0, 1.0, 0.0]
                upVector = [0.0, 0.0, 1.0]
            elif (viewY > 0.999) and (upZ > 0.999):
                # XZ -> YZ
                viewVector = [-1.0, 0.0, 0.0]
                upVector = [0.0, 0.0, 1.0]
            else:
                # XY
                viewVector = [0.0, 0.0, -1.0]
                upVector = [0.0, 1.0, 0.0]
            eyePosition = sub(lookatPosition, mult(viewVector, viewDistance))
            sceneviewer.setLookatParametersNonSkew(eyePosition, lookatPosition, upVector)

    def _viewAll_buttonClicked(self):
        if self._ui.alignmentsceneviewerwidget.getSceneviewer() is not None:
            self._ui.alignmentsceneviewerwidget.viewAll()

    def _build_segments_list(self):
        """
        Fill the segments list including visibility check boxes.
        """
        if self._ui.segments_listWidget is not None:
            self._ui.segments_listWidget.clear()
        stitcher = self._model.get_stitcher()
        segments = stitcher.get_segments()
        for segment in segments:
            name = segment.get_name()
            item = QtWidgets.QListWidgetItem(name)
            item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
            visible = segment.get_base_region().getScene().getVisibilityFlag()
            item.setCheckState(QtCore.Qt.CheckState.Checked if visible else QtCore.Qt.CheckState.Unchecked)
            self._ui.segments_listWidget.addItem(item)
            if segment == self._model.get_current_segment():
                self._ui.segments_listWidget.setCurrentItem(item)
        self._ui.segments_listWidget.itemClicked.connect(self._segments_list_itemClicked)
        self._ui.segments_listWidget.show()

    def _segments_list_itemClicked(self, item):
        """
        Either changes visibility flag or selects current segment.
        """
        clicked_index = self._ui.segments_listWidget.row(item)
        stitcher = self._model.get_stitcher()
        segments = stitcher.get_segments()
        segment = segments[clicked_index]
        visible = item.checkState() == QtCore.Qt.CheckState.Checked
        segment.get_base_region().getScene().setVisibilityFlag(visible)
        selected_modelIndex = self._ui.segments_listWidget.currentIndex()
        if clicked_index == selected_modelIndex.row():
            self._model.set_current_segment(segment)
            self._refresh_segment_data()

    def _refresh_segment_data(self):
        segment = self._model.get_current_segment()
        realFormat = "{:.7g}"
        rotation = segment.get_rotation_degrees()
        self._ui.segmentRotation_lineEdit.setText(", ".join(realFormat.format(value) for value in rotation))
        translation = segment.get_translation()
        self._ui.segmentTranslation_lineEdit.setText(", ".join(realFormat.format(value) for value in translation))

    def _segments_listWidget_set_all_visibility(self, visible):
        stitcher = self._model.get_stitcher()
        segments = stitcher.get_segments()
        for i, segment in enumerate(segments):
            segment.get_base_region().getScene().setVisibilityFlag(visible)
            item = self._ui.segments_listWidget.item(i)
            item.setCheckState(QtCore.Qt.CheckState.Checked if visible else QtCore.Qt.CheckState.Unchecked)

    def _segments_listWidget_look_at_segment(self):
        selected_item = self._ui.segments_listWidget.currentItem()
        if selected_item:
            clicked_index = self._ui.segments_listWidget.row(selected_item)
            stitcher = self._model.get_stitcher()
            segments = stitcher.get_segments()
            segment = segments[clicked_index]
            lookat_point = segment.transform_coordinates(segment.get_coordinates_midpoint())
            sceneviewer = self._ui.alignmentsceneviewerwidget.getSceneviewer()
            sceneviewer.setLookatParametersNonSkew(
                sceneviewer.getEyePosition()[1], lookat_point, sceneviewer.getUpVector()[1])
            selected_item.setCheckState(QtCore.Qt.CheckState.Checked)
            self._segments_list_itemClicked(selected_item)

    def _segments_listWidget_contextMenu(self, pos):
        menu = QtWidgets.QMenu(self._ui.segments_listWidget)
        action_hide_all = menu.addAction("Hide all")
        action_show_all = menu.addAction("Show all")
        action_look_at = menu.addAction("Look at segment")
        action_hide_all.triggered.connect(lambda: self._segments_listWidget_set_all_visibility(False))
        action_show_all.triggered.connect(lambda: self._segments_listWidget_set_all_visibility(True))
        action_look_at.triggered.connect(self._segments_listWidget_look_at_segment)
        # Display the menu at the global position of the mouse click
        menu.exec(self._ui.segments_listWidget.mapToGlobal(pos))

    def _segmentRotation_lineEditChanged(self):
        segment = self._model.get_current_segment()
        rotation = parse_vector(self._ui.segmentRotation_lineEdit)
        if rotation:
            while len(rotation) < 3:
                rotation.append(0.0)
            if len(rotation) > 3:
                rotation = rotation[:3]
            self._model.set_segment_rotation_degrees(segment, rotation)
        else:
            self._refresh_segment_data()

    def _segmentTranslation_lineEditChanged(self):
        segment = self._model.get_current_segment()
        translation = parse_vector(self._ui.segmentTranslation_lineEdit)
        if translation:
            while len(translation) < 3:
                translation.append(0.0)
            if len(translation) > 3:
                translation = translation[:3]
            self._model.set_segment_translation(segment, translation)
        else:
            self._refresh_segment_data()

    def _build_connections_list(self):
        """
        Fill the connections list including visibility check boxes.
        """
        if self._ui.connections_listWidget is not None:
            self._ui.connections_listWidget.clear()
        stitcher = self._model.get_stitcher()
        connections = stitcher.get_connections()
        for connection in connections:
            name = connection.get_name()
            item = QtWidgets.QListWidgetItem(name)
            item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
            visible = connection.get_region().getScene().getVisibilityFlag()
            item.setCheckState(QtCore.Qt.CheckState.Checked if visible else QtCore.Qt.CheckState.Unchecked)
            self._ui.connections_listWidget.addItem(item)
            if connection == self._model.get_current_connection():
                self._ui.connections_listWidget.setCurrentItem(item)
        self._ui.connections_listWidget.itemClicked.connect(self._connections_list_itemClicked)
        self._ui.connections_listWidget.show()

    def _connections_list_itemClicked(self, item):
        """
        Either changes visibility flag or selects current connection.
        """
        clicked_index = self._ui.connections_listWidget.row(item)
        stitcher = self._model.get_stitcher()
        connections = stitcher.get_connections()
        connection = connections[clicked_index]
        visible = item.checkState() == QtCore.Qt.CheckState.Checked
        connection.get_region().getScene().setVisibilityFlag(visible)
        selected_modelIndex = self._ui.connections_listWidget.currentIndex()
        if clicked_index == selected_modelIndex.row():
            self._model.set_current_connection(connection)

    def _connections_listWidget_set_all_visibility(self, visible):
        stitcher = self._model.get_stitcher()
        connections = stitcher.get_connections()
        for i, connection in enumerate(connections):
            connection.get_region().getScene().setVisibilityFlag(visible)
            item = self._ui.connections_listWidget.item(i)
            item.setCheckState(QtCore.Qt.CheckState.Checked if visible else QtCore.Qt.CheckState.Unchecked)

    def _connections_listWidget_look_at_connection(self):
        connection = self._model.get_current_connection()
        if connection:
            lookat_point = connection.get_coordinates_midpoint()
            if lookat_point:
                sceneviewer = self._ui.alignmentsceneviewerwidget.getSceneviewer()
                sceneviewer.setLookatParametersNonSkew(
                    sceneviewer.getEyePosition()[1], lookat_point, sceneviewer.getUpVector()[1])
            current_item = self._ui.connections_listWidget.currentItem()
            current_item.setCheckState(QtCore.Qt.CheckState.Checked)

    def _connections_listWidget_link_and_lock_selected_ends(self):
        connection = self._model.get_current_connection()
        if connection:
            self._model.connection_link_and_lock_selected_ends(connection)

    def _connections_listWidget_set_link_locking_from_selection(self, lock):
        connection = self._model.get_current_connection()
        if connection:
            self._model.connection_set_link_locking_from_selection(connection, lock)

    def _connections_listWidget_remove_selected_links(self):
        connection = self._model.get_current_connection()
        if connection:
            self._model.connection_remove_selected_links(connection)

    def _connections_listWidget_select_locked_links(self):
        connection = self._model.get_current_connection()
        if connection:
            self._model.connection_add_locked_links_to_selection(connection)

    def _connections_listWidget_auto_align_segment(self, dependent_segment_index):
        connection = self._model.get_current_connection()
        if connection:
            auto_align_dialog = AutoAlignDialog(self, connection, dependent_segment_index)
            if auto_align_dialog.exec():
                phase1_align, gap_distance, phase_2_optimize = auto_align_dialog.get_options()
                self._model.connection_auto_align_segment(
                    connection, dependent_segment_index, phase1_align, gap_distance, phase_2_optimize)

    def _connections_listWidget_create_connection(self):
        stitcher = self._model.get_stitcher()
        new_connection_dialog = NewConnectionDialog(self, stitcher)
        if new_connection_dialog.exec():
            segments = new_connection_dialog.get_segments()
            connection = self._model.create_connection(segments)
            if connection:
                self._build_connections_list()

    def _connections_listWidget_delete_connection(self):
        connection = self._model.get_current_connection()
        if connection:
            reply = QtWidgets.QMessageBox.question(
                self, 'Confirm action',
                'Delete connection \'' + connection.get_name() + '\'?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.No)
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                self._model.delete_connection(connection)
                self._build_connections_list()

    def _update_current_connection(self):
        """
        Get the current connection pointed at in the connections_listWidget.
        :return: Stitcher Connection, current_item in list widget
        """
        current_item = self._ui.connections_listWidget.currentItem()
        if current_item:
            connection_index = self._ui.connections_listWidget.row(current_item)
            stitcher = self._model.get_stitcher()
            connections = stitcher.get_connections()
            connection = connections[connection_index]
        else:
            connection = None
        self._model.set_current_connection(connection)
        return connection, current_item

    def _connections_listWidget_contextMenu(self, pos):
        menu = QtWidgets.QMenu(self._ui.connections_listWidget)
        self._update_current_connection()
        connection = self._model.get_current_connection()
        if connection:
            action_hide_all = menu.addAction("Hide all")
            action_show_all = menu.addAction("Show all")
            action_look_at = menu.addAction("Look at connection")
            action_hide_all.triggered.connect(lambda: self._connections_listWidget_set_all_visibility(False))
            action_show_all.triggered.connect(lambda: self._connections_listWidget_set_all_visibility(True))
            action_look_at.triggered.connect(self._connections_listWidget_look_at_connection)
            menu.addSeparator()
            segments = connection.get_segments()
            action_link_and_lock_selected_ends = menu.addAction("Link and lock selected ends")
            action_link_and_lock_selected_ends.setToolTip("Make and lock links between selected end points in segments")
            action_lock_selected_links = menu.addAction("Lock selected links")
            action_lock_selected_links.setToolTip("Lock selected links in this connection until unlocked")
            action_remove_selected_links = menu.addAction("Remove selected links")
            action_unlock_selected_links = menu.addAction("Unlock selected links")
            action_select_locked_links = menu.addAction("Select locked links")
            action_link_and_lock_selected_ends.triggered.connect(
                self._connections_listWidget_link_and_lock_selected_ends)
            action_lock_selected_links.triggered.connect(
                lambda: self._connections_listWidget_set_link_locking_from_selection(True))
            action_remove_selected_links.triggered.connect(
                lambda: self._connections_listWidget_remove_selected_links())
            action_unlock_selected_links.triggered.connect(
                lambda: self._connections_listWidget_set_link_locking_from_selection(False))
            action_select_locked_links.triggered.connect(self._connections_listWidget_select_locked_links)
            action_auto_align0 = menu.addAction("Auto-align " + segments[0].get_name() + "...")
            action_auto_align1 = menu.addAction("Auto-align " + segments[1].get_name() + "...")
            action_auto_align0.triggered.connect(lambda: self._connections_listWidget_auto_align_segment(0))
            action_auto_align1.triggered.connect(lambda: self._connections_listWidget_auto_align_segment(1))
            menu.addSeparator()
        action_create = menu.addAction("Create connection...")
        action_create.triggered.connect(self._connections_listWidget_create_connection)
        if connection:
            action_delete = menu.addAction("Delete connection...")
            action_delete.triggered.connect(self._connections_listWidget_delete_connection)
        # Display the menu at the global position of the mouse click
        menu.exec(self._ui.connections_listWidget.mapToGlobal(pos))

    def _displayAxes_clicked(self):
        self._model.set_display_axes(self._ui.displayAxes_checkBox.isChecked())

    def _displayMarkerPoints_clicked(self):
        self._model.set_display_marker_points(self._ui.displayMarkerPoints_checkBox.isChecked())

    def _displayMarkerNames_clicked(self):
        self._model.set_display_marker_names(self._ui.displayMarkerNames_checkBox.isChecked())

    def _displayNodePoints_clicked(self):
        self._model.set_display_node_points(self._ui.displayNodePoints_checkBox.isChecked())

    def _displayNodeNumbers_clicked(self):
        self._model.set_display_node_numbers(self._ui.displayNodeNumbers_checkBox.isChecked())

    def _displayNodeGroupChanged(self, index):
        if index == 0:
            name = None
        else:
            name = self._ui.displayNodeGroup_comboBox.itemText(index)
        self._model.set_display_node_group_name(name)

    def _displayLineGeneral_clicked(self):
        self._model.set_display_line_general(self._ui.displayLineGeneral_checkBox.isChecked())

    def _displayLineGeneralRadius_clicked(self):
        self._model.set_display_line_general_radius(self._ui.displayLineGeneralRadius_checkBox.isChecked())

    def _displayLineGeneralTrans_clicked(self):
        self._model.set_display_line_general_trans(self._ui.displayLineGeneralTrans_checkBox.isChecked())

    def _displayIndepNetworks_clicked(self):
        self._model.set_display_line_independent_network(self._ui.displayIndepNetworks_checkBox.isChecked())

    def _displayIndepNetworksRadius_clicked(self):
        self._model.set_display_line_independent_network_radius(self._ui.displayIndepNetworksRadius_checkBox.isChecked())

    def _displayIndepNetworksTrans_clicked(self):
        self._model.set_display_line_independent_network_trans(self._ui.displayIndepNetworksTrans_checkBox.isChecked())

    def _displayNetworkGroup1_clicked(self):
        self._model.set_display_line_network_group_1(self._ui.displayNetworkGroup1_checkBox.isChecked())

    def _displayNetworkGroup1Radius_clicked(self):
        self._model.set_display_line_network_group_1_radius(self._ui.displayNetworkGroup1Radius_checkBox.isChecked())

    def _displayNetworkGroup1Trans_clicked(self):
        self._model.set_display_line_network_group_1_trans(self._ui.displayNetworkGroup1Trans_checkBox.isChecked())

    def _displayNetworkGroup2_clicked(self):
        self._model.set_display_line_network_group_2(self._ui.displayNetworkGroup2_checkBox.isChecked())

    def _displayNetworkGroup2Radius_clicked(self):
        self._model.set_display_line_network_group_2_radius(self._ui.displayNetworkGroup2Radius_checkBox.isChecked())

    def _displayNetworkGroup2Trans_clicked(self):
        self._model.set_display_line_network_group_2_trans(self._ui.displayNetworkGroup2Trans_checkBox.isChecked())

    def _displayEndPointDirections_clicked(self):
        self._model.set_display_end_point_directions(self._ui.displayEndPointDirections_checkBox.isChecked())

    def _displayEndPointBestFitLines_clicked(self):
        self._model.set_display_end_point_best_fit_lines(self._ui.displayEndPointBestFitLines_checkBox.isChecked())

    def _displayEndPointRadius_clicked(self):
        self._model.set_display_end_point_radius(self._ui.displayEndPointRadius_checkBox.isChecked())

    def _displayEndPointTrans_clicked(self):
        self._model.set_display_end_point_trans(self._ui.displayEndPointTrans_checkBox.isChecked())

    def _refresh_node_points_scale(self):
        realFormat = "{:.4g}"
        node_points_scale = self._model.get_display_node_points_scale()
        node_points_scale_str = realFormat.format(node_points_scale)
        self._ui.displayNodePointsScale_lineEdit.setText(node_points_scale_str)

    def _displayNodePointsScale_entered(self):
        node_points_scale = parse_real_non_negative(self._ui.displayNodePointsScale_lineEdit)
        if node_points_scale >= 0.0:
            self._model.set_display_node_points_scale(node_points_scale)
        self._refresh_node_points_scale()

    def _refresh_radius_scale(self):
        realFormat = "{:.4g}"
        radius_scale = self._model.get_display_radius_scale()
        radius_scale_str = realFormat.format(radius_scale)
        self._ui.displayRadiusScale_lineEdit.setText(radius_scale_str)

    def _displayRadiusScale_entered(self):
        radius_scale = parse_real_non_negative(self._ui.displayRadiusScale_lineEdit)
        if radius_scale >= 0.0:
            self._model.set_display_radius_scale(radius_scale)
        self._refresh_radius_scale()

    def _display_theme_changed(self, index):
        theme_name = self._ui.displayTheme_comboBox.itemText(index)
        self._model.set_display_theme(theme_name)
        self._set_display_theme_background()
