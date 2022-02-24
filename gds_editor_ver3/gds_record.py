from gds_editor_ver3 import gds_tags
import struct
import math
from datetime import datetime, MINYEAR
from gds_editor_ver3 import user_define_exceptions
import warnings
class GDS_HEADER():
    def __init__(self, tag=gds_tags.DICT['HEADER'], gds_data=None):
        self.tag=tag
        self.gds_version=gds_data

    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.gds_version)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        gds_version,=struct.unpack('>h',gds_data)
        self.tag=tag
        self.gds_version=gds_version

class GDS_BGNLIB():
    def __init__(self, tag=gds_tags.DICT['BGNLIB'], gds_data=None):
        self.tag=tag
        self.time_modi=datetime(MINYEAR,1,1,0,0,0)
        self.time_access=datetime(MINYEAR,1,1,0,0,0)
        
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHhhhhhhhhhhhh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.time_modi.year,self.time_modi.month,self.time_modi.day,self.time_modi.hour,self.time_modi.minute,self.time_modi.second\
                                    ,self.time_access.year,self.time_access.month,self.time_access.day,self.time_access.hour,self.time_access.minute,self.time_access.second)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        last_modi_year,last_modi_month,last_modi_date, last_modi_hour, last_modi_minute, last_modi_second,\
        last_access_year, last_access_month, last_access_date, last_access_hour, last_access_minute, last_access_second=struct.unpack('>hhhhhhhhhhhh',gds_data)
        """
        gdstxt_stream.write(record_tag_dictionary.REV_DICT[record_tag]+':'+'\n'+'last modification time:'+str(last_modi_year)+':'+str(last_modi_month)+':'+str(last_modi_day)+':'\
        + str(last_modi_hour)+':'+str(last_modi_minute)+':'+str(last_modi_second)+'\n'+'last access time:'+str(last_access_year)+':'+ str(last_access_month)+\
        ':'+str(last_access_day)+':'+ str(last_access_hour)+':'+str(last_access_minute)+':'+str(last_access_second)+'\n' )
        """
        
        self.tag=tag
        self.time_modi=datetime(last_modi_year,last_modi_month,last_modi_date,last_modi_hour,last_modi_minute, last_modi_second)
        self.time_access=datetime(last_access_year,last_access_month,last_access_date,last_access_hour,last_access_minute, last_access_second)    
        
class GDS_LIBDIRSIZE():
    def __init__(self,tag=gds_tags.DICT['LIBDIRSIZE'],gds_data=None):
        
        
        self.tag=tag
        self.libdirsize=gds_data
        
        
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.libdirsize)
        binary_gds_stream.write(fmt_binary_data)
        
        
    def read_binary_gds_stream(self,tag,gds_data):
        libdirsize_data,=struct.unpack('>h',gds_data)
        self.tag=tag
        self.libdirsize=libdirsize_data
        
    """    libdirsize_data,=struct.unpack('>h',record_data)
    gdstxt_stream.write(record_tag_dictionary.REV_DICT[record_tag]+':'+str(libdirsize)+'\n')"""
        
        
class GDS_SRFNAME():
    def __init__(self,tag=gds_tags.DICT['SRFNAME'],gds_data=None):
        
        self.tag=tag
        self.srfname=gds_data
        
    def write_binary_gds_stream(self,binary_gds_stream):
        
        if len(self.srfname)%2:
            fmt='>HH'+str(len(self.srfname)+1)+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.srfname)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
        
            
        else:
            fmt='>HH'+str(len(self.srfname))+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.srfname)
            binary_gds_stream.write(fmt_binary_data)
            #struct.pack(fmt,struct.calcsize(fmt),record_tag_dictionary.DICT[record_name],record_parameter )
    
    
    
    def read_binary_gds_stream(self, tag, gds_data):
        srfname_data,=struct.unpack('>'+str(len(gds_data))+'s',gds_data)
        self.tag=tag
        self.srfname=srfname_data
class GDS_LIBSECUR():
    def __init__(self,tag=gds_tags.DICT['LIBSECUR'],gds_data=None):
        self.tag=tag
        self.libsecur=gds_data
    
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.libsecur)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        libsecur_data,=struct.unpack('>h',gds_data)
        self.tag=tag
        self.libsecur=libsecur_data
        
