
import csv,os

fields = ['Name', 'Branch', 'Year', 'CGPA']

rows = [
    ['Krishna', 'CSE', '2021', '8.1'],
    ['ishan', 'CSE', '2021', '7.0'],
    ['jasan', 'MECH', '2021', '8.1'],
    ['aman', 'IOT', '2021', '8.1'],
    ['Aisha', 'SE', '2023', '8.1'],
    ['Nisha', 'EP', '2022', '8.1'],
    ['ishan', 'CSE', '2021', '7.0'],
    ['jasan', 'MECH', '2021', '8.1'],
    ['aman', 'IOT', '2021', '8.1'],
    ['Aisha', 'SE', '2023', '8.1'],
    ['Nisha', 'EP', '2022', '8.1'],  ['ishan', 'CSE', '2021', '7.0'],
    ['jasan', 'MECH', '2021', '8.1'],
    ['aman', 'IOT', '2021', '8.1'],
    ['Aisha', 'SE', '2023', '8.1'],
    ['Nisha', 'EP', '2022', '8.1'],
]


def csv_list_writter(filename:str, list_data:list,fields:list, mode:str, is_initial=False):
    if os.path.isfile(path=filename):
        with open(file=filename, mode=mode) as csvfile:
            csvwriter = csv.writer(csvfile) #

            if is_initial:
                try:
                    csvwriter.writerow(fields) # writting here rows
                except:
                    print('Error while field row writting')
                
            try:
                csvwriter.writerows(list_data)
            except:
                print('Error While Row data writting')
            else:
                print('Data successfuly written')
filepath = 'C:/Users/HP/Desktop/csvhandlers/csvfiles/university.csv'


csv_list_writter(filename=filepath, list_data=rows, fields=fields, mode='a')