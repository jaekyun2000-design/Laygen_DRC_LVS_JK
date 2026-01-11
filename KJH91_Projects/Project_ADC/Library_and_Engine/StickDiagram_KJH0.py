import numpy as np
import copy
import math

from . import StickDiagram


class _StickDiagram_KJH(StickDiagram._StickDiagram):

    def __init__(self):
        pass

    def n_for3(self,flag,tmp1:list,tmp2:list,tmp3:list,j):

            if flag<len(tmp1)-1:

                if flag==0:
                    for i in range(0,len(tmp1[flag])):
                        tmp2.append([tmp1[flag][i]])
                        tmp2, tmp3, j = self.n_for3(flag+1,tmp1,tmp2,tmp3,j)
                        #tmp3.append(tmp2)
                        tmp3=copy.deepcopy(tmp3)
                        del tmp2[flag:]

                else:
                    for i in range(0,len(tmp1[flag])):
                        tmp2.append([tmp1[flag][i]])
                        tmp2, tmp3, j = self.n_for3(flag+1,tmp1,tmp2,tmp3,j)
                        #tmp3.append(tmp2)
                        tmp3=copy.deepcopy(tmp3)
                        del tmp2[flag:]


            else:
                tmp = []
                for j in range(0,len(tmp1[flag])):
                    tmp.append( tmp1[flag][j] )
                    tmp2.append(tmp)
                    tmp3.append(tmp2)
                    tmp3=copy.deepcopy(tmp3)
                    del tmp2[flag:]
                    tmp=[]

            return tmp2,tmp3,j



    def get_rot_coord(self,origin:list,p1:list,angle):

        distance = math.sqrt( (p1[0]-origin[0])**2 + (p1[1]-origin[1])**2)

        if distance == 0:
            p2_X = p1[0]
            p2_Y = p1[1]

        else:
            cosx = math.cos(angle*math.pi/180)
            sinx = math.sin(angle*math.pi/180)
            cosy = (p1[0]-origin[0])/distance
            siny = (p1[1]-origin[1])/distance

            p2_X = distance * ( cosx*cosy - sinx*siny ) + origin[0]
            p2_Y = distance * ( sinx*cosy + cosx*siny ) + origin[1]

        p2 = [p2_X, p2_Y]

        return p2

    def get_param_KJH(self,*hier_element_tuple:str):

        '''Manual
        Function:
                    Returns center_coordinates, four_edges, four_boundaries, XYwidths and area of Boundary_element
                    Returns point1|2_coordinates, center_coordinates, four_edges, four_boundaries, XYwidths and area of path_element
                    Returns center_coordinates of Sref_element
        Assumption:
                    For path_element, path_element must be two point connection.
        '''
        #Error if self._DesignParameter does not exist
        if '_DesignParameter' not in self.__dict__:
                raise Exception("There is no DesignParameter.")

        #Transform Tuple to list
        HierElementList = list(hier_element_tuple)

        #Error if the most top Hierelement name does not exist in self._DesignParameter
        if HierElementList[0] not in self._DesignParameter:
            raise Exception(f"Invalid Hierarchy element name: {HierElementList[0]}")

        #Define element
        element = self._DesignParameter[HierElementList.pop(0)]

        #Define XYcooridnate of most top hier element
        _XYcoor_top_element = [element['_XYCoordinates']]
        elementXY = [element['_XYCoordinates']]

        #Go to bottom hierarchy
        for hierarchy_element in HierElementList:

            #Error if hierelement name is wrong
            if hierarchy_element not in element['_DesignObj']._DesignParameter:
                raise Exception(f"Invalid Hierarchy element name: {hierarchy_element}.")

            #Go to bottom; buildup element name
            element = element['_DesignObj']._DesignParameter[hierarchy_element]

            #append XYcoord
            elementXY.append(element['_XYCoordinates'])

        #Accumulate XYcoord
        elementXY_Xaccum = 0
        elementXY_Yaccum = 0
        for i in range(0,len(HierElementList)):
            if len(elementXY[i]) != 0:
                elementXY_Xaccum = elementXY_Xaccum + elementXY[i][0][0]
                elementXY_Yaccum = elementXY_Yaccum + elementXY[i][0][1]
            else:
                pass

        #Check _DesignParametertype
        if element['_DesignParametertype'] == 1:    # 1: Boundary, 2: Path, 3: Sref

            tmp=[]
            for i in range (0,len(element['_XYCoordinates'])):

                #Define parameters
                if len(HierElementList) == 0:
                    center_XYcoord = [ elementXY[0][0][0], elementXY[0][0][1] ]
                else:
                    center_XYcoord = [ element['_XYCoordinates'][i][0]+elementXY_Xaccum, element['_XYCoordinates'][i][1]+elementXY_Yaccum ]

                left_XYcoord    = [ center_XYcoord[0] - 0.5*element['_XWidth'] , center_XYcoord[1] ]
                right_XYcoord   = [ center_XYcoord[0] + 0.5*element['_XWidth'] , center_XYcoord[1] ]
                up_XYcoord      = [ center_XYcoord[0], center_XYcoord[1] + 0.5*element['_YWidth'] ]
                down_XYcoord    = [ center_XYcoord[0], center_XYcoord[1] - 0.5*element['_YWidth'] ]

                up_right     = [ right_XYcoord[0], up_XYcoord[1] ]
                up_left      = [ left_XYcoord[0],  up_XYcoord[1] ]
                down_right   = [ right_XYcoord[0], down_XYcoord[1] ]
                down_left    = [ left_XYcoord[0],  down_XYcoord[1] ]

                xwidth = right_XYcoord[0] - left_XYcoord[0]
                ywidth = up_XYcoord[1] - down_XYcoord[1]

                area = xwidth * ywidth

                #Gen dictionary
                a = locals()['param_{}'.format(i)] = dict(
                                                        _XY_cent = center_XYcoord,
                                                        _XY_left = left_XYcoord,
                                                        _XY_right = right_XYcoord,
                                                        _XY_up    = up_XYcoord,
                                                        _XY_down  = down_XYcoord,
                                                        _XY_up_right = up_right,
                                                        _XY_up_left  = up_left,
                                                        _XY_down_right = down_right,
                                                        _XY_down_left  = down_left,
                                                        _Xwidth =  xwidth,
                                                        _Ywidth =  ywidth,
                                                        _Area   =  area,
                                                      )

                tmp.append(a)

        #Check _DesignParametertype
        if element['_DesignParametertype'] == 2:    # 1: Boundary, 2: Path, 3: Sref

            tmp=[]
            for i in range (0,len(element['_XYCoordinates'])):

                #Define parameters
                P1_XYcoord = [ element['_XYCoordinates'][i][0][0]+elementXY_Xaccum, element['_XYCoordinates'][i][0][1]+elementXY_Yaccum  ]
                P2_XYcoord = [ element['_XYCoordinates'][i][1][0]+elementXY_Xaccum, element['_XYCoordinates'][i][1][1]+elementXY_Yaccum  ]

                center_XYcoord = [ 0.5*(P1_XYcoord[0]+P2_XYcoord[0]), 0.5*(P1_XYcoord[1]+P2_XYcoord[1]) ]

                if P1_XYcoord[1] == P2_XYcoord[1] and P1_XYcoord[0] != P2_XYcoord[0]:
                    xwidth = abs(P1_XYcoord[0] - P2_XYcoord[0])
                    ywidth = element['_Width']

                elif P1_XYcoord[0] == P2_XYcoord[0] and P1_XYcoord[1] != P2_XYcoord[1]:
                    xwidth = element['_Width']
                    ywidth = abs(P1_XYcoord[1] - P2_XYcoord[1])
                else:
                    raise Exception(f"assumption error kjh")

                left_XYcoord    = [ center_XYcoord[0] - 0.5*xwidth , center_XYcoord[1] ]
                right_XYcoord   = [ center_XYcoord[0] + 0.5*xwidth , center_XYcoord[1] ]
                up_XYcoord      = [ center_XYcoord[0], center_XYcoord[1] + 0.5*ywidth ]
                down_XYcoord    = [ center_XYcoord[0], center_XYcoord[1] - 0.5*ywidth ]

                up_right     = [ right_XYcoord[0], up_XYcoord[1] ]
                up_left      = [ left_XYcoord[0],  up_XYcoord[1] ]
                down_right   = [ right_XYcoord[0], down_XYcoord[1] ]
                down_left    = [ left_XYcoord[0],  down_XYcoord[1] ]

                area = xwidth * ywidth

                #Gen dictionary
                a = locals()['param_{}'.format(i)] = dict(
                                                        _XY_p1  = P1_XYcoord,
                                                        _XY_p2  = P2_XYcoord,
                                                        _XY_cent = center_XYcoord,
                                                        _XY_left = left_XYcoord,
                                                        _XY_right = right_XYcoord,
                                                        _XY_up    = up_XYcoord,
                                                        _XY_down  = down_XYcoord,
                                                        _XY_up_right = up_right,
                                                        _XY_up_left  = up_left,
                                                        _XY_down_right = down_right,
                                                        _XY_down_left  = down_left,
                                                        _Xwidth =  xwidth,
                                                        _Ywidth =  ywidth,
                                                        _Area   =  area,
                                                      )

                tmp.append(a)

        #Check _DesignParametertype
        if element['_DesignParametertype'] == 3:    # 1: Boundary, 2: Path, 3: Sref

            if len(HierElementList) == 0:
                XYcoord = [ elementXY[0][0][0], elementXY[0][0][1] ]
            else:
                XYcoord = [ element['_XYCoordinates'][0][0]+elementXY_Xaccum, element['_XYCoordinates'][0][1]+elementXY_Yaccum ]

            tmp=[]
            a = _XY_sref = XYcoord
            tmp.append(a)

        return tmp

    def trans_coord_KJH(self,ref_coord,type,_XWidth,_YWidth):
        '''Manual
        Function:
                    Returns center_coordinates
                    move type_coord to ref_coord and calculate corresponding center_coord
        '''

        if type=='_XY_cent':
            center = [ ref_coord[0],ref_coord[1] ]
        elif type=='_XY_left':
            center = [ ref_coord[0]+0.5*_XWidth,ref_coord[1] ]
        elif type=='_XY_right':
            center = [ ref_coord[0]-0.5*_XWidth,ref_coord[1] ]
        elif type=='_XY_up':
            center = [ ref_coord[0],ref_coord[1]-0.5*_YWidth ]
        elif type=='_XY_down':
            center = [ ref_coord[0],ref_coord[1]+0.5*_YWidth ]
        elif type=='_XY_up_right':
            center = [ ref_coord[0]-0.5*_XWidth,ref_coord[1]-0.5*_YWidth ]
        elif type=='_XY_up_left':
            center = [ ref_coord[0]+0.5*_XWidth,ref_coord[1]-0.5*_YWidth ]
        elif type=='_XY_down_right':
            center = [ ref_coord[0]-0.5*_XWidth,ref_coord[1]+0.5*_YWidth ]
        elif type=='_XY_down_left':
            center = [ ref_coord[0]+0.5*_XWidth,ref_coord[1]+0.5*_YWidth ]
        else:
            raise Exception(f"typo error kjh")

        return center
   
    def get_param_ovlp_KJH(self,element1:dict,element2:dict):
        '''Manual
        Function:
                    Returns parameters of overlapped area of element1 and element2.
        '''
        if element1['_XY_up'][1] >= element2['_XY_up'][1]:
            tmp_up = element2['_XY_up'][1]
        else:
            tmp_up = element1['_XY_up'][1]

        if element1['_XY_down'][1] >= element2['_XY_down'][1]:
            tmp_down = element1['_XY_down'][1]
        else:
            tmp_down = element2['_XY_down'][1]

        if element1['_XY_right'][0] >= element2['_XY_right'][0]:
            tmp_right = element2['_XY_right'][0]
        else:
            tmp_right = element1['_XY_right'][0]

        if element1['_XY_left'][0] >= element2['_XY_left'][0]:
            tmp_left = element1['_XY_left'][0]
        else:
            tmp_left = element2['_XY_left'][0]

        #Define parameters
        up_right     = [ tmp_right,tmp_up  ]
        up_left      = [ tmp_left,tmp_up ]
        down_right   = [ tmp_right,tmp_down ]
        down_left    = [ tmp_left,tmp_down ]

        left_XYcoord    = [ 0.5*(up_left[0]+down_left[0]), 0.5*(up_left[1]+down_left[1]) ]
        right_XYcoord  = [ 0.5*(up_right[0]+down_right[0]), 0.5*(up_right[1]+down_right[1]) ]
        up_XYcoord      = [ 0.5*(up_left[0]+up_right[0]), 0.5*(up_left[1]+up_right[1]) ]
        down_XYcoord    = [ 0.5*(down_left[0]+down_right[0]), 0.5*(down_left[1]+down_right[1]) ]

        center_XYcoord = [ 0.5*(left_XYcoord[0]+right_XYcoord[0]), 0.5*(left_XYcoord[1]+right_XYcoord[1]) ]

        xwidth = abs(right_XYcoord[0] - left_XYcoord[0])
        ywidth = abs(up_XYcoord[1] - down_XYcoord[1])

        area = xwidth * ywidth

        #Gen dictionary
        tmp=[]
        a =  dict(
                    _XY_cent = center_XYcoord,
                    _XY_left = left_XYcoord,
                    _XY_right = right_XYcoord,
                    _XY_up    = up_XYcoord,
                    _XY_down  = down_XYcoord,
                    _XY_up_right = up_right,
                    _XY_up_left  = up_left,
                    _XY_down_right = down_right,
                    _XY_down_left  = down_left,
                    _Xwidth =  xwidth,
                    _Ywidth =  ywidth,
                    _Area   =  area,
                  )

        tmp.append(a)

        return tmp

    def get_param_KJH1(self,*hier_element_tuple:str):

        '''Manual
        Function:
                    Returns center_coordinates, four_edges, four_boundaries, XYwidths and area of Boundary_element
                    Returns point1|2_coordinates, center_coordinates, four_edges, four_boundaries, XYwidths and area of path_element
                    Returns center_coordinates of Sref_element
        Assumption:
                    For path_element, path_element must be two point connection.
        '''
        #Error if self._DesignParameter does not exist
        if '_DesignParameter' not in self.__dict__:
                raise Exception("There is no DesignParameter.")

        #Transform Tuple to list
        HierElementList = list(hier_element_tuple)

        #For top hier_element, referencing structure is exceptional
            #Error if the most top Hierelement name does not exist in self._DesignParameter
        if HierElementList[0] not in self._DesignParameter:
            raise Exception(f"Invalid Hierarchy element name: {HierElementList[0]}")

            #Referencing top hier_element
        element = self._DesignParameter[HierElementList[0]]

            #Define XYcooridnate of most top hier_element
        elementXY = [copy.deepcopy(element['_XYCoordinates'])]


        #For general hier_elements, referencing structure is <element>['_DesignObj']._DesignParameter[next_element]
            #Go to bottom hierarchy
        for hierarchy_element in HierElementList[1:]:

            #Error if hierelement name is wrong
            if hierarchy_element not in element['_DesignObj']._DesignParameter:
                raise Exception(f"Invalid Hierarchy element name: {hierarchy_element}.")

            #Go to bottom; buildup element name
            element = element['_DesignObj']._DesignParameter[hierarchy_element]

            #append XYcoord
            elementXY.append(element['_XYCoordinates'])


        #Builup and Accumulate for XYcoord of bottom hier_element
        tmp = []
        for i in range(0,len(elementXY)):

            #trans list to array
            tmp.append(np.array(elementXY[i]))

            #This is XYcoordinates of bot_element
        bot_elementXY=sum(tmp)

        #Check _DesignParametertype
        if element['_DesignParametertype'] == 1:    # 1: Boundary, 2: Path, 3: Sref

            tmp=[]
            for i in range (0,len(bot_elementXY)):

                center_XYcoord = bot_elementXY[i]

                left_XYcoord    = [ center_XYcoord[0] - 0.5*element['_XWidth'] , center_XYcoord[1] ]
                right_XYcoord   = [ center_XYcoord[0] + 0.5*element['_XWidth'] , center_XYcoord[1] ]
                up_XYcoord      = [ center_XYcoord[0], center_XYcoord[1] + 0.5*element['_YWidth'] ]
                down_XYcoord    = [ center_XYcoord[0], center_XYcoord[1] - 0.5*element['_YWidth'] ]

                up_right     = [ right_XYcoord[0], up_XYcoord[1] ]
                up_left      = [ left_XYcoord[0],  up_XYcoord[1] ]
                down_right   = [ right_XYcoord[0], down_XYcoord[1] ]
                down_left    = [ left_XYcoord[0],  down_XYcoord[1] ]

                xwidth = right_XYcoord[0] - left_XYcoord[0]
                ywidth = up_XYcoord[1] - down_XYcoord[1]

                area = xwidth * ywidth

                #Gen dictionary
                a = locals()['param_{}'.format(i)] = dict(
                                                        _XY_cent = center_XYcoord,
                                                        _XY_left = left_XYcoord,
                                                        _XY_right = right_XYcoord,
                                                        _XY_up    = up_XYcoord,
                                                        _XY_down  = down_XYcoord,
                                                        _XY_up_right = up_right,
                                                        _XY_up_left  = up_left,
                                                        _XY_down_right = down_right,
                                                        _XY_down_left  = down_left,
                                                        _Xwidth =  xwidth,
                                                        _Ywidth =  ywidth,
                                                        _Area   =  area,
                                                      )

                tmp.append(a)

        #Check _DesignParametertype
        if element['_DesignParametertype'] == 2:    # 1: Boundary, 2: Path, 3: Sref

            tmp=[]
            # i-th path where the path structure [ [p1,p2], [p2,p3], ...  ] and the 1-th path is [p1,p2]
            for i in range(0,len(bot_elementXY)):

                P1_XYcoord = bot_elementXY[i][0]
                P2_XYcoord = bot_elementXY[i][1]

                center_XYcoord = [ 0.5*(P1_XYcoord[0]+P2_XYcoord[0]), 0.5*(P1_XYcoord[1]+P2_XYcoord[1]) ]

                if P1_XYcoord[1] == P2_XYcoord[1] and P1_XYcoord[0] != P2_XYcoord[0]:
                    xwidth = abs(P1_XYcoord[0] - P2_XYcoord[0])
                    ywidth = element['_Width']

                elif P1_XYcoord[0] == P2_XYcoord[0] and P1_XYcoord[1] != P2_XYcoord[1]:
                    xwidth = element['_Width']
                    ywidth = abs(P1_XYcoord[1] - P2_XYcoord[1])
                else:
                    raise Exception(f"assumption error kjh")

                left_XYcoord    = [ center_XYcoord[0] - 0.5*xwidth , center_XYcoord[1] ]
                right_XYcoord   = [ center_XYcoord[0] + 0.5*xwidth , center_XYcoord[1] ]
                up_XYcoord      = [ center_XYcoord[0], center_XYcoord[1] + 0.5*ywidth ]
                down_XYcoord    = [ center_XYcoord[0], center_XYcoord[1] - 0.5*ywidth ]

                up_right     = [ right_XYcoord[0], up_XYcoord[1] ]
                up_left      = [ left_XYcoord[0],  up_XYcoord[1] ]
                down_right   = [ right_XYcoord[0], down_XYcoord[1] ]
                down_left    = [ left_XYcoord[0],  down_XYcoord[1] ]

                area = xwidth * ywidth

            #Gen dictionary
                a = locals()['param_{}'.format(i)] = dict(
                                                        _XY_p1  = P1_XYcoord,
                                                        _XY_p2  = P2_XYcoord,
                                                        _XY_cent = center_XYcoord,
                                                        _XY_left = left_XYcoord,
                                                        _XY_right = right_XYcoord,
                                                        _XY_up    = up_XYcoord,
                                                        _XY_down  = down_XYcoord,
                                                        _XY_up_right = up_right,
                                                        _XY_up_left  = up_left,
                                                        _XY_down_right = down_right,
                                                        _XY_down_left  = down_left,
                                                        _Xwidth =  xwidth,
                                                        _Ywidth =  ywidth,
                                                        _Area   =  area,
                                                      )

                tmp.append(a)

        #Check _DesignParametertype
        if element['_DesignParametertype'] == 3:    # 1: Boundary, 2: Path, 3: Sref

            XYcoord = bot_elementXY

            tmp=[]
            a = _XY_sref = XYcoord
            tmp.append(a)

        return tmp

    def get_param_KJH2(self,*hier_element_tuple:str):

        '''Manual
        Function:
                    Returns center_coordinates, four_edges, four_boundaries, XYwidths and area of Boundary_element
                    Returns point1|2_coordinates, center_coordinates, four_edges, four_boundaries, XYwidths and area of path_element
                    Returns center_coordinates of Sref_element
        Assumption:
                    For path_element, path_element must be two point connection. #####
        '''
        #Error if self._DesignParameter does not exist
        if '_DesignParameter' not in self.__dict__:
                raise Exception("There is no DesignParameter.")

        #Transform Tuple to list
        HierElementList = list(hier_element_tuple)

        #For top hier_element, referencing structure is exceptional
            #Error if the most top Hierelement name does not exist in self._DesignParameter
        if HierElementList[0] not in self._DesignParameter:
            raise Exception(f"Invalid Hierarchy element name: {HierElementList[0]}")

            #Referencing top hier_element
        element = self._DesignParameter[HierElementList[0]]

            #Define XYcooridnate of most top hier_element
        elementXY = [copy.deepcopy(element['_XYCoordinates'])]

        if element['_DesignParametertype'] == 3:
                #Define Sref Reflection
            element_Reflection = [copy.deepcopy(element['_Reflect'])]

                #Define Sref Angle
            element_Angle = [copy.deepcopy(element['_Angle'])]

                #Sref element flags
            element_Sref_flag = [1]
        else:
                #Define Sref Reflection
            element_Reflection = [[-1,-1,-1]]

                #Define Sref Angle
            element_Angle = [-360]

                #Sref element flags
            element_Sref_flag = [0]


        #For general hier_elements, referencing structure is <element>['_DesignObj']._DesignParameter[next_element]
            #Go to bottom hierarchy
        for hierarchy_element in HierElementList[1:]:

                #Error if hierelement name is wrong
            if hierarchy_element not in element['_DesignObj']._DesignParameter:
                raise Exception(f"Invalid Hierarchy element name: {hierarchy_element}.")

                #Go to bottom; buildup element name
            element = element['_DesignObj']._DesignParameter[hierarchy_element]

                #append XYcoord
            elementXY.append(element['_XYCoordinates'])

                #append _Reflection
                    #append _Reflectoin if Sref
            if element['_DesignParametertype'] == 3:
                element_Reflection.append(element['_Reflect'])
            else:
                element_Reflection.append([-1, -1, -1])

                #append _Angle
                    #append _Angle if Sref
            if element['_DesignParametertype'] == 3:
                element_Angle.append(element['_Angle'])
            else:
                element_Angle.append(-360)

                #append Boundary flag
                    #append Boundary flag
            if element['_DesignParametertype'] == 3:
                element_Sref_flag.append(1)
            else:
                element_Sref_flag.append(0)

        #Reverse list for bottom up strategy.
        reverse_element_Angle       = list(reversed(element_Angle))
        reverse_element_Reflection  = list(reversed(element_Reflection))
        reverse_element_Sref_flag   = list(reversed(element_Sref_flag))
            #reverse_elementXY
                #Re-organize for the calculation
        tmp1 = elementXY
        tmp2 = []
        tmp3 = []
        trash1, result3, trash2 = self.n_for3(0, tmp1 , tmp2, tmp3, 0)

        reverse_elementXY=[]
        for i in range(0,len(result3)):
            reverse_elementXY.append(list(reversed(result3[i])))
        del result3, trash1, trash2

        #Check _DesignParametertype of bottom
        if element['_DesignParametertype'] == 1:    # 1: Boundary, 2: Path, 3: Sref
            tmp = []

            for i in range(0,len(reverse_elementXY)):

                for j in range(0,len(reverse_elementXY[i])):
                    #define XYorigin
                    XYorigin = reverse_elementXY[i][j][0]

                    #Calculate most bottom coord
                    if j == 0:
                        tmp_XY_cent         = [0,0]
                        tmp_XY_left         = [ tmp_XY_cent[0] - 0.5*element['_XWidth'], tmp_XY_cent[1] ]
                        tmp_XY_right        = [ tmp_XY_cent[0] + 0.5*element['_XWidth'], tmp_XY_cent[1] ]
                        tmp_XY_up           = [ tmp_XY_cent[0], tmp_XY_cent[1] + 0.5*element['_YWidth'] ]
                        tmp_XY_down         = [ tmp_XY_cent[0], tmp_XY_cent[1] - 0.5*element['_YWidth'] ]
                        tmp_XY_up_right     = [ tmp_XY_right[0], tmp_XY_up[1] ]
                        tmp_XY_up_left      = [ tmp_XY_left[0], tmp_XY_up[1] ]
                        tmp_XY_down_right   = [ tmp_XY_right[0], tmp_XY_down[1] ]
                        tmp_XY_down_left    = [ tmp_XY_left[0], tmp_XY_down[1] ]
                        tmp_xwidth          = abs( tmp_XY_right[0] - tmp_XY_left[0] )
                        tmp_ywidth          = abs( tmp_XY_up[1] - tmp_XY_down[1] )
                        tmp_area            = tmp_xwidth * tmp_ywidth

                    #Change XYcoord for new origin
                    tmp_XY_cent       = np.array(XYorigin) + np.array(tmp_XY_cent)
                    tmp_XY_left       = np.array(XYorigin) + np.array(tmp_XY_left)
                    tmp_XY_right      = np.array(XYorigin) + np.array(tmp_XY_right)
                    tmp_XY_up         = np.array(XYorigin) + np.array(tmp_XY_up)
                    tmp_XY_down       = np.array(XYorigin) + np.array(tmp_XY_down)
                    tmp_XY_up_right   = np.array(XYorigin) + np.array(tmp_XY_up_right)
                    tmp_XY_up_left    = np.array(XYorigin) + np.array(tmp_XY_up_left)
                    tmp_XY_down_right = np.array(XYorigin) + np.array(tmp_XY_down_right)
                    tmp_XY_down_left  = np.array(XYorigin) + np.array(tmp_XY_down_left)


                    #Reflectoin and rotation calculation when Sref.
                    if reverse_element_Sref_flag[j] == 1:
                            #if reflection, reflect to Ydirection based on XYorigin
                        if reverse_element_Reflection[j] is not None:
                            if reverse_element_Reflection[j][0]==1:
                                tmp_XY_cent[1]       = 2*XYorigin[1] - tmp_XY_cent[1]
                                tmp_XY_left[1]       = 2*XYorigin[1] - tmp_XY_left[1]
                                tmp_XY_right[1]      = 2*XYorigin[1] - tmp_XY_right[1]
                                tmp_XY_up[1]         = 2*XYorigin[1] - tmp_XY_up[1]
                                tmp_XY_down[1]       = 2*XYorigin[1] - tmp_XY_down[1]
                                tmp_XY_up_right[1]   = 2*XYorigin[1] - tmp_XY_up_right[1]
                                tmp_XY_up_left[1]    = 2*XYorigin[1] - tmp_XY_up_left[1]
                                tmp_XY_down_right[1] = 2*XYorigin[1] - tmp_XY_down_right[1]
                                tmp_XY_down_left[1]  = 2*XYorigin[1] - tmp_XY_down_left[1]
                        if reverse_element_Angle[j] is not None:
                            #Rotation calculation
                            tmp_XY_cent         = self.get_rot_coord(XYorigin,tmp_XY_cent,reverse_element_Angle[j])
                            tmp_XY_left         = self.get_rot_coord(XYorigin,tmp_XY_left,reverse_element_Angle[j])
                            tmp_XY_right        = self.get_rot_coord(XYorigin,tmp_XY_right,reverse_element_Angle[j])
                            tmp_XY_up           = self.get_rot_coord(XYorigin,tmp_XY_up,reverse_element_Angle[j])
                            tmp_XY_down         = self.get_rot_coord(XYorigin,tmp_XY_down,reverse_element_Angle[j])
                            tmp_XY_up_right     = self.get_rot_coord(XYorigin,tmp_XY_up_right,reverse_element_Angle[j])
                            tmp_XY_up_left      = self.get_rot_coord(XYorigin,tmp_XY_up_left,reverse_element_Angle[j])
                            tmp_XY_down_right   = self.get_rot_coord(XYorigin,tmp_XY_down_right,reverse_element_Angle[j])
                            tmp_XY_down_left    = self.get_rot_coord(XYorigin,tmp_XY_down_left,reverse_element_Angle[j])

                #Gen dictionary
                a = locals()['param_{}'.format(i)] = dict(
                                                        _XY_cent        = tmp_XY_cent,
                                                        _XY_left        = tmp_XY_left,
                                                        _XY_right       = tmp_XY_right,
                                                        _XY_up          = tmp_XY_up,
                                                        _XY_down        = tmp_XY_down,
                                                        _XY_up_right    = tmp_XY_up_right,
                                                        _XY_up_left     = tmp_XY_up_left,
                                                        _XY_down_right  = tmp_XY_down_right,
                                                        _XY_down_left   = tmp_XY_down_left,
                                                        _Xwidth         = tmp_xwidth,
                                                        _Ywidth         = tmp_ywidth,
                                                        _Area           = tmp_area,
                                                      )
                tmp.append(a)

        #Check _DesignParametertype of bottom
        if element['_DesignParametertype'] == 2:    # 1: Boundary, 2: Path, 3: Sref
            tmp = []

            #
            for i in range(0,len(reverse_elementXY)):

                for j in range(0,len(reverse_elementXY[i])):

                    #define XYorigin
                    if j ==0:
                        XYorigin = ( np.array(reverse_elementXY[i][j][0][0]) + np.array(reverse_elementXY[i][j][0][1]) ) * 0.5
                    else:
                        XYorigin = reverse_elementXY[i][j][0]

                    #Calculate most bottom coord
                    if j == 0:
                        #calcuate tmp_XY_cent for initialization
                        tmp_p1              = reverse_elementXY[i][j][0][0]
                        tmp_p2              = reverse_elementXY[i][j][0][1]
                        tmp_XY_cent         = ( np.array(reverse_elementXY[i][j][0][0]) + np.array(reverse_elementXY[i][j][0][1]) ) * 0.5

                        #initialize every points
                        tmp_p1              = np.array(tmp_p1) - np.array(tmp_XY_cent)
                        tmp_p2              = np.array(tmp_p2) - np.array(tmp_XY_cent)
                        tmp_XY_cent         = [0,0]

                            #Define _XWidth and _YWidth
                        if tmp_p1[1] == tmp_p2[1] and tmp_p1[0] != tmp_p2[0]:
                            tmp_xwidth = abs(tmp_p1[0] - tmp_p2[0])
                            tmp_ywidth = element['_Width']
                        elif tmp_p1[0] == tmp_p2[0] and tmp_p1[1] != tmp_p2[1]:
                            tmp_xwidth = element['_Width']
                            tmp_ywidth = abs(tmp_p1[1] - tmp_p2[1])
                        else:
                            raise Exception(f"assumption error kjh")

                        tmp_XY_left         = [ tmp_XY_cent[0] - 0.5*tmp_xwidth, tmp_XY_cent[1] ]
                        tmp_XY_right        = [ tmp_XY_cent[0] + 0.5*tmp_xwidth, tmp_XY_cent[1] ]
                        tmp_XY_up           = [ tmp_XY_cent[0], tmp_XY_cent[1] + 0.5*tmp_ywidth ]
                        tmp_XY_down         = [ tmp_XY_cent[0], tmp_XY_cent[1] - 0.5*tmp_ywidth ]
                        tmp_XY_up_right     = [ tmp_XY_right[0], tmp_XY_up[1] ]
                        tmp_XY_up_left      = [ tmp_XY_left[0], tmp_XY_up[1] ]
                        tmp_XY_down_right   = [ tmp_XY_right[0], tmp_XY_down[1] ]
                        tmp_XY_down_left    = [ tmp_XY_left[0], tmp_XY_down[1] ]
                        #tmp_xwidth          = abs( tmp_XY_right[0] - tmp_XY_left[0] )
                        #tmp_ywidth          = abs( tmp_XY_up[1] - tmp_XY_down[1] )
                        tmp_area            = tmp_xwidth * tmp_ywidth

                    #Change XYcoord for new origin
                    tmp_p1            = np.array(XYorigin) + np.array(tmp_p1)
                    tmp_p2            = np.array(XYorigin) + np.array(tmp_p2)
                    tmp_XY_cent       = np.array(XYorigin) + np.array(tmp_XY_cent)
                    tmp_XY_left       = np.array(XYorigin) + np.array(tmp_XY_left)
                    tmp_XY_right      = np.array(XYorigin) + np.array(tmp_XY_right)
                    tmp_XY_up         = np.array(XYorigin) + np.array(tmp_XY_up)
                    tmp_XY_down       = np.array(XYorigin) + np.array(tmp_XY_down)
                    tmp_XY_up_right   = np.array(XYorigin) + np.array(tmp_XY_up_right)
                    tmp_XY_up_left    = np.array(XYorigin) + np.array(tmp_XY_up_left)
                    tmp_XY_down_right = np.array(XYorigin) + np.array(tmp_XY_down_right)
                    tmp_XY_down_left  = np.array(XYorigin) + np.array(tmp_XY_down_left)

                    #Reflectoin and rotation calculation when Sref.
                    if reverse_element_Sref_flag[j] == 1:
                            #if reflection, reflect to Ydirection based on XYorigin
                        if reverse_element_Reflection[j] is not None:
                            if reverse_element_Reflection[j][0]==1:
                                tmp_p1[1]            = 2*XYorigin[1] - tmp_p1[1]
                                tmp_p2[1]            = 2*XYorigin[1] - tmp_p2[1]
                                tmp_XY_cent[1]       = 2*XYorigin[1] - tmp_XY_cent[1]
                                tmp_XY_left[1]       = 2*XYorigin[1] - tmp_XY_left[1]
                                tmp_XY_right[1]      = 2*XYorigin[1] - tmp_XY_right[1]
                                tmp_XY_up[1]         = 2*XYorigin[1] - tmp_XY_up[1]
                                tmp_XY_down[1]       = 2*XYorigin[1] - tmp_XY_down[1]
                                tmp_XY_up_right[1]   = 2*XYorigin[1] - tmp_XY_up_right[1]
                                tmp_XY_up_left[1]    = 2*XYorigin[1] - tmp_XY_up_left[1]
                                tmp_XY_down_right[1] = 2*XYorigin[1] - tmp_XY_down_right[1]
                                tmp_XY_down_left[1]  = 2*XYorigin[1] - tmp_XY_down_left[1]
                        if reverse_element_Angle[j] is not None:
                            #Rotation calculation
                            tmp_p1              = self.get_rot_coord(XYorigin,tmp_p1,reverse_element_Angle[j])
                            tmp_p2              = self.get_rot_coord(XYorigin,tmp_p2,reverse_element_Angle[j])
                            tmp_XY_cent         = self.get_rot_coord(XYorigin,tmp_XY_cent,reverse_element_Angle[j])
                            tmp_XY_left         = self.get_rot_coord(XYorigin,tmp_XY_left,reverse_element_Angle[j])
                            tmp_XY_right        = self.get_rot_coord(XYorigin,tmp_XY_right,reverse_element_Angle[j])
                            tmp_XY_up           = self.get_rot_coord(XYorigin,tmp_XY_up,reverse_element_Angle[j])
                            tmp_XY_down         = self.get_rot_coord(XYorigin,tmp_XY_down,reverse_element_Angle[j])
                            tmp_XY_up_right     = self.get_rot_coord(XYorigin,tmp_XY_up_right,reverse_element_Angle[j])
                            tmp_XY_up_left      = self.get_rot_coord(XYorigin,tmp_XY_up_left,reverse_element_Angle[j])
                            tmp_XY_down_right   = self.get_rot_coord(XYorigin,tmp_XY_down_right,reverse_element_Angle[j])
                            tmp_XY_down_left    = self.get_rot_coord(XYorigin,tmp_XY_down_left,reverse_element_Angle[j])

                #Gen dictionary
                a = locals()['param_{}'.format(i)] = dict(
                                                        _XY_p1          = tmp_p1,
                                                        _XY_p2          = tmp_p2,
                                                        _XY_cent        = tmp_XY_cent,
                                                        _XY_left        = tmp_XY_left,
                                                        _XY_right       = tmp_XY_right,
                                                        _XY_up          = tmp_XY_up,
                                                        _XY_down        = tmp_XY_down,
                                                        _XY_up_right    = tmp_XY_up_right,
                                                        _XY_up_left     = tmp_XY_up_left,
                                                        _XY_down_right  = tmp_XY_down_right,
                                                        _XY_down_left   = tmp_XY_down_left,
                                                        _Xwidth         = tmp_xwidth,
                                                        _Ywidth         = tmp_ywidth,
                                                        _Area           = tmp_area,
                                                      )
                tmp.append(a)


        #Check _DesignParametertype of bottom
        if element['_DesignParametertype'] == 3:    # 1: Boundary, 2: Path, 3: Sref
            tmp = []

            #
            for i in range(0,len(reverse_elementXY)):

                for j in range(0,len(reverse_elementXY[i])):

                    #Define XYorigin
                    XYorigin = reverse_elementXY[i][j][0]

                    #Calculate most bottom coord
                    if j == 0:
                        tmp_XY_cent = [0,0]

                    #Change XYcoord for new origin
                    tmp_XY_cent = np.array(XYorigin) + np.array(tmp_XY_cent)

                    #Reflectoin and rotation calculation when Sref.
                    if reverse_element_Sref_flag[j] == 1:
                        if reverse_element_Reflection[j] is not None:
                                #if reflection, reflect to Ydirection based on XYorigin
                            if reverse_element_Reflection[j][0]==1:
                                tmp_XY_cent[1] = 2*XYorigin[1] - tmp_XY_cent[1]
                        if reverse_element_Angle[j] is not None:
                            #Rotation calculation
                            tmp_XY_cent = self.get_rot_coord(XYorigin,tmp_XY_cent,reverse_element_Angle[j])

                #Gen dictionary
                a = locals()['param_{}'.format(i)] = dict(
                                                            _XY_cent        = tmp_XY_cent,
                                                          )
                tmp.append(a)

        return tmp


    def get_Bcoord_KJH(self,target_coord,approaching_type,B_XWidth,B_YWidth):
        '''Manual
        Function:
                    Returns center_coordinates
                    move approaching_type_coord to target_coord and calculate corresponding center_coord
                    exactly same as trans_coord_KJH1
        '''

        if approaching_type=='_XY_cent':
            center = [ target_coord[0],target_coord[1] ]
        elif approaching_type=='_XY_left':
            center = [ target_coord[0]+0.5*B_XWidth,target_coord[1] ]
        elif approaching_type=='_XY_right':
            center = [ target_coord[0]-0.5*B_XWidth,target_coord[1] ]
        elif approaching_type=='_XY_up':
            center = [ target_coord[0],target_coord[1]-0.5*B_YWidth ]
        elif approaching_type=='_XY_down':
            center = [ target_coord[0],target_coord[1]+0.5*B_YWidth ]
        elif approaching_type=='_XY_up_right':
            center = [ target_coord[0]-0.5*B_XWidth,target_coord[1]-0.5*B_YWidth ]
        elif approaching_type=='_XY_up_left':
            center = [ target_coord[0]+0.5*B_XWidth,target_coord[1]-0.5*B_YWidth ]
        elif approaching_type=='_XY_down_right':
            center = [ target_coord[0]-0.5*B_XWidth,target_coord[1]+0.5*B_YWidth ]
        elif approaching_type=='_XY_down_left':
            center = [ target_coord[0]+0.5*B_XWidth,target_coord[1]+0.5*B_YWidth ]
        else:
            raise Exception(f"typo error kjh")

        return center



    def get_Scoord_KJH(self,target_coord:list,approaching_coord:list,Scoord:list):

        '''Manual
        Function:
                    Returns origin_coordinates whose bottom_element coordinate matchs to target coordinate
        '''

        #Get relative coord between approaching_coord and Scoord
        relative_coord = np.array(approaching_coord) - np.array(Scoord)

        #Get displacement_coord between approaching_coord and target_coord
        displacement_coord = np.array(target_coord) - np.array(approaching_coord)

        #New Scoord
        S_XYcoord = np.array(Scoord)+np.array(displacement_coord)
        #S_XYcoord = np.round(S_XYcoord,2)
        S_XYcoord = np.round(S_XYcoord,3)

        return S_XYcoord

    def get_Scoord_KJH4(self,target_coord:list,approaching_coord:list,Scoord:list):

        '''Manual
        Function:
                    Returns origin_coordinates whose bottom_element coordinate matchs to target coordinate
        '''

        #Get relative coord between approaching_coord and Scoord
        relative_coord = np.array(approaching_coord) - np.array(Scoord)

        #Get displacement_coord between approaching_coord and target_coord
        displacement_coord = np.array(target_coord) - np.array(approaching_coord)

        #New Scoord
        S_XYcoord = np.array(Scoord)+np.array(displacement_coord)
        S_XYcoord = S_XYcoord

        return S_XYcoord


    def get_ovlp_coord_KJH(self,element1:dict,element2:dict):
        '''Manual
        Function:
                    Returns parameters of overlapped area of element1 and element2.
                    Element 1 and 2 can be parameter of either boundary_element or path_element
        '''

        #check if element1 or element2 is tilted
        tilt_sensing1 = np.array(element1['_XY_up']) - np.array(element1['_XY_down'])
        tilt_sensing2 = np.array(element2['_XY_up']) - np.array(element2['_XY_down'])
        if tilt_sensing1[0] == 0 or tilt_sensing1[1] == 0:
            pass
        else:
            raise Exception(f"get_ovlp_coord_KJH: element1 tilt")

        if tilt_sensing2[0] == 0 or tilt_sensing2[1] == 0:
            pass
        else:
            raise Exception(f"get_ovlp_coord_KJH: element2 tilt")

        #Re-define up down right left
            #element1
        element1_ymax = max ( element1['_XY_up'][1], element1['_XY_down'][1], element1['_XY_right'][1], element1['_XY_left'][1]  )
        element1_ymin = min ( element1['_XY_up'][1], element1['_XY_down'][1], element1['_XY_right'][1], element1['_XY_left'][1]  )
        element1_xmax = max ( element1['_XY_up'][0], element1['_XY_down'][0], element1['_XY_right'][0], element1['_XY_left'][0]  )
        element1_xmin = min ( element1['_XY_up'][0], element1['_XY_down'][0], element1['_XY_right'][0], element1['_XY_left'][0]  )
            #element2
        element2_ymax = max ( element2['_XY_up'][1], element2['_XY_down'][1], element2['_XY_right'][1], element2['_XY_left'][1]  )
        element2_ymin = min ( element2['_XY_up'][1], element2['_XY_down'][1], element2['_XY_right'][1], element2['_XY_left'][1]  )
        element2_xmax = max ( element2['_XY_up'][0], element2['_XY_down'][0], element2['_XY_right'][0], element2['_XY_left'][0]  )
        element2_xmin = min ( element2['_XY_up'][0], element2['_XY_down'][0], element2['_XY_right'][0], element2['_XY_left'][0]  )

        if element1_ymax >= element2_ymax:
            tmp_up = element2_ymax
        else:
            tmp_up = element1_ymax

        if element1_ymin >= element2_ymin:
            tmp_down = element1_ymin
        else:
            tmp_down = element2_ymin

        if element1_xmax >= element2_xmax:
            tmp_right = element2_xmax
        else:
            tmp_right = element1_xmax

        if element1_xmin >= element2_xmin:
            tmp_left = element1_xmin
        else:
            tmp_left = element2_xmin

        #Check overlapped
        if tmp_left > tmp_right or tmp_down > tmp_up:
            raise Exception(f"get_ovlp_coord_KJH: No overlap")
        else:
            pass

        #Define parameters
        up_right     = [ tmp_right,tmp_up  ]
        up_left      = [ tmp_left,tmp_up ]
        down_right   = [ tmp_right,tmp_down ]
        down_left    = [ tmp_left,tmp_down ]

        left_XYcoord    = [ 0.5*(up_left[0]+down_left[0]), 0.5*(up_left[1]+down_left[1]) ]
        right_XYcoord   = [ 0.5*(up_right[0]+down_right[0]), 0.5*(up_right[1]+down_right[1]) ]
        up_XYcoord      = [ 0.5*(up_left[0]+up_right[0]), 0.5*(up_left[1]+up_right[1]) ]
        down_XYcoord    = [ 0.5*(down_left[0]+down_right[0]), 0.5*(down_left[1]+down_right[1]) ]

        center_XYcoord = [ 0.5*(left_XYcoord[0]+right_XYcoord[0]), 0.5*(left_XYcoord[1]+right_XYcoord[1]) ]

        xwidth = abs(right_XYcoord[0] - left_XYcoord[0])
        ywidth = abs(up_XYcoord[1] - down_XYcoord[1])

        area = xwidth * ywidth

        #Gen dictionary
        tmp=[]
        a =  dict(
                    _XY_cent = center_XYcoord,
                    _XY_left = left_XYcoord,
                    _XY_right = right_XYcoord,
                    _XY_up    = up_XYcoord,
                    _XY_down  = down_XYcoord,
                    _XY_up_right = up_right,
                    _XY_up_left  = up_left,
                    _XY_down_right = down_right,
                    _XY_down_left  = down_left,
                    _Xwidth =  xwidth,
                    _Ywidth =  ywidth,
                    _Area   =  area,
                  )

        tmp.append(a)

        return tmp