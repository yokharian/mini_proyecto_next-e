import logging
from os import getenv, environ

import boto3
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DYNAMODB_TABLE: str = environ["DYNAMODB_TABLE"]
AWS_DEFAULT_REGION: str = getenv("AWS_DEFAULT_REGION", "us-east-2")
LIMIT_OUTPUT: int = int(getenv("LIMIT_OUTPUT", 8))
LATITUDE: float = float(getenv("LATITUDE"))
LONGITUDE: float = float(getenv("LONGITUDE"))
APPID: str = getenv("APPID")

dynamodb = boto3.resource("dynamodb", region_name=AWS_DEFAULT_REGION)
table = dynamodb.Table(DYNAMODB_TABLE)

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
