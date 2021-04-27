import os
import logging
from threading import Thread

__version__ = '0.0.3'

try:
    os.environ['OUTDATED_IGNORE'] = '1'
    from outdated import check_outdated  # noqa
except ImportError:
    check_outdated = None


def check():
    try:
        is_outdated, latest = check_outdated('ogb_lite', __version__)
        if is_outdated:
            logging.warning(
                "The OGB package is out of date. Your version is "
                "{}, while the latest version is {}.".format(__version__, latest))
    except Exception:
        pass


if check_outdated is not None:
    thread = Thread(target=check)
    thread.start()