class GDS_LIBNAME():
    def __init__(self, tag=gds_tags.DICT['LIBNAME'],gds_data=None):
        self.tag=tag
        self.libname=gds_data
        
    def write_binary_gds_stream(self,binary_gds_stream):
        if len(self.libname)%2:
            fmt='>HH'+str(len(self.libname)+1)+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.libname)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
        else:
            fmt='>HH'+str(len(self.libname))+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.libname)
            binary_gds_stream.write(fmt_binary_data)
        
            
    def read_binary_gds_stream(self,tag,gds_data):
        lib_name,=struct.unpack('>'+str(len(gds_data))+'s',gds_data)
        self.tag=tag
        self.libname=lib_name
        
class GDS_REFLIBS():
    def __init__(self,tag=gds_tags.DICT['REFLIBS'],gds_data=None):
        self.tag=tag
        self.reflibs
        
    def write_binary_gds_stream(self,binary_gds_stream):
        if len(self.reflibs)%2:
            fmt='>HH'+str(len(self.reflibs)+1)+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.reflibs)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
        else:
            fmt='>HH'+str(len(self.reflibs))+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.reflibs)
            binary_gds_stream.write(fmt_binary_data)
        
        
    def read_binary_gds_stream(self,tag,gds_data):
        reflibs_name,=struct.unpack('>'+str(len(gds_data))+'s',gds_data)
        self.tag=tag
        self.reflibs=reflibs_name
        
class GDS_FONTS():
    def __init__(self,tag=gds_tags.DICT['FONTS'],gds_data=None):
        self.tag=tag
        self.fonts=gds_data
        
    def write_binary_gds_stream(self,binary_gds_stream):
        if len(self.fonts)%2:
            fmt='>HH'+str(len(self.fonts)+1)+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.fonts)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
        else:
            fmt='>HH'+str(len(self.fonts))+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.fonts)
            binary_gds_stream.write(fmt_binary_data)

    def read_binary_gds_stream(self,tag,gds_data):
        fonts_data,=struct.unpack('>'+str(len(gds_data))+'s',gds_data)
        self.tag=tag
        self.fonts=fonts_data
        
class GDS_ATTRTABLE():
    def __init__(self,tag=gds_tags.DICT['ATTRTABLE'],gds_data=None):
        self.tag=tag
        self.attrtable=gds_data
        
    def write_binary_gds_stream(self,binary_gds_stream):
        if len(self.attrtable)%2:
            fmt='>HH'+str(len(self.attrtable)+1)+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.attrtable)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
        else:
            fmt='>HH'+str(len(self.attrtable))+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.attrtable)
            binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag=gds_tags.DICT['ATTRTABLE'], gds_data=None):
        attrtable_data,=struct.unpack('>'+str(len(gds_data))+'s',gds_data)
        self.tag=tag
        self.attrtable=attrtable_data
class GDS_GENERATIONS():
    def __init__(self,tag=gds_tags.DICT['GENERATIONS'],gds_data=None):
        self.tag=tag
        self.generations=gds_data
        
    def write_binary_gds_stream(self,binary_gds_stream):
        
        fmt='>HH{0}h'.format(len(binary_gds_stream))
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,*[data for data in self.generations])
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag=gds_tags.DICT['GENERATIONS'], gds_data=None):
        
        generations_data,= struct.unpack('>h',gds_data)
        self.tag=tag
        self.generations=generations_data
        
class GDS_UNITS():
    def __init__(self,tag=gds_tags.DICT['UNITS'], gds_data=[0.001,1e-9]):
        self.tag=tag
        self.unit_user=gds_data[0]
        self.unit_meter=gds_data[1]
        
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHQQ'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,excess64_8byte_encode(self.unit_user),excess64_8byte_encode(self.unit_meter))
        binary_gds_stream.write(fmt_binary_data)
        
        
    def read_binary_gds_stream(self,tag,gds_data):
        record_unit_num1, record_unit_num2 = struct.unpack('>QQ',gds_data)
        self.tag=tag
        self.unit_user=excess64_8byte_decode(record_unit_num1)
        self.unit_meter=excess64_8byte_decode(record_unit_num2)
        
