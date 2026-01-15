import numpy as np
import copy
import math

from . import StickDiagram_KJH0
from . import DRC
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters


class _StickDiagram_KJH(StickDiagram_KJH0._StickDiagram_KJH):

	def __init__(self):
		pass

##################################################################################################################################################
	def get_rot_coord(self,origin:list,p1:list,angle):
		'''
		Manual
		: This is used in get_param_KJHx for applying Sref angle
		'''

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

	def iterative_forloop_calculation(self,N,element,structure_list:list,XYcoord:list,XYcoord_Hier:list,Reflection:list,Angle:list,Type:list):
		'''
		Manual
		: This function used in get_param_KJHx for calculating parameter
		'''
		number_of_iteration = len(XYcoord)

		#If not bottom
		if N < (number_of_iteration-1):
			for i in range(0,len(XYcoord[N])):
				self.iterative_forloop_calculation(N+1,element,structure_list[i],XYcoord,XYcoord_Hier[i],Reflection,Angle,Type)


		#Bottom hiear
		else:
			for i in range(0,len(XYcoord[N])):
				#If boundary element
				if Type[N] == 1:

					for j in range(0,len(XYcoord)):

						#Calculate Parameter of target element
						XYorigin = XYcoord_Hier[i][0][-1-1*j]
							#Most bottom
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

						tmp_XY_cent       = np.array(XYorigin) + np.array(tmp_XY_cent)
						tmp_XY_left       = np.array(XYorigin) + np.array(tmp_XY_left)
						tmp_XY_right      = np.array(XYorigin) + np.array(tmp_XY_right)
						tmp_XY_up         = np.array(XYorigin) + np.array(tmp_XY_up)
						tmp_XY_down       = np.array(XYorigin) + np.array(tmp_XY_down)
						tmp_XY_up_right   = np.array(XYorigin) + np.array(tmp_XY_up_right)
						tmp_XY_up_left    = np.array(XYorigin) + np.array(tmp_XY_up_left)
						tmp_XY_down_right = np.array(XYorigin) + np.array(tmp_XY_down_right)
						tmp_XY_down_left  = np.array(XYorigin) + np.array(tmp_XY_down_left)

						#Apply Reflection and Rotation
							#If Sref than apply Reflection and Rotation
						if Type[-1-1*j] == 3:
								#Apply Reflectoin: Reflect to Ydirection based on XYorigin
							if Reflection[-1-1*j][0] == 1 :
								tmp_XY_cent[1]       = 2*XYorigin[1] - tmp_XY_cent[1]
								tmp_XY_left[1]       = 2*XYorigin[1] - tmp_XY_left[1]
								tmp_XY_right[1]      = 2*XYorigin[1] - tmp_XY_right[1]
								tmp_XY_up[1]         = 2*XYorigin[1] - tmp_XY_up[1]
								tmp_XY_down[1]       = 2*XYorigin[1] - tmp_XY_down[1]
								tmp_XY_up_right[1]   = 2*XYorigin[1] - tmp_XY_up_right[1]
								tmp_XY_up_left[1]    = 2*XYorigin[1] - tmp_XY_up_left[1]
								tmp_XY_down_right[1] = 2*XYorigin[1] - tmp_XY_down_right[1]
								tmp_XY_down_left[1]  = 2*XYorigin[1] - tmp_XY_down_left[1]

								#Apply Rotation
							if Angle[-1*j] is not None:
								tmp_XY_cent         = self.get_rot_coord(XYorigin,tmp_XY_cent,Angle[-1-1*j])
								tmp_XY_left         = self.get_rot_coord(XYorigin,tmp_XY_left,Angle[-1-1*j])
								tmp_XY_right        = self.get_rot_coord(XYorigin,tmp_XY_right,Angle[-1-1*j])
								tmp_XY_up           = self.get_rot_coord(XYorigin,tmp_XY_up,Angle[-1-1*j])
								tmp_XY_down         = self.get_rot_coord(XYorigin,tmp_XY_down,Angle[-1-1*j])
								tmp_XY_up_right     = self.get_rot_coord(XYorigin,tmp_XY_up_right,Angle[-1-1*j])
								tmp_XY_up_left      = self.get_rot_coord(XYorigin,tmp_XY_up_left,Angle[-1-1*j])
								tmp_XY_down_right   = self.get_rot_coord(XYorigin,tmp_XY_down_right,Angle[-1-1*j])
								tmp_XY_down_left    = self.get_rot_coord(XYorigin,tmp_XY_down_left,Angle[-1-1*j])


							#If not Sref, There is no Reflection and Rotation
						else:
							pass

					#Make dictionary
					tmp = dict(
									_XY_cent         = np.round(tmp_XY_cent,2),
									_XY_left         = np.round(tmp_XY_left,2),
									_XY_right        = np.round(tmp_XY_right,2),
									_XY_up           = np.round(tmp_XY_up,2),
									_XY_down         = np.round(tmp_XY_down,2),
									_XY_up_right     = np.round(tmp_XY_up_right,2),
									_XY_up_left      = np.round(tmp_XY_up_left,2),
									_XY_down_right   = np.round(tmp_XY_down_right,2),
									_XY_down_left    = np.round(tmp_XY_down_left,2),
									_Xwidth          = np.round(tmp_xwidth,2),
									_Ywidth          = np.round(tmp_ywidth,2),
									_Area            = np.round(tmp_area,2)  ,
					)

					#
					tmp1 = copy.deepcopy(tmp)
					structure_list[i].append(tmp1)

				#If path element
				if Type[N] == 2:
					for j in range(0,len(XYcoord)):
						#Define XYorigin
						if j ==0:
							XYorigin = ( np.array(XYcoord_Hier[i][0][-1-1*j][0]) + np.array(XYcoord_Hier[i][0][-1-1*j][1]) ) * 0.5
						else:
							XYorigin = XYcoord_Hier[i][0][-1-1*j]

						#Calculate most bottom coord
						if j == 0:
							#calcuate tmp_XY_cent for initialization
							tmp_p1              = XYcoord_Hier[i][0][-1-1*j][0]
							tmp_p2              = XYcoord_Hier[i][0][-1-1*j][1]
							tmp_XY_cent         = ( np.array(XYcoord_Hier[i][0][-1-1*j][0]) + np.array(XYcoord_Hier[i][0][-1-1*j][1]) ) * 0.5

							#initialize every points: change origin to [0,0]
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
								raise Exception(f"assumption error kjh: Path is not Hrz or Vtc ")

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

						#Apply Reflection and Rotation
							#If Sref than apply Reflection and Rotation
						if Type[-1-1*j] == 3:
								#Apply Reflectoin: Reflect to Ydirection based on XYorigin
							if Reflection[-1-1*j][0] == 1 :
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

								#Apply Rotation
							if Angle[-1*j] is not None:
								tmp_p1              = self.get_rot_coord(XYorigin,tmp_p1,Angle[-1-1*j])
								tmp_p2              = self.get_rot_coord(XYorigin,tmp_p2,Angle[-1-1*j])
								tmp_XY_cent         = self.get_rot_coord(XYorigin,tmp_XY_cent,Angle[-1-1*j])
								tmp_XY_left         = self.get_rot_coord(XYorigin,tmp_XY_left,Angle[-1-1*j])
								tmp_XY_right        = self.get_rot_coord(XYorigin,tmp_XY_right,Angle[-1-1*j])
								tmp_XY_up           = self.get_rot_coord(XYorigin,tmp_XY_up,Angle[-1-1*j])
								tmp_XY_down         = self.get_rot_coord(XYorigin,tmp_XY_down,Angle[-1-1*j])
								tmp_XY_up_right     = self.get_rot_coord(XYorigin,tmp_XY_up_right,Angle[-1-1*j])
								tmp_XY_up_left      = self.get_rot_coord(XYorigin,tmp_XY_up_left,Angle[-1-1*j])
								tmp_XY_down_right   = self.get_rot_coord(XYorigin,tmp_XY_down_right,Angle[-1-1*j])
								tmp_XY_down_left    = self.get_rot_coord(XYorigin,tmp_XY_down_left,Angle[-1-1*j])


							#If not Sref, There is no Reflection and Rotation
						else:
							pass
  
					#Make dictionary
					tmp = dict(
									_XY_p1           = np.round(tmp_p1,2),
									_XY_p2           = np.round(tmp_p2,2),
									_XY_cent         = np.round(tmp_XY_cent,2),
									_XY_left         = np.round(tmp_XY_left,2),
									_XY_right        = np.round(tmp_XY_right,2),
									_XY_up           = np.round(tmp_XY_up,2),
									_XY_down         = np.round(tmp_XY_down,2),
									_XY_up_right     = np.round(tmp_XY_up_right,2),
									_XY_up_left      = np.round(tmp_XY_up_left,2),
									_XY_down_right   = np.round(tmp_XY_down_right,2),
									_XY_down_left    = np.round(tmp_XY_down_left,2),
									_Xwidth          = np.round(tmp_xwidth,2)    ,
									_Ywidth          = np.round(tmp_ywidth,2),
									_Area            = np.round(tmp_area,2)  ,
					)

					#
					tmp1 = copy.deepcopy(tmp)
					structure_list[i].append(tmp1)
  

				#If Sref element
				if Type[N] == 3:
					for j in range(0,len(XYcoord)):

						#Define XYorigin
						XYorigin = XYcoord_Hier[i][0][-1-1*j]

						#Calculate most bottom coord
						if j == 0:
							tmp_XY_cent = [0,0]

						#Change XYcoord for new origin
						tmp_XY_cent = np.array(XYorigin) + np.array(tmp_XY_cent)

						#Apply Reflection and Rotation
							#If Sref than apply Reflection and Rotation
						if Type[-1-1*j] == 3:
								#Apply Reflectoin: Reflect to Ydirection based on XYorigin
							if Reflection[-1-1*j][0] == 1 :
								tmp_XY_cent[1] = 2*XYorigin[1] - tmp_XY_cent[1]

								#Apply Rotation
							if Angle[-1*j] is not None:
								tmp_XY_cent = self.get_rot_coord(XYorigin,tmp_XY_cent,Angle[-1-1*j])

							#If not Sref, There is no Reflection and Rotation
						else:
							pass

					#Make dictionary
					tmp = dict(

									_XY_cent         = np.round(tmp_XY_cent,2),

					)

					#
					tmp1 = copy.deepcopy(tmp)
					structure_list[i].append(tmp1)

		return structure_list


	def iterative_forloop(self,N,tmp:list,structure_list:list,XYcoord:list):
		'''
		Manual
		: This function is used in get_param_KJH3 to re-organize XYcoordinate of target element for structural referencing.
		This fills an hiearachical empty-list which is built ahead with hiearachical XYcoordinates
		To fills the list, This function automatically iterate forloop ntimes according to its' element
		'''
		number_of_iteration = len(XYcoord)

		#If not bottom
		if N < (number_of_iteration-1):

			for i in range(0,len(XYcoord[N])):
				tmp2 = copy.deepcopy(tmp)
				tmp2.append(XYcoord[N][i])
				self.iterative_forloop(N+1,tmp2,structure_list[i],XYcoord)

		#Bottom hiear
		else:
			for i in range(0,len(XYcoord[N])):
				tmp3 = copy.deepcopy(tmp)
				tmp3.append(XYcoord[N][i])
				structure_list[i].append(tmp3)

		return structure_list

	def empty_list_gen(self,N,empty_list:list,XYcoord:list):
		'''
		Manual
		: This function generates empty-list which have size of target element
		its generated list is used for the following "iterative_forloop" function.
		'''
		number_of_iteration = len(XYcoord)

		if N < (number_of_iteration-1):
			result = []
			for i in range(0,len(XYcoord[N])):
				result2 = self.empty_list_gen(N+1,empty_list,XYcoord)
				result.append(result2)
		else:
			tmp = []
			for i in range(0,len(XYcoord[N])):
				tmp.append([])
			result = copy.deepcopy(tmp)

		return result



	def get_param_KJH3(self,*hier_element_tuple:str):

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

		#Referencing the most top hierachical element(Because the referencing structure differ from the other)
			#Error if the most top Hierelement name does not exist in self._DesignParameter
		if HierElementList[0] not in self._DesignParameter:
			raise Exception(f"Invalid Hierarchy element name: {HierElementList[0]}")

			#Referencing top hier_element
		element = self._DesignParameter[HierElementList[0]]

			#Record XYcoord,Reflection,Angle,element_type
				#If the most top hier_element is Sref type
		if element['_DesignParametertype'] == 3:
				#Define XYcooridnate of most top hier_element
			element_XYcoord     = [copy.deepcopy(element['_XYCoordinates'])]
				#Define Sref Reflection
			element_Reflection  = [copy.deepcopy(element['_Reflect'])]
				#Define Sref Angle
			element_Angle       = [copy.deepcopy(element['_Angle'])]
				#Sref element flags: 1=Boundary, 2=Path, 3=Sref
			element_Type_flag   = [3]

				#If the most top hier_element is Path type
		elif element['_DesignParametertype'] == 2:
				#Define XYcooridnate of most top hier_element
			element_XYcoord     = [copy.deepcopy(element['_XYCoordinates'])]
				#Define Sref Reflection
			element_Reflection  = [[-1,-1,-1]]
				#Define Sref Angle
			element_Angle       = [-360]
				#Sref element flags: 1=Boundary, 2=Path, 3=Sref
			element_Type_flag   = [2]

				#If the most top hier_element is Boundary type
		else:
				#Define XYcooridnate of most top hier_element
			element_XYcoord     = [copy.deepcopy(element['_XYCoordinates'])]
				#Define Sref Reflection
			element_Reflection  = [[-1,-1,-1]]
				#Define Sref Angle
			element_Angle       = [-360]
				#Sref element flags: 1=Boundary, 2=Path, 3=Sref
			element_Type_flag   = [1]
  
		#Referencing the sub-hierachical element
			#Search from 2nd most hiearchy to bottom one.
		for hierarchy_element in HierElementList[1:]:

			#Error if hierelement name is wrong
			if hierarchy_element not in element['_DesignObj']._DesignParameter:
				raise Exception(f"Invalid Hierarchy element name: {hierarchy_element}.")

			#Building-up element name
			element = element['_DesignObj']._DesignParameter[hierarchy_element]

			#Record XYcoord,Reflection,Angle,element_type
				#If the sub_element is Sref type
			if element['_DesignParametertype'] == 3:
				#Define XYcooridnate of most top hier_element
				element_XYcoord.append(element['_XYCoordinates'])
				#Define Sref Reflection
				element_Reflection.append(element['_Reflect'])
				#Define Sref Angle
				element_Angle.append(element['_Angle'])
				#Sref element flags: 1=Boundary, 2=Path, 3=Sref
				element_Type_flag.append(3)

				#If the sub_element is Path type
			elif element['_DesignParametertype'] == 2:
				#Define XYcooridnate of most top hier_element
				element_XYcoord.append(element['_XYCoordinates'])
				#Define Sref Reflection
				element_Reflection.append([-1,-1,-1])
				#Define Sref Angle
				element_Angle.append(-360)
				#Sref element flags: 1=Boundary, 2=Path, 3=Sref
				element_Type_flag.append(2)

				#If the sub_element is Boundary type
			else:
				#Define XYcooridnate of most top hier_element
				element_XYcoord.append(element['_XYCoordinates'])
				#Define Sref Reflection
				element_Reflection.append([-1,-1,-1])
				#Define Sref Angle
				element_Angle.append(-360)
				#Sref element flags: 1=Boundary, 2=Path, 3=Sref
				element_Type_flag.append(1)

		#Re-organize element_XYcoord for hierachical referencing
			#Making empty list
		N = 0
		empty_list =[[]]
		structure_list = self.empty_list_gen(N,empty_list,element_XYcoord)
		structure_list2 = copy.deepcopy(structure_list)
			#Re-organize element_XYcoord for hierachical referencing
		N = 0
		tmp = []
		element_Hier_XYcoord = self.iterative_forloop(N,tmp,structure_list,element_XYcoord)
  
		#Cal Parameter of target element
		N = 0
		Calculation_result = self.iterative_forloop_calculation(N,element,structure_list2,element_XYcoord,element_Hier_XYcoord,element_Reflection,element_Angle,element_Type_flag)

		return Calculation_result











