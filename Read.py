# Python program to read
# json file


import json

# Opening JSON file
f = open('Stock List.json',)

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
raw_data ={}
for i in data:

	# raw_data = i['close']
    raw_data['close'] = i['close']
    raw_data['open'] = i['open']
    raw_data['high'] = i['high']
    raw_data['low'] = i['low']
    print(raw_data)

	# print("close :",raw_data)

# Closing file
f.close()