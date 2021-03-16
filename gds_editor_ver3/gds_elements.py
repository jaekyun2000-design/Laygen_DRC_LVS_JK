from gds_editor_ver3 import user_define_exceptions
import struct
from gds_editor_ver3 import gds_tags
from gds_editor_ver3 import gds_record

class GDS_ELEMENT():
    def __init__(self,gds_data=None, _GDS_ELEMENT_NAME=None):
        self._ELEMENTS=None
        self._PROPERTY=[]
        self._ENDEL=None


        self._GDS_ELEMENT_NAME=_GDS_ELEMENT_NAME
        
    def write_binary_gds_stream(self,binary_gds_stream):
        self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)
        """
        if '_BOUNDARY' in dir(self._ELEMENTS):
            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)
        elif '_PATH' in dir(self._ELEMENTS):
            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)
        elif '_SREF' in dir(self._ELEMENTS):
            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)
        elif '_AREF' in dir(self._ELEMENTS):
            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)
        elif '_TEXT' in dir(self._ELEMENTS):
            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)
        elif '_NODE' in dir(self._ELEMENTS):
            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)
        elif '_BOX' in dir(self._ELEMENTS):
            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)
        """

        if self._GDS_ELEMENT_NAME:
            value_property = GDS_PROPERTY()
            value_property._PROPATTR = gds_record.GDS_PROPATTR()
            value_property._PROPATTR.propattr = 126
            value_property._PROPVALUE = gds_record.GDS_PROPVALUE()
            value_property._PROPVALUE.propvalue = self._GDS_ELEMENT_NAME
            self._PROPERTY.append(value_property)
            name_property = GDS_PROPERTY()
            name_property._PROPATTR = gds_record.GDS_PROPATTR()
            name_property._PROPATTR.propattr = 61
            name_property._PROPVALUE = gds_record.GDS_PROPVALUE()
            name_property._PROPVALUE.propvalue = self._GDS_ELEMENT_NAME
            self._PROPERTY.append(name_property)


        if self._PROPERTY!=[]:
            for i in range(0,len(self._PROPERTY)):
                self._PROPERTY[i].write_binary_gds_stream(binary_gds_stream)
        self._ENDEL.write_binary_gds_stream(binary_gds_stream)
        
    
    
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            
            if temp[0]==gds_tags.DICT['BOUNDARY']:
                temp_list=[]
                temp_list.append(temp)
                while True:
                    temp=gds_data.pop(0)
                    if temp[0]==gds_tags.DICT['XY']:
                        temp_list.append(temp)
                        self._ELEMENTS=GDS_BOUNDARY()
                        self._ELEMENTS.read_binary_gds_stream(temp_list)
                        temp_list=[]
                        del temp_list    
                        break                                
                    else:
                        temp_list.append(temp)
                        
                            
            elif  temp[0]==gds_tags.DICT['PATH']:
                temp_list=[]
                temp_list.append(temp)
                while True:
                    temp=gds_data.pop(0)
                    if temp[0]==gds_tags.DICT['XY']:
                        temp_list.append(temp)
                        self._ELEMENTS=GDS_PATH()
                        self._ELEMENTS.read_binary_gds_stream(temp_list)
                        temp_list=[]
                        del temp_list      
                        break                      
                    else:
                        temp_list.append(temp)
                        
            elif temp[0]==gds_tags.DICT['SREF']:
                temp_list=[]
                temp_list.append(temp)
                while True:
                    temp=gds_data.pop(0)
                    if temp[0]==gds_tags.DICT['XY']:
                        temp_list.append(temp)
                        self._ELEMENTS=GDS_SREF()
                        self._ELEMENTS.read_binary_gds_stream(temp_list)
                        temp_list=[]
                        del temp_list     
                        break                       
                    else:
                        temp_list.append(temp)
                        
            elif temp[0]==gds_tags.DICT['AREF']:
                temp_list=[]
                temp_list.append(temp)
                while True:
                    temp=gds_data.pop(0)
                    if temp[0]==gds_tags.DICT['XY']:
                        temp_list.append(temp)
                        self._ELEMENTS=GDS_AREF()
                        self._ELEMENTS.read_binary_gds_stream(temp_list)
                        temp_list=[]
                        del temp_list                
                        break            
                    else:
                        temp_list.append(temp)
            
            elif temp[0]==gds_tags.DICT['TEXT']:
                temp_list=[]
                temp_list.append(temp)
                while True:
                    temp=gds_data.pop(0)
                    if temp[0]==gds_tags.DICT['STRING']:
                        temp_list.append(temp)
                        self._ELEMENTS=GDS_TEXT()
                        self._ELEMENTS.read_binary_gds_stream(temp_list)
                        temp_list=[]
                        del temp_list 
                        break                           
                    else:
                        temp_list.append(temp)
            
            elif temp[0]==gds_tags.DICT['NODE']:
                temp_list=[]
                temp_list.append(temp)
                while True:
                    temp=gds_data.pop(0)
                    if temp[0]==gds_tags.DICT['XY']:
                        temp_list.append(temp)
                        self._ELEMENTS=GDS_NODE()
                        self._ELEMENTS.read_binary_gds_stream(temp_list)
                        temp_list=[]
                        del temp_list       
                        break                     
                    else:
                        temp_list.append(temp)
                        
            elif temp[0]==gds_tags.DICT['BOX']:
                temp_list=[]
                temp_list.append(temp)
                while True:
                    temp=gds_data.pop(0)
                    if temp[0]==gds_tags.DICT['XY']:
                        temp_list.append(temp)
                        self._ELEMENTS=GDS_BOX()
                        self._ELEMENTS.read_binary_gds_stream(temp_list)
                        temp_list=[]
                        del temp_list 
                        break                           
                    else:
                        temp_list.append(temp)
            elif temp[0]==gds_tags.DICT['PROPATTR']:
                temp_list=[]
                temp_list.append(temp)
                temp=gds_data.pop(0) # PROPBALUE
                temp_list.append(temp)
                _gds_property_tmp=GDS_PROPERTY()
                _gds_property_tmp.read_binary_gds_stream(temp_list)
                self._PROPERTY.append(_gds_property_tmp)
                _gds_property_tmp=None
                temp_list=[]
                del temp_list, _gds_property_tmp

            elif temp[0]==gds_tags.DICT['ENDEL']:
                self._ENDEL=gds_record.GDS_ENDEL()
                break

        #Code For Recovery element name from Property
        for property in self._PROPERTY:
            if property._PROPATTR.propattr is 61:
                self._GDS_ELEMENT_NAME = property._PROPVALUE.propvalue.decode()
                break

