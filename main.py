import pandas as pd
import random
lst = ['robot']*10 + ['human']*10
random.shuffle(lst)
data = pd.DataFrame({'whoAmi':lst})

data['robot'] = (data['whoAmi'] == 'robot').astype(int)
data['human'] = (data['whoAmi'] == 'human').astype(int)
print(data.head(10))
