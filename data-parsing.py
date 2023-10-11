import json
import csv


def read_tab_file(file_name): 
    data = []
    with open(file_name, 'r') as file: 
        header = file.readline().strip().split('\t')  #header 
        for line in file:
            values = line.strip().split('\t')
            data_dict = {}  #new empty dictionary
            for i, header_name in enumerate(header): # go through the header 
                data_dict[header_name] = values[i]  # Assign to header name
            data.append(data_dict)
            
        return data 

def save_json(data, output_file): 
    with open(output_file, 'w') as file: 
        json.dump(data, file, indent = 4)

def save_csv(data, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__': 
    file_name = input("Please enter the file name: "); 
    conversion = input("Enter -c to convert to CSV, -j to convert to JSON and -x to convert to XML: ")
    data = read_tab_file(file_name)
    if (conversion == '-j'):
        json_output_file = file_name.split('.')[0] + '.json'
        save_json(data, json_output_file)
        print("Converted to json")
    elif (conversion == '-c'):
        csv_output_file = file_name.split('.')[0] + '.csv'
        save_csv(data, csv_output_file)
        print("Converted to CSV")

    