import sys

def get_input_courses(courses_file):
	courses = []
	flag = 0
	for course in courses_file:
		if flag == 0:
			flag = 1
		else:
			course_dict = {}
			course_info = course.split(",")
			course_dict["id"] = int(course_info[0])
			course_dict["name"] = course_info[1]
			course_dict["teacher"] = course_info[2][:-1]
			courses.append(course_dict)
	return courses

def get_input_students(students_file):
	students = []
	flag = 0
	for student in students_file:
		if flag == 0:
			flag = 1
		else:
			student_dict = {}
			student_info = student.split(",")
			student_dict["id"] = int(student_info[0])
			student_dict["name"] = student_info[1][:-1]
			students.append(student_dict)
	return students

def get_input_tests(tests_file):
	tests = []
	flag = 0
	for test in tests_file:
		if flag == 0:
			flag = 1
		else:
			test_dict = {}
			test_info = test.split(",")
			test_dict["id"] = int(test_info[0])
			test_dict["course_id"] = int(test_info[1])
			test_dict["weight"] = int(test_info[2][:-1])
			tests.append(test_dict)
	return tests

def get_input_marks(marks_file):
	marks = []
	flag = 0
	for mark in marks_file:
		if flag == 0:
			flag = 1
		else:
			mark_dict = {}
			mark_info = mark.split(",")
			mark_dict["test_student_id"] = [int(mark_info[0]) , int(mark_info[1])]
			mark_dict["mark"] = int(mark_info[2][:-1])
			marks.append(mark_dict)
	return marks


if(len(sys.argv) != 6):
	print("Plese provide arguments as follows, \n python main.py {path-to-courses-file} {path-to-students-file} {path-to-tests-file} {path-to-marks-file} {path-to-output-file}")
	sys.exit()

path_to_courses_file = sys.argv[1]
path_to_students_file = sys.argv[2]
path_to_tests_file = sys.argv[3]
path_to_marks_file = sys.argv[4]
path_to_output_file = sys.argv[5]

courses_file = open(path_to_courses_file, "r")
courses = get_input_courses(courses_file)
print(courses)

students_file = open(path_to_students_file, "r")
students = get_input_students(students_file)
print(students)

tests_file = open(path_to_tests_file, "r")
tests = get_input_tests(tests_file)
print(tests)

marks_file = open(path_to_marks_file, "r")
marks = get_input_marks(marks_file)
print(marks)

# output_file = open(path_to_output_file, "w")


