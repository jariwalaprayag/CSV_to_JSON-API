import sys

def get_input_courses(courses_file):
	courses = {}
	flag = 0
	for course in courses_file:
		if flag == 0:
			flag = 1
		else:
			course_info = course.split(",")
			course_id = int(course_info[0])
			courses[course_id] = {}
			courses[course_id]["name"] = course_info[1]
			courses[course_id]["teacher"] = course_info[2][:-1]
	return courses

def get_input_students(students_file):
	students = {}
	flag = 0
	for student in students_file:
		if flag == 0:
			flag = 1
		else:
			student_info = student.split(",")
			student_id = int(student_info[0])
			students[student_id] = {}
			students[student_id]["name"] = student_info[1][:-1]
	return students

def get_input_tests(tests_file):
	tests = {}
	flag = 0
	for test in tests_file:
		if flag == 0:
			flag = 1
		else:
			test_info = test.split(",")
			test_id = int(test_info[0])
			tests[test_id] = {}
			tests[test_id]["course_id"] = int(test_info[1])
			tests[test_id]["weight"] = int(test_info[2][:-1])
	return tests

def get_input_marks(marks_file):
	marks = {}
	flag = 0
	for mark in marks_file:
		if flag == 0:
			flag = 1
		else:
			mark_info = mark.split(",")
			student_id = int(mark_info[1])
			if(student_id in marks.keys()):
				marks[student_id].append([int(mark_info[0]), int(mark_info[2][:-1])])
			else:
				marks[student_id] = [[int(mark_info[0]), int(mark_info[2][:-1])]]
	return marks

def check_test_weights(tests):
	valid_tests = {}
	for test in tests.values():
		if(test["course_id"] in valid_tests.keys()):
			valid_tests[test["course_id"]]["weight"] += test["weight"]
			valid_tests[test["course_id"]]["count"] += 1
		else:
			valid_tests[test["course_id"]] = {}
			valid_tests[test["course_id"]]["weight"] = test["weight"]
			valid_tests[test["course_id"]]["count"] = 1
	return valid_tests

def generate_output(courses, students, test, marks):
	 valid_tests = check_test_weights(test)
	 return valid_tests


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

students_file = open(path_to_students_file, "r")
students = get_input_students(students_file)

tests_file = open(path_to_tests_file, "r")
tests = get_input_tests(tests_file)

marks_file = open(path_to_marks_file, "r")
marks = get_input_marks(marks_file)

output_file = open(path_to_output_file, "w")
output = generate_output(courses, students, tests, marks)
print(output)


