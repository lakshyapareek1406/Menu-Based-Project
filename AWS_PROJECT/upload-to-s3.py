
#Uploading the any object to s3


#!/usr/bin/env python
import cgi
import boto3

print("Content-type:text/html\r\n\r\n")

form = cgi.FieldStorage()

# Replace with your S3 credentials
region = 'region'
aws_access_key_id = 'your key'
aws_secret_access_key = 'your secret key'

try:
    # Get file data and bucket name from form
    file_item = form['file']
    bucket_name = form.getvalue('bucketName')

    # Upload file to S3
    s3 = boto3.client('s3', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    s3.upload_fileobj(file_item.file, bucket_name, file_item.filename)

    print(f"File '{file_item.filename}' uploaded successfully to '{bucket_name}'.")
except Exception as e:
    print(f"Error uploading file: {e}")
