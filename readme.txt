-Run it on spyder IDE and Python3.
-Put the csv data file in the same directory as code.
-Relative Path of the file is given in function read_csv()
-Running the code generates r.csv and r1.csv corresponding to results for all users and for one specific user.


Algorith:
-Pick transactions for each users
-Pick transaction happend to each unique merchant
-merchant_name picked for getting unique merchants
-Dropping the duplicate transaction for a user happend to same merchant on same day.

Improvements:
-Same merchants with names 'Uber BV' and 'UBER BV' treated as different because of different merchant_id. Can convert all
the names to upper or lower case to treat them one.

Results:
-Duplicates removed.
-Dataset cleansed to 6160 rows from 7016 rows
-For a specific user number of transactions reduced to 350 from 396.
-Code takes a little bit of time in function omit_same_day_transaction() because it contains a nested for loop.
-Size of r.csv is little bigger than the dataset file because it contains two new columns of data and time compared to 
dataset file. But we can omit these. Kept for the sake to analyze easily.