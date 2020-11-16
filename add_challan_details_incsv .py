def add_details(Name,unique_id,email_id,phone_no):
    import os
    from datetime import date 
    from datetime import datetime
    today = str(date.today())
    print(today)
    time=str(datetime.now())
    time=time[11:19]
    print(time)
    name=today+".csv"
    print(name)

    list_of_elem=[unique_id,Name,email_id,phone_no,today,time]
    
    from csv import writer
    # Open file in append mode
    path=os.path.join("unmask_detail",name)
    with open(path, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
def check_sms_send(Id):
    import pandas as pd
    import os
    available=os.listdir("unmask_detail")
    from datetime import date 
    from datetime import datetime

    today = str(date.today())
    name=today+".csv"
    if name in available:
        df=pd.read_csv(os.path.join("unmask_detail",name))
        df=df.values
        unique_ids=df[0]
        if Id in unique_ids:
            return
        from sms_send import send_sms
        send_sms(9315630275,Id)
        from get_details import details
        detail=details(Id)
        add_details(detail[1],Id,detail[2],detail[3])


# add_details("anand","456","anand_fake_mail@gmail.com","9736363636")
# check_sms_send(312)