##################################################################################################################################################


	def iterative_forloop_getparam(self,N,Hier_list:list,Param_list:list,Ref_list:list,result:list):
		'''
		Manual
		:
		'''


		#Go to bottom
		if N < (len(Hier_list)):

			for i in range(0,len(Param_list)):
				Param_list_tmp = copy.deepcopy(Param_list[i])
				Ref_list_tmp = copy.deepcopy(Ref_list)
				Ref_list_tmp.append(i)
				self.iterative_forloop_getparam(N+1,Hier_list,Param_list_tmp,Ref_list_tmp,result)

		#Bottom hiear
		else:
			tmp2 = copy.deepcopy(Param_list)
			tmp2.append(Hier_list)
			tmp2.append(Ref_list)
			result.append(tmp2)

		return result


	def iterative_forloop_finding(self,result:list,tmp:list,element:dict):
		'''
		Manual
		:
		'''

		#Building up
		element_list = list(element.keys())

		#If go to bottom
		if '_DesignObj' in element_list:
			#Building up element
			element = element['_DesignObj']._DesignParameter
			#list up
			element_list = list(element.keys())

			#check which is sub-module
			for sub_element in element_list:
				if sub_element == '_XYcoordAsCent': continue
				# 1,2,3 are boundary,path,sref, repectively
				if element['{}'.format(sub_element)]['_DesignParametertype'] < 4 :
					tmp1 = copy.deepcopy(tmp)
					tmp1.append(sub_element)
					self.iterative_forloop_finding(result,tmp1,element['{}'.format(sub_element)])

				else:
					pass

		#reach to bottom
		else:
			tmp1 = copy.deepcopy(tmp)
			result.append(tmp1)


		return result


	def get_outter_KJH(self,*hier_element_tuple:str):

		#Error if self._DesignParameter does not exist
		if '_DesignParameter' not in self.__dict__:
				raise Exception("There is no DesignParameter.")


		#Transform Tuple to list
		HierElementList = list(hier_element_tuple)

		#Referencing the most top hierachical element(Because the referencing structure differ from the other)
			#Error if the most top Hierelement name does not exist in self._DesignParameter
		if HierElementList[0] not in self._DesignParameter:
			raise Exception(f"Invalid Hierarchy element name: {HierElementList[0]}")

			#Referencing top hier_element
		element = self._DesignParameter[HierElementList[0]]


		#Referencing the sub-hierachical element
			#Search from 2nd most hiearchy to bottom one.
		for hierarchy_element in HierElementList[1:]:

			#Error if hierelement name is wrong
			if hierarchy_element not in element['_DesignObj']._DesignParameter:
				raise Exception(f"Invalid Hierarchy element name: {hierarchy_element}.")

			#Building-up element name
			element = element['_DesignObj']._DesignParameter[hierarchy_element]


		#Finding every elements
		tmp = []
		result =[]
		result = self.iterative_forloop_finding(result,tmp,element)


		#Calculate parameter
		flatten_result = []
		for i in range(0,len(result)):

			#Calculate param
			#Param_list = self.get_param_KJH3('{}'.format(HierElementList[0]),*result[i])
			Param_list = self.get_param_KJH3(*HierElementList,*result[i])

			#flattening the parameter
			N=0
			Hier_list = copy.deepcopy(result[i])
			Hier_list = HierElementList + Hier_list
			Index_list = []
			result2 = []

			result2 = self.iterative_forloop_getparam(N,Hier_list,Param_list,Index_list,result2)
			flatten_result.append(result2)

		#flatten every element's parameter
		flatten_result2 = []
		for i in range(0,len(flatten_result)):
			for j in range(0,len(flatten_result[i])):
				flatten_result2.append(flatten_result[i][j])

		#find the most upper
		most_up_ycoord = []
		most_up_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_up_ycoord.append( flatten_result2[i][0]['_XY_up'][1] )
				most_up_index.append( i )
			else:
				if most_up_ycoord[0] > flatten_result2[i][0]['_XY_up'][1]:
					pass
				elif most_up_ycoord[0] < flatten_result2[i][0]['_XY_up'][1]:
					most_up_ycoord = []
					most_up_ycoord.append(flatten_result2[i][0]['_XY_up'][1])
					most_up_index = []
					most_up_index.append(i)
				elif most_up_ycoord[0] == flatten_result2[i][0]['_XY_up'][1]:
					most_up_ycoord.append(flatten_result2[i][0]['_XY_up'][1])
					most_up_index.append( i )

		#find the most down
		most_down_ycoord = []
		most_down_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_down_ycoord.append( flatten_result2[i][0]['_XY_down'][1] )
				most_down_index.append( i )
			else:
				if most_down_ycoord[0] < flatten_result2[i][0]['_XY_down'][1]:
					pass
				elif most_down_ycoord[0] > flatten_result2[i][0]['_XY_down'][1]:
					most_down_ycoord = []
					most_down_ycoord.append(flatten_result2[i][0]['_XY_down'][1])
					most_down_index = []
					most_down_index.append(i)
				elif most_down_ycoord[0] == flatten_result2[i][0]['_XY_down'][1]:
					most_down_ycoord.append(flatten_result2[i][0]['_XY_down'][1])
					most_down_index.append( i )

		#find the most right
		most_right_xcoord = []
		most_right_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_right_xcoord.append( flatten_result2[i][0]['_XY_right'][0] )
				most_right_index.append( i )
			else:
				if most_right_xcoord[0] > flatten_result2[i][0]['_XY_right'][0]:
					pass
				elif most_right_xcoord[0] < flatten_result2[i][0]['_XY_right'][0]:
					most_right_xcoord = []
					most_right_xcoord.append(flatten_result2[i][0]['_XY_right'][0])
					most_right_index = []
					most_right_index.append(i)
				elif most_right_xcoord[0] == flatten_result2[i][0]['_XY_right'][0]:
					most_right_xcoord.append(flatten_result2[i][0]['_XY_right'][0])
					most_right_index.append( i )

		#find the most left
		most_left_xcoord = []
		most_left_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_left_xcoord.append( flatten_result2[i][0]['_XY_left'][0] )
				most_left_index.append( i )
			else:
				if most_left_xcoord[0] < flatten_result2[i][0]['_XY_left'][0]:
					pass
				elif most_left_xcoord[0] > flatten_result2[i][0]['_XY_left'][0]:
					most_left_xcoord = []
					most_left_xcoord.append(flatten_result2[i][0]['_XY_left'][0])
					most_left_index = []
					most_left_index.append(i)
				elif most_left_xcoord[0] == flatten_result2[i][0]['_XY_left'][0]:
					most_left_xcoord.append(flatten_result2[i][0]['_XY_left'][0])
					most_left_index.append( i )

		tmp = dict(
						_Layername  = result,
						_Layercoord = flatten_result2,
						_Mostdown	= dict( index = most_down_index, 	coord = most_down_ycoord),
						_Mostleft	= dict( index = most_left_index, 	coord = most_left_xcoord),
						_Mostright	= dict( index = most_right_index, 	coord = most_right_xcoord),
						_Mostup		= dict( index = most_up_index, 		coord = most_up_ycoord),
				)


		#return flatten_result2, result,[most_down_index,most_down_ycoord], [most_left_index,most_left_xcoord], [most_right_index,most_right_xcoord], [most_up_index,most_up_ycoord]
		return tmp







##################################################################################################################################################

	def get_delete_KJH(self,*hier_element_tuple:str):

		#Error if self._DesignParameter does not exist
		if '_DesignParameter' not in self.__dict__:
				raise Exception("There is no DesignParameter.")


		#Transform Tuple to list
		HierElementList = list(hier_element_tuple)

		#Referencing the most top hierachical element(Because the referencing structure differ from the other)
			#Error if the most top Hierelement name does not exist in self._DesignParameter
		if HierElementList[0] not in self._DesignParameter:
			raise Exception(f"Invalid Hierarchy element name: {HierElementList[0]}")

			#Referencing top hier_element
		element = self._DesignParameter[HierElementList[0]]


		#Referencing the sub-hierachical element
			#Search from 2nd most hiearchy to bottom one.
		for hierarchy_element in HierElementList[1:]:

			#Error if hierelement name is wrong
			if hierarchy_element not in element['_DesignObj']._DesignParameter:
				raise Exception(f"Invalid Hierarchy element name: {hierarchy_element}.")

			#Building-up element name
			element = element['_DesignObj']._DesignParameter[hierarchy_element]

		Fucking = self._DesignParameter.keys()

		del Fucking




