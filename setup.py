from config import session, ROLE_NAME, INSTANCE_PROFILE_NAME, BUCKET_NAME, S3_FULLACCESS_POLICY_ARN


def setup_role():
    iam = session.client("iam")

    iam.create_role(
        RoleName=ROLE_NAME,
        AssumeRolePolicyDocument=open("ec2AssumeRole.json").read(),
    )

    iam.attach_role_policy(
        RoleName=ROLE_NAME,
        PolicyArn=S3_FULLACCESS_POLICY_ARN,
    )

    iam.create_instance_profile(
        InstanceProfileName=INSTANCE_PROFILE_NAME,
    )

    iam.add_role_to_instance_profile(
        InstanceProfileName=INSTANCE_PROFILE_NAME,
        RoleName=ROLE_NAME,
    )

def setup_s3():
    s3 = session.client("s3")

    s3.create_bucket(
        ACL='private',
        Bucket=BUCKET_NAME
    ) 

setup_s3()