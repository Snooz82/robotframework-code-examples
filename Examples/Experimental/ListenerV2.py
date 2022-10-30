from robot.api import logger


class ListenerV2:

    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        logger.console(f"🔹 Listener Init")

    def start_suite(self, name, attrs):
        logger.console(f"🔹 .start_suite    name: {name}     attrs: {attrs}")

    def start_test(self, name, attrs):
        logger.console(f"🔹 ..start_test    name: {name}     attrs: {attrs}")

    def start_keyword(self, name, attrs):
        logger.console(f"🔹 ...start_keyword    name: {name}     attrs: {attrs}")

    def end_keyword(self, name, attrs):
        logger.console(f"🔹 ...end_keyword    name: {name}     attrs: {attrs}")

    def end_test(self, name, attrs):
        logger.console(f"🔹 ..end_test    name: {name}     attrs: {attrs}")

    def end_suite(self, name, attrs):
        logger.console(f"🔹 .end_suite    name: {name}     attrs: {attrs}")

    def log_message(self, message):
        logger.console(f"🔹 log_message   {message}")

    def message(self, message):
        logger.console(f"🔹 message   {message}")

    def library_import(self, name, attrs):
        logger.console(f"🔹 library_import    name: {name}     attrs: {attrs}")

    def resource_import(self, name, attrs):
        logger.console(f"🔹 resource_import    name: {name}     attrs: {attrs}")

    def variables_import(self, name, attrs):
        logger.console(f"🔹 variables_import    name: {name}     attrs: {attrs}")

    def output_file(self, path):
        logger.console(f"🔹 output_file")

    def log_file(self, path):
        logger.console(f"🔹 log_file")

    def report_file(self, path):
        logger.console(f"🔹 report_file")

    def xunit_file(self, path):
        logger.console(f"🔹 xunit_file")

    def debug_file(self, path):
        logger.console(f"🔹 debug_file")

    def close(self):
        logger.console(f"🔹 close")