class GDS_BOUNDARY():
    def __init__(self,gds_data=None):
        self._BOUNDARY=None
        self._ELFLAGS=None
        self._PLEX=None
        self._LAYER=None
        self._DATATYPE=None
        self._XY=None
    
    def write_binary_gds_stream(self,binary_gds_stream):
        self._BOUNDARY.write_binary_gds_stream(binary_gds_stream)
        if self._ELFLAGS!=None:
            self._ELFLAGS.write_binary_gds_stream(binary_gds_stream)
            
        if self._PLEX!=None:
            self._PLEX.write_binary_gds_stream(binary_gds_stream)
            
        self._LAYER.write_binary_gds_stream(binary_gds_stream)
        self._DATATYPE.write_binary_gds_stream(binary_gds_stream)
        self._XY.write_binary_gds_stream(binary_gds_stream)
    
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            if temp[0]==gds_tags.DICT['BOUNDARY']:
                self._BOUNDARY=gds_record.GDS_BOUNDARY()
                #self._BOUNDARY.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['ELFLAGS']:
                self._ELFLAGS=gds_record.GDS_ELFLAGS()
                self._ELFLAGS.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['PLEX']:
                self._PLEX=gds_record.GDS_PLEX()
                self._PLEX.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['LAYER']:
                self._LAYER=gds_record.GDS_LAYER()
                self._LAYER.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['DATATYPE']:
                self._DATATYPE=gds_record.GDS_DATATYPE()
                self._DATATYPE.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['XY']:
                self._XY=gds_record.GDS_XY()
                self._XY.read_binary_gds_stream(temp[0],temp[1])
                break

