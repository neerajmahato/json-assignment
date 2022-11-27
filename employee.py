import json
employee_1 = {"Name": "Abhishek Singh","DOB":"5th May 1997","Height":"5 feet 5 inches","City":"Jamshedpur","State":"Jharkhand"}
employee_2 = {"Name": "Neeraj Mahato ","DOB":"31st October 1998","Height":"5 feet 7 inches","City":"Jamshedpur","State":"Jharkhand"}
employee_3 = {"Name": "Arkodeep ","DOB":"20th November 1997","Height":"5 feet 9 inches","City":"Jamshedpur","State":"Jharkhand"}
employee_4 = {"Name": "Nikhil Kumar ","DOB":"12th May 1997","Height":"6 feet 2 inches","City":"Jamshedpur","State":"Jharkhand"}
employee_5 = {"Name": "Ajay Mahato","DOB":"3rd April 1998","Height":"5 feet 2 inches","City":"Jamshedpur","State":"Jharkhand"}
with open("employee.json","w") as f:
  json.dump(employee_1,f)
  json.dump(employee_2,f)
  json.dump(employee_3,f)
  json.dump(employee_4,f)
  json.dump(employee_5,f)
  print("Json Completed")