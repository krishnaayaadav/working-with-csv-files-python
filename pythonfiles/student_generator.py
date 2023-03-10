
"name, email, age, address"
import os, csv, requests
from bs4 import BeautifulSoup


def web_scrapper(target_url:str):

    web_page = requests.get(url=target_url)
    soup = BeautifulSoup(web_page.content, 'lxml')

    theads = soup.find('table').find('tr').find_all('th')
    
    # getting all headlings here
    allheading = [theads[i].text for i in range(len(theads))]

    # print(allheading)
    
    all_trs     = soup.find('table').find_all('tr', class_ ='trhvr')
    
    all_emp_data = []

    ln = len(all_trs)
    for i in range(ln):
        tds = all_trs[i].find_all('td')
        emp_id = tds[0].text
        emp_name = tds[2].text
        emp_depart = tds[3].text
        emp_salary = tds[4].text
        emp_email = tds[5].text

        employee = {
            'id':  emp_id,
            'name': emp_name,
            'emial': emp_email,
            'salary':  emp_salary,
            'department': emp_depart
        }

        # 
        # ['id', 'name',, 'emial',  'salary', 'department']

        all_emp_data.append(employee)


        # print(emp_email)

        print(emp_id,emp_name, emp_email, emp_depart, emp_salary)
    
    return all_emp_data

class CSVHandler:

    def __init__(self, filename:str, mode:str):
        self.filename = filename
        self.mode     = mode
    
    def csvdict_writter(self, dict_data:dict, key_field:list, is_inital=False):

        if os.path.isfile(self.filename):
            with open(self.filename, mode=self.mode) as csvfile:

                if csvfile.writable():
                    csvwriter = csv.DictWriter(csvfile, fieldnames=key_field)

                    if is_inital == True:
                        try:
                            csvwriter.writeheader() # wrting headlers
                        except:
                            print('Error while file hander writting ')
                    
                    try:
                        csvwriter.writerows(dict_data)
                    except:
                        print('Error while dict data(rows) writter')
                    else:
                        print('Data Successful Written')

                else:
                    print('Current File Does Not have permission to write')
        else:
            print('Error: File Does Not Exist')

    def csvdict_reader(self):
        pass

    def list_csv_writer(self):
        pass


# emp_keys = ['id', 'name', 'emial', 'salary', 'department']

URL = 'https://krishnayadv.pythonanywhere.com/?page='
filepath = 'C:/Users/HP/Desktop/csvhandlers/csvfiles/employees.csv'

csv1 = CSVHandler(filename=filepath, mode='a')

# emps_data = web_scrapper(URL)
# csv1.csvdict_writter(dict_data=emps_data, key_field=emp_keys, is_inital=True)

def writter_page(page:int, URL:str):
    emp_keys = ['id', 'name', 'emial', 'salary', 'department']


    for i in range(1,page+1):
        URL += f'{i}'
        emp_data = web_scrapper(target_url=URL)
        inital = False
        if i == 1:
            inital = True
        csv1.csvdict_writter(dict_data=emp_data, key_field=emp_keys, is_inital=inital)

writter_page(page=5, URL=URL)
        


        