class GDS_PATH():
    def __init__(self,gds_data=None):
        self._PATH=None
        self._ELFLAGS=None
        self._PLEX=None
        self._LAYER=None
        self._DATATYPE=None
        self._PATHTYPE=None
        self._WIDTH=None
        self._BGNEXTN=None
        self._ENDEXTN=None
        self._XY=None
        
    def write_binary_gds_stream(self,binary_gds_stream):
        self._PATH.write_binary_gds_stream(binary_gds_stream)
        if self._ELFLAGS!=None:
            self._ELFLAGS.write_binary_gds_stream(binary_gds_stream)
            
        if self._PLEX!=None:
            self._PLEX.write_binary_gds_stream(binary_gds_stream)
            
        self._LAYER.write_binary_gds_stream(binary_gds_stream)
        self._DATATYPE.write_binary_gds_stream(binary_gds_stream)
        if self._PATHTYPE!=None:
            self._PATHTYPE.write_binary_gds_stream(binary_gds_stream)
        
        if self._WIDTH!=None:
            self._WIDTH.write_binary_gds_stream(binary_gds_stream)
        if self._BGNEXTN!=None:
            self._BGNEXTN.write_binary_gds_stream(binary_gds_stream)
        if self._ENDEXTN!=None:
            self._ENDEXTN.write_binary_gds_stream(binary_gds_stream)
        self._XY.write_binary_gds_stream(binary_gds_stream)
        
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            if temp[0]==gds_tags.DICT['PATH']:
                self._PATH=gds_record.GDS_PATH()
                
            elif temp[0]==gds_tags.DICT['ELFLAGS']:
                self._ELFLAGS=gds_record.GDS_ELFLAGS()
                self._ELFLAGS.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['PLEX']:
                self._PLEX=gds_record.GDS_PLEX()
                self._PLEX.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['LAYER']:
                self._LAYER=gds_record.GDS_LAYER()
                self._LAYER.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['DATATYPE']:
                self._DATATYPE=gds_record.GDS_DATATYPE()
                self._DATATYPE.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['PATHTYPE']:
                self._PATHTYPE=gds_record.GDS_PATHTYPE()
                self._PATHTYPE.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['WIDTH']:
                self._WIDTH=gds_record.GDS_WIDTH()
                self._WIDTH.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['BGNEXTN']:
                
                self._BGNEXTN=gds_record.GDS_BGNEXTN()
                self._BGNEXTN.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['ENDEXTN']:
                
                self._ENDEXTN=gds_record.GDS_ENDEXTN()
                self._ENDEXTN.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['XY']:
                self._XY=gds_record.GDS_XY()
                self._XY.read_binary_gds_stream(temp[0],temp[1])
                break

class GDS_SREF():
    def __init__(self,gds_data=None):
        self._SREF=None
        self._ELFLAGS=None
        self._PLEX=None
        self._SNAME=None
        self._STRANS=None
        self._XY=None
        
    def write_binary_gds_stream(self,binary_gds_stream):
        self._SREF.write_binary_gds_stream(binary_gds_stream)
        if self._ELFLAGS!=None:
            self._ELFLAGS.write_binary_gds_stream(binary_gds_stream)
            
        if self._PLEX!=None:
            self._PLEX.write_binary_gds_stream(binary_gds_stream)
            
        self._SNAME.write_binary_gds_stream(binary_gds_stream)
        if self._STRANS !=None:
            self._STRANS.write_binary_gds_stream(binary_gds_stream)
        
        self._XY.write_binary_gds_stream(binary_gds_stream)
        
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            if temp[0]==gds_tags.DICT['SREF']:
                self._SREF=gds_record.GDS_SREF()
            elif temp[0]==gds_tags.DICT['ELFLAGS']:
                self._ELFLAGS=gds_record.GDS_ELFLAGS()
                self._ELFLAGS.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['LAYER']:
                self._LAYER=gds_record.GDS_LAYER()
                self._LAYER.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['SNAME']:
                self._SNAME=gds_record.GDS_SNAME()
                self._SNAME.read_binary_gds_stream(temp[0],temp[1])
            
            elif temp[0]==gds_tags.DICT['STRANS']:
                temp_list=[]
                temp_list.append(temp)
                if gds_data[0][0]==gds_tags.DICT['MAG'] or gds_data[0][0]==gds_tags.DICT['ANGLE']:
                    temp=gds_data.pop(0)
                    temp_list.append(temp)
                    if gds_data[0][0]==gds_tags.DICT['ANGLE']:
                        temp=gds_data.pop(0)
                        temp_list.append(temp)
                self._STRANS=GDS_STRANS()
                self._STRANS.read_binary_gds_stream(temp_list)
                temp_list=[]
                del temp_list
                             
                
            elif temp[0]==gds_tags.DICT['XY']:
                self._XY=gds_record.GDS_XY()
                self._XY.read_binary_gds_stream(temp[0],temp[1])
                break

