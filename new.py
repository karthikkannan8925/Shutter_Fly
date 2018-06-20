import pandas as pd

df = pd.read_json('C:\Karthik\Spark\Shutter_fly_test\sample_input.txt')


types = df[df.types == 'CUSTOMER']

print(types)