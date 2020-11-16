def details(Id):
    import pandas as pd
    df=pd.read_csv("./data.csv")
    data=df.values
    unique_ids=list(data[:,0])
    print(unique_ids)
    row_index=unique_ids.index(Id)
    return data[row_index]
# check=details(312)
# print(check)
