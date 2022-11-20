#!/bin/bash
echo "Sleeping for 100 seconds…"
aws s3 ls s3://{bucket}
sleep 10
echo "Shuting down..."
shutdown -h now