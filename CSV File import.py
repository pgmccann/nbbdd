from behave import given, when, then
import os.path
@given('the csv file to import exists')
def step_the_csv_file_to_import_exists(context):
	assert os.path.exists("results.csv"), "results.csv does not exist"
@when('I call pandas read_csv')
def step_I_call_pandas_read_csv(context):
	context.loader = CSVLoader("results.csv")
	context.loader.load()
@given('a dataframe with 3 columns and 5 rows should be returned')
def step_a_dataframe_with_3_columns_and_5_rows_should_be_returned(context):
	shape = context.loader.df_Results.shape
	assert (shape[0] == 5), "5 rows not returned"
	assert (shape[1] == 3), "3 columns not returned"