class GDS_AREF():
    def __init__(self,gds_data=None):
        self._AREF=None
        self._ELFLAGS=None
        self._PLEX=None
        self._SNAME=None
        self._STRANS=None
        self._COLROW=None
        self._XY=None
    def write_binary_gds_stream(self,binary_gds_stream):
        self._AREF.write_binary_gds_stream(binary_gds_stream)
        if self._ELFLAGS!=None:
            self._ELFLAGS.write_binary_gds_stream(binary_gds_stream)
            
        if self._PLEX!=None:
            self._PLEX.write_binary_gds_stream(binary_gds_stream)
            
        self._SNAME.write_binary_gds_stream(binary_gds_stream)
        if self._STRANS !=None:
            self._STRANS.write_binary_gds_stream(binary_gds_stream)
        self._COLROW.write_binary_gds_stream(binary_gds_stream)
        self._XY.write_binary_gds_stream(binary_gds_stream)
        
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            if temp[0]==gds_tags.DICT['AREF']:
                self._AREF=gds_record.GDS_AREF()
            elif temp[0]==gds_tags.DICT['ELFLAGS']:
                self._ELFLAGS=gds_record.GDS_ELFLAGS()
                self._ELFLAGS.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['LAYER']:
                self._LAYER=gds_record.GDS_LAYER()
                self._LAYER.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['SNAME']:
                self._SNAME=gds_record.GDS_SNAME()
                self._SNAME.read_binary_gds_stream(temp[0],temp[1])
            
            elif temp[0]==gds_tags.DICT['STRANS']:
                temp_list=[]
                temp_list.append(temp)
                if gds_data[0][0]==gds_tags.DICT['MAG'] or gds_data[0][0]==gds_tags.DICT['ANGLE']:
                    temp=gds_data.pop(0)
                    temp_list.append(temp)
                    if gds_data[0][0]==gds_tags.DICT['ANGLE']:
                        temp=gds_data.pop(0)
                        temp_list.append(temp)
                self._STRANS=GDS_STRANS()
                self._STRANS(temp_list)
                temp_list=[]
                del temp_list
            
            elif temp[0]==gds_tags.DICT['COLROW']:
                self._COLROW=gds_record.GDS_COLROW()
                self._COLROW.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['XY']:
                self._XY=gds_record.GDS_XY()
                self._XY.read_binary_gds_stream(temp[0],temp[1])
                break
class GDS_TEXT():
    def __init__(self,gds_data=None):
        self._TEXT=None
        self._ELFLAGS=None
        self._PLEX=None
        self._LAYER=None
        self._TEXTBODY=None
        
    def write_binary_gds_stream(self,binary_gds_stream):
        self._TEXT.write_binary_gds_stream(binary_gds_stream)
        if self._ELFLAGS!=None:
            self._ELFLAGS.write_binary_gds_stream(binary_gds_stream)
            
        if self._PLEX!=None:
            self._PLEX.write_binary_gds_stream(binary_gds_stream)
            
        self._LAYER.write_binary_gds_stream(binary_gds_stream)
        self._TEXTBODY.write_binary_gds_stream(binary_gds_stream)
        
        
        
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            if temp[0]==gds_tags.DICT['TEXT']:
                self._TEXT=gds_record.GDS_TEXT()
            elif temp[0]==gds_tags.DICT['ELFLAGS']:
                self._ELFLAGS=gds_record.GDS_ELFLAGS()
            elif temp[0]==gds_tags.DICT['PLEX']:
                self._PLEX=gds_record.GDS_PLEX()
                self._PLEX.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['LAYER']:
                self._LAYER=gds_record.GDS_LAYER()
                self._LAYER.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['TEXTTYPE']:
                temp_list=[]
                temp_list.append(temp)
                while True:
                    temp=gds_data.pop(0)
                    if temp[0]==gds_tags.DICT['STRING']:
                        temp_list.append(temp)
                        self._TEXTBODY=GDS_TEXTBODY()
                        self._TEXTBODY.read_binary_gds_stream(temp_list)
                        temp_list=[]
                        del temp_list
                        break
                    else :
                        temp_list.append(temp)
                break
                    
            
        
        
    
        
