from __future__ import annotations

from typing import List

import requests
from requests import Response

from config import DATE_FORMAT, APPID
from models import OpenWeatherInsight


class BaseApi:
    API_DATE_FORMAT = DATE_FORMAT
    BASE_URL = "https://api.openweathermap.org/"
    APPID = APPID

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def _request(self, endpoint, method="GET", **kwargs) -> Response:
        _BASE_URL = self.BASE_URL if self.BASE_URL.endswith("/") else self.BASE_URL[:-1]
        _ENDPOINT = endpoint[1:] if endpoint.startswith("/") else endpoint

        url = _BASE_URL + _ENDPOINT
        PARAMS = {"APPID": self.APPID}

        final_kwargs = {"url": url, "method": method, "params": PARAMS}
        if 'params' in kwargs:
            final_kwargs['params'].update(kwargs.pop('params'))

        return requests.request(**final_kwargs)


class OneCallAPI(BaseApi):
    DATA_ONE_CALL_ENDPOINT = "/data/2.5/onecall"
    EXCLUDE = "current,minutely,daily,alerts"
    UNITS = "metric"
    LANG = "es"

    def __init__(self, latitude: float, longitude: float, **kwargs):
        self.latitude, self.longitude = latitude, longitude
        super().__init__(**kwargs)

    def _request(self, method="GET", **kwargs):
        PARAMS = dict(exclude=self.EXCLUDE, units=self.UNITS, lang=self.LANG)
        _ENDPOINT = OneCallAPI.DATA_ONE_CALL_ENDPOINT

        final_kwargs = dict(method=method, endpoint=_ENDPOINT, params=PARAMS)
        # use default class variables, if they doesn't exists at kwargs
        if 'params' in kwargs:
            final_kwargs['params'].update(kwargs.pop('params'))
        final_kwargs.update(**kwargs)

        return super()._request(**final_kwargs)

    def extract_next_48_hours(self, output_limit=6) -> List[OpenWeatherInsight]:
        response = self._request(params=dict(lat=self.latitude, lon=self.longitude))
        response.raise_for_status()

        output: List[OpenWeatherInsight] = []
        for index, hour in enumerate(response.json()["hourly"]):
            weather: List[dict] = hour.pop("weather")
            weather: dict = weather and weather.pop()
            output += [OpenWeatherInsight(**hour, weather=weather)]

            if output_limit and (index + 1 >= output_limit):
                break
        return output