class GDS_ENDLIB():
    def __init__(self, tag=gds_tags.DICT['ENDLIB'],gds_data=None):
        self.tag=tag
    
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag)
        binary_gds_stream.write(fmt_binary_data)
        

class GDS_FORMATTYPE():
    def __init__(self,gds_data=None):
        self._FORMAT=None
        self._MASK=[]
        self._ENDMASK=None
    """
    def write_binary_gds_stream(self,binary_gds_stream):
        
        self._FORMAT.write_binary_gds_stream()
    """ 
    def write_binary_gds_stream(self,binary_gds_stream):
        self._FORMAT.write_binary_gds_stream(binary_gds_stream)
        if self._MASK!=[]:
            for i in range(0,len(self._MASK)):
                self._MASK[i].write_binary_gds_stream(binary_gds_stream)
        
        if self._ENDMASK!=None:
            self._ENDMASK.write_binary_gds_stream(binary_gds_stream)
    
    
    def read_binary_gds_stream(self,gds_data):
        
        while True:
            temp = gds_data.pop(0)
            
            if temp[0]==gds_tags.DICT['FORMAT']:
                self._FORMAT=GDS_FORMAT()
                self._FORMAT.read_binary_gds_stream(temp[0],temp[1])
                if gds_data==[]:
                    break
                
            elif temp[0]==gds_tags.DICT['MASK']:
                _gds_mask_tmp=None
                _gds_mask_tmp=GDS_MASK()
                _gds_mask_tmp.read_binary_gds_stream(temp[0], temp[1])
                self._MASK.append(_gds_mask_tmp)
                _gds_mask_tmp=None
                del _gds_mask_tmp
            elif temp[0]==gds_tags.DICT['ENDMASK']:
                self._ENDMASK=GDS_ENDMASKS()
                break
                
            """
            elif 
            
        for i in range(0,len(gds_data)):
            if i==0:
                self._FORMAT=GDS_FORMAT()
                self._FORMAT.read_binary_gds_stream(gds_data[0][0], gds_data[0][1])
        if len(gds_data)>1:
            for i in range(2,len(gds_data)+1):
                if i>1 and i<len(gds_data):
                    self._MASK.append(GDS_MASK())
                    self._MASK[i-2].read_binary_gds_stream(gds_data[i-1][0],gds_data[i-1][1])
                elif i==len(gds_data):
                    self._ENDMASK=GDS_ENDMASKS()
            """
                
     
class GDS_FORMAT():
    def __init__(self,tag=gds_tags.DICT['FORMAT'],gds_data=None):
        self.tag=tag
        self.format_data=gds_data
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.format_data)
        binary_gds_stream.write(fmt_binary_data)
        
        
        
    def read_binary_gds_stream(self,tag,gds_data):
        format_unpack,=struct.unpack('>h',gds_data)
        self.tag=tag
        self.format_data=format_unpack
        
class GDS_MASK():
    def __init__(self,tag=gds_tags.DICT['MASK'],gds_data=None):
        self.tag=tag
        self.mask=gds_data
    def write_binary_gds_stream(self,binary_gds_stream):
        if len(self.mask)%2:
            fmt='>HH'+str(len(self.mask)+1)+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.mask)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
        else:
            fmt='>HH'+str(len(self.mask))+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.mask)
            binary_gds_stream.write(fmt_binary_data)
        
        
    def read_binary_gds_stream(self,tag,gds_data):
        mask_data,=struct.unpack('>'+str(len(gds_data))+'s',gds_data)
        self.tag=tag
        self.mask=mask_data
        
class GDS_ENDMASKS():
    def __init__(self, tag=gds_tags.DICT['ENDMASKS'],gds_data=None):
        self.tag=tag
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag)
        binary_gds_stream.write(fmt_binary_data)
        
