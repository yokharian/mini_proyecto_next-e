from datetime import datetime
from typing import List

import pandas as pd

from config import logger, table
from src.models import OpenWeatherInsight


def get_average(event, context):
    # current_time = datetime.now().time()
    # name = context.function_name
    # logger.info("Your cron function " + name + " ran at " + str(current_time))

    # TODO add chunk iterator to optimize ram usage & allow bigger date ranges
    # https://math.stackexchange.com/questions/22348/how-to-add-and-subtract-values-from-an-average

    response_items: List[OpenWeatherInsight] = OpenWeatherInsight.read(
        table=table,
        date_from=datetime.fromtimestamp(62862200),
        date_to=datetime.fromtimestamp(62871560),
    )
    columns_to_keep = ["clouds", "dew_point", "feels_like", "humidity", "pop", "pressure", "temp", "uvi", "visibility", "wind_deg","wind_gust", "wind_speed"]
    df = pd.DataFrame.from_records([i.dict() for i in response_items])
    output = df[columns_to_keep].describe().to_dict()
    return output


if __name__ == '__main__':
    print(get_average('',''))

