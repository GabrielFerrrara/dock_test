class Date:
    def __init__(self, inText: str):
        self._inText = inText
        self._format = self.__defineFormat()
        self._printFormat =self.__convertToYYYYMMDD()
        self._numeric = self.__defineNumeric()
    
    def __str__(self):
        return self._printFormat

    def __defineFormat(self):
        if('/' in self._inText):
            return 'DD/MM/YYYY'
        else:
            return 'YYYYMMDD'

    def __convertToYYYYMMDD(self):
        if(self._format == 'DD/MM/YYYY'):
            return f'{self._inText[6:]}{self._inText[3:5]}{self._inText[:2]}'
        else:
            return self._inText            

    def __defineNumeric(self):
        day = int(self._printFormat[6:])
        month = int(self._printFormat[4:6])
        year = int(self._printFormat[:4])
        return ((year * 365.25) + (month * 31) + (day))
  

    def getFormat(self) -> str:
        return self._printFormat

    def getFormatInit(self):
        return self._inText


    def getNumeric(self) -> int:
        return self._numeric


