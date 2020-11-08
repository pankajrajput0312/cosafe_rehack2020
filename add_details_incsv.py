def add_details(Name,unique_id,email_id,phone_no):
    list_of_elem=[unique_id,Name,email_id,phone_no]
    from csv import writer
    # Open file in append mode
    with open("data.csv", 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
# add_details("anand","456","anand_fake_mail@gmail.com")
