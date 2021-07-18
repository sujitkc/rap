"""
Formatting professor research interests
"""
import csv

def Extract_Data(path):
        """
        Start time,Completion time,Email,Name,Topics
        """
        with open(path) as csv_file:
          csv_reader = csv.reader(csv_file, delimiter=',')
          line_count = 0
          # sort based on email ids
          dictionary = dict()
          for row in csv_reader:
              if line_count == 0:
                  print(f'Column names are {", ".join(row)}')
                  line_count += 1
              else:
                  # dictionary['roshni@gmail.com'] = ["name", ["Data Science"]]
                  # dictionary['roshni@gmail.com'] = ["name", ["Data Science, ML, AI"]]
                  # row[6] = email_id
                  # row[5] = name
                  name = row[3]
                  list_of_topics = row[4].split(";")   

                  trimmed_list_of_topics = [x.strip() for x in list_of_topics]

                  cleaned_list_of_topics = [x for x in trimmed_list_of_topics if str(x) != 'nan' and str(x) != '']
                  # trimmed_cleaned_list_of_topics = [x.strip() for x in cleaned_list_of_topics]         
                  dictionary[name] = cleaned_list_of_topics
         
                  # print(row[6])
                  line_count += 1
        print(dictionary)
        print(f'Processed {line_count} lines.')
        del dictionary[""]
        return dictionary

def write_to_csv(path, dictionary):
    data= []
    for key, value in dictionary.items():
        for topic in value:
            row = []
            row.append(key)
            row.append(topic)
            data.append(row)

    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)

        # write the header
        # writer.writerow(header)

        # write multiple rows
        writer.writerows(data)

if __name__ == "__main__":
  #Extract_Data("research-interests-21-csv.csv")
  dictionary = Extract_Data("new-topics-2019.csv")
  write_to_csv("final-research-topics-21.csv", dictionary)
