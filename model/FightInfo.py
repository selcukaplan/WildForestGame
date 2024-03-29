

from enum import Enum

class FIGHTRESULT(Enum):
    # int values are assigned for creating the enums. they don't have a specific mean.
    # Todo: is it a good approach?
    WON = 1
    LOST = -1
    SCORELESS = 0
    NOENEMY = 2  #  there is no enemy to fight


class FightInfo:

    def __init__(self,enemyToFight,fightResult,newCoordinates):
        if (enemyToFight is None):
            assert fightResult == FIGHTRESULT.NOENEMY,"If there is no enemy to fight, fight result must be 'NOENEMY'"
        if (fightResult == FIGHTRESULT.NOENEMY):
            assert enemyToFight == None, "If there is no fight, there is no enemy!"
        self.__enemyToFight=enemyToFight
        self.__fightResult=fightResult
        self.__newCoordinates=newCoordinates

    def getNewCoordinates(self):
        return self.__newCoordinates

    def getFightResult(self):
        return self.__fightResult

    def getEnemy(self):
        return self.__enemyToFight