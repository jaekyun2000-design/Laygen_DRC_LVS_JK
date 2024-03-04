from gds_editor_ver3 import user_define_exceptions
import struct
from gds_editor_ver3 import gds_tags
from gds_editor_ver3 import gds_record
from gds_editor_ver3 import gds_elements

class GDS_STRUCTURE():
    def __init__(self,gds_data=None):
        self._BGNSTR=None
        self._STRNAME=None
        self._STRCLASS=None
        self._ELEMENTS=[]
        self._ENDSTR=None
        
    
    def write_binary_gds_stream(self,binary_gds_stream):
        self._BGNSTR.write_binary_gds_stream(binary_gds_stream)
        self._STRNAME.write_binary_gds_stream(binary_gds_stream)
        if self._STRCLASS!=None:
            self._STRCLASS.write_binary_gds_stream(binary_gds_stream)
        for i in range(0,len(self._ELEMENTS)):
            self._ELEMENTS[i].write_binary_gds_stream(binary_gds_stream)
            
            
        self._ENDSTR.write_binary_gds_stream(binary_gds_stream)
    
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            
            
            if temp[0]==gds_tags.DICT['BGNSTR']:
                self._BGNSTR=gds_record.GDS_BGNSTR()
                self._BGNSTR.read_binary_gds_stream(temp[0], temp[1])
            elif temp[0]==gds_tags.DICT['STRNAME']:
                self._STRNAME=gds_record.GDS_STRNAME()
                self._STRNAME.read_binary_gds_stream(temp[0], temp[1])
            elif temp[0]==gds_tags.DICT['STRNAME']:
                self._STRCLASS=gds_record.GDS_STRCLASS()
                self._STRCLASS.read_binary_gds_stream(temp[0], temp[1])
            elif temp[0]==gds_tags.DICT['ENDSTR']:
                self._ENDSTR=gds_record.GDS_ENDSTR()
                #temp delete???
                del temp
                break
            else :
                if temp[0]==gds_tags.DICT['BOUNDARY'] or temp[0]==gds_tags.DICT['PATH'] or temp[0]==gds_tags.DICT['SREF'] or temp[0]==gds_tags.DICT['AREF'] \
                or temp[0]==gds_tags.DICT['TEXT'] or temp[0]==gds_tags.DICT['NODE'] or temp[0]==gds_tags.DICT['BOX']:
                    temp_list=[]
                    temp_list.append(temp)
                    while True:
                        temp=gds_data.pop(0)
                        if temp[0]==gds_tags.DICT['ENDEL']:
                            temp_list.append(temp)
                            _gds_element_tmp=gds_elements.GDS_ELEMENT()
                            _gds_element_tmp.read_binary_gds_stream(temp_list)
                            self._ELEMENTS.append(_gds_element_tmp)
                            _gds_element_tmp=None
                            del _gds_element_tmp
                            temp_list=[]
                            del temp_list    
                            break                        
                        else:
                            temp_list.append(temp)