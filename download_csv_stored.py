from urllib import request

# --------------------------------------------------------------------------------

# Different way of importing modules is:
# from urllib import request
# Example to download a CSV file. For that we are going to use available csv file from Internet.


print()
print('Example to download a CSV file. For that we are going to use available csv file from Internet')
print()

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=10&b=28&c=2016&d=11&e=28&f=2016&g=d&ignore=.csv'

# We define a function to download the file


def download_csv_file_date(csv_url):
    # We tell python to connect to Internet, for that we define a variable response, which will get the
    # request.urlopen() function with the csv_url parameter, the url from any internet page stored into the
    # response variable
    response = request.urlopen(csv_url)
    # Define a variable 'csv' that will store data that is read from the url file. So we use the response.read()
    # function which will read data from any url we are pointing to csv_url. Whatever data is read from the file
    # we convert into a string to prevent errors, for example in case data is just numbers, date data, etc.
    csv = response.read()
    csv_str = str(csv)
    # Since the csv_str variable has the content of the cvs file which can be many lines, the cvs_str variable has
    # all that data in a single line, this can be confusing, so we need to display/print data in different lines as
    # the original csv file is. For that we use the function split which will break it up the data in different lines
    var_lines = csv_str.split("\\n")
    # Finally we stored to file into our mac/pc. Define a variable were we are going to save it
    destination_file = r'goog.csv'
    # Define a a variable to open the file and write into it the content of our cvs file that we downloaded from
    # Internet and printed into the goog.csv file
    file_dest = open(destination_file, "w")
    for line in var_lines:
        file_dest.write(line + "\n")
    file_dest.close()

# Finally we call the function


download_csv_file_date(goog_url)
