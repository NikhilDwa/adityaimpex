import configparser
from pathlib import Path


class PathUtils:
    __base_path = Path(__file__).resolve().parent.parent

    def get_base_path(self):
        """
        Returns the project root path.
        """
        return self.__base_path

    def get_configuration(self):
        """
        Gets the configuration file, read and parse the configuration file.
        """
        config = configparser.ConfigParser()
        config.read(self.__base_path.joinpath("config", "config.ini"))

        return config

    def get_log_path(self, filename):
        """
        Gets logs directory and join filename with it and return the log file path.
        Args:
            filename (string): Filename sent by the Logger class.
        Returns:
            string: log_file_path.
        """
        log_dir = self.__base_path.joinpath("logs")
        log_file_path = log_dir.joinpath(filename)

        return log_file_path
