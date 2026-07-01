import boto3
from function import list_s3_bucket, upload_file_s3_bucket, list_files_in_s3_bucket

s3_obj = boto3.resource('s3')

print(dir(s3_obj.__doc__))


list_s3_bucket(s3_obj)

upload_file_s3_bucket(s3_obj, 'newbucket12332', 'my_new_file2.txt')

list_files_in_s3_bucket(s3_obj, 'newbucket12332')