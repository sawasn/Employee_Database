'''
Created on Jul 4, 2019

@author: HI TECH
'''

import BaseClass as b


class GetAllEmployee(b.BaseClass):
    '''

    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def getAllEmployee(self):
        self.connectData()
        self.getAllEmployees()


GetAllEmployee().getAllEmployee()
