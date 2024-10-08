"""
MAP Client Plugin Step
"""
import json
import pathlib

from PySide6 import QtGui, QtWidgets, QtCore

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint

from mapclientplugins.segmentationstitcherstep.configuredialog import ConfigureDialog
from mapclientplugins.segmentationstitcherstep.model.segmentationstitchermodel import SegmentationStitcherModel
from mapclientplugins.segmentationstitcherstep.view.segmentationstitcherwidget import SegmentationStitcherWidget

class SegmentationStitcherStep(WorkflowStepMountPoint):
    """
    Step instance of segmentation stitcher plugin.
    """

    def __init__(self, location):
        super(SegmentationStitcherStep, self).__init__('Segmentation Stitcher', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Segmentation'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/segmentationstitcherstep/images/segmentation.png')
        # Ports:
        self.addPort([('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'),
                      ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#uses-list-of',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location')
                      ])
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        # Config:
        self._config = {
            'identifier': '',
            'network group 1 keywords': ['vagus', 'nerve', 'trunk', ' branch'],
            'network group 2 keywords': ['fascicle']
        }
        # Port data:
        self._segmentation_file_locations = None  # file_location
        self._model = None
        self._view = None

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
        try:
            self._model = SegmentationStitcherModel(
                self._segmentation_file_locations, self._location, self._config['identifier'],
                self._config['network group 1 keywords'], self._config['network group 2 keywords'])
            self._view = SegmentationStitcherWidget(self._model)
            self._view.register_done_callback(self._doneExecution)
            self._setCurrentWidget(self._view)
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        if not isinstance(dataIn, list):
            dataIn = [dataIn]

        self._segmentation_file_locations = [pathlib.PureWindowsPath(p).as_posix() for p in dataIn]  # file_location

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        return self._model.get_output_segmentation_file_name()

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
