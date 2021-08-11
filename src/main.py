from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from config import table, LONGITUDE, LATITUDE, logger, DATETIME_FORMAT, LIMIT_OUTPUT
from models import OpenWeatherInsight
from openweather_api import OneCallAPI

if __name__ == "__main__":
    api = OneCallAPI(latitude=LATITUDE, longitude=LONGITUDE)
    response: List[OpenWeatherInsight] = api.extract_next_48_hours(
        output_limit=LIMIT_OUTPUT
    )

    errors = 0

    for insight in response:
        try:
            print(insight.put(table=table))
        except Exception as e:
            logger.exception(e)
            errors += 1
            continue

    print(f"\n{errors=} & successfully uploaded {len(response)} items")

    date_from: Optional[OpenWeatherInsight] = (
        response.pop(0) if len(response) > 0 else None
    )
    date_from: Optional[datetime] = (
        datetime.fromtimestamp(date_from.dt) if date_from else None
    )
    date_from: Optional[str] = (
        date_from.strftime(DATETIME_FORMAT) if date_from else None
    )

    date_to: Optional[OpenWeatherInsight] = (
        response.pop() if len(response) > 0 else date_from
    )
    date_to: Optional[datetime] = (
        datetime.fromtimestamp(date_to.dt) if date_to else None
    )
    date_to: Optional[str] = date_to.strftime(DATETIME_FORMAT) if date_to else None

    print(f"extracted from {date_from} to {date_to}")
