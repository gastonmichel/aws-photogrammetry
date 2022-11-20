from config import session, ROLE_NAME, INSTANCE_PROFILE_NAME, S3_FULLACCESS_POLICY_ARN

iam = session.client("iam")


iam.remove_role_from_instance_profile(
    InstanceProfileName=INSTANCE_PROFILE_NAME,
    RoleName=ROLE_NAME
)

iam.delete_instance_profile(
    InstanceProfileName=INSTANCE_PROFILE_NAME
)

iam.detach_role_policy(
    RoleName=ROLE_NAME,
    PolicyArn=S3_FULLACCESS_POLICY_ARN
)

iam.delete_role(
    RoleName=ROLE_NAME,
)