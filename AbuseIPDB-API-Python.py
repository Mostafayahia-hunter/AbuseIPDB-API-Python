import requests
import json
import pandas
import csv

file_path = str(input('please Enter The File Path: '))
IP_CSV = pandas.read_csv((file_path))

ip=IP_CSV['IP'].tolist()


API_KEY = 'YOURAPIKEY'
url = 'https://api.abuseipdb.com/api/v2/check'

csv_columns = ['ipAddress','isPublic','ipVersion','isWhitelisted','abuseConfidenceScore','countryCode','usageType','isp','domain','hostnames','totalReports','numDistinctUsers','lastReportedAt']

headers = {
    'Accept': 'application/json',
    'Key': API_KEY
}
with open("AbuseIP_results.csv","a", newline='') as filecsv:
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    writer.writeheader()
for i in ip:
    parameters = {
        'ipAddress': i,
        'maxAgeInDays': '90'}

    respnse= requests.get( url=url,headers=headers,params=parameters)
    json_Data = json.loads(respnse.content)
    json_main = json_Data["data"]
    with open("AbuseIP_results.csv","a", newline='')as filecsv:
        writer= csv.DictWriter(filecsv,fieldnames=csv_columns)
        writer.writerow(json_main)
