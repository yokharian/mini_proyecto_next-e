import logging
from os import getenv, environ

import boto3
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

AWS_DEFAULT_REGION: str = getenv("AWS_DEFAULT_REGION", "us-east-2")
DYNAMODB_TABLE: str = environ["DYNAMODB_TABLE"]
LIMIT_OUTPUT: int = int(getenv("LIMIT_OUTPUT", 8))
APPID: str = getenv("APPID")

monterrey_latitude = 25.6714
monterrey_longitude = -100.31847
LATITUDE: float = float(getenv("LATITUDE", monterrey_latitude))
LONGITUDE: float = float(getenv("LONGITUDE", monterrey_longitude))

dynamodb = boto3.resource("dynamodb", region_name=AWS_DEFAULT_REGION)
table = dynamodb.Table(DYNAMODB_TABLE)

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
