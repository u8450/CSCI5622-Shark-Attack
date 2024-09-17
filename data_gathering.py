import requests

End = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/global-shark-attack/records'

# Api has a limit of 100, the complete data have over 2500 rows so I will be downloading it
URLPost = {'limit':'100',
           'refine': 'country:"USA"'}
# print(URLPost)

response1 = requests.get(End, URLPost)
# print(response1)

jsontxt = response1.json()
#print(jsontxt)

filename = "shark.csv"

MyFILE=open(filename, 'w')

# Naming the columns
WriteThis = "Date,Year,Type,Country,Area,Activity,Sex,Age,Fatal (Y/N)\n"
MyFILE.write(WriteThis)
MyFILE.close()

# Reading file into csv
MyFILE = open(filename, "a")

# Adding items into the csv
for items in jsontxt["results"]:
    date = items['date']
    year = items['year']
    type = items['type']
    country = items['country']
    area = items['area']
    activity = items['activity']
    sex = items['sex']
    age = items['age']
    fatal = items['fatal_y_n']

    WriteThis=str(date)+","+str(year)+","+ str(type) + "," + str(country) + "," + str(area) + "," + str(activity) + "," + str(sex) + "," + str(age) + "," + str(fatal) + "\n"
    MyFILE.write(WriteThis)

MyFILE.close()
