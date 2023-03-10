import csv, os

key = ['name', 'branch', 'cgpa', 'age']

student_data = [
    {
      'name': 'Krishna', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
    
    {
      'name': 'Aisha', 
      'branch': 'ME',
      'cgpa': 8.1,
      'age': 24
     },
    
    {
      'name': 'Karna', 
      'branch': 'ME',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Krishna', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Lala', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Krishna', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
    
    {
      'name': 'Aisha', 
      'branch': 'ME',
      'cgpa': 8.1,
      'age': 24
     },
    
    {
      'name': 'Karna', 
      'branch': 'ME',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Krishna', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Lala', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Krishna', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
    
    {
      'name': 'Aisha', 
      'branch': 'ME',
      'cgpa': 8.1,
      'age': 24
     },
    
    {
      'name': 'Karna', 
      'branch': 'ME',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Krishna', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Lala', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Krishna', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
    
    {
      'name': 'Aisha', 
      'branch': 'ME',
      'cgpa': 8.1,
      'age': 24
     },
    
    {
      'name': 'Karna', 
      'branch': 'ME',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Krishna', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Lala', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Krishna', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
    
    {
      'name': 'Aisha', 
      'branch': 'ME',
      'cgpa': 8.1,
      'age': 24
     },
    
    {
      'name': 'Karna', 
      'branch': 'ME',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Krishna', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
     {
      'name': 'Lala', 
      'branch': 'CSE',
      'cgpa': 8.1,
      'age': 22
     },
     
]


def dict_csv_writter(file_name:str, mode:str, dict_data:dict, keys:list,  is_initial=False):
    if os.path.isfile(path=file_name):
        with open(file=file_name, mode=mode) as csvfile:

            csvwriter = csv.DictWriter(csvfile, fieldnames=key)

            if is_initial:
                try:
                    csvwriter.writeheader() # writin headers only
                except:
                    print('Error while header writing')
                
            try:
                csvwriter.writerows(dict_data) # writing dict datas here
            except:
                print('Error while rows data writing in dict func')
            else:
                print('Data successful written')

    else:
        print('Erorr file does found')

filepath = 'C:/Users/HP/Desktop/csvhandlers/csvfiles/university2.csv'

dict_csv_writter(file_name=filepath,mode='a', is_initial=True, dict_data=student_data, keys=key)