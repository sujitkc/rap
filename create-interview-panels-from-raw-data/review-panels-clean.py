"""
Create interview panels from raw data
"""
import csv

def Extract_Data(path):
        """
        Application Code,Full Name,Email,Gender,Program,Domain,FT / PT,Mobile,Interview Panel,Faculty Member,Willing to Supervise,Date,Time,Meeting Room Link,Host Credentials
        """
        with open(path) as csv_file:
          csv_reader = csv.reader(csv_file, delimiter=',')
          line_count = 0
          # sort based on email ids
          dictionary = dict()
          for row in csv_reader:
            #   print(row)
              if line_count == 0:
                  print(f'Column names are {", ".join(row)}')
                  line_count += 1
              else:
                  # row[3] = email_id
                  # row[10] = facultyname
                  email = row[2]
                  prof = row[9]   

                  if email in dictionary.keys():
                      dictionary[email].append(prof)
                  elif email not in dictionary.keys():
                      dictionary[email] = [prof]
                  line_count += 1
        print(dictionary)
        print(f'Processed {line_count} lines.')
        return dictionary

def write_to_csv(path, dictionary):
    data= []
    for key, value in dictionary.items():
        row = []
        row.append(key)
        for prof in value:
            row.append(prof)
        data.append(row)

    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)

        # write the header
        # writer.writerow(header)

        # write multiple rows
        writer.writerows(data)

if __name__ == "__main__":
  #Extract_Data("research-interests-21-csv.csv")
  dictionary = Extract_Data("Research_Admissions_Interview_Schedule_Revised_NCSP.csv")
  write_to_csv("interview-panels-ms-cs.csv", dictionary)