"""
records in structure 
"""
class GDS_BGNSTR():
    def __init__(self,tag=gds_tags.DICT['BGNSTR'],gds_data=None):
        self.tag=tag
        self.time_creation=datetime(MINYEAR,1,1,0,0,0)
        self.time_modi=datetime(MINYEAR,1,1,0,0,0)
        
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHhhhhhhhhhhhh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.time_creation.year,self.time_creation.month,self.time_creation.day,self.time_creation.hour,self.time_creation.minute,self.time_creation.second\
                                    ,self.time_modi.year,self.time_modi.month,self.time_modi.day,self.time_modi.hour,self.time_modi.minute,self.time_modi.second)
        binary_gds_stream.write(fmt_binary_data)

    def read_binary_gds_stream(self,tag,gds_data):
        last_creation_year,last_creation_month,last_creation_date, last_creation_hour, last_creation_minute, last_creation_second,\
        last_modi_year, last_modi_month, last_modi_date, last_modi_hour, last_modi_minute, last_modi_second=struct.unpack('>hhhhhhhhhhhh',gds_data)
        """
        gdstxt_stream.write(record_tag_dictionary.REV_DICT[record_tag]+':'+'\n'+'last modification time:'+str(last_modi_year)+':'+str(last_modi_month)+':'+str(last_modi_day)+':'\
        + str(last_modi_hour)+':'+str(last_modi_minute)+':'+str(last_modi_second)+'\n'+'last access time:'+str(last_access_year)+':'+ str(last_access_month)+\
        ':'+str(last_access_day)+':'+ str(last_access_hour)+':'+str(last_access_minute)+':'+str(last_access_second)+'\n' )
        """
        
        self.tag=tag
        self.time_creation=datetime(last_creation_year,last_creation_month,last_creation_date,last_creation_hour,last_creation_minute, last_creation_second)
        self.time_modi=datetime(last_modi_year,last_modi_month,last_modi_date,last_modi_hour,last_modi_minute, last_modi_second)
        
class GDS_STRNAME():
    def __init__(self,tag=gds_tags.DICT['STRNAME'],gds_data=None):
        self.tag=tag
        self.strname=None
        
    def write_binary_gds_stream(self,binary_gds_stream):
        if type(self.strname) == bytes:
            decoded_str  = self.strname.decode()
            if '\x00' in decoded_str:
                self.strname = decoded_str.split('\x00', 1)[0]
            else:
                self.strname = decoded_str
        if len(self.strname)%2:
            fmt='>HH'+str(len(self.strname)+1)+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.strname)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
        else:
            fmt='>HH'+str(len(self.strname))+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.strname))
            binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag, gds_data):
        record_name,=struct.unpack('>'+str(len(gds_data))+'s',gds_data)
        self.tag=tag
        self.strname=record_name
        
class GDS_STRCLASS():
    def __init__(self,tag=gds_tags.DICT['STRCLASS'],gds_data=None):
        self.tag=tag
        self.strclass=None
        
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.strclass)
        binary_gds_stream.write(fmt_binary_data)
        
        
        
    def read_binary_gds_stream(self,tag,gds_data):
        strclass_data,=struct.unpack('>H',gds_data)
        self.tag=tag
        self.strclass=strclass_data
        
class GDS_ENDSTR():
    def __init__(self,tag=gds_tags.DICT['ENDSTR'],gds_data=None):
        self.tag=tag        
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag)
        binary_gds_stream.write(fmt_binary_data)
"""
record in GDS_ELEMENT
"""
class GDS_ENDEL():
    def __init__(self,tag=gds_tags.DICT['ENDEL'],gds_data=None):
        self.tag=tag
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag)
        binary_gds_stream.write(fmt_binary_data)

class GDS_BOUNDARY():
    def __init__(self,tag=gds_tags.DICT['BOUNDARY'],gds_data=None):
        self.tag=tag
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag)
        binary_gds_stream.write(fmt_binary_data)
        
        
class GDS_ELFLAGS():
    def __init__(self,tag=gds_tags.DICT['ELFLAGS'],gds_data=None):
        self.tag=tag
        self.template_15bit=None
        self.external_14bit=None
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,((self.external_14bit<<1)+self.template_15bit ))
        binary_gds_stream.write(fmt_binary_data)
        
        
    def read_binary_gds_stream(self,tag,gds_data):
        elflags_data,= struct.unpack('>H',gds_data)
        self.tag=tag
        self.template_15bit=(elflags_data & 0x0001)
        self.external_14bit=((elflags_data & 0x0002)>>1)
