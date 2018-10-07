import json
#adding comments

with open('C:\Karthik\Spark\Shutter_fly_test\sample_input.txt') as json_file:
    data = json.load(json_file)

def customer():
    output_dict = [x for x in data if x['key'] == '1']

    return output_dict


def site_visit():
    for i in data:
        if (i['type']) == "SITE_VISIT":
             return(i)

def image():
    for i in data:
        if (i['type']) == "IMAGE":
            return(i)

def order():
    for i in data:

        if (i['type']) == "ORDER":
            return(i)



if (customer()['key']) == order()['customer_id']:
    print("the customer name is {} and the order value is {}".format(customer()['last_name'],order()['total_amount']))







