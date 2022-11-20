from decouple import config
import boto3

AWS_PROFILE = config("AWS_PROFILE", cast=str)
AWS_REGION = config("AWS_REGION", cast=str)
ROLE_NAME = "EC2ReadWriteS3Role"
INSTANCE_PROFILE_NAME = "EC2ReadWriteS3InstanceProfileName"
S3_FULLACCESS_POLICY_ARN = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
BUCKET_NAME = "photogrametry-images"

session = boto3.Session(profile_name=AWS_PROFILE, region_name=AWS_REGION)
