'''
Created on Jul 3, 2019

@author: HI TECH
'''
import BaseClass as b


class RemoveEmployee(b.BaseClass):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def removeEmployees(self):
        self.connectData()
        arge = self.argumentParser()
        self.removeEmployee(arge.id)


RemoveEmployee().removeEmployees()