##################################################################################################################################################

	def get_ovlp_KJH2(self,element1:dict,element2:dict):
		'''Manual
		Function:
					Returns parameters of overlapped area of element1 and element2.
					Element 1 and 2 can be parameter of either boundary_element or path_element
					Element 1 and 2 must be squared form

					modified for having data structure of get_param_KJH3
					update: no matter inverted or not

		'''

		#Calculate up, down , left , right
			#element1
				#Up
		element1_most_up_ycoord = []
		element1_most_up_index = []
		for i in ['_XY_up','_XY_down','_XY_left','_XY_right']:
			if i == '_XY_up':
				element1_most_up_ycoord.append( element1['_XY_up'][1] )
				element1_most_up_index.append( i )
			else:
				if element1_most_up_ycoord[0] > element1['{}'.format(i)][1]:
					pass
				elif element1_most_up_ycoord[0] < element1['{}'.format(i)][1]:
					element1_most_up_ycoord = []
					element1_most_up_ycoord.append( element1['{}'.format(i)][1] )
					element1_most_up_index = []
					element1_most_up_index.append(i)
				elif element1_most_up_ycoord[0] == element1['{}'.format(i)][1]:
					element1_most_up_ycoord.append( element1['{}'.format(i)][1] )
					element1_most_up_index.append( i )

				#Down
		element1_most_down_ycoord = []
		element1_most_down_index = []
		for i in ['_XY_down','_XY_up','_XY_left','_XY_right']:
			if i == '_XY_down':
				element1_most_down_ycoord.append( element1['_XY_down'][1] )
				element1_most_down_index.append( i )
			else:
				if element1_most_down_ycoord[0] < element1['{}'.format(i)][1]:
					pass
				elif element1_most_down_ycoord[0] > element1['{}'.format(i)][1]:
					element1_most_down_ycoord = []
					element1_most_down_ycoord.append( element1['{}'.format(i)][1] )
					element1_most_down_index = []
					element1_most_down_index.append(i)
				elif element1_most_down_ycoord[0] == element1['{}'.format(i)][1]:
					element1_most_down_ycoord.append( element1['{}'.format(i)][1] )
					element1_most_down_index.append( i )

				#left
		element1_most_left_xcoord = []
		element1_most_left_index = []
		for i in ['_XY_left','_XY_down','_XY_up','_XY_right']:
			if i == '_XY_left':
				element1_most_left_xcoord.append( element1['_XY_left'][0] )
				element1_most_left_index.append( i )
			else:
				if element1_most_left_xcoord[0] < element1['{}'.format(i)][0]:
					pass
				elif element1_most_left_xcoord[0] > element1['{}'.format(i)][0]:
					element1_most_left_xcoord = []
					element1_most_left_xcoord.append( element1['{}'.format(i)][0] )
					element1_most_left_index = []
					element1_most_left_index.append(i)
				elif element1_most_left_xcoord[0] == element1['{}'.format(i)][0]:
					element1_most_left_xcoord.append( element1['{}'.format(i)][0] )
					element1_most_left_index.append( i )

				#right
		element1_most_right_xcoord = []
		element1_most_right_index = []
		for i in ['_XY_right','_XY_down','_XY_up','_XY_left']:
			if i == '_XY_right':
				element1_most_right_xcoord.append( element1['_XY_right'][0] )
				element1_most_right_index.append( i )
			else:
				if element1_most_right_xcoord[0] > element1['{}'.format(i)][0]:
					pass
				elif element1_most_right_xcoord[0] < element1['{}'.format(i)][0]:
					element1_most_right_xcoord = []
					element1_most_right_xcoord.append( element1['{}'.format(i)][0] )
					element1_most_right_index = []
					element1_most_right_index.append(i)
				elif element1_most_right_xcoord[0] == element1['{}'.format(i)][0]:
					element1_most_right_xcoord.append( element1['{}'.format(i)][0] )
					element1_most_right_index.append( i )

			#element2
				#Up
		element2_most_up_ycoord = []
		element2_most_up_index = []
		for i in ['_XY_up','_XY_down','_XY_left','_XY_right']:
			if i == '_XY_up':
				element2_most_up_ycoord.append( element1['_XY_up'][1] )
				element2_most_up_index.append( i )
			else:
				if element2_most_up_ycoord[0] > element1['{}'.format(i)][1]:
					pass
				elif element2_most_up_ycoord[0] < element1['{}'.format(i)][1]:
					element2_most_up_ycoord = []
					element2_most_up_ycoord.append( element1['{}'.format(i)][1] )
					element2_most_up_index = []
					element2_most_up_index.append(i)
				elif element2_most_up_ycoord[0] == element1['{}'.format(i)][1]:
					element2_most_up_ycoord.append( element1['{}'.format(i)][1] )
					element2_most_up_index.append( i )

				#Down
		element2_most_down_ycoord = []
		element2_most_down_index = []
		for i in ['_XY_down','_XY_up','_XY_left','_XY_right']:
			if i == '_XY_down':
				element2_most_down_ycoord.append( element1['_XY_down'][1] )
				element2_most_down_index.append( i )
			else:
				if element2_most_down_ycoord[0] < element1['{}'.format(i)][1]:
					pass
				elif element2_most_down_ycoord[0] > element1['{}'.format(i)][1]:
					element2_most_down_ycoord = []
					element2_most_down_ycoord.append( element1['{}'.format(i)][1] )
					element2_most_down_index = []
					element2_most_down_index.append(i)
				elif element2_most_down_ycoord[0] == element1['{}'.format(i)][1]:
					element2_most_down_ycoord.append( element1['{}'.format(i)][1] )
					element2_most_down_index.append( i )

				#left
		element2_most_left_xcoord = []
		element2_most_left_index = []
		for i in ['_XY_left','_XY_down','_XY_up','_XY_right']:
			if i == '_XY_left':
				element2_most_left_xcoord.append( element1['_XY_left'][0] )
				element2_most_left_index.append( i )
			else:
				if element2_most_left_xcoord[0] < element1['{}'.format(i)][0]:
					pass
				elif element2_most_left_xcoord[0] > element1['{}'.format(i)][0]:
					element2_most_left_xcoord = []
					element2_most_left_xcoord.append( element1['{}'.format(i)][0] )
					element2_most_left_index = []
					element2_most_left_index.append(i)
				elif element2_most_left_xcoord[0] == element1['{}'.format(i)][0]:
					element2_most_left_xcoord.append( element1['{}'.format(i)][0] )
					element2_most_left_index.append( i )

				#right
		element2_most_right_xcoord = []
		element2_most_right_index = []
		for i in ['_XY_right','_XY_down','_XY_up','_XY_left']:
			if i == '_XY_right':
				element2_most_right_xcoord.append( element1['_XY_right'][0] )
				element2_most_right_index.append( i )
			else:
				if element2_most_right_xcoord[0] > element1['{}'.format(i)][0]:
					pass
				elif element2_most_right_xcoord[0] < element1['{}'.format(i)][0]:
					element2_most_right_xcoord = []
					element2_most_right_xcoord.append( element1['{}'.format(i)][0] )
					element2_most_right_index = []
					element2_most_right_index.append(i)
				elif element2_most_right_xcoord[0] == element1['{}'.format(i)][0]:
					element2_most_right_xcoord.append( element1['{}'.format(i)][0] )
					element2_most_right_index.append( i )


		#Re-define up,down,left,right
		element1_up     = element1[element1_most_up_index[0]]
		element1_down   = element1[element1_most_down_index[0]]
		element1_left   = element1[element1_most_left_index[0]]
		element1_right  = element1[element1_most_right_index[0]]

		element2_up     = element2[element2_most_up_index[0]]
		element2_down   = element2[element2_most_down_index[0]]
		element2_left   = element2[element2_most_left_index[0]]
		element2_right  = element2[element2_most_right_index[0]]


		#check if element1 or element2 is tilted
		tilt_sensing1 = np.array(element1_up) - np.array(element1_down)
		tilt_sensing2 = np.array(element2_up) - np.array(element2_down)
		if tilt_sensing1[0] < 0.01 or tilt_sensing1[1] < 0.01:
			pass
		else:
			raise Exception(f"get_ovlp_coord_KJH: element1 tilt")

		if tilt_sensing2[0] <0.01 or tilt_sensing2[1] < 0.01:
			pass
		else:
			raise Exception(f"get_ovlp_coord_KJH: element2 tilt")

		#Re-define up down right left
			#element1
		element1_ymax = max ( element1_up[1], element1_down[1], element1_right[1], element1_left[1]  )
		element1_ymin = min ( element1_up[1], element1_down[1], element1_right[1], element1_left[1]  )
		element1_xmax = max ( element1_up[0], element1_down[0], element1_right[0], element1_left[0]  )
		element1_xmin = min ( element1_up[0], element1_down[0], element1_right[0], element1_left[0]  )
			#element2
		element2_ymax = max ( element2_up[1], element2_down[1], element2_right[1], element2_left[1]  )
		element2_ymin = min ( element2_up[1], element2_down[1], element2_right[1], element2_left[1]  )
		element2_xmax = max ( element2_up[0], element2_down[0], element2_right[0], element2_left[0]  )
		element2_xmin = min ( element2_up[0], element2_down[0], element2_right[0], element2_left[0]  )

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

