import json

with open('C:\Karthik\Spark\Shutter_fly_test\sample_input.txt') as json_file:
    data = json.load(json_file)

    output_dict = [x for x in data if x["customer_id"] == '1']
    print(output_dict)