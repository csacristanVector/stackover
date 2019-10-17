from lambda_archetype import utils


logger = utils.log_util.setup_logger('INFO', 'app_unit')


def function_app_unit():
    utils.util_a.function_util_a()
    print('Application run here')
