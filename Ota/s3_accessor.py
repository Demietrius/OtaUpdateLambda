import json
import logging
import os

# import cglogging as cgl
import boto3
import uuid
from datetime import datetime
from datetime import timezone



def get_file(name):
    try:
        s3 = boto3.resource('s3', region_name=os.getenv("REGION"))

        # bucket = 'charterandgoreplaymessages'    # name of the s3 bucket
        bucket = "ota-software-storage"
        file_key = "2021/" + name

        object = s3.Object(bucket, file_key)
        body = object.get()["Body"].read()
        return 0, body
    except Exception as details:
        logging.debug("unexpecter error: (0)".format(details))
        return 1, "Unknown error retrieving  the update"




