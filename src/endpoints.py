from datetime import datetime
from datetime import datetime
from typing import List

import pandas as pd

from config import logger, table, DATETIME_FORMAT
from src.models import (
    OpenWeatherInsight,
    Response400,
    Response200,
)


def get_average(event, context):
    date_from = event["queryStringParameters"]["date_from"]
    date_from = datetime.strptime(date_from, DATETIME_FORMAT)

    date_to = event["queryStringParameters"]["date_to"]
    date_to = datetime.strptime(date_to, DATETIME_FORMAT)

    # TODO add chunk iterator to optimize ram usage & allow bigger date ranges
    # https://math.stackexchange.com/questions/22348/how-to-add-and-subtract-values-from-an-average
    response_items: List[OpenWeatherInsight] = OpenWeatherInsight.read(
        table=table,
        date_from=date_from,
        date_to=date_to,
    )
    if not response_items:
        return Response400(body={"error": "not found data for specified dates"}).dict()

    try:
        df = pd.DataFrame.from_records([i.dict() for i in response_items])
        COLUMNS_TO_KEEP = [
            "clouds",
            "dew_point",
            "feels_like",
            "humidity",
            "pop",
            "pressure",
            "temp",
            "uvi",
            "visibility",
            "wind_deg",
            "wind_gust",
            "wind_speed",
        ]
        output = df[COLUMNS_TO_KEEP].describe().to_dict()
        Response200(body=output).dict()
    except Exception as e:
        logger.error(e)
        Response400(
            body={
                "error": f"wrong data found for specified dates save this "
                f"timestamp for further debug {datetime.now().timestamp()}"
            }
        ).dict()