class GDS_PLEX():
    def __init__(self,tag=gds_tags.DICT['PLEX'],gds_data=None):
        self.tag=tag
        self.plex=gds_data
        
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHi'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.plex)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag, gds_data):
        plex_data,=struct.unpack('>i',gds_data)
        self.tag=tag
        self.plex=plex_data
        
class GDS_LAYER():
    def __init__(self,tag=gds_tags.DICT['LAYER'],gds_data=None):
        self.tag=tag
        self.layer=gds_data
    def write_binary_gds_stream(self,binary_gds_stream):
        
        fmt='>HHh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.layer)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        record_layer,=struct.unpack('>h',gds_data)
        self.tag=tag
        self.layer=record_layer
class GDS_DATATYPE():
    def __init__(self,tag=gds_tags.DICT['DATATYPE'],gds_data=None):
        self.tag=tag
        self.datatype=gds_data
    def write_binary_gds_stream(self,binary_gds_stream):
        
        fmt='>HHh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.datatype)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        record_datatype,=struct.unpack('>h',gds_data)
        self.tag=tag
        self.datatype=record_datatype
class GDS_XY():
    def __init__(self,tag=gds_tags.DICT['XY'],gds_data=None):
        self.tag=tag
        self.xy=[]
        
    def write_binary_gds_stream(self,binary_gds_stream):
        
        temp_list=[]
        for i in range(0,len(self.xy)):
            temp_list.append(int(self.xy[i][0]))
            temp_list.append(int(self.xy[i][1]))
        
        fmt='>HH{0}i'.format(len(temp_list))
        
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag, *temp_list )
        binary_gds_stream.write(fmt_binary_data)
        del temp_list
        
        
        
    def read_binary_gds_stream(self,tag, gds_data):
        unpack_fmt='>'
        xy_len=len(gds_data)
        
        if not xy_len or (xy_len % 8)!=0:
            raise user_define_exceptions.IncorrectDataSize('incorrect data size')
        
        for i in range(int(xy_len/4)): ## since data is four byte data --> number of data = data_size(byte)/4
            unpack_fmt+='i'
        
        xy_data=struct.unpack(unpack_fmt,gds_data)
        
        
        for i in range(int(xy_len/8)): #to make tuple format with N number of data --> N/2 tuples comes out
            self.xy.append([xy_data[2*i],xy_data[2*i+1]])


"""
"""          
class GDS_PATH():
    def __init__(self,tag=gds_tags.DICT['PATH'],gds_data=None):
        self.tag=tag
        
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag)
        binary_gds_stream.write(fmt_binary_data)
        
class GDS_PATHTYPE():
    def __init__(self,tag=gds_tags.DICT['PATHTYPE'],gds_data=None):
        self.tag=tag
        self.pathtype=gds_data
    def write_binary_gds_stream(self,binary_gds_stream):
        
        fmt='>HHh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.pathtype)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        pathtype_data,= struct.unpack('>h',gds_data)
        self.tag=tag
        self.pathtype=pathtype_data
        
class GDS_WIDTH():
    def __init__(self,tag=gds_tags.DICT['WIDTH'],gds_data=None ):
        self.tag=tag
        self.width=gds_data
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHi'
        if type(self.width):
            self.width = int(self.width)
            warnings.warn('Float type width input detected!')
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.width)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag, gds_data):
        record_width,=struct.unpack('>i',gds_data)
        self.tag=tag
        self.width=record_width
class GDS_BGNEXTN():
    def __init__(self,tag=gds_tags.DICT['BGNEXTN'],gds_data=None):
        self.tag=tag
        self.bgnextn=gds_data
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHi'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.bgnextn)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        bgnextn_data,=struct.unpack('>i',gds_data)
        self.tag=tag
        self.bgnextn=bgnextn_data
class GDS_ENDEXTN():
    def __init__(self,tag=gds_tags.DICT['ENDEXTN'],gds_data=None):
        self.tag=tag
        self.endextn=gds_data
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHi'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.endextn)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        endextn_data,=struct.unpack('>i',gds_data)
        self.tag=tag
        self.endextn=endextn_data
