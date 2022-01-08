import os
import csv
import random
import numpy

# Generating New data on the basis of an existing data

faculty = [
'KV Dinesha',
'Janaki Srinivasan', 
'Balaji Parthasarathy', 
'Prof. T K Srikanth', 
'Chandrashekar Ramanathan', 
'Sujit Kumar Chakrabarti', 
'Varadharajan Sridhar', 
'Jaya Nair', 
'Shiva Kumar Malapaka', 
'Manisha Kulkarni', 
'Dr Amit Chattopadhyay', 
'Jayprakash Lalchandani', 
'Meenakshi DSouza', 
'Debabrata Das', 
'Amit Prakash', 
'Srinivasa Raghavan', 
'Pradeesha', 
'Srinivas Vivek', 
'Jyotsna Bapat', 
'Bidisha Chaudhuri', 
'GN Srinivasa Prasanna Prasanna', 
'Prof. Brijesh Kumar Mishra', 
'Tricha Anjali', 
'Dinesh J', 
'Balakrishnan Ashok', 
'Neelam Sinha', 
'Subir Kumar roy', 
'Preeti Mudliar', 
'Shrisha Rao', 
'Srinath Srinavasa', 
'Uttam Kumar', 
'Rajagopalan S', 
'Chetan Parikh', 
'Ashish Choudhury', 
'Nanditha Rao', 
'Subajit Sen', 
'Muralidhara V.N', 
'Sachit Rao']
faculty_count=[1,2,3,4,5]
for i in range(10):
	csvfile = open('test/review-panels'+str(i)+'.csv', 'wt', newline='')
	obj = csv.writer(csvfile, delimiter="\t", quoting = csv.QUOTE_NONE) 
	#count of faculty in existing dataset
	# {'KV Dinesha': 13, 'Janaki Srinivasan': 23, 'Balaji Parthasarathy': 18, 'Prof. T K Srikanth': 22, 'Chandrashekar Ramanathan': 29, 'Sujit Kumar Chakrabarti': 22, 'Varadharajan Sridhar': 28, 'Jaya Nair': 42, 'Shiva Kumar Malapaka': 6, 'Manisha Kulkarni': 11, 'Dr Amit Chattopadhyay': 11, 'Jayprakash Lalchandani': 17, 'Meenakshi D’Souza': 18, 'Debabrata Das': 32, 'Amit Prakash': 10, 'Srinivasa Raghavan': 30, 'Pradeesha': 18, 'Srinivas Vivek': 26, 'Jyotsna Bapat': 24, 'Bidisha Chaudhuri': 19, 'GN Srinivasa Prasanna Prasanna': 28, 'Prof. Brijesh Kumar Mishra': 11, 'Tricha Anjali': 34, 'Dinesh J': 30, 'Balakrishnan Ashok': 34, 'Neelam Sinha': 37, 'Subir Kumar roy': 36, 'Preeti Mudliar': 21, 'Shrisha Rao': 25, 'Srinath Srinavasa': 44, 'Uttam Kumar': 17, 'Rajagopalan S': 14, 'Chetan Parikh': 21, 'Ashish Choudhury': 15, 'Nanditha Rao': 44, 'Subajit Sen': 29, 'Muralidhara V.N': 9, 'Sachit Rao': 10}
	for i in range(500):
		list1 = []
		# To assign bell like curve for number of faculty for each candidate
		p=random.choices(faculty_count, weights=(10,20,30,20,10), k=1)
		random_faculty=str(random.choices(faculty, weights=(13, 23, 18, 22, 29,22, 28, 42, 6, 11,11, 17, 18, 32, 10,30, 18, 26, 24, 19,28, 11, 34, 30, 34,37, 36, 21, 25, 44,17, 14, 21, 15, 44,29,9,10), k=p[0]))[1:-1]
		# random_faculty=str(random.choices(faculty, weights=(13, 23, 18, 22, 29,22, 28, 42, 6, 11,11, 17, 18, 32, 10,30, 18, 26, 24, 19,28, 11, 34, 30, 34,37, 36, 21, 25, 44,17, 14, 21, 15, 44,29,9,10), k=))[1:-1]

		list1.append("candidate"+str(i+1)+"@gmail.com,"+random_faculty)
		obj.writerow(list1 )

















