from decimal import Decimal

from pydantic import BaseModel

ONE_HOUR = 3600


class OpenWeatherInsight(BaseModel):
    clouds: int
    dew_point: Decimal
    dt: int
    dt_difference: int = ONE_HOUR
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

    class Weather(BaseModel):
        description: str
        icon: str
        id: int
        main: str

    weather: Weather

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
                "dt_end": self.dt + self.dt_difference,
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
