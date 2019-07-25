'''
Created on Jul 3, 2019

@author: HI TECH
'''
import BaseClass as b


class AddEngineer(b.BaseClass):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        #self.checkFile()

    def addEngineer(self):
        self.connectData()
        arge = self.argumentParser()
        self.addEmployee(arge.id, arge.name, "Engineer", arge.salary)


AddEngineer().addEngineer()
