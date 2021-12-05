import gzip
import shutil
import urllib.request
import os
import zipfile

def retrieve_citibike_data():

    """Retrieves trip data from Citibike's S3 buckets as zip files.
    Downloads trip data from October 2016 to December 2017
    Returns:
        Nothing
    """

    target = 'C:/Users/Ben/Documents/GIT/fury-chelsea/tripdata/gz/'
    for year in range(2018, 2022):
        for month in range(1, 13):

            date_format = str(year) + '{:02d}'.format(month)

            # retrieve data from citibike's s3 buckets and store in zip directory
            if year < 2017:
                urllib.request.urlretrieve("https://s3.amazonaws.com/tripdata/" + date_format +
                                           "-citibike-tripdata.zip", target + date_format + ".zip")
            else:
                urllib.request.urlretrieve("https://s3.amazonaws.com/tripdata/" + date_format +
                                           "-citibike-tripdata.csv.zip", target + date_format + ".csv.zip")
            print(str(year) + "-" + str(month) + " done")
if __name__== "__main__":
    retrieve_citibike_data()