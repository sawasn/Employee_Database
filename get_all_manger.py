'''
Created on Jul 3, 2019

@author: HI TECH
'''
import BaseClass as b


class GetAllManger(b.BaseClass):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def getAllManger(self):
        self.connectData()
        self.getAllEmployees("Manger")


GetAllManger().getAllManger()
