import os
from google.cloud import storage
import settings

# this function works for uploading single files
def upload_to_bucket(blob_name='static/test.txt', path_to_file='static/test.txt', bucket_name='ubyssey-prd-flex'):
    """ Upload data to a bucket"""

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        settings.GCS_CREDENTIALS_FILE)

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)

    #returns a public url
    return blob.public_url  

def select_file(path='static/gcs/'):
  """ Go through all files in the static directory and upload them """

  dir = os.listdir(path)

  for dir_name in dir:
    abs_path = os.path.join(path, dir_name)
    # if directory, enter it recursively
    if (os.path.isdir(abs_path)):
      select_file(abs_path)
    # else file, upload it
    else:
      print('uploaded to: ', upload_to_bucket('static/', abs_path))

print('UPLOADING STATIC FILES TO GCS...')
  
select_file(settings.STATIC_COLLECT)