

import json
import collections
from collections import OrderedDict 




#convert value for key 'quantity' for 100gm into value for data 23gm,50gm and 260gm
def conversion(value):
    value = float(value)
    to_23 = value*(0.23)
    to_50 = value*(0.5)
    to_260 = value*(2.60)
    return to_23,to_50,to_260


#generate value for key 'quantity' for data 23gm,50gm and 260gm
def generate(value):
    to_23,to_50,to_260 = conversion(value)
    return to_23,to_50,to_260


#update value of key 'quantity' for data 100gm  with value for data 23gm,50gm and 260gm 
def update_data(key):
    value = key['quantity']
    if int(value) != 0:
        new_value = generate(value)
        key['quantity'] = new_value
    else:
        #if value is 0 no conversion is required as value for data 23gm,50gm and 260g will be 0
        key['quantity'] = (0.0,)*3




#recursively update value of key 'quantity' for data 100gm  with value for data 23gm,50gm and 260gm 
def quantity_conversion(data):
    if isinstance(data, dict) == True:
        key_list= data.keys()
        if 'quantity' not in key_list:
            for key in key_list:
                new_data = data[key] 
                quantity_conversion(new_data) 
        else:
            update_data(data)

    else:
        for key in range(len(data)):
            value_list = data[key].values()
            for value in value_list:
                quantity_conversion(value)


#load data from data.json file
orig_data = json.load(open("data.json"), object_pairs_hook=OrderedDict)
orig_data = orig_data
data = orig_data['data']


#get data for 100gm
data = data['100gm']

#Update value of key 'quantity' for 23gm, 50gm and 260gm
y = quantity_conversion(data)


#write updated data to data.json file
fp = open("data.json", 'w')
fp.write(json.dumps(orig_data, indent = 4))

