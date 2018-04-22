##############################################################################
# Copyright (c) 2005-2015 Real-Time Innovations, Inc. All rights reserved.
# Permission to modify and use for internal purposes granted.
# This software is provided "as is", without warranty, express or implied.
##############################################################################
"""Samples's writer."""

from sys import path as sysPath
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../rticonnextdds-connector/")
import rticonnextdds_connector as rti

connector = rti.Connector("MyParticipantLibrary::Zero",
                          filepath + "\PythonDDSPlayhouse.xml")                         
outputDDS = connector.getOutput("MyPublisher::MySampleWriter")

for i in range(1, 500):
    outputDDS.instance.setString("message", "Hi Gil")
    outputDDS.write()
    sleep(2)
