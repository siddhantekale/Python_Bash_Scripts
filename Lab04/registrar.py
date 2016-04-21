#! /usr/bin/envpython3.4
#
#$Author: ee364a09 $
#$Date: 2016-02-16 10:26:19 -0500 (Tue, 16 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a09/Lab04/registrar.py $
#$Revision: 88210 $

import glob
import os

def embedPayload(self, payload, override = False):

def getDetails():
	students_list = {}
	ret_dict = {}
	with open('files/students.txt') as value:
		readfile = value.readlines()
		for line in readfile[2:]:
			line = line.split('|')
			name = line[0].strip()
			student_id = line[1].strip()
			students_list[student_id] = name
	value.close()

	filenames = glob.glob('files/EECS*')
	for file in filenames:
		with open(file) as value:

			readfile = value.readlines()
			coursename = file[10:13]
			for line in readfile[2:]:
				line= line.split()
				student_id_1 = line[0].strip()
				grade_temp = line[1].strip()
				grade = int(grade_temp)
				value_tuple = (coursename,grade)
				#if(students_list.get(student_id_1) is not None):
				student_name = students_list[student_id_1]
				if student_name in ret_dict:
					ret_dict[student_name].add(value_tuple)

				else:
					ret_dict[student_name] = {value_tuple}



	return ret_dict

def getHighest(classNumber):
    list_students = {}

    with open('files/students.txt') as fptr1:
    	lines_comb = fptr1.readlines()
    	for line in lines_comb[2:]:
    		values_line = line.split('|')
    		student_name = values_line[0].strip() #removes the extra spaces
    		student_id = values_line[1].strip() #removes the extra spaces
    		list_students[student_id] = student_name
    
    max_value = 0
    name_max = ''
    list_files = 'files/EECS%s.txt' %classNumber

    if not os.path.exists(list_files):
    	return()

    with open(list_files) as fptr0:
    	value_in_file = fptr0.readlines()
    	length = len(value_in_file)
    	for i in range(2, length):
    		value = value_in_file[i].split()	
    		if(int(value[1]) > max_value):
    			max_value = float(value[1])
    			name_max = list_students[value[0]]

    return(name_max, max_value)

def getLowest(classNumber):
    list_students = {}

    with open('files/students.txt') as fptr1:
    	lines_comb = fptr1.readlines()
    	for line in lines_comb[2:]:
    		values_line = line.split('|')
    		student_name = values_line[0].strip() #removes the extra spaces
    		student_id = values_line[1].strip() #removes the extra spaces
    		list_students[student_id] = student_name
    
    min_value = 1000000
    name_min = ''
    list_files = 'files/EECS%s.txt' %classNumber

    if not os.path.exists(list_files):
    	return()

    with open(list_files) as fptr0:
    	value_in_file = fptr0.readlines()
    	length = len(value_in_file)
    	for i in range(2, length):
    		value = value_in_file[i].split()	
    		if(int(value[1]) < min_value):
    			min_value = float(value[1])
    			name_min = list_students[value[0]]

    return(name_min, min_value)



def getAverageScore(studentName):

	list_student_files = "files/students.txt"
	student_dict_values = {}
	with open(list_student_files) as fptr0:
		file_content = fptr0.readlines()
		length_file = len(file_content)
		for num_counter in range (2,length_file):
			file_content_inner = file_content[num_counter].split()
			first = file_content_inner[0]
			middle = file_content_inner[1]
			last = file_content_inner[2]

			name_student = first + ' ' + middle + ' ' + last
			id_student = file_content_inner[4]
			student_dict_values[id_student] = name_student
			
	#print(student_dict_values)

	sum_subject = 0
	average_subject = 0.0
	counter = 0
	list_files = glob.glob('files/EE*')
	for file_val in list_files:
		with open(file_val) as fptr1:
			value_in_file = fptr1.readlines()
			length = len(value_in_file)
			for second_line in range(2, length):
				value = value_in_file[second_line].split()
				if student_dict_values[value[0]] == studentName:
					sum_subject = sum_subject + int(value[1])
					counter = counter + 1

	return_val = 1					

	return_val = getreturnValue(counter)

	if(return_val == 0):
		return None

	average_subject = sum_subject / counter
	return average_subject

def findScore(studentName, classNumber):
    list_files = 'files/EECS%s.txt'%classNumber
    flag = 0
    list_students = {}
    if not os.path.exists(list_files):
        return None    

    with open('files/students.txt') as fptr1:
    	lines_comb = fptr1.readlines()
    	for line in lines_comb[2:]:
    		values_line = line.split('|')
    		student_name = values_line[0].strip() #removes the extra spaces
    		student_id = values_line[1].strip() #removes the extra spaces
    		list_students[student_id] = student_name

    #print(list_students)

    with open(list_files) as fptr0:
   		value_in_file = fptr0.readlines()
   		length = len(value_in_file)
   		for i in range(2,length):
   			value = value_in_file[i].split()
   			check_name = list_students[value[0]]
   			if check_name == studentName:
   				flag = 1
   				grade = int(value[1])

    if(flag == 1):
   		return grade

    else:
   		return None


def getStudentList(classNumber):

	list_files = 'files/EECS%s.txt'%classNumber

	if not os.path.exists(list_files):
		return []

	list_students = {}
	list_names = []

	with open('files/students.txt') as fptr1:
		lines_comb = fptr1.readlines()
		for line in lines_comb[2:]:
			values_line = line.split('|')
			student_name = values_line[0].strip() #removes the extra spaces
			student_id = values_line[1].strip() #removes the extra spaces
			list_students[student_id] = student_name


	with open(list_files) as fptr2:
		value_files = fptr2.readlines()
		for i in range(2,len(value_files)):
			value = value_files[i].split()
			key_val = value[0]
			list_names.append(list_students[key_val])
			list.sort(list_names)

	return list_names

def searchForName(studentName):
	students_list = {}
	ret_dict = {}
	with open('files/students.txt') as value:
		readfile = value.readlines()
		for line in readfile[2:]:
			line = line.split('|')
			name = line[0].strip()
			student_id = line[1].strip()
			students_list[student_id] = name
	value.close()

	filenames = glob.glob('files/EECS*')

	for file in filenames:
		with open(file) as value:
			readfile = value.readlines()
			coursename = file[10:13]
			for line in readfile[2:]:
				line= line.split()
				student_id_1 = line[0].strip()
				grade_temp = line[1].strip()
				grade = int(grade_temp)

				if studentName == students_list[student_id_1]:
					if coursename in ret_dict:
						ret_dict[coursename].add(grade)
					else:
						ret_dict[coursename] = grade
	return ret_dict

def searchForID(studentId):
	students_list = {}
	ret_dict = {}
	with open('files/students.txt') as value:
		readfile = value.readlines()
		for line in readfile[2:]:
			line = line.split('|')
			name = line[0].strip()
			student_id = line[1].strip()
			students_list[student_id] = name
	value.close()

	filenames = glob.glob('files/EECS*')

	for file in filenames:
		with open(file) as value:
			readfile = value.readlines()
			coursename = file[10:13]
			for line in readfile[2:]:
				line= line.split()
				student_id_1 = line[0].strip()
				grade_temp = line[1].strip()
				grade = int(grade_temp)

				if studentId == student_id_1:
					if coursename in ret_dict:
						ret_dict[coursename].add(grade)
					else:
						ret_dict[coursename] = grade
	return ret_dict






def getreturnValue(counter):
	if(counter == 0):
		return 0

	else:
		return 1


if __name__ == "__main__" :
	print(getDetails())
    #getAverageScore("Carolyn G King")


