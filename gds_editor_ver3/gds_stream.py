from KJH91_Projects.gds_editor_ver3 import user_define_exceptions
import struct
from KJH91_Projects.gds_editor_ver3 import gds_tags
from KJH91_Projects.gds_editor_ver3 import gds_record
from KJH91_Projects.gds_editor_ver3 import gds_structures

"""_HEADER=None
_BGNLIB=None
_LIBDIRSIZE=None
_SRFNAME=None
_LIBSECUR=None
_LIBNAME=None
_REFLIBS=None
_FONTS=None
_ATTRTABLE=None
_GENERATIONS=None
_FORMATTYPE=None
_UNITS=None
_STRUCTURES=None
_ENDLIB=None"""

class GDS_STREAM():
    
    def __init__(self):
        self._HEADER=None
        #self._HEADER=gds_record.GDS_HEADER()
        self._BGNLIB=None
        #self._BGNLIB=gds_record.GDS_BGNLIB()
        self._LIBDIRSIZE=None
        self._SRFNAME=None
        self._LIBSECUR=None
        self._LIBNAME=None
        #self._LIBNAME=gds_record.GDS_LIBNAME()
        self._REFLIBS=None
        self._FONTS=None
        self._ATTRTABLE=None
        self._GENERATIONS=None
        self._FORMATTYPE=None
        self._UNITS=None
        #self._UNITS=gds_record.GDS_UNITS()
        self._STRUCTURES=[]
        self._ENDLIB=None
        #self._ENDLIB=gds_record.GDS_ENDLIB()
        
        
    """
    
    read binary record data --> classify the binary data  
    
    record
    [record header:[record length, record type,data type], data]
    
    """
    
    
    def read_record (self, gds_file):
        record_header=gds_file.read(4)
    
        if not record_header or len(record_header)<4:
            raise user_define_exceptions.EndofFileError
    
        record_size, record_tag = struct.unpack('>HH', record_header)
    
        if record_size < 4:
            raise user_define_exceptions.IncorrectRecordSize ('record size is too small')
    
        if (record_size % 2): 
            raise user_define_exceptions.IncorrectRecordSize ('incorrect record size')
    
        record_size-=4
        record_data=gds_file.read(record_size)
    
        if record_size != len(record_data):
            raise user_define_exceptions.EndofFileError
    
        record_datatype=record_tag & 0xff #read lower 1byte from record_tag(2byte data)
        record_type=(record_tag>>8) & 0xff # read upper 1byte from record_tag
        gds_file.seek(-(record_size+4),1)
        record_binary_stream=gds_file.read(record_size+4)
        #record_data,=struct.unpack('>h',record_data)
        
        """ return record size, record tag, record type, record data type, record data, record binary stream"""
        return [(record_size+4), record_tag, record_type, record_datatype, record_data, record_binary_stream]
    
    
    def write_binary_gds_stream(self,gds_file):
        self._HEADER.write_binary_gds_stream(gds_file)
        self._BGNLIB.write_binary_gds_stream(gds_file)
        if self._LIBDIRSIZE!=None:
            self._LIBDIRSIZE.write_binary_gds_stream(gds_file)
        if self._SRFNAME!=None:
            self._SRFNAME.write_binary_gds_stream(gds_file)
        if self._LIBSECUR!=None:
            self._LIBSECUR.write_binary_gds_stream(gds_file)
        
        self._LIBNAME.write_binary_gds_stream(gds_file)
        
        if self._REFLIBS!=None:
            self._REFLIBS.write_binary_gds_stream(gds_file)
        if self._FONTS!=None:
            self._FONTS.write_binary_gds_stream(gds_file)
        
        if self._ATTRTABLE!=None:
            self._ATTRTABLE.write_binary_gds_stream(gds_file)
        
        if self._GENERATIONS!=None:
            self._GENERATIONS.write_binary_gds_stream(gds_file)
        
        if self._FORMATTYPE!=None:
            self._FORMATTYPE.write_binary_gds_stream(gds_file)
             

        self._UNITS.write_binary_gds_stream(gds_file)
        
        if self._STRUCTURES!=[]:
            num_of_structure=len(self._STRUCTURES)
            for i in range(0,num_of_structure):
                
                self._STRUCTURES[i].write_binary_gds_stream(gds_file)
                
                
         
        self._ENDLIB.write_binary_gds_stream(gds_file)
        
        
        
        
    
    def read_binary_gds_stream(self, gds_file):
        """
        read record binary stream separately
        """
        while True:
            """extract binary gds data until units"""
            
            [record_size, record_tag, record_type, record_datatype, record_data, record_binary_stream] = self.read_record(gds_file=gds_file)
            
            if gds_tags.DICT['HEADER']==record_tag:
                self._HEADER=gds_record.GDS_HEADER()
                self._HEADER.read_binary_gds_stream(record_tag,record_data)
                #break
                
            elif gds_tags.DICT['BGNLIB']==record_tag:
                self._BGNLIB=gds_record.GDS_BGNLIB()
                self._BGNLIB.read_binary_gds_stream(record_tag,record_data)
                
            elif gds_tags.DICT['LIBDIRSIZE']==record_tag:
                self._LIBDIRSIZE=gds_record.GDS_LIBDIRSIZE()
                self._LIBDIRSIZE.read_binary_gds_stream(record_tag,record_data)
                
            elif gds_tags.DICT['SRFNAME']==record_tag:
                self._SRFNAME=gds_record.GDS_SRFNAME()
                self._SRFNAME.read_binary_gds_stream(record_tag, record_data)
            elif gds_tags.DICT['LIBSECUR']==record_tag:
                self._LIBSECUR=gds_record.GDS_LIBSECUR()
                self._LIBSECUR.read_binary_gds_stream(record_tag, record_data)
            elif gds_tags.DICT['LIBNAME']==record_tag:
                self._LIBNAME=gds_record.GDS_LIBNAME()
                self._LIBNAME.read_binary_gds_stream(record_tag, record_data)
            elif gds_tags.DICT['REFLIBS']==record_tag:
                self._REFLIBS=gds_record.GDS_REFLIBS()
                self._REFLIBS.read_binary_gds_stream(record_tag, record_data)
            elif gds_tags.DICT['FONTS']==record_tag:
                self._FONTS=gds_record.GDS_FONTS()
                self._FONTS.read_binary_gds_stream(record_tag, record_data)
            elif gds_tags.DICT['ATTRTABLE']==record_tag:
                self._ATTRTABLE=gds_record.GDS_ATTRTABLE()
                self._ATTRTABLE.read_binary_gds_stream(record_tag, record_data)
            elif gds_tags.DICT['GENERATIONS']==record_tag:
                self._GENERATIONS=gds_record.GDS_GENERATIONS()
                self._GENERATIONS.read_binary_gds_stream(record_tag, record_data)
            elif gds_tags.DICT['FORMAT']==record_tag:
                temp=[]
                temp.append([record_tag,record_data])
                
                
                #self._FORMATTYPE.append([record_tag,record_data])
                
                """extract FORMATTYPE binary data"""
                while True: 
                    [record_size, record_tag, record_type, record_datatype, record_data, record_binary_stream] = self.read_record(gds_file=gds_file)
                    
                    if gds_tags.DICT['UNITS']==record_tag:
                        self._FORMATTYPE=gds_record.GDS_FORMATTYPE()
                        self._FORMATTYPE.read_binary_gds_stream(temp)
                        temp=[]
                        del temp
                                                
                        gds_file.seek(-record_size,1)
                        break
                    else :
                        temp.append([record_tag,record_data])
                    
            elif gds_tags.DICT['UNITS']==record_tag:
                self._UNITS=gds_record.GDS_UNITS()
                self._UNITS.read_binary_gds_stream(record_tag, record_data)
                break    
            """    
            elif gds_tags.DICT['FORMAT']==record_tag:
                self._FORMATTYPE.append(record_binary_stream)
            """
            #    """extract FORMATTYPE binary data"""
            """
                while True: 
                    [record_size, record_tag, record_type, record_datatype, record_data, record_binary_stream] = self.read_record(gds_file=gds_file)
                    if gds_tags.DICT['MASK']==record_tag:
                        self._FORMATTYPE.append(record_binary_stream)
                    elif gds_tags.DICT['ENDMASKS']:
                        self._FORMATTYPE.append(record_binary_stream)
                        break
                    elif gds_tags.DICT['UNITS']==record_tag:
            """
            #            """when MASK doesn't exist"""
            """
                        gds_file.seek(-record_size,1)
                        break
            """     
                    
            
            
        """extract structures & endlib"""
        while True:
            temp=[]
            _gds_struct_tmp=None
            [record_size, record_tag, record_type, record_datatype, record_data, record_binary_stream] = self.read_record(gds_file=gds_file)
            
            if gds_tags.DICT['BGNSTR']==record_tag:
                """extract each binary structure data"""
                temp.append([record_tag,record_data])
                #temp.append(record_binary_stream)
                while True:
                    [record_size, record_tag, record_type, record_datatype, record_data, record_binary_stream] = self.read_record(gds_file=gds_file)
                    if gds_tags.DICT['ENDSTR']==record_tag:
                        #temp.append(record_binary_stream)
                        temp.append([record_tag,record_data])
                        #self._STRUCTURES.append(temp)
                        #print 'temp'
                        #print temp
                        
                        _gds_struct_tmp=gds_structures.GDS_STRUCTURE()
                        _gds_struct_tmp.read_binary_gds_stream(temp)
                        self._STRUCTURES.append(_gds_struct_tmp)
                        _gds_struct_tmp=None
                        del _gds_struct_tmp
                        break
                    else:
                        temp.append([record_tag,record_data])
                        #temp.append(record_binary_stream)
                
                
                
            elif gds_tags.DICT['ENDLIB']==record_tag:
                self._ENDLIB=gds_record.GDS_ENDLIB()
                del temp
                """delete temp=[] in the while loop"""
                break
    
    
    """
    _HEADER=None
    _BGNLIB=None
    _LIBDIRSIZE=None
    _SRFNAME=None
    _LIBSECUR=None
    _LIBNAME=None
    _REFLIBS=None
    _FONTS=None
    _ATTRTABLE=None
    _GENERATIONS=None
    _FORMATTYPE=None
    _UNITS=None
    _STRUCTURES=None
    _ENDLIB=None
    """
    """
    _gds_stream=(_HEADER, _BGNLIB, _LIBDIRSIZE,_SRFNAME,_LIBSECUR, _LIBNAME, \
                _REFLIBS, _FONTS, _ATTRTABLE,_GENERATIONS,_FORMATTYPE,_UNITS,\
                _STRUCTURES,_ENDLIB)
                """
    """
    GDS stream format:
        .. productionlist::
            library: HEADER
                   : BGNLIB
                   : [LIBDIRSIZE]
                   : [SRFNAME]
                   : [LIBSECUR]
                   : LIBNAME
                   : [REFLIBS]
                   : [FONTS]
                   : [ATTRTABLE]
                   : [GENERATIONS]
                   : [`format`]
                   : UNITS
                   : {`structure`}*
                   : ENDLIB
            format: FORMAT
                  : [MASK+ ENDMASKS]
    """
