from __future__ import print_function

import sys
import os
import logging

from sys import path as sysPath
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../rticonnextdds-connector/")

import rticonnextdds_connector as rti

connector = rti.Connector("MyParticipantLibrary::Zero",
                          filepath + "\\PythonDDSPlayhouse.xml")
inputDDS = connector.getInput("MySubscriber::MySampleReader")

instanceNumber = '0'
if len(sys.argv) > 1:
    instanceNumber = sys.argv[1]

logging.basicConfig(filename='EndProcessor_DDSTest_' + instanceNumber + '.log', level=logging.DEBUG,
                    format='%(asctime)-15s - %(levelname)8s - %(lineno)d - %(message)s')
logging.info('------------------Logging started------------------')
print('logging started to EndProcessor_DDSTest_' + instanceNumber + '.log')

# 'default.topic.config': {'auto.offset.reset': 'smallest'}
#c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'python_ends_client'})
#c.subscribe(['TowEndWindow'])
#print 'Subscribed to TowEndWindow'
#logging.info('Subscribed to TowEndWindow')

running = True
while running:
    inputDDS.take()
    numOfSamples = inputDDS.samples.getLength()
    for j in range(1, numOfSamples+1):
        if inputDDS.infos.isValid(j):
            # This gives you a dictionary
            sample = inputDDS.samples.getDictionary(j)
            message = sample['Message']
            
            # Or you can just access the field directly
            #size = inputDDS.samples.getNumber(j, "shapesize")
            #color = inputDDS.samples.getString(j, "color")
            #toPrint = "Received x: " + repr(x) + " y: " + repr(y) + \
            #          " size: " + repr(size) + " color: " + repr(color)

            print(message)
    sleep(2)

logging.info('------------------Logging ended------------------')

