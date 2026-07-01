def list_s3_bucket(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)
        
        
# function that upload file to s3 bucket
def upload_file_s3_bucket(s3, bucket_name, file_name):
    s3.Bucket(bucket_name).upload_file(file_name, file_name)
    print(f"File {file_name} uploaded to bucket {bucket_name} successfully.")
    
#list files in s3 bucket
def list_files_in_s3_bucket(s3, bucket_name):
    bucket=s3.Bucket(bucket_name)
    for names in bucket.objects.all():
        print(names.key)