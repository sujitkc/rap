"""
Takes raw candidate applications and outputs candidate research interests to final-research-applications-21.csv
"""
import csv

def Extract_Data(path):
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
                  name = row[5]
                  list_of_topics = row[8].split(";")
                  values = []
                  values.append(name)
                  values.append(list_of_topics)
                  if row[6] in dictionary and len(list_of_topics) > len(dictionary[row[6]]):
                    dictionary[row[6]] = values
                  elif not row[6] in dictionary:
                    dictionary[row[6]] = values
                
                  # print(row[6])
                  line_count += 1
        print(dictionary)
        print(f'Processed {line_count} lines.')
        return dictionary

def write_to_csv(path, dictionary):
    data= []
    for key, value in dictionary.items():
        row = []
        row.append(value[0])
        row.append(key)
        for topic in value[1]:
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
  dictionary = Extract_Data("research-interests-21-csv.csv")
  write_to_csv("final-research-applications-21.csv", dictionary)
