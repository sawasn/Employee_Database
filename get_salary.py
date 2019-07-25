'''
Created on Jul 4, 2019

@author: HI TECH
'''
import BaseClass as b


class GetSalary(b.BaseClass):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def getSalarys(self):
        self.connectData()
        arge = self.argumentParser()
        self.getSalary(arge.id)


GetSalary().getSalarys()
