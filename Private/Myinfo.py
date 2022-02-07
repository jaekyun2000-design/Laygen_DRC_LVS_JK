class USER:

    def __init__(self, tech=None):
        """
        :Function: Set user information and directory paths
        :param _tech: (optional) Write your technology to specify directory paths.
                      ex) '028nm' or '065nm' or empty(default: 028nm)
        """
        self.ID = 'jicho0927'
        self.PW = 'cho89140616!!'
        self.server = '141.223.29.62'

        if tech in ('SS28nm', None):
            self.Dir_Work = '/mnt/sdc/jicho0927/OPUS/SAMSUNG28n'
        elif tech == 'TSMC65nm':
            self.Dir_Work = '/mnt/sdc/jicho0927/OPUS/tsmc65n'
        elif tech == 'TSMC40nm':
            self.Dir_Work = '/mnt/sdc/jicho0927/OPUS/tsmc40n'
        elif tech == 'TSMC90nm':
            self.Dir_Work = '/mnt/sdc/jicho0927/OPUS/tsmc90n'

        else:
            raise NotImplemented

        self.Dir_GDS = self.Dir_Work
        self.Dir_DRCrun = self.Dir_Work + '/DRC/run'

        ''' telegram bot '''
        self.BotToken = ''
        self.ChatID =0