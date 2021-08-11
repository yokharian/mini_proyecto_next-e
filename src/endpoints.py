from datetime import datetime

from config import logger


def get_average(event, context):
    current_time = datetime.now().time()
    name = context.function_name
    logger.info("Your cron function " + name + " ran at " + str(current_time))

    # TODO add chunk iterator to optimize ram usage & allow bigger date ranges
    # https://math.stackexchange.com/questions/22348/how-to-add-and-subtract-values-from-an-average

