'''
Created on Jul 3, 2019

@author: HI TECH
'''
import BaseClass as b


class AddManger(b.BaseClass):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        #self.checkFile()

    def addManger(self):
        self.connectData()
        arge = self.argumentParser()
        self.addEmployee(arge.id, arge.name, "Manger", arge.salary)


AddManger().addManger()
