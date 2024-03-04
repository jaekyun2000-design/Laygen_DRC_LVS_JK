class PrintStr:
    def __init__(self):
        self.MaxStrLength = 105
        self.FillChar = '='
        self.dummyString = ''.center(self.MaxStrLength, self.FillChar)


    def Start(self, string, FillChar=None):
        _FillChar = self.FillChar if FillChar is None else FillChar

        print(self._dummyString(_FillChar))
        print(('   {}   '.format(string)).center(self.MaxStrLength, _FillChar))


    def End(self, string, FillChar=None):
        _FillChar = self.FillChar if FillChar is None else FillChar

        print(('   {}   '.format(string)).center(self.MaxStrLength, _FillChar))
        print(self._dummyString(_FillChar))


    def OneLine(self, string, FillChar=None):
        _FillChar = self.FillChar if FillChar is None else FillChar

        print(('   {}   '.format(string)).center(self.MaxStrLength, _FillChar))


    def ThreeLine(self, string, FillChar=None):
        _FillChar = self.FillChar if FillChar is None else FillChar

        print(self._dummyString(_FillChar))
        print(('   {}   '.format(string)).center(self.MaxStrLength, _FillChar))
        print(self._dummyString(_FillChar))


    def DummyLine(self, string, FillChar=None):
        _FillChar = self.FillChar if FillChar is None else FillChar

        print(self._dummyString(_FillChar))

    def _dummyString(self, FillChar=None):
        return ''.center(self.MaxStrLength, self.FillChar if FillChar is None else FillChar)


    # def Box(self, string):
    #     print('|' + (''.center(self.MaxStrLength - 2)) + '|')
    #     print('|' + (('   {}   '.format(string)).center(self.MaxStrLength-2)) + '|')
    #     print('|' + (''.center(self.MaxStrLength - 2)) + '|')