class GDS_NODE():
    def __init__(self,gds_data=None):
        self._NODE=None
        self._ELFLAGS=None
        self._PLEX=None
        self._LAYER=None
        self._NODETYPE=None
        self._XY=None
    def write_binary_gds_stream(self,binary_gds_stream):
        self._NODE.write_binary_gds_stream(binary_gds_stream)
        if self._ELFLAGS!=None:
            self._ELFLAGS.write_binary_gds_stream(binary_gds_stream)
            
        if self._PLEX!=None:
            self._PLEX.write_binary_gds_stream(binary_gds_stream)
            
        self._LAYER.write_binary_gds_stream(binary_gds_stream)
        self._NODETYPE.write_binary_gds_stream(binary_gds_stream)
        
        self._XY.write_binary_gds_stream(binary_gds_stream)
        
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            if temp[0]==gds_tags.DICT['NODE']:
                self._NODE=gds_record.GDS_NODE()
                
            elif temp[0]==gds_tags.DICT['ELFLAGS']:
                self._ELFLAGS=gds_record.GDS_ELFLAGS()
                self._ELFLAGS.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['PLEX']:
                self._PLEX=gds_record.GDS_PLEX()
                self._PLEX.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['LAYER']:
                self._LAYER=gds_record.GDS_LAYER()
                self._LAYER.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['NODETYPE']:
                self._NODETYPE=gds_record.GDS_NODETYPE()
                self._NODETYPE.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['XY']:
                self._XY=gds_record.GDS_XY()
                self._XY.read_binary_gds_stream(temp[0],temp[1])
                break
        
class GDS_BOX():
    def __init__(self,gds_data=None):
        self._BOX=None
        self._ELFLAGS=None
        self._LAYER=None
        self._BOXTYPE=None
        self._XY=None
    def write_binary_gds_stream(self,binary_gds_stream):
        self._BOX.write_binary_gds_stream(binary_gds_stream)
        if self._ELFLAGS!=None:
            self._ELFLAGS.write_binary_gds_stream(binary_gds_stream)
            
        if self._PLEX!=None:
            self._PLEX.write_binary_gds_stream(binary_gds_stream)
            
        self._LAYER.write_binary_gds_stream(binary_gds_stream)
        self._BOXTYPE.write_binary_gds_stream(binary_gds_stream)
        
        self._XY.write_binary_gds_stream(binary_gds_stream)
        
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            if temp[0]==gds_tags.DICT['BOX']:
                self._BOX=gds_record.GDS_BOX()
                
            elif temp[0]==gds_tags.DICT['ELFLAGS']:
                self._ELFLAGS=gds_record.GDS_ELFLAGS()
                self._ELFLAGS.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['PLEX']:
                self._PLEX=gds_record.GDS_PLEX()
                self._PLEX.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['LAYER']:
                self._LAYER=gds_record.GDS_LAYER()
                self._LAYER.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['BOXTYPE']:
                self._BOXTYPE=gds_record.GDS_BOXTYPE()
                self._BOXTYPE.read_binary_gds_stream(temp[0],temp[1])
            elif temp[0]==gds_tags.DICT['XY']:
                self._XY=gds_record.GDS_XY()
                self._XY.read_binary_gds_stream(temp[0],temp[1])
                break


