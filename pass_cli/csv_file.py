import os,csv

from  pass_cli.config import fieldnames
class Data_Operator:
    def __init__(self,file_name):
        self.filename=file_name
        self.fieldnames=fieldnames

    def readit(self):
        if not os.path.exists(self.filename):return FileNotFoundError("File doesnt exist")
        with open(self.filename,'r') as csv_file:
            csv_reader=csv.DictReader(csv_file)
            extracted_data=[i for i in csv_reader]
    
        return extracted_data

    def writeit(self,data=None):
        if data:
            if not len(data)==3:return ValueError("Input must have 3 columns")
        if os.path.exists(self.filename):self.exist_state=True
        with open(self.filename,'a',newline='') as csv_file:
            csv_writer=csv.DictWriter(csv_file,fieldnames=self.fieldnames)
            if data==None: csv_writer.writeheader()
            else: csv_writer.writerow(data)
    
    def editit(self,data):
        with open(self.filename,'w',newline='') as csv_file:
            csv_writer=csv.DictWriter(csv_file,fieldnames=self.fieldnames)
            csv_writer.writeheader()
            for row in data:
                 csv_writer.writerow(row)