##################################################################################################################################################

	@classmethod
	def _CalculateNumViaByXYWidth(cls, XWidth=None, YWidth=None, Mode=None):
		"""
		:param XWidth:
		:param YWidth:
		:param Mode:    None or 'MinEnclosureX' or 'MinEnclosureY'
		:return:
		"""

		_DRCObj = DRC.DRC()

		LengthBtwVias_case1 = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace
		LengthBtwVias_case2 = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2  # when exceeding 2x2 array (3x2 or 2x3, ...)

		if Mode == 'MinEnclosureX':
			MetMinEnclosureX = _DRCObj._Metal1MinEnclosureVia1
			MetMinEnclosureY = _DRCObj._Metal1MinEnclosureVia12
		elif Mode == 'MinEnclosureY':
			MetMinEnclosureX = _DRCObj._Metal1MinEnclosureVia12
			MetMinEnclosureY = _DRCObj._Metal1MinEnclosureVia1
		elif Mode == 'SameEnclosure':
			MetMinEnclosureX = _DRCObj._Metal1MinEnclosureVia3
			MetMinEnclosureY = _DRCObj._Metal1MinEnclosureVia3
		else:
			MetMinEnclosureX = _DRCObj._Metal1MinEnclosureVia12
			MetMinEnclosureY = _DRCObj._Metal1MinEnclosureVia12

		# MetMinEnclosureX = _DRCObj._Metal1MinEnclosureVia1 if (Mode is 'MinEnclosureX') else _DRCObj._Metal1MinEnclosureVia12
		# MetMinEnclosureY = _DRCObj._Metal1MinEnclosureVia1 if (Mode is 'MinEnclosureY') else _DRCObj._Metal1MinEnclosureVia12

		NumViaX_case1 = int((XWidth - 2*MetMinEnclosureX - _DRCObj._VIAxMinWidth) // LengthBtwVias_case1) + 1
		NumViaY_case1 = int((YWidth - 2*MetMinEnclosureY - _DRCObj._VIAxMinWidth) // LengthBtwVias_case1) + 1
		NumViaX_case2 = int((XWidth - 2*MetMinEnclosureX - _DRCObj._VIAxMinWidth) // LengthBtwVias_case2) + 1
		NumViaY_case2 = int((YWidth - 2*MetMinEnclosureY - _DRCObj._VIAxMinWidth) // LengthBtwVias_case2) + 1

		'''
		if (NumViaX_case1 > 2) and (NumViaY_case1 > 2):
			NumViaX = NumViaX_case2
			NumViaY = NumViaY_case2
		else:
			NumViaX = NumViaX_case1
			NumViaY = NumViaY_case1
		'''
		# when exceeding 2x2 array (3x2 or 2x3, ...)
		if (NumViaX_case1 > 2):
			if (NumViaY_case1 > 2):
				NumViaX = NumViaX_case2
				NumViaY = NumViaY_case2
			elif (NumViaY_case1 == 2):
				NumViaX = NumViaX_case2
				NumViaY = NumViaY_case2
			else:
				NumViaX = NumViaX_case1
				NumViaY = NumViaY_case1

		elif (NumViaX_case1 == 2):
			if (NumViaY_case1 > 2):
				NumViaX = NumViaX_case2
				NumViaY = NumViaY_case2
			elif (NumViaY_case1 == 2):
				NumViaX = NumViaX_case1
				NumViaY = NumViaY_case1
			else:
				NumViaX = NumViaX_case1
				NumViaY = NumViaY_case1
		else:
			if (NumViaY_case1 > 2):
				NumViaX = NumViaX_case1
				NumViaY = NumViaY_case1
			elif (NumViaY_case1 == 2):
				NumViaX = NumViaX_case1
				NumViaY = NumViaY_case1
			else:
				NumViaX = NumViaX_case1
				NumViaY = NumViaY_case1


		#if (NumViaX < 1) or (NumViaY < 1):
		#    raise NotImplementedError

		# print('NumViaX_case1', NumViaX_case1, 'NumViaY_case1', NumViaY_case1, 'NumViaX_case2', NumViaX_case2, 'NumViaY_case2', NumViaY_case2)

		return NumViaX, NumViaY

	@classmethod
	def CalcNumVia(cls, XWidth=None, YWidth=None):
		return cls._CalculateNumViaByXYWidth(XWidth=XWidth, YWidth=YWidth, Mode=None)

	@classmethod
	def CalcNumViaMinEnclosureX(cls, XWidth=None, YWidth=None):
		return cls._CalculateNumViaByXYWidth(XWidth=XWidth, YWidth=YWidth, Mode='MinEnclosureX')

	@classmethod
	def CalcNumViaMinEnclosureY(cls, XWidth=None, YWidth=None):
		return cls._CalculateNumViaByXYWidth(XWidth=XWidth, YWidth=YWidth, Mode='MinEnclosureY')

	@classmethod
	def CalcNumViaSameEnclosure(cls, XWidth=None, YWidth=None):
		return cls._CalculateNumViaByXYWidth(XWidth=XWidth, YWidth=YWidth, Mode='SameEnclosure')



##################################################################################################################################################

	def CenterCoordinateAndWidth2XYCoordinate_KJH(self, _XY_DownLeft, _WidthX, _WidthY):
		x_list = [ _XY_DownLeft[0], _XY_DownLeft[0] + _WidthX ]
		y_list = [ _XY_DownLeft[1], _XY_DownLeft[1] + _WidthY ]
		return self.MinMaxXY2XYCoordinate([x_list, y_list])

##################################################################################################################################################
	def get_rot_coord4(self, origin: list, p1: list, angle):
		'''
		Manual
		: This is used in get_param_KJHx for applying Sref angle
		'''

		# distance = math.sqrt((p1[0] - origin[0]) ** 2 + (p1[1] - origin[1]) ** 2)
		distance = np.sqrt(((int(p1[0]) - int(origin[0])) ** 2 + (int(p1[1]) - int(origin[1])) ** 2))

		if distance == 0:
			p2_X = p1[0]
			p2_Y = p1[1]

		else:
			cosx = math.cos(angle * math.pi / 180)
			sinx = math.sin(angle * math.pi / 180)
			cosy = (p1[0] - origin[0]) / distance
			siny = (p1[1] - origin[1]) / distance

			p2_X = distance * (cosx * cosy - sinx * siny) + origin[0]
			p2_Y = distance * (sinx * cosy + cosx * siny) + origin[1]

		p2 = [p2_X, p2_Y]

		return p2

	def iterative_forloop_calculation4(self, N, element, structure_list: list, XYcoord: list, XYcoord_Hier: list,Reflection: list, Angle: list, Type: list):
		'''
		Manual
		: This function used in get_param_KJHx for calculating parameter
		'''
		number_of_iteration = len(XYcoord)

		# If not bottom
		if N < (number_of_iteration - 1):
			for i in range(0, len(XYcoord[N])):
				self.iterative_forloop_calculation4(N + 1, element, structure_list[i], XYcoord, XYcoord_Hier[i],Reflection, Angle, Type)


		# Bottom hiear
		else:
			for i in range(0, len(XYcoord[N])):
				# If boundary element
				if Type[N] == 1:

					for j in range(0, len(XYcoord)):

						# Calculate Parameter of target element: XYorigin is down left for boundary element
						XYorigin = XYcoord_Hier[i][0][-1 - 1 * j]
						# Most bottom
						if j == 0:
							tmp_XY_down_left = [0, 0]

							tmp_XY_left         = [tmp_XY_down_left[0], tmp_XY_down_left[1] + 0.5 * element['_YWidth'] ]
							tmp_XY_right        = [tmp_XY_down_left[0] + 1 * element['_XWidth'], tmp_XY_down_left[1] + 0.5 * element['_YWidth']]
							tmp_XY_up           = [tmp_XY_down_left[0] + 0.5 * element['_XWidth'], tmp_XY_down_left[1] + 1 * element['_YWidth']]
							tmp_XY_down         = [tmp_XY_down_left[0] + 0.5 * element['_XWidth'], tmp_XY_down_left[1]]
							tmp_XY_up_right     = [tmp_XY_down_left[0] + 1 * element['_XWidth'], tmp_XY_down_left[1] + 1 * element['_YWidth']]
							tmp_XY_up_left      = [tmp_XY_down_left[0], tmp_XY_down_left[0] + 1 * element['_YWidth']]
							tmp_XY_down_right   = [tmp_XY_down_left[0] + 1 * element['_XWidth'], tmp_XY_down_left[1]]
							tmp_XY_cent         = [tmp_XY_down_left[0] + 0.5 * element['_XWidth'], tmp_XY_down_left[1] + 0.5 * element['_YWidth']]
							tmp_xwidth = abs(tmp_XY_right[0] - tmp_XY_left[0])
							tmp_ywidth = abs(tmp_XY_up[1] - tmp_XY_down[1])
							tmp_area = tmp_xwidth * tmp_ywidth

						# Round for cent, left, right, up, down
						tmp_XY_cent         = np.round(tmp_XY_cent)
						tmp_XY_left         = np.round(tmp_XY_left)
						tmp_XY_right        = np.round(tmp_XY_right)
						tmp_XY_up           = np.round(tmp_XY_up)
						tmp_XY_down         = np.round(tmp_XY_down)
						tmp_XY_up_right     = np.round(tmp_XY_up_right)
						tmp_XY_up_left      = np.round(tmp_XY_up_left)
						tmp_XY_down_right   = np.round(tmp_XY_down_right)
						tmp_XY_down_left    = np.round(tmp_XY_down_left)

						# Change to new Origin
						tmp_XY_cent = np.array(XYorigin) + np.array(tmp_XY_cent)
						tmp_XY_left = np.array(XYorigin) + np.array(tmp_XY_left)
						tmp_XY_right = np.array(XYorigin) + np.array(tmp_XY_right)
						tmp_XY_up = np.array(XYorigin) + np.array(tmp_XY_up)
						tmp_XY_down = np.array(XYorigin) + np.array(tmp_XY_down)
						tmp_XY_up_right = np.array(XYorigin) + np.array(tmp_XY_up_right)
						tmp_XY_up_left = np.array(XYorigin) + np.array(tmp_XY_up_left)
						tmp_XY_down_right = np.array(XYorigin) + np.array(tmp_XY_down_right)
						tmp_XY_down_left = np.array(XYorigin) + np.array(tmp_XY_down_left)



						# Apply Reflection and Rotation
						# If Sref than apply Reflection and Rotation
						if Type[-1 - 1 * j] == 3:
							# Apply Reflectoin: Reflect to Ydirection based on XYorigin
							if Reflection[-1 - 1 * j][0] == 1:
								tmp_XY_cent[1] = 2 * XYorigin[1] - tmp_XY_cent[1]
								tmp_XY_left[1] = 2 * XYorigin[1] - tmp_XY_left[1]
								tmp_XY_right[1] = 2 * XYorigin[1] - tmp_XY_right[1]
								tmp_XY_up[1] = 2 * XYorigin[1] - tmp_XY_up[1]
								tmp_XY_down[1] = 2 * XYorigin[1] - tmp_XY_down[1]
								tmp_XY_up_right[1] = 2 * XYorigin[1] - tmp_XY_up_right[1]
								tmp_XY_up_left[1] = 2 * XYorigin[1] - tmp_XY_up_left[1]
								tmp_XY_down_right[1] = 2 * XYorigin[1] - tmp_XY_down_right[1]
								tmp_XY_down_left[1] = 2 * XYorigin[1] - tmp_XY_down_left[1]

								# Apply Rotation
							if Angle[-1 * j] is not None:
								tmp_XY_cent = self.get_rot_coord4(XYorigin, tmp_XY_cent, Angle[-1 - 1 * j])
								tmp_XY_left = self.get_rot_coord4(XYorigin, tmp_XY_left, Angle[-1 - 1 * j])
								tmp_XY_right = self.get_rot_coord4(XYorigin, tmp_XY_right, Angle[-1 - 1 * j])
								tmp_XY_up = self.get_rot_coord4(XYorigin, tmp_XY_up, Angle[-1 - 1 * j])
								tmp_XY_down = self.get_rot_coord4(XYorigin, tmp_XY_down, Angle[-1 - 1 * j])
								tmp_XY_up_right = self.get_rot_coord4(XYorigin, tmp_XY_up_right, Angle[-1 - 1 * j])
								tmp_XY_up_left = self.get_rot_coord4(XYorigin, tmp_XY_up_left, Angle[-1 - 1 * j])
								tmp_XY_down_right = self.get_rot_coord4(XYorigin, tmp_XY_down_right, Angle[-1 - 1 * j])
								tmp_XY_down_left = self.get_rot_coord4(XYorigin, tmp_XY_down_left, Angle[-1 - 1 * j])

								tmp_XY_cent = np.round(tmp_XY_cent,3)
								tmp_XY_left = np.round(tmp_XY_left,3)
								tmp_XY_right = np.round(tmp_XY_right,3)
								tmp_XY_up = np.round(tmp_XY_up,3)
								tmp_XY_down = np.round(tmp_XY_down,3)
								tmp_XY_up_right = np.round(tmp_XY_up_right,3)
								tmp_XY_up_left = np.round(tmp_XY_up_left,3)
								tmp_XY_down_right = np.round(tmp_XY_down_right,3)
								tmp_XY_down_left = np.round(tmp_XY_down_left,3)

							# If not Sref, There is no Reflection and Rotation
						else:
							pass

					# Make dictionary
					tmp = dict(
						_XY_cent        =tmp_XY_cent,
						_XY_left        =tmp_XY_left,
						_XY_right       =tmp_XY_right,
						_XY_up          =tmp_XY_up,
						_XY_down        =tmp_XY_down,
						_XY_up_right    =tmp_XY_up_right,
						_XY_up_left     =tmp_XY_up_left,
						_XY_down_right  =tmp_XY_down_right,
						_XY_down_left   =tmp_XY_down_left,
						_Xwidth         =tmp_xwidth,
						_Ywidth         =tmp_ywidth,
						_Area           =tmp_area,
						_XY_origin      =tmp_XY_down_left,
					)

					#
					tmp1 = copy.deepcopy(tmp)
					structure_list[i].append(tmp1)

				# If path element
				if Type[N] == 2:
					for j in range(0, len(XYcoord)):
						# Define XYorigin: XYorigin is down left for path element
						if j == 0:
							# calcuate tmp_XY_cent for initialization
							tmp_p1 = XYcoord_Hier[i][0][-1 - 1 * j][0]
							tmp_p2 = XYcoord_Hier[i][0][-1 - 1 * j][1]

							# Define _XWidth and _YWidth
							if tmp_p1[1] == tmp_p2[1] and tmp_p1[0] != tmp_p2[0]:
								tmp_xwidth = abs(tmp_p1[0] - tmp_p2[0])
								tmp_ywidth = element['_Width']
							elif tmp_p1[0] == tmp_p2[0] and tmp_p1[1] != tmp_p2[1]:
								tmp_xwidth = element['_Width']
								tmp_ywidth = abs(tmp_p1[1] - tmp_p2[1])
							else:
								raise Exception(f"assumption error kjh: Path is not Hrz or Vtc ")

							# Define XYorigin
								# Case1: Horizontal
							if tmp_p1[1] == tmp_p2[1] and tmp_p1[0] != tmp_p2[0]:
									# Case1-1: P1 is at leftside
								if tmp_p1[0] <= tmp_p2[0]:
									XYorigin = [tmp_p1[0] , tmp_p1[1] - 0.5 * tmp_ywidth ]
									# Case1-2: P2 is at leftside
								else:
									XYorigin = [tmp_p2[0] , tmp_p2[1] - 0.5 * tmp_ywidth ]
								# Case2: Vertical
							elif tmp_p1[0] == tmp_p2[0] and tmp_p1[1] != tmp_p2[1]:
									# Case2-1: P1 is at downside
								if tmp_p1[1] <= tmp_p2[1]:
									XYorigin = [tmp_p1[0] - 0.5 * tmp_xwidth, tmp_p1[1]]
									# Case2-2: P2 is at downside
								else:
									XYorigin = [tmp_p2[0] - 0.5 * tmp_xwidth, tmp_p2[1]]
							else:
								raise Exception(f"assumption error kjh: Path is not Hrz or Vtc ")
						else:
							XYorigin = XYcoord_Hier[i][0][-1 - 1 * j]

						# Calculate most bottom coord
						if j == 0:
							# Calcuate Points
							tmp_XY_cent         = (np.array(XYcoord_Hier[i][0][-1 - 1 * j][0]) + np.array(XYcoord_Hier[i][0][-1 - 1 * j][1])) * 0.5
							tmp_XY_left         = [XYorigin[0], XYorigin[1] + 0.5 * tmp_ywidth]
							tmp_XY_right        = [XYorigin[0] + 1 * tmp_xwidth, XYorigin[1] + 0.5 * tmp_ywidth]
							tmp_XY_up           = [XYorigin[0] + 0.5 * tmp_xwidth, XYorigin[1] + 1 * tmp_ywidth]
							tmp_XY_down         = [XYorigin[0] + 0.5 * tmp_xwidth, XYorigin[1] ]
							tmp_XY_up_right     = [XYorigin[0] + 1 * tmp_xwidth, XYorigin[1] + 1 * tmp_ywidth]
							tmp_XY_up_left      = [XYorigin[0], XYorigin[1] + 1 * tmp_ywidth]
							tmp_XY_down_right   = [XYorigin[0] + 1 * tmp_xwidth, XYorigin[1]]
							tmp_XY_down_left    = [XYorigin[0], XYorigin[1]]
							# tmp_xwidth          = abs( tmp_XY_right[0] - tmp_XY_left[0] )
							# tmp_ywidth          = abs( tmp_XY_up[1] - tmp_XY_down[1] )
							tmp_area            = tmp_xwidth * tmp_ywidth

							# initialize every point: change origin to [0,0]
							tmp_p1              = np.array(tmp_p1) - np.array(XYorigin)
							tmp_p2              = np.array(tmp_p2) - np.array(XYorigin)
							tmp_XY_cent         = np.array(tmp_XY_cent) - np.array(XYorigin)
							tmp_XY_left         = np.array(tmp_XY_left) - np.array(XYorigin)
							tmp_XY_right        = np.array(tmp_XY_right) - np.array(XYorigin)
							tmp_XY_up           = np.array(tmp_XY_up) - np.array(XYorigin)
							tmp_XY_down         = np.array(tmp_XY_down) - np.array(XYorigin)
							tmp_XY_up_right     = np.array(tmp_XY_up_right) - np.array(XYorigin)
							tmp_XY_up_left      = np.array(tmp_XY_up_left) - np.array(XYorigin)
							tmp_XY_down_right   = np.array(tmp_XY_down_right) - np.array(XYorigin)
							tmp_XY_down_left    = np.array(tmp_XY_down_left) - np.array(XYorigin)

						# Round for cent, left, right, up, down
						tmp_XY_cent         = np.round(tmp_XY_cent)
						tmp_XY_left         = np.round(tmp_XY_left)
						tmp_XY_right        = np.round(tmp_XY_right)
						tmp_XY_up           = np.round(tmp_XY_up)
						tmp_XY_down         = np.round(tmp_XY_down)
						tmp_XY_up_right     = np.round(tmp_XY_up_right)
						tmp_XY_up_left      = np.round(tmp_XY_up_left)
						tmp_XY_down_right   = np.round(tmp_XY_down_right)
						tmp_XY_down_left    = np.round(tmp_XY_down_left)

						# Change XYcoord for new origin
						tmp_p1 = np.array(XYorigin) + np.array(tmp_p1)
						tmp_p2 = np.array(XYorigin) + np.array(tmp_p2)
						tmp_XY_cent = np.array(XYorigin) + np.array(tmp_XY_cent)
						tmp_XY_left = np.array(XYorigin) + np.array(tmp_XY_left)
						tmp_XY_right = np.array(XYorigin) + np.array(tmp_XY_right)
						tmp_XY_up = np.array(XYorigin) + np.array(tmp_XY_up)
						tmp_XY_down = np.array(XYorigin) + np.array(tmp_XY_down)
						tmp_XY_up_right = np.array(XYorigin) + np.array(tmp_XY_up_right)
						tmp_XY_up_left = np.array(XYorigin) + np.array(tmp_XY_up_left)
						tmp_XY_down_right = np.array(XYorigin) + np.array(tmp_XY_down_right)
						tmp_XY_down_left = np.array(XYorigin) + np.array(tmp_XY_down_left)

						# Apply Reflection and Rotation
						# If Sref than apply Reflection and Rotation
						if Type[-1 - 1 * j] == 3:
							# Apply Reflectoin: Reflect to Ydirection based on XYorigin
							if Reflection[-1 - 1 * j][0] == 1:
								tmp_p1[1] = 2 * XYorigin[1] - tmp_p1[1]
								tmp_p2[1] = 2 * XYorigin[1] - tmp_p2[1]
								tmp_XY_cent[1] = 2 * XYorigin[1] - tmp_XY_cent[1]
								tmp_XY_left[1] = 2 * XYorigin[1] - tmp_XY_left[1]
								tmp_XY_right[1] = 2 * XYorigin[1] - tmp_XY_right[1]
								tmp_XY_up[1] = 2 * XYorigin[1] - tmp_XY_up[1]
								tmp_XY_down[1] = 2 * XYorigin[1] - tmp_XY_down[1]
								tmp_XY_up_right[1] = 2 * XYorigin[1] - tmp_XY_up_right[1]
								tmp_XY_up_left[1] = 2 * XYorigin[1] - tmp_XY_up_left[1]
								tmp_XY_down_right[1] = 2 * XYorigin[1] - tmp_XY_down_right[1]
								tmp_XY_down_left[1] = 2 * XYorigin[1] - tmp_XY_down_left[1]

								# Apply Rotation
							if Angle[-1 * j] is not None:
								tmp_p1 = self.get_rot_coord4(XYorigin, tmp_p1, Angle[-1 - 1 * j])
								tmp_p2 = self.get_rot_coord4(XYorigin, tmp_p2, Angle[-1 - 1 * j])
								tmp_XY_cent = self.get_rot_coord4(XYorigin, tmp_XY_cent, Angle[-1 - 1 * j])
								tmp_XY_left = self.get_rot_coord4(XYorigin, tmp_XY_left, Angle[-1 - 1 * j])
								tmp_XY_right = self.get_rot_coord4(XYorigin, tmp_XY_right, Angle[-1 - 1 * j])
								tmp_XY_up = self.get_rot_coord4(XYorigin, tmp_XY_up, Angle[-1 - 1 * j])
								tmp_XY_down = self.get_rot_coord4(XYorigin, tmp_XY_down, Angle[-1 - 1 * j])
								tmp_XY_up_right = self.get_rot_coord4(XYorigin, tmp_XY_up_right, Angle[-1 - 1 * j])
								tmp_XY_up_left = self.get_rot_coord4(XYorigin, tmp_XY_up_left, Angle[-1 - 1 * j])
								tmp_XY_down_right = self.get_rot_coord4(XYorigin, tmp_XY_down_right,Angle[-1 - 1 * j])
								tmp_XY_down_left = self.get_rot_coord4(XYorigin, tmp_XY_down_left, Angle[-1 - 1 * j])

									#Round for Rotation
								tmp_p1  = np.round(tmp_p1,3)
								tmp_p2  = np.round(tmp_p2,3)
								tmp_XY_cent = np.round(tmp_XY_cent,3)
								tmp_XY_left = np.round(tmp_XY_left,3)
								tmp_XY_right = np.round(tmp_XY_right,3)
								tmp_XY_up = np.round(tmp_XY_up,3)
								tmp_XY_down = np.round(tmp_XY_down,3)
								tmp_XY_up_right = np.round(tmp_XY_up_right,3)
								tmp_XY_up_left = np.round(tmp_XY_up_left,3)
								tmp_XY_down_right = np.round(tmp_XY_down_right,3)
								tmp_XY_down_left = np.round(tmp_XY_down_left,3)

							# If not Sref, There is no Reflection and Rotation
						else:
							pass

					# Make dictionary
					tmp = dict(
						_XY_p1          =tmp_p1,
						_XY_p2          =tmp_p2,
						_XY_cent        =tmp_XY_cent,
						_XY_left        =tmp_XY_left,
						_XY_right       =tmp_XY_right,
						_XY_up          =tmp_XY_up,
						_XY_down        =tmp_XY_down,
						_XY_up_right    =tmp_XY_up_right,
						_XY_up_left     =tmp_XY_up_left,
						_XY_down_right  =tmp_XY_down_right,
						_XY_down_left   =tmp_XY_down_left,
						_Xwidth         =tmp_xwidth,
						_Ywidth         =tmp_ywidth,
						_Area           =tmp_area,
						_XY_origin      =tmp_XY_down_left,
					)

					#
					tmp1 = copy.deepcopy(tmp)
					structure_list[i].append(tmp1)

				# If Sref element
				if Type[N] == 3:
					for j in range(0, len(XYcoord)):

						# Define XYorigin
						XYorigin = XYcoord_Hier[i][0][-1 - 1 * j]

						# Calculate most bottom coord
						if j == 0:
							tmp_XY_cent = [0, 0]

						# Round
						tmp_XY_cent = np.round(tmp_XY_cent)

						# Change XYcoord for new origin
						tmp_XY_cent = np.array(XYorigin) + np.array(tmp_XY_cent)

						# Apply Reflection and Rotation
						# If Sref than apply Reflection and Rotation
						if Type[-1 - 1 * j] == 3:
							# Apply Reflectoin: Reflect to Ydirection based on XYorigin
							if Reflection[-1 - 1 * j][0] == 1:
								tmp_XY_cent[1] = 2 * XYorigin[1] - tmp_XY_cent[1]

								# Apply Rotation
							if Angle[-1 * j] is not None:
								tmp_XY_cent = self.get_rot_coord4(XYorigin, tmp_XY_cent, Angle[-1 - 1 * j])
									# Round for rotation
								tmp_XY_cent = np.round(tmp_XY_cent,3)

							# If not Sref, There is no Reflection and Rotation
						else:
							pass

					# Make dictionary
					tmp = dict(

						_XY_origin = tmp_XY_cent,

					)

					#
					tmp1 = copy.deepcopy(tmp)
					structure_list[i].append(tmp1)

		return structure_list

	def iterative_forloop4(self, N, tmp: list, structure_list: list, XYcoord: list):
		'''
		Manual
		: This function is used in get_param_KJH3 to re-organize XYcoordinate of target element for structural referencing.
		This fills an hiearachical empty-list which is built ahead with hiearachical XYcoordinates
		To fills the list, This function automatically iterate forloop ntimes according to its' element
		'''
		number_of_iteration = len(XYcoord)

		# If not bottom
		if N < (number_of_iteration - 1):

			for i in range(0, len(XYcoord[N])):
				tmp2 = copy.deepcopy(tmp)
				tmp2.append(XYcoord[N][i])
				self.iterative_forloop4(N + 1, tmp2, structure_list[i], XYcoord)

		# Bottom hiear
		else:
			for i in range(0, len(XYcoord[N])):
				tmp3 = copy.deepcopy(tmp)
				tmp3.append(XYcoord[N][i])
				structure_list[i].append(tmp3)

		return structure_list

	def empty_list_gen4(self, N, empty_list: list, XYcoord: list):
		'''
		Manual
		: This function generates empty-list which have size of target element
		its generated list is used for the following "iterative_forloop" function.
		'''
		number_of_iteration = len(XYcoord)

		if N < (number_of_iteration - 1):
			result = []
			for i in range(0, len(XYcoord[N])):
				result2 = self.empty_list_gen4(N + 1, empty_list, XYcoord)
				result.append(result2)
		else:
			tmp = []
			for i in range(0, len(XYcoord[N])):
				tmp.append([])
			result = copy.deepcopy(tmp)

		return result

	def get_param_KJH4(self, *hier_element_tuple: str):

		'''Manual
		Update: XY coord = down left

		Function:
					Returns center_coordinates, four_edges, four_boundaries, XYwidths and area of Boundary_element
					Returns point1|2_coordinates, center_coordinates, four_edges, four_boundaries, XYwidths and area of path_element
					Returns center_coordinates of Sref_element
		Assumption:
					For path_element, path_element must be two point connection. #####
		'''

		# Error if self._DesignParameter does not exist
		if '_DesignParameter' not in self.__dict__:
			raise Exception("There is no DesignParameter.")

		# Transform Tuple to list
		HierElementList = list(hier_element_tuple)

		# Referencing the most top hierachical element(Because the referencing structure differ from the other)
		# Error if the most top Hierelement name does not exist in self._DesignParameter
		if HierElementList[0] not in self._DesignParameter:
			raise Exception(f"Invalid Hierarchy element name: {HierElementList[0]}")

			# Referencing top hier_element
		element = self._DesignParameter[HierElementList[0]]

		# Record XYcoord,Reflection,Angle,element_type
		# If the most top hier_element is Sref type
		if element['_DesignParametertype'] == 3:
			# Define XYcooridnate of most top hier_element
			element_XYcoord = [copy.deepcopy(element['_XYCoordinates'])]
			# Define Sref Reflection
			element_Reflection = [copy.deepcopy(element['_Reflect'])]
			# Define Sref Angle
			element_Angle = [copy.deepcopy(element['_Angle'])]
			# Sref element flags: 1=Boundary, 2=Path, 3=Sref
			element_Type_flag = [3]

			# If the most top hier_element is Path type
		elif element['_DesignParametertype'] == 2:
			# Define XYcooridnate of most top hier_element
			element_XYcoord = [copy.deepcopy(element['_XYCoordinates'])]
			# Define Sref Reflection
			element_Reflection = [[-1, -1, -1]]
			# Define Sref Angle
			element_Angle = [-360]
			# Sref element flags: 1=Boundary, 2=Path, 3=Sref
			element_Type_flag = [2]

			# If the most top hier_element is Boundary type
		else:
			# Define XYcooridnate of most top hier_element
			element_XYcoord = [copy.deepcopy(element['_XYCoordinates'])]
			# Define Sref Reflection
			element_Reflection = [[-1, -1, -1]]
			# Define Sref Angle
			element_Angle = [-360]
			# Sref element flags: 1=Boundary, 2=Path, 3=Sref
			element_Type_flag = [1]

		# Referencing the sub-hierachical element
		# Search from 2nd most hiearchy to bottom one.
		for hierarchy_element in HierElementList[1:]:

			# Error if hierelement name is wrong
			if hierarchy_element not in element['_DesignObj']._DesignParameter:
				raise Exception(f"Invalid Hierarchy element name: {hierarchy_element}.")

			# Building-up element name
			element = element['_DesignObj']._DesignParameter[hierarchy_element]

			# Record XYcoord,Reflection,Angle,element_type
			# If the sub_element is Sref type
			if element['_DesignParametertype'] == 3:
				# Define XYcooridnate of most top hier_element
				element_XYcoord.append(element['_XYCoordinates'])
				# Define Sref Reflection
				element_Reflection.append(element['_Reflect'])
				# Define Sref Angle
				element_Angle.append(element['_Angle'])
				# Sref element flags: 1=Boundary, 2=Path, 3=Sref
				element_Type_flag.append(3)

				# If the sub_element is Path type
			elif element['_DesignParametertype'] == 2:
				# Define XYcooridnate of most top hier_element
				element_XYcoord.append(element['_XYCoordinates'])
				# Define Sref Reflection
				element_Reflection.append([-1, -1, -1])
				# Define Sref Angle
				element_Angle.append(-360)
				# Sref element flags: 1=Boundary, 2=Path, 3=Sref
				element_Type_flag.append(2)

				# If the sub_element is Boundary type
			else:
				# Define XYcooridnate of most top hier_element
				element_XYcoord.append(element['_XYCoordinates'])
				# Define Sref Reflection
				element_Reflection.append([-1, -1, -1])
				# Define Sref Angle
				element_Angle.append(-360)
				# Sref element flags: 1=Boundary, 2=Path, 3=Sref
				element_Type_flag.append(1)

		# Re-organize element_XYcoord for hierachical referencing
		# Making empty list
		N = 0
		empty_list = [[]]
		structure_list = self.empty_list_gen4(N, empty_list, element_XYcoord)
		structure_list2 = copy.deepcopy(structure_list)
		# Re-organize element_XYcoord for hierachical referencing
		N = 0
		tmp = []
		element_Hier_XYcoord = self.iterative_forloop4(N, tmp, structure_list, element_XYcoord)

		# Cal Parameter of target element
		N = 0
		Calculation_result = self.iterative_forloop_calculation4(N, element, structure_list2, element_XYcoord, element_Hier_XYcoord, element_Reflection, element_Angle, element_Type_flag)

		return Calculation_result




	def get_outter_KJH4(self,*hier_element_tuple:str):

		#Error if self._DesignParameter does not exist
		if '_DesignParameter' not in self.__dict__:
				raise Exception("There is no DesignParameter.")


		#Transform Tuple to list
		HierElementList = list(hier_element_tuple)

		#Referencing the most top hierachical element(Because the referencing structure differ from the other)
			#Error if the most top Hierelement name does not exist in self._DesignParameter
		if HierElementList[0] not in self._DesignParameter:
			raise Exception(f"Invalid Hierarchy element name: {HierElementList[0]}")

			#Referencing top hier_element
		element = self._DesignParameter[HierElementList[0]]


		#Referencing the sub-hierachical element
			#Search from 2nd most hiearchy to bottom one.
		for hierarchy_element in HierElementList[1:]:

			#Error if hierelement name is wrong
			if hierarchy_element not in element['_DesignObj']._DesignParameter:
				raise Exception(f"Invalid Hierarchy element name: {hierarchy_element}.")

			#Building-up element name
			element = element['_DesignObj']._DesignParameter[hierarchy_element]


		#Finding every elements
		tmp = []
		result =[]
		result = self.iterative_forloop_finding(result,tmp,element)


		#Calculate parameter
		flatten_result = []
		for i in range(0,len(result)):

			#Calculate param
			#Param_list = self.get_param_KJH3('{}'.format(HierElementList[0]),*result[i])
			Param_list = self.get_param_KJH4(*HierElementList,*result[i])

			#flattening the parameter
			N=0
			Hier_list = copy.deepcopy(result[i])
			Hier_list = HierElementList + Hier_list
			Index_list = []
			result2 = []

			result2 = self.iterative_forloop_getparam(N,Hier_list,Param_list,Index_list,result2)
			flatten_result.append(result2)

		#flatten every element's parameter
		flatten_result2 = []
		for i in range(0,len(flatten_result)):
			for j in range(0,len(flatten_result[i])):
				flatten_result2.append(flatten_result[i][j])

		#find the most upper
		most_up_ycoord = []
		most_up_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_up_ycoord.append( flatten_result2[i][0]['_XY_up'][1] )
				most_up_index.append( i )
			else:
				if most_up_ycoord[0] > flatten_result2[i][0]['_XY_up'][1]:
					pass
				elif most_up_ycoord[0] < flatten_result2[i][0]['_XY_up'][1]:
					most_up_ycoord = []
					most_up_ycoord.append(flatten_result2[i][0]['_XY_up'][1])
					most_up_index = []
					most_up_index.append(i)
				elif most_up_ycoord[0] == flatten_result2[i][0]['_XY_up'][1]:
					most_up_ycoord.append(flatten_result2[i][0]['_XY_up'][1])
					most_up_index.append( i )

		#find the most down
		most_down_ycoord = []
		most_down_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_down_ycoord.append( flatten_result2[i][0]['_XY_down'][1] )
				most_down_index.append( i )
			else:
				if most_down_ycoord[0] < flatten_result2[i][0]['_XY_down'][1]:
					pass
				elif most_down_ycoord[0] > flatten_result2[i][0]['_XY_down'][1]:
					most_down_ycoord = []
					most_down_ycoord.append(flatten_result2[i][0]['_XY_down'][1])
					most_down_index = []
					most_down_index.append(i)
				elif most_down_ycoord[0] == flatten_result2[i][0]['_XY_down'][1]:
					most_down_ycoord.append(flatten_result2[i][0]['_XY_down'][1])
					most_down_index.append( i )

		#find the most right
		most_right_xcoord = []
		most_right_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_right_xcoord.append( flatten_result2[i][0]['_XY_right'][0] )
				most_right_index.append( i )
			else:
				if most_right_xcoord[0] > flatten_result2[i][0]['_XY_right'][0]:
					pass
				elif most_right_xcoord[0] < flatten_result2[i][0]['_XY_right'][0]:
					most_right_xcoord = []
					most_right_xcoord.append(flatten_result2[i][0]['_XY_right'][0])
					most_right_index = []
					most_right_index.append(i)
				elif most_right_xcoord[0] == flatten_result2[i][0]['_XY_right'][0]:
					most_right_xcoord.append(flatten_result2[i][0]['_XY_right'][0])
					most_right_index.append( i )

		#find the most left
		most_left_xcoord = []
		most_left_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_left_xcoord.append( flatten_result2[i][0]['_XY_left'][0] )
				most_left_index.append( i )
			else:
				if most_left_xcoord[0] < flatten_result2[i][0]['_XY_left'][0]:
					pass
				elif most_left_xcoord[0] > flatten_result2[i][0]['_XY_left'][0]:
					most_left_xcoord = []
					most_left_xcoord.append(flatten_result2[i][0]['_XY_left'][0])
					most_left_index = []
					most_left_index.append(i)
				elif most_left_xcoord[0] == flatten_result2[i][0]['_XY_left'][0]:
					most_left_xcoord.append(flatten_result2[i][0]['_XY_left'][0])
					most_left_index.append( i )

		tmp = dict(
						_Layername  = result,
						_Layercoord = flatten_result2,
						_Mostdown	= dict( index = most_down_index, 	coord = most_down_ycoord),
						_Mostleft	= dict( index = most_left_index, 	coord = most_left_xcoord),
						_Mostright	= dict( index = most_right_index, 	coord = most_right_xcoord),
						_Mostup		= dict( index = most_up_index, 		coord = most_up_ycoord),
				)


		#return flatten_result2, result,[most_down_index,most_down_ycoord], [most_left_index,most_left_xcoord], [most_right_index,most_right_xcoord], [most_up_index,most_up_ycoord]
		return tmp




	def get_outter_KJH5(self,*hier_element_tuple:str):

		'''
		Manual
		: KJH5 version is for future plan
		KJH4 does not work in the element rotation and reflection situation
		New idea is that bring the reflection and rotation information the re-arrange up/down/right/left
		For example, if I got reflection and rotation information of [000] and 180, it brings a change of up<->down and right<->left
		'''

		#Error if self._DesignParameter does not exist
		if '_DesignParameter' not in self.__dict__:
				raise Exception("There is no DesignParameter.")


		#Transform Tuple to list
		HierElementList = list(hier_element_tuple)

		#Referencing the most top hierachical element(Because the referencing structure differ from the other)
			#Error if the most top Hierelement name does not exist in self._DesignParameter
		if HierElementList[0] not in self._DesignParameter:
			raise Exception(f"Invalid Hierarchy element name: {HierElementList[0]}")

			#Referencing top hier_element
		element = self._DesignParameter[HierElementList[0]]


		#Referencing the sub-hierachical element
			#Search from 2nd most hiearchy to bottom one.
		for hierarchy_element in HierElementList[1:]:

			#Error if hierelement name is wrong
			if hierarchy_element not in element['_DesignObj']._DesignParameter:
				raise Exception(f"Invalid Hierarchy element name: {hierarchy_element}.")

			#Building-up element name
			element = element['_DesignObj']._DesignParameter[hierarchy_element]


		#Finding every elements
		tmp = []
		result =[]
		result = self.iterative_forloop_finding(result,tmp,element)


		#Calculate parameter
		flatten_result = []
		for i in range(0,len(result)):

			#Calculate param
			#Param_list = self.get_param_KJH3('{}'.format(HierElementList[0]),*result[i])
			Param_list = self.get_param_KJH4(*HierElementList,*result[i])

			#flattening the parameter
			N=0
			Hier_list = copy.deepcopy(result[i])
			Hier_list = HierElementList + Hier_list
			Index_list = []
			result2 = []

			result2 = self.iterative_forloop_getparam(N,Hier_list,Param_list,Index_list,result2)
			flatten_result.append(result2)

		#flatten every element's parameter
		flatten_result2 = []
		for i in range(0,len(flatten_result)):
			for j in range(0,len(flatten_result[i])):
				flatten_result2.append(flatten_result[i][j])

		#find the most upper
		most_up_ycoord = []
		most_up_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_up_ycoord.append( flatten_result2[i][0]['_XY_up'][1] )
				most_up_index.append( i )
			else:
				if most_up_ycoord[0] > flatten_result2[i][0]['_XY_up'][1]:
					pass
				elif most_up_ycoord[0] < flatten_result2[i][0]['_XY_up'][1]:
					most_up_ycoord = []
					most_up_ycoord.append(flatten_result2[i][0]['_XY_up'][1])
					most_up_index = []
					most_up_index.append(i)
				elif most_up_ycoord[0] == flatten_result2[i][0]['_XY_up'][1]:
					most_up_ycoord.append(flatten_result2[i][0]['_XY_up'][1])
					most_up_index.append( i )

		#find the most down
		most_down_ycoord = []
		most_down_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_down_ycoord.append( flatten_result2[i][0]['_XY_down'][1] )
				most_down_index.append( i )
			else:
				if most_down_ycoord[0] < flatten_result2[i][0]['_XY_down'][1]:
					pass
				elif most_down_ycoord[0] > flatten_result2[i][0]['_XY_down'][1]:
					most_down_ycoord = []
					most_down_ycoord.append(flatten_result2[i][0]['_XY_down'][1])
					most_down_index = []
					most_down_index.append(i)
				elif most_down_ycoord[0] == flatten_result2[i][0]['_XY_down'][1]:
					most_down_ycoord.append(flatten_result2[i][0]['_XY_down'][1])
					most_down_index.append( i )

		#find the most right
		most_right_xcoord = []
		most_right_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_right_xcoord.append( flatten_result2[i][0]['_XY_right'][0] )
				most_right_index.append( i )
			else:
				if most_right_xcoord[0] > flatten_result2[i][0]['_XY_right'][0]:
					pass
				elif most_right_xcoord[0] < flatten_result2[i][0]['_XY_right'][0]:
					most_right_xcoord = []
					most_right_xcoord.append(flatten_result2[i][0]['_XY_right'][0])
					most_right_index = []
					most_right_index.append(i)
				elif most_right_xcoord[0] == flatten_result2[i][0]['_XY_right'][0]:
					most_right_xcoord.append(flatten_result2[i][0]['_XY_right'][0])
					most_right_index.append( i )

		#find the most left
		most_left_xcoord = []
		most_left_index = []
		for i in range(0,len(flatten_result2)):
			if i == 0:
				most_left_xcoord.append( flatten_result2[i][0]['_XY_left'][0] )
				most_left_index.append( i )
			else:
				if most_left_xcoord[0] < flatten_result2[i][0]['_XY_left'][0]:
					pass
				elif most_left_xcoord[0] > flatten_result2[i][0]['_XY_left'][0]:
					most_left_xcoord = []
					most_left_xcoord.append(flatten_result2[i][0]['_XY_left'][0])
					most_left_index = []
					most_left_index.append(i)
				elif most_left_xcoord[0] == flatten_result2[i][0]['_XY_left'][0]:
					most_left_xcoord.append(flatten_result2[i][0]['_XY_left'][0])
					most_left_index.append( i )

		tmp = dict(
						_Layername  = result,
						_Layercoord = flatten_result2,
						_Mostdown	= dict( index = most_down_index, 	coord = most_down_ycoord),
						_Mostleft	= dict( index = most_left_index, 	coord = most_left_xcoord),
						_Mostright	= dict( index = most_right_index, 	coord = most_right_xcoord),
						_Mostup		= dict( index = most_up_index, 		coord = most_up_ycoord),
				)


		#return flatten_result2, result,[most_down_index,most_down_ycoord], [most_left_index,most_left_xcoord], [most_right_index,most_right_xcoord], [most_up_index,most_up_ycoord]
		return tmp

	def get_PTHcoord_KJH(self,Path_coord:list,Path_width):

		'''Manual
		Function:
					Re-calculate Path coordination to make junction (corner) smooth
		'''

		for i in range(0,len(Path_coord)-1):
			#If path coord is consecutive
			if Path_coord[i][1][0] == Path_coord[i+1][0][0] and Path_coord[i][1][1] == Path_coord[i+1][0][1]:
				#If P1 Path is y-direction
				if Path_coord[i][0][0] == Path_coord[i][1][0]:
					#from P1 to downward
					if Path_coord[i][0][1] > Path_coord[i][1][1]:
						Path_coord[i][1][1] = Path_coord[i][1][1] - 0.5 * Path_width
					#from P1 to Upward
					else:
						Path_coord[i][1][1] = Path_coord[i][1][1] + 0.5 * Path_width
				#If P1 Path is x-direction
				elif Path_coord[i][0][1] == Path_coord[i][1][1]:
					#from P1 to Leftward
					if Path_coord[i][0][0] > Path_coord[i][1][0]:
						Path_coord[i][1][0] = Path_coord[i][1][0] - 0.5 * Path_width
					#from P1 to Rightward
					else:
						Path_coord[i][1][0] = Path_coord[i][1][0] + 0.5 * Path_width
				else:
					pass

				#If P2 Path is y-direction
				if Path_coord[i+1][0][0] == Path_coord[i+1][1][0]:
					#from P1 to downward
					if Path_coord[i+1][0][1] > Path_coord[i+1][1][1]:
						Path_coord[i+1][0][1] = Path_coord[i+1][0][1] + 0.5 * Path_width
					#from P1 to Upward
					else:
						Path_coord[i+1][0][1] = Path_coord[i+1][0][1] - 0.5 * Path_width
				#If P2 Path is x-direction
				elif Path_coord[i+1][0][1] == Path_coord[i+1][1][1]:
					#from P1 to Leftward
					if Path_coord[i+1][0][0] > Path_coord[i+1][1][0]:
						Path_coord[i+1][0][0] = Path_coord[i+1][0][0] + 0.5 * Path_width
					#from P1 to Rightward
					else:
						Path_coord[i+1][0][0] = Path_coord[i+1][0][0] - 0.5 * Path_width
				else:
					pass

			#If path coord is not consecutive, do not make corner smoothing
			else:
				pass


		return Path_coord


	def get_PTH_KJH(self,Path_name, Path_width,tmpXY:list,tmpMetal:list,tmpViaTF:list,tmpViaDir:list,tmpViaWid:list):
		
		from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
		
		'''Manual
		Function:
					Re-calculate Path coordination to make junction (corner) smooth
		'''
		
		tmp = self.get_PTHcoord_KJH(tmpXY,Path_width)
		_Path_name =[]
		for i in range(0,len(tmpXY)):
			_Path_name.append( 'PTH_' + Path_name + '_{}'.format(i) )
			
			if i ==0:
				self._DesignParameter[_Path_name[i]] = self._PathElementDeclaration(
		            _Layer          =   DesignParameters._LayerMapping['METAL{}'.format(tmpMetal[i])][0],
				    _Datatype       =   DesignParameters._LayerMapping['METAL{}'.format(tmpMetal[i])][1],
				    _XYCoordinates  =   [],
				    _Width          =   Path_width,)
	
				self._DesignParameter[_Path_name[i]]['_XYCoordinates'] = [tmpXY[i]]
				
			else:
				self._DesignParameter[_Path_name[i]] = self._PathElementDeclaration(
					_Layer=DesignParameters._LayerMapping['METAL{}'.format(tmpMetal[i])][0],
					_Datatype=DesignParameters._LayerMapping['METAL{}'.format(tmpMetal[i])][1],
					_XYCoordinates=[],
					_Width=Path_width, )
				
				self._DesignParameter[_Path_name[i]]['_XYCoordinates'] = [tmpXY[i]]
				
				if tmpViaTF[i-1] == 1:

					if tmpMetal[i-1] > tmpMetal[i]:
						low_metal = tmpMetal[i]
						top_metal = tmpMetal[i-1]
					else:
						low_metal = tmpMetal[i-1]
						top_metal = tmpMetal[i]

					_Via_name = 'SRF_' + Path_name +'_{}'.format(i-1) + '_ViaM{}M{}'.format(low_metal,top_metal)

					# Vtc
					if tmpViaDir[i-1] == 1:
						
						## Sref generation: ViaX
						## Define ViaX Parameter
						_Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
						_Caculation_Parameters['_Layer1'] = low_metal
						_Caculation_Parameters['_Layer2'] = top_metal
						_Caculation_Parameters['_COX'] = None
						_Caculation_Parameters['_COY'] = None
						
						## Sref ViaX declaration
						self._DesignParameter[_Via_name] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name=_Via_name))[0]
						
						## Define Sref Relection
						self._DesignParameter[_Via_name]['_Reflect'] = [0, 0, 0]
						
						## Define Sref Angle
						self._DesignParameter[_Via_name]['_Angle'] = 0
						
						## Calcuate Overlapped XYcoord
						tmp1 = self.get_param_KJH4(_Path_name[i-1])
						tmp2 = self.get_param_KJH4(_Path_name[i])
						Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])
						
						## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
						_COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureX')
						
						if _COX == 0:
							raise Exception(f"_Cox or _Coy is zero")
						
						if _COY < 2:
							_COY = 2
						
						if tmpViaWid[i-1] == None:
							pass
						else:
							pass
							_COX = tmpViaWid[i-1][0]
							_COY = tmpViaWid[i-1][1]
						
						## Define _COX and _COY
						_Caculation_Parameters['_COX'] = _COX
						_Caculation_Parameters['_COY'] = _COY
						
						## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
						self._DesignParameter[_Via_name]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)
						
						## Calculate Sref XYcoord
						tmpcoord = []
						## initialized Sref coordinate
						self._DesignParameter[_Via_name]['_XYCoordinates'] = [[0, 0]]
						
						## Calculate
						# [tmpXY[i-1][0][0] tmpXY[i-1][0][1]] [tmpXY[i-1][1][0] tmpXY[i-1][1][1]] [tmpXY[i][0][0] tmpXY[i][0][1]] [tmpXY[i][1][0] tmpXY[i][1][1]]
						
						# if [tmpXY[i-1][1][0], tmpXY[i-1][1][1]] != [tmpXY[i][0][0], tmpXY[i][0][1]]:
						# 	raise Exception(f"Path1 Path2 is not connected")

						#Path1 is vtc
						if tmpXY[i-1][0][0] == tmpXY[i-1][1][0]:
							#Path2 is vtc
							if tmpXY[i][0][0] == tmpXY[i][1][0]:
								raise Exception(f"Path1 and Path2 is Vtc")
							#Path2 is hrz
							elif tmpXY[i][0][1]==tmpXY[i][1][1]:
								if tmpXY[i-1][0][1] > tmpXY[i-1][1][1]:
									#path1 vtc downward
									stickto = 'down'
								else:
									#path1 vtc upward
									stickto = 'up'
							#Path2 is not orthogonal
							else:
								raise Exception(f"Path2 is not orthogonal")
						#Path1 is hrz
						elif tmpXY[i-1][0][1] == tmpXY[i-1][1][1]:
							# Path2 is vtc
							if tmpXY[i][0][0] == tmpXY[i][1][0]:
								if tmpXY[i][0][1] > tmpXY[i][1][1]:
									#path2 vtc downward
									stickto = 'up'
								else:
									#path2 vtc upward
									stickto = 'down'
							# Path2 is hrz
							elif tmpXY[i][0][1] == tmpXY[i][1][1]:
								raise Exception(f"Path1 and Path2 is Hrz")
							# Path2 is not orthogonal
							else:
								raise Exception(f"Path2 is not orthogonal")
						#Path1 is not orthogonal
						else:
							raise Exception(f"Path1 is not orthogonal")
						
						## Target_coord
						target_coord = Ovlpcoord[0]['_XY_'+stickto]
						## Approaching_coord
						tmp2 = self.get_param_KJH4(_Via_name, 'SRF_ViaM{}M{}'.format(low_metal, low_metal + 1), 'BND_Met{}Layer'.format(low_metal))
						approaching_coord = tmp2[0][0][0][0]['_XY_'+stickto]
						## Sref coord
						tmp3 = self.get_param_KJH4(_Via_name)
						Scoord = tmp3[0][0]['_XY_origin']
						## Calculate
						New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
						tmpcoord.append(New_Scoord)
						## Define
						self._DesignParameter[_Via_name]['_XYCoordinates'] = tmpcoord
						
					# Hrz
					elif tmpViaDir[i-1] ==0:
						
						## Sref generation: ViaX
						## Define ViaX Parameter
						_Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
						_Caculation_Parameters['_Layer1'] = low_metal
						_Caculation_Parameters['_Layer2'] = top_metal
						_Caculation_Parameters['_COX'] = None
						_Caculation_Parameters['_COY'] = None
						
						## Sref ViaX declaration
						self._DesignParameter[_Via_name] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name=_Via_name))[0]
						
						## Define Sref Relection
						self._DesignParameter[_Via_name]['_Reflect'] = [0, 0, 0]
						
						## Define Sref Angle
						self._DesignParameter[_Via_name]['_Angle'] = 0
						
						## Calcuate Overlapped XYcoord
						tmp1 = self.get_param_KJH4(_Path_name[i-1])
						tmp2 = self.get_param_KJH4(_Path_name[i])
						Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])
						
						## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
						_COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')
						
						if _COY == 0:
							raise Exception(f"_Cox or _Coy is zero")
						
						if _COX < 2:
							_COX = 2
						
						if tmpViaWid[i-1] == None:
							pass
						else:
							pass
							_COX = tmpViaWid[i - 1][0]
							_COY = tmpViaWid[i - 1][1]
						
						## Define _COX and _COY
						_Caculation_Parameters['_COX'] = _COX
						_Caculation_Parameters['_COY'] = _COY
						
						## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
						self._DesignParameter[_Via_name]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)
						
						## Calculate Sref XYcoord
						tmpcoord = []
						## initialized Sref coordinate
						self._DesignParameter[_Via_name]['_XYCoordinates'] = [[0, 0]]
						
						## Calculate
						# [tmpXY[i-1][0][0] tmpXY[i-1][0][1]] [tmpXY[i-1][1][0] tmpXY[i-1][1][1]] [tmpXY[i][0][0] tmpXY[i][0][1]] [tmpXY[i][1][0] tmpXY[i][1][1]]
						
						# if [tmpXY[i-1][1][0], tmpXY[i-1][1][1]] != [tmpXY[i][0][0], tmpXY[i][0][1]]:
						# 	raise Exception(f"Path1 Path2 is not connected")
						
						# Path1 is vtc
						if tmpXY[i - 1][0][0] == tmpXY[i - 1][1][0]:
							# Path2 is vtc
							if tmpXY[i][0][0] == tmpXY[i][1][0]:
								raise Exception(f"Path1 and Path2 is Vtc")
							# Path2 is hrz
							elif tmpXY[i][0][1] == tmpXY[i][1][1]:
								if tmpXY[i][0][0] > tmpXY[i][1][0]:
									# path2 hrz leftward
									stickto = 'right'
								else:
									# path2 hrz rightward
									stickto = 'left'
							# Path2 is not orthogonal
							else:
								raise Exception(f"Path2 is not orthogonal")
						# Path1 is hrz
						elif tmpXY[i - 1][0][1] == tmpXY[i - 1][1][1]:
							# Path2 is vtc
							if tmpXY[i][0][0] == tmpXY[i][1][0]:
								if tmpXY[i-1][0][0] > tmpXY[i-1][1][0]:
									# path1 hrz downward
									stickto = 'left'
								else:
									# path1 vtc upward
									stickto = 'right'
							# Path2 is hrz
							elif tmpXY[i][0][1] == tmpXY[i][1][1]:
								raise Exception(f"Path1 and Path2 is Hrz")
							# Path2 is not orthogonal
							else:
								raise Exception(f"Path2 is not orthogonal")
						# Path1 is not orthogonal
						else:
							raise Exception(f"Path1 is not orthogonal")
						
						## Target_coord
						target_coord = Ovlpcoord[0]['_XY_' + stickto]
						## Approaching_coord
						tmp2 = self.get_param_KJH4(_Via_name, 'SRF_ViaM{}M{}'.format(low_metal, low_metal + 1), 'BND_Met{}Layer'.format(low_metal))
						approaching_coord = tmp2[0][0][0][0]['_XY_' + stickto]
						## Sref coord
						tmp3 = self.get_param_KJH4(_Via_name)
						Scoord = tmp3[0][0]['_XY_origin']
						## Calculate
						New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
						tmpcoord.append(New_Scoord)
						## Define
						self._DesignParameter[_Via_name]['_XYCoordinates'] = tmpcoord
					# Overlap
					elif tmpViaDir[i-1] == 2:
						## Sref generation: ViaX
						## Define ViaX Parameter
						_Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
						_Caculation_Parameters['_Layer1'] = low_metal
						_Caculation_Parameters['_Layer2'] = top_metal
						_Caculation_Parameters['_COX'] = None
						_Caculation_Parameters['_COY'] = None

						## Sref ViaX declaration
						self._DesignParameter[_Via_name] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name=_Via_name))[0]

						## Define Sref Relection
						self._DesignParameter[_Via_name]['_Reflect'] = [0, 0, 0]

						## Define Sref Angle
						self._DesignParameter[_Via_name]['_Angle'] = 0

						## Calcuate Overlapped XYcoord
						tmp1 = self.get_param_KJH4(_Path_name[i-1])
						tmp2 = self.get_param_KJH4(_Path_name[i])
						Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

						## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
						_COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], None)

						if _COX==0 or _COY==0:
							raise Exception(f"_Cox or _Coy is zero")
						
						## Define _COX and _COY
						_Caculation_Parameters['_COX'] = _COX
						_Caculation_Parameters['_COY'] = _COY

						## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
						self._DesignParameter[_Via_name]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

						## Calculate Sref XYcoord
						tmpcoord = []
						## initialized Sref coordinate
						self._DesignParameter[_Via_name]['_XYCoordinates'] = [[0, 0]]
						## Calculate
						## Target_coord
						target_coord = Ovlpcoord[0]['_XY_cent']
						## Approaching_coord
						tmp2 = self.get_param_KJH4(_Via_name,'SRF_ViaM{}M{}'.format(low_metal,low_metal+1),'BND_Met{}Layer'.format(low_metal))
						approaching_coord = tmp2[0][0][0][0]['_XY_cent']
						## Sref coord
						tmp3 = self.get_param_KJH4(_Via_name)
						Scoord = tmp3[0][0]['_XY_origin']
						## Calculate
						New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
						tmpcoord.append(New_Scoord)
						## Define
						self._DesignParameter[_Via_name]['_XYCoordinates'] = tmpcoord
						
					else:
						pass

				else:
					pass
				
		return

	def get_PTH_KJH2(self, Path_name, Path_width, tmpXY: list, tmpMetal: list, tmpViaTF: list, tmpViaDir: list, tmpViaWid: list, _Name):

		from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3

		'''Manual
		Function:
					Re-calculate Path coordination to make junction (corner) smooth
		'''

		tmp = self.get_PTHcoord_KJH(tmpXY, Path_width)
		_Path_name = []
		for i in range(0, len(tmpXY)):
			_Path_name.append('PTH_' + Path_name + '_{}'.format(i))

			if i == 0:
				self._DesignParameter[_Path_name[i]] = self._PathElementDeclaration(
					_Layer=DesignParameters._LayerMapping['METAL{}'.format(tmpMetal[i])][0],
					_Datatype=DesignParameters._LayerMapping['METAL{}'.format(tmpMetal[i])][1],
					_XYCoordinates=[],
					_Width=Path_width, )

				self._DesignParameter[_Path_name[i]]['_XYCoordinates'] = [tmpXY[i]]

			else:
				self._DesignParameter[_Path_name[i]] = self._PathElementDeclaration(
					_Layer=DesignParameters._LayerMapping['METAL{}'.format(tmpMetal[i])][0],
					_Datatype=DesignParameters._LayerMapping['METAL{}'.format(tmpMetal[i])][1],
					_XYCoordinates=[],
					_Width=Path_width, )

				self._DesignParameter[_Path_name[i]]['_XYCoordinates'] = [tmpXY[i]]

				if tmpViaTF[i - 1] == 1:

					if tmpMetal[i - 1] > tmpMetal[i]:
						low_metal = tmpMetal[i]
						top_metal = tmpMetal[i - 1]
					else:
						low_metal = tmpMetal[i - 1]
						top_metal = tmpMetal[i]

					_Via_name = '{}:SRF_'.format(_Name) + Path_name + '_{}'.format(i - 1) + '_ViaM{}M{}'.format(low_metal, top_metal)

					# Vtc
					if tmpViaDir[i - 1] == 1:

						## Sref generation: ViaX
						## Define ViaX Parameter
						_Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
						_Caculation_Parameters['_Layer1'] = low_metal
						_Caculation_Parameters['_Layer2'] = top_metal
						_Caculation_Parameters['_COX'] = None
						_Caculation_Parameters['_COY'] = None

						## Sref ViaX declaration
						self._DesignParameter[_Via_name] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name=_Via_name))[0]

						## Define Sref Relection
						self._DesignParameter[_Via_name]['_Reflect'] = [0, 0, 0]

						## Define Sref Angle
						self._DesignParameter[_Via_name]['_Angle'] = 0

						## Calcuate Overlapped XYcoord
						tmp1 = self.get_param_KJH4(_Path_name[i - 1])
						tmp2 = self.get_param_KJH4(_Path_name[i])
						Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

						## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
						_COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureX')

						if _COX == 0:
							raise Exception(f"_Cox or _Coy is zero")

						if _COY < 2:
							_COY = 2

						if tmpViaWid[i - 1] == None:
							pass
						else:
							pass
							_COX = tmpViaWid[i - 1][0]
							_COY = tmpViaWid[i - 1][1]

						## Define _COX and _COY
						_Caculation_Parameters['_COX'] = _COX
						_Caculation_Parameters['_COY'] = _COY

						## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
						self._DesignParameter[_Via_name]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

						## Calculate Sref XYcoord
						tmpcoord = []
						## initialized Sref coordinate
						self._DesignParameter[_Via_name]['_XYCoordinates'] = [[0, 0]]

						## Calculate
						# [tmpXY[i-1][0][0] tmpXY[i-1][0][1]] [tmpXY[i-1][1][0] tmpXY[i-1][1][1]] [tmpXY[i][0][0] tmpXY[i][0][1]] [tmpXY[i][1][0] tmpXY[i][1][1]]

						# if [tmpXY[i-1][1][0], tmpXY[i-1][1][1]] != [tmpXY[i][0][0], tmpXY[i][0][1]]:
						# 	raise Exception(f"Path1 Path2 is not connected")

						# Path1 is vtc
						if tmpXY[i - 1][0][0] == tmpXY[i - 1][1][0]:
							# Path2 is vtc
							if tmpXY[i][0][0] == tmpXY[i][1][0]:
								raise Exception(f"Path1 and Path2 is Vtc")
							# Path2 is hrz
							elif tmpXY[i][0][1] == tmpXY[i][1][1]:
								if tmpXY[i - 1][0][1] > tmpXY[i - 1][1][1]:
									# path1 vtc downward
									stickto = 'down'
								else:
									# path1 vtc upward
									stickto = 'up'
							# Path2 is not orthogonal
							else:
								raise Exception(f"Path2 is not orthogonal")
						# Path1 is hrz
						elif tmpXY[i - 1][0][1] == tmpXY[i - 1][1][1]:
							# Path2 is vtc
							if tmpXY[i][0][0] == tmpXY[i][1][0]:
								if tmpXY[i][0][1] > tmpXY[i][1][1]:
									# path2 vtc downward
									stickto = 'up'
								else:
									# path2 vtc upward
									stickto = 'down'
							# Path2 is hrz
							elif tmpXY[i][0][1] == tmpXY[i][1][1]:
								raise Exception(f"Path1 and Path2 is Hrz")
							# Path2 is not orthogonal
							else:
								raise Exception(f"Path2 is not orthogonal")
						# Path1 is not orthogonal
						else:
							raise Exception(f"Path1 is not orthogonal")

						## Target_coord
						target_coord = Ovlpcoord[0]['_XY_' + stickto]
						## Approaching_coord
						tmp2 = self.get_param_KJH4(_Via_name, 'SRF_ViaM{}M{}'.format(low_metal, low_metal + 1), 'BND_Met{}Layer'.format(low_metal))
						approaching_coord = tmp2[0][0][0][0]['_XY_' + stickto]
						## Sref coord
						tmp3 = self.get_param_KJH4(_Via_name)
						Scoord = tmp3[0][0]['_XY_origin']
						## Calculate
						New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
						tmpcoord.append(New_Scoord)
						## Define
						self._DesignParameter[_Via_name]['_XYCoordinates'] = tmpcoord

					# Hrz
					elif tmpViaDir[i - 1] == 0:

						## Sref generation: ViaX
						## Define ViaX Parameter
						_Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
						_Caculation_Parameters['_Layer1'] = low_metal
						_Caculation_Parameters['_Layer2'] = top_metal
						_Caculation_Parameters['_COX'] = None
						_Caculation_Parameters['_COY'] = None

						## Sref ViaX declaration
						self._DesignParameter[_Via_name] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name=_Via_name))[0]

						## Define Sref Relection
						self._DesignParameter[_Via_name]['_Reflect'] = [0, 0, 0]

						## Define Sref Angle
						self._DesignParameter[_Via_name]['_Angle'] = 0

						## Calcuate Overlapped XYcoord
						tmp1 = self.get_param_KJH4(_Path_name[i - 1])
						tmp2 = self.get_param_KJH4(_Path_name[i])
						Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

						## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
						_COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

						if _COY == 0:
							raise Exception(f"_Cox or _Coy is zero")

						if _COX < 2:
							_COX = 2

						if tmpViaWid[i - 1] == None:
							pass
						else:
							pass
							_COX = tmpViaWid[i - 1][0]
							_COY = tmpViaWid[i - 1][1]

						## Define _COX and _COY
						_Caculation_Parameters['_COX'] = _COX
						_Caculation_Parameters['_COY'] = _COY

						## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
						self._DesignParameter[_Via_name]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

						## Calculate Sref XYcoord
						tmpcoord = []
						## initialized Sref coordinate
						self._DesignParameter[_Via_name]['_XYCoordinates'] = [[0, 0]]

						## Calculate
						# [tmpXY[i-1][0][0] tmpXY[i-1][0][1]] [tmpXY[i-1][1][0] tmpXY[i-1][1][1]] [tmpXY[i][0][0] tmpXY[i][0][1]] [tmpXY[i][1][0] tmpXY[i][1][1]]

						# if [tmpXY[i-1][1][0], tmpXY[i-1][1][1]] != [tmpXY[i][0][0], tmpXY[i][0][1]]:
						# 	raise Exception(f"Path1 Path2 is not connected")

						# Path1 is vtc
						if tmpXY[i - 1][0][0] == tmpXY[i - 1][1][0]:
							# Path2 is vtc
							if tmpXY[i][0][0] == tmpXY[i][1][0]:
								raise Exception(f"Path1 and Path2 is Vtc")
							# Path2 is hrz
							elif tmpXY[i][0][1] == tmpXY[i][1][1]:
								if tmpXY[i][0][0] > tmpXY[i][1][0]:
									# path2 hrz leftward
									stickto = 'right'
								else:
									# path2 hrz rightward
									stickto = 'left'
							# Path2 is not orthogonal
							else:
								raise Exception(f"Path2 is not orthogonal")
						# Path1 is hrz
						elif tmpXY[i - 1][0][1] == tmpXY[i - 1][1][1]:
							# Path2 is vtc
							if tmpXY[i][0][0] == tmpXY[i][1][0]:
								if tmpXY[i - 1][0][0] > tmpXY[i - 1][1][0]:
									# path1 hrz downward
									stickto = 'left'
								else:
									# path1 vtc upward
									stickto = 'right'
							# Path2 is hrz
							elif tmpXY[i][0][1] == tmpXY[i][1][1]:
								raise Exception(f"Path1 and Path2 is Hrz")
							# Path2 is not orthogonal
							else:
								raise Exception(f"Path2 is not orthogonal")
						# Path1 is not orthogonal
						else:
							raise Exception(f"Path1 is not orthogonal")

						## Target_coord
						target_coord = Ovlpcoord[0]['_XY_' + stickto]
						## Approaching_coord
						tmp2 = self.get_param_KJH4(_Via_name, 'SRF_ViaM{}M{}'.format(low_metal, low_metal + 1), 'BND_Met{}Layer'.format(low_metal))
						approaching_coord = tmp2[0][0][0][0]['_XY_' + stickto]
						## Sref coord
						tmp3 = self.get_param_KJH4(_Via_name)
						Scoord = tmp3[0][0]['_XY_origin']
						## Calculate
						New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
						tmpcoord.append(New_Scoord)
						## Define
						self._DesignParameter[_Via_name]['_XYCoordinates'] = tmpcoord
					# Overlap
					elif tmpViaDir[i - 1] == 2:
						## Sref generation: ViaX
						## Define ViaX Parameter
						_Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
						_Caculation_Parameters['_Layer1'] = low_metal
						_Caculation_Parameters['_Layer2'] = top_metal
						_Caculation_Parameters['_COX'] = None
						_Caculation_Parameters['_COY'] = None

						## Sref ViaX declaration
						self._DesignParameter[_Via_name] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name=_Via_name))[0]

						## Define Sref Relection
						self._DesignParameter[_Via_name]['_Reflect'] = [0, 0, 0]

						## Define Sref Angle
						self._DesignParameter[_Via_name]['_Angle'] = 0

						## Calcuate Overlapped XYcoord
						tmp1 = self.get_param_KJH4(_Path_name[i - 1])
						tmp2 = self.get_param_KJH4(_Path_name[i])
						Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

						## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY' or 'SameEnclosure'
						_COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], None)

						if _COX == 0 or _COY == 0:
							raise Exception(f"_Cox or _Coy is zero")

						## Define _COX and _COY
						_Caculation_Parameters['_COX'] = _COX
						_Caculation_Parameters['_COY'] = _COY

						## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
						self._DesignParameter[_Via_name]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

						## Calculate Sref XYcoord
						tmpcoord = []
						## initialized Sref coordinate
						self._DesignParameter[_Via_name]['_XYCoordinates'] = [[0, 0]]
						## Calculate
						## Target_coord
						target_coord = Ovlpcoord[0]['_XY_cent']
						## Approaching_coord
						tmp2 = self.get_param_KJH4(_Via_name, 'SRF_ViaM{}M{}'.format(low_metal, low_metal + 1), 'BND_Met{}Layer'.format(low_metal))
						approaching_coord = tmp2[0][0][0][0]['_XY_cent']
						## Sref coord
						tmp3 = self.get_param_KJH4(_Via_name)
						Scoord = tmp3[0][0]['_XY_origin']
						## Calculate
						New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
						tmpcoord.append(New_Scoord)
						## Define
						self._DesignParameter[_Via_name]['_XYCoordinates'] = tmpcoord

					else:
						pass

				else:
					pass

		return

	def rename_srf_prefix(self, node, old, new):
		"""
        _DesignParameter 트리 전체에서 '_Name' 값에 old 가 포함돼 있으면
        new 로 치환한다.
        """
		# check if SRF
		if node['_DesignParametertype'] == 3:
			tmp = node['_DesignObj']._DesignParameter['_Name']['_Name']
			tmp2 = tmp.replace(old,new,1)
			node['_DesignObj']._DesignParameter['_Name']['_Name']= tmp2

			tmp3 = node['_DesignObj']._DesignParameter.values()

			for tmp4 in node['_DesignObj']._DesignParameter:
				if tmp4 not in ('_Name','_GDSFile','_XYcoordAsCent'):
					print(tmp4)
					self.rename_srf_prefix(node['_DesignObj']._DesignParameter[tmp4], old, new)

		return

	# def rename_srf_prefix(self, node, old, new):
	# 	"""
	# 	_DesignParameter 트리 전체에서 '_Name' 값에 old 가 포함돼 있으면
	# 	new 로 치환한다.
	# 	"""
	# 	# 1) 딕셔너리
	# 	if isinstance(node, dict):
	# 		# 현재 레벨에 _Name 이 있으면 갱신
	# 		if '_Name' in node and isinstance(node['_Name'], dict):
	# 			name_val = node['_Name']['_Name']
	# 			if old in name_val:
	# 				node['_Name']['_Name'] = name_val.replace(old, new, 1)
	#
	# 		# 모든 value 순회
	# 		for v in node.values():
	# 			rename_srf_prefix(self, v, old, new)
	#
	# 	# 2) 순차형 컨테이너
	# 	elif isinstance(node, (list, tuple, set)):
	# 		for item in node:
	# 			rename_srf_prefix(self, item, old, new)
	#
	# 	# 3) 객체 — 내부에 _DesignParameter 속성이 있으면 재귀
	# 	else:
	# 		if hasattr(node, '_DesignParameter'):
	# 			rename_srf_prefix(self._DesignParameter, old, new)
	#
	# 	return

	def get_first_chain(self, data, depth):
		node = data
		for _ in range(depth):
			node = node[0]  # 매 단계마다 0번 요소로 내려가기
		return node

	def get_last_chain(self, data, depth):
		node = data
		for _ in range(depth):
			node = node[-1]  # 매 단계마다 0번 요소로 내려가기
		return node

	################################################################################################################################### Calculation_End
	print('##############################')
	print('##     Calculation_End      ##')
	print('##############################')