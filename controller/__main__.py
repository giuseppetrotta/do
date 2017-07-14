# -*- coding: utf-8 -*-

"""
    Command line script: main function
"""

import better_exceptions as be
from controller.app import Application
from utilities.logs import get_logger

log = get_logger(__name__)


def main():
    be  # activate better exceptions
    try:
        Application()
    except KeyboardInterrupt:
        log.critical("Interrupted by the user")
    else:
        log.verbose("Application completed")


if __name__ == '__main__':
    main()