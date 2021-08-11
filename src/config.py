import logging
from os import getenv, environ

import boto3

AWS_DEFAULT_REGION = getenv("AWS_DEFAULT_REGION", "us-east-2")
DYNAMODB_TABLE = getenv("DYNAMODB_TABLE", "openweather_insights_next_e")
LIMIT_OUTPUT = int(getenv("LIMIT_OUTPUT", 8))
APPID = environ["APPID"]

monterrey_latitude = 25.6714
monterrey_longitude = -100.31847
LATITUDE = float(getenv("LATITUDE", monterrey_latitude))
LONGITUDE = float(getenv("LONGITUDE", monterrey_longitude))

dynamodb = boto3.resource("dynamodb", region_name=AWS_DEFAULT_REGION)
table = dynamodb.Table(DYNAMODB_TABLE)

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
logging.basicConfig()
logger = logging.getLogger("root")
