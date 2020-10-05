#!/usr/bin/env python3

import os
import time
import logging
from common.server import Server


def parse_config_params():
    """ Parse env variables to find program config params

    Function that search and parse program configuration parameters in the
    program environment variables. If at least one of the config parameters
    is not found a KeyError exception is thrown. If a parameter could not
    be parsed, a ValueError is thrown. If parsing succeeded, the function
    returns a map with the env variables
    """
    print("reading cfg from env...")
    config_params = {}
    try:
        config_params["port"] = int(os.environ["SERVER_PORT"])
        config_params["listen_backlog"] = int(os.environ["SERVER_LISTEN_BACKLOG"])
    except KeyError as e:
        raise KeyError("Key was not found. Error: {} .Aborting server".format(e))
    except ValueError as e:
        raise ValueError("Key could not be parsed. Error: {}. Aborting server".format(e))

    return config_params


def parse_config_params_from_file():
    print("reading cfg from file...")
    read_params = {}
    config_params = {}
    f = open("/var/cfg/server.cfg", "r")
    while line := f.readline():
        line = line.split('=')
        read_params[line[0]] = line[1]
    f.close()

    config_params["port"] = int(read_params["SERVER_PORT"])
    config_params["listen_backlog"] = int(read_params["SERVER_LISTEN_BACKLOG"])
    return config_params



def main():
    initialize_log()
    try:
        config_params = parse_config_params_from_file()
    except:
        config_params = parse_config_params()

    # Initialize server and start server loop
    server = Server(config_params["port"], config_params["listen_backlog"])
    server.run()


def initialize_log():
    """
    Python custom logging initialization

    Current timestamp is added to be able to identify in docker
    compose logs the date when the log has arrived
    """
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
    )


if __name__ == "__main__":
    main()
