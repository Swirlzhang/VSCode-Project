from Package_A.Package_A_1 import Module_A_1
from Package_A.Package_A_2 import Module_A_2
from Package_B.Package_B_1 import Module_B_1
from Package_B.Package_B_2 import Module_B_2

print(Module_A_1.A_1)
# function that calculates how many days between two dates 
def days_between_dates(date1, date2):
    from datetime import datetime
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

print(days_between_dates("2023-01-01", "2023-12-31"))

# function that connects to mongo db
def connect_to_mongo(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost', 27017)
    db = client[db_name]
    return db

print(__name__)


list_A: Any = [1, 2, None]
if all(list_A):
    print("All elements are truthy" )
elif any(list_A):
    print("At least one element is truthy" )
else:
    print("No elements are truthy" )    

