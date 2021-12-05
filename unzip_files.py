import gzip
import shutil
import urllib.request
import os
import zipfile
def unzip_citibike_data():

    """Unzips Citibike zip files for both NY and JC.
    Returns:
        Nothing
    """

    zip_dir = 'C:/Users/Ben/Documents/GIT/fury-chelsea/tripdata/gz/'
    csv_dir = 'C:/Users/Ben/Documents/GIT/fury-chelsea/tripdata/'
    extension = ".zip"

    # for each zip file in zip_dir extract data to csv_dir
    for item in os.listdir(zip_dir):
        if item.endswith(extension):

            # create zipfile object and extract
            file_name = zip_dir + item
            with zipfile.ZipFile(file_name, "r") as zip_ref:
                zip_ref.extractall(csv_dir)
                print(item + " done")
                #os.remove(file_name)
if __name__== "__main__":
    unzip_citibike_data()