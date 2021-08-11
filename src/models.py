from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from json import dumps
from typing import List

from boto3.dynamodb.conditions import Key
from pydantic import BaseModel, Field

ONE_HOUR = 3600


class WeatherSpecs(BaseModel):
    description: str
    icon: str
    id: int
    main: str


class OpenWeatherInsight(BaseModel):
    dt: int
    dt_difference: int = ONE_HOUR
    clouds: int
    dew_point: Decimal
    feels_like: Decimal
    humidity: int
    pop: Decimal
    pressure: int
    temp: Decimal
    uvi: Decimal
    visibility: int
    wind_deg: int
    wind_gust: Decimal
    wind_speed: Decimal

    weather: WeatherSpecs

    def put(self, table):
        """\
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.put_item
        :param table: Dynamodb Table
        :return: dynamodb response
        """
        response = table.put_item(
            Item={
                "clouds": self.clouds,
                "dew_point": self.dew_point,
                "dt": self.dt,
                "dt_difference": self.dt_difference,
                "feels_like": self.feels_like,
                "humidity": self.humidity,
                "pop": self.pop,
                "pressure": self.pressure,
                "temp": self.temp,
                "uvi": self.uvi,
                "visibility": self.visibility,
                "wind_deg": self.wind_deg,
                "wind_gust": self.wind_gust,
                "wind_speed": self.wind_speed,
                "weather": {
                    "description": self.weather.description,
                    "icon": self.weather.icon,
                    "id": self.weather.id,
                    "main": self.weather.main,
                },
            }
        )
        return response

    @classmethod
    def read(
        cls, table, date_from: datetime, date_to: datetime, dt_difference=3600
    ) -> List[OpenWeatherInsight]:
        date_from: Decimal = Decimal(date_from.timestamp())
        date_to: Decimal = Decimal(date_to.timestamp())

        # keep date_from the lower in order to keep range logic
        if date_to < date_from:
            date_from, date_to = date_to, date_from

        _response = table.query(
            KeyConditionExpression=Key("dt").between(date_from, date_to)
            & Key("dt_difference").eq(dt_difference),
        )
        return [OpenWeatherInsight(**i) for i in _response.get("Items", [])]


class LambdaTriggerResponse(BaseModel):
    statusCode: int
    body: str = Field(default_factory=dumps)
    isBase64Encoded: bool = False
    headers: dict = {}

    def to_json(self):
        return dumps(self.dict())


class Response400(BaseModel):
    statusCode: int = 400


class Response200(BaseModel):
    statusCode: int = 200