"""
"""
class GDS_SREF():
    def __init__(self,tag=gds_tags.DICT['SREF'],gds_data=None):
        self.tag=tag
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag)
        binary_gds_stream.write(fmt_binary_data)
        
class GDS_SNAME():
    def __init__(self,tag=gds_tags.DICT['SNAME'],gds_data=None):
        self.tag=tag
        self.sname=None
    def write_binary_gds_stream(self,binary_gds_stream):
        if type(self.sname) == bytes:
            decoded_str = self.sname.decode()
            if '\x00' in decoded_str:
                self.sname = decoded_str.split('\x00', 1)[0]
            else:
                self.sname = decoded_str
        if len(self.sname)%2:
            fmt='>HH'+str(len(self.sname)+1)+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.sname)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
        else:
            fmt='>HH'+str(len(self.sname))+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.sname)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
            
    def read_binary_gds_stream(self,tag,gds_data):
        record_name,=struct.unpack('>'+str(len(gds_data))+'s',gds_data)
        self.tag=tag
        self.sname=record_name
        
"""
"""
class GDS_AREF():
    def __init__(self,tag=gds_tags.DICT['AREF'],gds_data=None):
        self.tag=tag
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag)
        binary_gds_stream.write(fmt_binary_data)
   
class GDS_COLROW():
    def __init__(self,tag=gds_tags.DICT['COLROW'],gds_data=None):
        self.tag=tag
        self.col=None
        self.row=None
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHhh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.col,self.row)
        binary_gds_stream.write(fmt_binary_data)
    def read_binary_gds_stream(self,tag,gds_data):
        colrow_2byte_data1,colrow_2byte_data2 = struct.unpack('>hh',gds_data)
        self.tag=tag
        self.col=colrow_2byte_data1
        self.row=colrow_2byte_data2
        
        
             
"""
"""
class GDS_TEXT():
    def __init__(self,tag=gds_tags.DICT['TEXT'],gds_data=None):
        self.tag=tag
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag)
        binary_gds_stream.write(fmt_binary_data)
        
class GDS_NODE():
    def __init__(self,tag=gds_tags.DICT['NODE'],gds_data=None):
        self.tag=tag
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag)
        binary_gds_stream.write(fmt_binary_data)

class GDS_NODETYPE():
    def __init__(self,tag=gds_tags.DICT['NODETYPE'],gds_data=None):
        self.tag=tag
        self.nodetype=gds_data
    def write_binary_gds_stream(self,binary_gds_stream):
        
        fmt='>HHh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.nodetype)
        binary_gds_stream.write(fmt_binary_data)
    def read_binary_gds_stream(self,tag,gds_data):
        elkey_data,=struct.unpack('>h',gds_data)
        self.tag=tag
        self.nodetype=elkey_data
               
class GDS_BOX():
    def __init__(self,tag=gds_tags.DICT['BOX'],gds_data=None):
        self.tag=tag
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag)
        binary_gds_stream.write(fmt_binary_data)
        
class GDS_BOXTYPE():
    def __init__(self,tag=gds_tags.DICT['BOXTYPE'],gds_data=None):
        self.tag=tag
        self.boxtype=gds_data
    def write_binary_gds_stream(self,binary_gds_stream):
        
        fmt='>HHh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.boxtype)
        binary_gds_stream.write(fmt_binary_data)
    def read_binary_gds_stream(self,tag,gds_data):
        boxtype_data,=struct.unpack('>h',gds_data)
        self.tag=tag
        self.boxtype=boxtype_data



class GDS_TEXTTYPE():
    def __init__(self,tag=gds_tags.DICT['TEXTTYPE'], gds_data=None):
        self.tag=tag
        self.texttype=None
    def write_binary_gds_stream(self,binary_gds_stream):
        
        fmt='>HHh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.texttype)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        texttype_data,= struct.unpack('>h',gds_data)
        self.tag=tag
        self.texttype=texttype_data
        
        
