#send sms using fastsms API
def send_sms(number, Id):
    import  requests
    import json
    import pandas as pd
    url = "https://www.fast2sms.com/dev/bulk"
    df=pd.read_csv("./data.csv")
    data=df.values
    from get_details import details
    person_details=list(details(Id))
    message_admin="Person Name "+str(person_details[1])+" unique_id "+str(person_details[0])+" Email_id: "+str(person_details[2])+" detected without mask in UAS LAB"
    message_violeter="you captured without mask in camera. We request you please wear mask for your safety and help us to stop covid."
    user_number=str(person_details[3])


    prams_voileter = {
        "authorization" : "Q7BKRrYei2pxU0z8t1D4gOuJFPLNaydIqmhbTk5fVoXWAElGcvOv71o4hVmin3cfZdDIFG56rwqjYNX9",
        "sender_id" : "FSTSMS",
        "route" : "p",
        "language" : "unicode",
        "numbers" : user_number,
        "message" : message_violeter
    }
    prams_admin={
        "authorization" : "Q7BKRrYei2pxU0z8t1D4gOuJFPLNaydIqmhbTk5fVoXWAElGcvOv71o4hVmin3cfZdDIFG56rwqjYNX9",
        "sender_id" : "FSTSMS",
        "route" : "p",
        "language" : "unicode",
        "numbers" : number,
        "message" : message_admin
    }
    response_voileter = requests.get(url, params= prams_voileter)
    response_admin=requests.get(url, params= prams_admin)
    dic_violeter= response_voileter.json()
    dic_admin=response_admin.json()
    print(dic_violeter)
    print(dic_admin)
# send_sms(9315630275,"message gaya hai abhi abhi")