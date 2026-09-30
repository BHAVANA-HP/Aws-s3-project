import boto3

s3 = boto3.client("s3", region_name="us-east-1")

bucket_name = "trial-bucket910816"

response = s3.create_bucket(Bucket=bucket_name)

print("Created bucket successfully")

file_name = 'eye.jpg'
s3.upload_file(file_name, bucket_name,file_name)
print("file is uploaded")
#s3.download_file(bucket_name,file_name,'downloaded-car.jpg')
#print("file is downloaded")
#response = s3.list_objects(Bucket = bucket_name)
#if 'Contents' in response:
    #for obj in response['Contents']:
        #print(obj['Key'])
#s3.delete_object( Bucket =bucket_name, Key= file_name)
#print("file deleted")
