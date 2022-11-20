from config import BUCKET_NAME, session, INSTANCE_PROFILE_NAME
from pprint import pprint as print
from time import sleep

ec2 = session.resource("ec2")
client = session.client("ec2")

instance = ec2.create_instances(
    MinCount=1,
    MaxCount=1,
    ImageId="ami-05f271938ea4f9121",
    InstanceType="t2.micro",
    InstanceMarketOptions={"MarketType": "spot"},
    InstanceInitiatedShutdownBehavior="terminate",
    UserData=open("shutdown.sh").read().format(bucket=BUCKET_NAME),
    IamInstanceProfile={"Name": INSTANCE_PROFILE_NAME},
)[0]

instance_running = client.get_waiter("instance_running")
instance_running.wait(
    InstanceIds=[
        instance.id,
    ],
)
print(f"Instance {instance.id} is running...")

sleep(5)
print(instance.state)
print(instance.console_output(Latest=False))