class GDS_PRESENTATION():
    def __init__(self,tag=gds_tags.DICT['PRESENTATION'],gds_data=None):
        self.tag=tag
        self.font=None
        self.vertical_presentation=None
        self.horizontal_presentation=None
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,(self.font<<4)+(self.vertical_presentation<<2)+self.horizontal_presentation)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        presentation_data,= struct.unpack('>H',gds_data)
        self.tag=tag
        self.font=((presentation_data & 0x0030)>>4)
        self.vertical_presentation=((presentation_data & 0x000c)>>2)
        self.horizontal_presentation=(presentation_data & 0x0003)
        

class GDS_STRING():
    def __init__(self,tag=gds_tags.DICT['STRING'],gds_data=None):
        self.tag=tag
        self.string_data=None
    def write_binary_gds_stream(self,binary_gds_stream):
        if len(self.string_data)%2:
            fmt='>HH'+str(len(self.string_data)+1)+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.string_data)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
        else:
            fmt='>HH'+str(len(self.string_data))+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.string_data)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
            
    def read_binary_gds_stream(self,tag,gds_data):
        record_string,=struct.unpack('>'+str(len(gds_data))+'s',gds_data)
        self.tag=tag
        self.string_data=record_string

class GDS_STRANS():
    def __init__(self,tag=gds_tags.DICT['STRANS'],gds_data=None):
        self.tag=tag
        self.reflection=None
        self.abs_mag=None
        self.abs_angle=None
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHH'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,(self.reflection<<15)+(self.abs_mag<<2)+(self.abs_angle<<1))
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        strans_data,= struct.unpack('>H',gds_data)
        self.tag=tag
        self.reflection=((strans_data & 0x8000)>>15)
        self.abs_mag=((strans_data & 0x0004)>>2)
        self.abs_angle=((strans_data & 0x0002)>>1)
        
class GDS_MAG():
    def __init__(self,tag=gds_tags.DICT['MAG'],gds_data=None):
        self.tag=tag
        self.mag=None
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHQ'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,excess64_8byte_encode(self.mag))
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        mag_data, = struct.unpack('>Q',gds_data)
        self.tag=tag
        self.mag=excess64_8byte_decode(mag_data)
        
        
class GDS_ANGLE():
    def __init__(self,tag=gds_tags.DICT['ANGLE'],gds_data=None):
        self.tag=tag
        self.angle=None
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHQ'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,excess64_8byte_encode(self.angle))
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        angle_data, = struct.unpack('>Q',gds_data)
        self.tag=tag
        self.angle=excess64_8byte_decode(angle_data)
        
class GDS_PROPATTR():
    def __init__(self,tag=gds_tags.DICT['PROPATTR'],gds_data=None):
        self.tag=tag
        self.propattr=None
        
    def write_binary_gds_stream(self,binary_gds_stream):
        fmt='>HHh'
        fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,self.propattr)
        binary_gds_stream.write(fmt_binary_data)
        
    def read_binary_gds_stream(self,tag,gds_data):
        propattr_data,=struct.unpack('>h',gds_data)
        self.tag=tag
        self.propattr=propattr_data
        
class GDS_PROPVALUE():
    def __init__(self,tag=gds_tags.DICT['PROPVALUE'],gds_data=None):
        self.tag=tag
        self.propvalue=None
        
    def write_binary_gds_stream(self,binary_gds_stream):
        
        if len(self.propvalue)%2:
            fmt='>HH'+str(len(self.propvalue)+1)+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.propvalue)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
        
            
        else:
            fmt='>HH'+str(len(self.propvalue))+'s'
            fmt_binary_data=struct.pack(fmt,struct.calcsize(fmt),self.tag,str.encode(self.propvalue)+b'\0')
            binary_gds_stream.write(fmt_binary_data)
            
    def read_binary_gds_stream(self,tag,gds_data):
        propvalue_data,=struct.unpack('>'+str(len(gds_data))+'s',gds_data)
        self.tag=tag
        self.propvalue=propvalue_data
        

        
        
        
