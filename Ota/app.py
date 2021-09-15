import json

# import requests
from Ota import s3_accessor


def lambda_handler(event, context):
    return_code, response = s3_accessor.get_file(event["body"]["request"]["fileName"])
    if return_code == 0:
        return {
            "statusCode": 200,
            "body": response
        }
    else:
        return {
            "statusCode": 500,
            "body": {
                "errorMessage": response
            }
        }
