'''
Created on Jul 3, 2019

@author: HI TECH
'''
import BaseClass as b


class GetAllEngineer(b.BaseClass):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def getAllEngineer(self):
        self.connectData()
        self.getAllEmployees("Engineer")


GetAllEngineer().getAllEngineer()
