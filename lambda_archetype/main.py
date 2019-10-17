from lambda_archetype import utils
from lambda_archetype import app_unit


logger = utils.log_util.setup_logger('INFO', 'main_lambda_handler')


def lambda_handler(even: dict, context: dict):
    logger.info('Start function')
    utils.util_a.function_util_a()
    utils.util_b.function_util_b()

    app_unit.main.function_app_unit()

    logger.info('Function completed')
    return 0


if __name__ == '__main__':
    lambda_handler(
        even=dict({'key1': 'value1'}),
        context=dict({'A-Key': 'A-Content'})
    )

