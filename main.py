import sys

if(len(sys.argv) != 6):
	print("Plese provide arguments as follows, \n python main.py {path-to-courses-file} {path-to-students-file} {path-to-tests-file} {path-to-marks-file} {path-to-output-file}")
	sys.exit()

path_to_courses_file = "../" + sys.argv[1]
path_to_students_file = "../" + sys.argv[2]
path_to_tests_file = "../" + sys.argv[3]
path_to_marks_file = "../" + sys.argv[4]
path_to_output_file = "../" + sys.argv[5]

courses_file = open(path_to_courses_file, "r")
courses = get_input_courses(courses_file)

students_file = open(path_to_students_file, "r")
students = get_input_students(courses_file)

tests_file = open(path_to_tests_file, "r")
tests = get_input_tests(courses_file)

marks_file = open(path_to_marks_file, "r")
marks = get_input_marks(courses_file)

output_file = open(path_to_output_file, "w")