"""
self._BOUNDARY=None
        self._ELFLAGS=None
        self._PLEX=None
        self._LAYER=None
        self._DATATYPE=None
        self._XY=None
"""
def excess64_8byte_encode(real_num):
    ieee64bit_float,= struct.unpack('>Q',struct.pack('>d',real_num))
    ieee64bit_float_sign=(ieee64bit_float & 0x8000000000000000)
                                            
    ieee64bit_float_exponent=( (ieee64bit_float >> 52) & 0x7ff )
    ieee64bit_float_fraction= (ieee64bit_float& 0xFFFFFFFFFFFFF)
    """                                            
    print ieee64bit_float_exponent
    print ieee64bit_float_fraction
    print ieee64bit_float_sign
    """
    if ieee64bit_float_exponent==0:
        return 0
    unbiased_ieee64bit_float_exponent=ieee64bit_float_exponent-1023
    excess64_8byte_mantissa=(ieee64bit_float_fraction+ 0x10000000000000)<<3
    excess64_8byte_exponent, rest=divmod(unbiased_ieee64bit_float_exponent+1 , 4)
    
    if rest:
        rest=4-rest
        excess64_8byte_exponent+=1
    
    excess64_8byte_mantissa=excess64_8byte_mantissa >> rest
    excess64_8byte_exponent=excess64_8byte_exponent+64  
    """ still 9bit --> real8's exponent uses 7bit """
    
    if excess64_8byte_exponent<0:
        excess64_8byte_mantissa=excess64_8byte_mantissa >> 4*(-excess64_8byte_exponent)
        excess64_8byte_exponent=0
    if excess64_8byte_exponent>0x7f:
        raise user_define_exceptions.IncorrectDataSize('the number is too large number for real8 format')
    """
    print excess64_8byte_exponent
    print excess64_8byte_mantissa
    """
    return ieee64bit_float_sign | (excess64_8byte_exponent << 56) | excess64_8byte_mantissa



def excess64_4byte_encode(real_num):
    ieee32bit_float,= struct.unpack('>L',struct.pack('>f',real_num))
    ieee32bit_float_sign=(ieee32bit_float & 0x80000000)
                                            
    ieee32bit_float_exponent=( (ieee32bit_float >> 23) & 0xff )
    ieee32bit_float_fraction= (ieee32bit_float & 0x7FFFFF)
                    

                           
    #print ieee32bit_float_exponent
    #print ieee32bit_float_fraction
    #print ieee32bit_float_sign
    
    
    if ieee32bit_float_exponent==0:
        return 0
    
    
    unbiased_ieee32bit_float_exponent=ieee32bit_float_exponent-127
    excess64_4byte_mantissa=(ieee32bit_float_fraction+ 0x800000)
    excess64_4byte_exponent, rest=divmod(unbiased_ieee32bit_float_exponent+1 , 4)
    
    
    if rest:
        rest=4-rest
        excess64_4byte_exponent+=1
    
    
    
    excess64_4byte_mantissa=excess64_4byte_mantissa >> rest
    excess64_4byte_exponent=excess64_4byte_exponent+64  
    """6bit --> real4's exponent uses 7bit """
    if excess64_4byte_exponent<0:
        excess64_4byte_mantissa=excess64_4byte_mantissa >> 4*(-excess64_4byte_exponent)
        excess64_4byte_exponent=0
    if excess64_4byte_exponent>0x7f:
        raise user_define_exceptions.IncorrectDataSize('the number is too large number for real8 format')
    
    
    
    return ieee32bit_float_sign | (excess64_4byte_exponent << 24) | excess64_4byte_mantissa

def excess64_8byte_decode (excess64_8byte_num):
    #0x 00 00 00 00 00 00 00 00
    num_sign=-1 if (excess64_8byte_num & 0x8000000000000000) else 1
    num_exponent=  (excess64_8byte_num & 0x7F00000000000000) >> 56
    num_mantissa=  (excess64_8byte_num & 0xFFFFFFFFFFFFFF )
    
    return math.ldexp(num_sign*num_mantissa, 4*(num_exponent-64) - 56 )

def excess64_4byte_decode (excess64_4byte_num):
    #0x 00 00 00 00
    num_sign=-1 if (excess64_4byte_num & 0x80000000) else 1
    num_exponent=  (excess64_4byte_num & 0x7F000000) >> 24
    num_mantissa=  (excess64_4byte_num & 0xFFFFFF)
    
    return math.ldexp(num_sign*num_mantissa, 4*(num_exponent-64) - 24 )