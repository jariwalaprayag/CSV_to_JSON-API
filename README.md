# CSV_to_JSON-API
This is a python script that demonstrates conversion of inputs from csv file to output in JSON format.

* The code is submitted by Prayag Jariwala as an onlinie Assessment for Trunk
* The main code is in main.py file
* In order to run the code you need following files to pass as an command line argument
	-courses.csv
	-marks.csv
	-students.csv
	-test.csv
* put all the files on the same location as main.py file
- for example, if you place input files in Example folder your folder should look like,
	-Example
	 |_ main.py
	 |_ courses.csv
	 |_ marks.csv
	 |_ students.csv
	 |_ test.csv

* After that, run the following command,
	> python main.py courses.csv students.csv tests.csv marks.csv output.json

* this will generate the output.json file that contains the information from csv files in json format.
