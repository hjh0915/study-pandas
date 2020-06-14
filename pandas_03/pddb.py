import pandas as pd 
import numpy as np

def get_series():
    x = pd.Series([1,4,2,9,190])
    y = pd.Series(['a', 9, 1, 'b']) 
    print(x)
    print(y)

def get_dataframe():
    x = pd.DataFrame([1,2,3,4,5,6,7,8,9], columns=['number'])
    print(x)

def get_index():
    x = pd.Index(np.arange(3))   
    print(x)

if __name__ == '__main__':
    print(get_series())
    print(get_dataframe())
    print(get_index())