#!/usr/bin/env python


from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import os
from azure.storage.blob import ContentSettings
#Connect to Account
CONNECT_STR= "DefaultEndpointsProtocol=https;AccountName=bgksolutions;AccountKey=y4vyQo7g+E2NC+GxkRrpewaK+F1Q4xOoTR8Q3KnnM9zGWErRJcyGabtcWiuDP0U9k54UMWPXb1yB0b8m+ac6XA==;EndpointSuffix=core.windows.net"
block_blob_service = BlobServiceClient.from_connection_string(CONNECT_STR)
print("connected")
#Create  Container
container_name="citibkiedata"
block_blob_service.create_container(container_name)

# Create a blob client using the local file name as the name for the blob
def run_citi_files():
    self_client = block_blob_service.get_container_client(container_name)
    local_path='C:/Users/Ben/Documents/GIT/fury-chelsea/tripdata/azure'
    path_remove = 'C:/Users/Ben/Documents/GIT/fury-chelsea/tripdata/'
    for r, d, f in os.walk(local_path):
        if f:
            for file in f:
                file_path_on_azure = os.path.join(r, file).replace(path_remove, "")
                file_path_on_local = os.path.join(r, file)
                blob_client = self_client.get_blob_client(file_path_on_azure)
                with open(file_path_on_local, 'rb') as data:
                    blob_client.upload_blob(data)

if __name__ == '__main__':
    run_citi_files()
    print("**completed**")