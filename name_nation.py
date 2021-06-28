import requests
import json

def ask_name_result():
    inputname = str(input('\nplease input the name you want to search \n'))
    url = "https://api.nationalize.io?name=" + inputname
    response = requests.request("GET", url)
    wellshow = json.loads(response.text)
    check_base=0
    check_limit=len(wellshow['country'])
    while check_base < check_limit:
        percentage_name= str(int(100*float(wellshow['country'][check_base]['probability'])))
        print( "the name  " + inputname  + " in country " + wellshow['country'][check_base]['country_id'] + " probability is " + percentage_name + "%")
        check_base = check_base + 1

while True:
    ask_name_result()