class GDS_TEXTBODY():
    def __init__(self,gds_data=None):
        self._TEXTTYPE=None
        self._PRESENTATION=None
        self._PATHTYPE=None
        self._WIDTH=None
        self._STRANS=None
        self._XY=None
        self._STRING=None
        
    def write_binary_gds_stream(self,binary_gds_stream):
        self._TEXTTYPE.write_binary_gds_stream(binary_gds_stream)
        
        if self._PRESENTATION!=None:
            self._PRESENTATION.write_binary_gds_stream(binary_gds_stream)
            
        
        if self._PATHTYPE!=None:
            self._PATHTYPE.write_binary_gds_stream(binary_gds_stream)
        
        if self._WIDTH!=None:
            self._WIDTH.write_binary_gds_stream(binary_gds_stream)
        if self._STRANS !=None:
            self._STRANS.write_binary_gds_stream(binary_gds_stream)
        self._XY.write_binary_gds_stream(binary_gds_stream)
        self._STRING.write_binary_gds_stream(binary_gds_stream)
        
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            if temp[0]==gds_tags.DICT['TEXTTYPE']:
                self._TEXTTYPE=gds_record.GDS_TEXTTYPE()
                self._TEXTTYPE.read_binary_gds_stream(temp[0], temp[1])
            elif temp[0]==gds_tags.DICT['PRESENTATION']:
                self._PRESENTATION=gds_record.GDS_PRESENTATION()
                self._PRESENTATION.read_binary_gds_stream(temp[0], temp[1])
            elif temp[0]==gds_tags.DICT['PATHTYPE']:
                self._PATHTYPE=gds_record.GDS_PATHTYPE()
                self._PATHTYPE.read_binary_gds_stream(temp[0], temp[1])
            elif temp[0]==gds_tags.DICT['WIDTH']:
                self._WIDTH=gds_record.GDS_WIDTH()
                self._WIDTH.read_binary_gds_stream(temp[0], temp[1])
            elif temp[0]==gds_tags.DICT['STRANS']:
                temp_list=[]
                temp_list.append(temp)
                if gds_data[0][0]==gds_tags.DICT['MAG'] or gds_data[0][0]==gds_tags.DICT['ANGLE']:
                    temp=gds_data.pop(0)
                    temp_list.append(temp)
                    if gds_data[0][0]==gds_tags.DICT['ANGLE']:
                        temp=gds_data.pop(0)
                        temp_list.append(temp)
                self._STRANS=GDS_STRANS()
                self._STRANS.read_binary_gds_stream(temp_list)
                temp_list=[]
                del temp_list
                
            elif temp[0]==gds_tags.DICT['XY']:
                self._XY=gds_record.GDS_XY()
                self._XY.read_binary_gds_stream(temp[0], temp[1])
            elif temp[0]==gds_tags.DICT['STRING']:
                self._STRING=gds_record.GDS_STRING()
                self._STRING.read_binary_gds_stream(temp[0], temp[1])
                break


class GDS_STRANS():
    def __init__(self,gds_data=None):
        self._STRANS=None
        self._MAG=None
        self._ANGLE=None
        
    def write_binary_gds_stream(self,binary_gds_stream):
        self._STRANS.write_binary_gds_stream(binary_gds_stream)
        if self._MAG!=None:
            self._MAG.write_binary_gds_stream(binary_gds_stream)
        if self._ANGLE!=None:
            self._ANGLE.write_binary_gds_stream(binary_gds_stream)
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            if temp[0]==gds_tags.DICT['STRANS']:
                
                self._STRANS=gds_record.GDS_STRANS()
                self._STRANS.read_binary_gds_stream(temp[0], temp[1])
                
            elif temp[0]==gds_tags.DICT['MAG']:
                self._MAG=gds_record.GDS_MAG()
                self._MAG.read_binary_gds_stream(temp[0], temp[1])
            elif temp[0]==gds_tags.DICT['ANGLE']:
                self._ANGLE=gds_record.GDS_ANGLE()
                self._ANGLE.read_binary_gds_stream(temp[0], temp[1])
            if gds_data==[]:
                break

class GDS_PROPERTY():
    def __init__(self,gds_data=None):
        self._PROPATTR=None
        self._PROPVALUE=None
    def write_binary_gds_stream(self,binary_gds_stream):
            self._PROPATTR.write_binary_gds_stream(binary_gds_stream)
            self._PROPVALUE.write_binary_gds_stream(binary_gds_stream)
    def read_binary_gds_stream(self,gds_data):
        while True:
            temp=gds_data.pop(0)
            if temp[0]==gds_tags.DICT['PROPATTR']:
                self._PROPATTR=gds_record.GDS_PROPATTR()
                self._PROPATTR.read_binary_gds_stream(temp[0], temp[1])
            elif temp[0]==gds_tags.DICT['PROPVALUE']:
                self._PROPVALUE=gds_record.GDS_PROPVALUE()
                self._PROPVALUE.read_binary_gds_stream(temp[0], temp[1])
                break
                
    
        
        