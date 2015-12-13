


Basically, you can simply run the scripts to see the results. 


----Loading behavior data----
For example, if you want to load a certain subject's behavior data, open load_data_scipt.py and put your subject number in the commented portion.
Then,

run load_data_script.py

Your np.array is stored in the variable name "behav"
Your dataframe is stored in the variable name "behav_df"



----Doing logistic regression on the subject's behavior data----

(Assume you hav "behav_df" before running this)
(you have to pass in data frame)

%run -i log_regression_script.py



----Doing linear regression on the subject's behavior data----

(Assume you hav "behav_df" before running this)
(you have to pass in data frame)

run log_regression_script.py




---Checking Summary Statistics on the subject's behavior data----

(Assume you hav "behav_df" before running this)
(you have to pass in data frame)

%run -i summary_stat_script.py


