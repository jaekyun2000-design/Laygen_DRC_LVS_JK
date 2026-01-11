

class USER:

    def __init__(self, tech=None):
        """
        :Function: Set user information and directory paths
        :param _tech: (optional) Write your technology to specify directory paths.
                      ex) '028nm' or '065nm' or empty(default: 028nm)
        """

        self.ID = 'kjh91'
        self.PW = 'akdl625'
        self.server = '141.223.24.54'


        if tech in ('028nm', None):
            self.Dir_Work = '/mnt/sdb/kjh91/OPUS/CAD_S28nm_Workspace'
        elif tech == '065nm':
            self.Dir_Work = '/mnt/sdb/kjh91/OPUS/tsmc65'
        else:
            raise NotImplemented

        self.Dir_GDS = self.Dir_Work + '/Download_GDS'
        self.Dir_DRCrun = self.Dir_Work + '/DRC/DRC_run'

        ''' telegram bot '''
        self.BotToken = '00000'
        self.ChatID = 00000
