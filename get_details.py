def details(Id):
    import pandas as pd
    df=pd.read_csv("./data.csv")
    data=df.values
    unque_ids=list(data[:,0])
    row_index=unque_ids.index(Id)
    return data[row_index]
# check=details(312)
# print(check)
