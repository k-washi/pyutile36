# coding:utf-8

"""
設定パラメータをConfigerクラスにまとめる

loggingの設定
 - 'PYTHON_LOG_LEVEL' に DEBUG, INFO, ERRORなどを設定
"""

import os
import logging
import logging.handlers

###############
# loggingの設定 #
###############

_LOG_LEVEL_ENV = 'PYTHON_LOG_LEVEL'
_LOG_FORMAT = '%(asctime)s | %(levelname)-8s | %(filename)-12s - %(funcName)-12s : %(lineno)-4s | %(message)s'
_LOG_FORMAT = logging.Formatter(_LOG_FORMAT)

_sh = logging.StreamHandler()
_sh.setFormatter(_LOG_FORMAT)
logging.getLogger().addHandler(_sh)

_LOG_LEVEL = os.environ.get(_LOG_LEVEL_ENV)
if _LOG_LEVEL == "DEBUG":
    logging.getLogger().setLevel(logging.DEBUG)
elif _LOG_LEVEL == "INFO":
    logging.getLogger().setLevel(logging.INFO)
elif _LOG_LEVEL == "ERROR":
    logging.getLogger().setLevel(logging.ERROR)
else:
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info(f"{_LOG_LEVEL_ENV}が設定されていないのでDEBUGとして設定する")
    _LOG_LEVEL = "DEBUG"


class Configure(object):
    LOG_LEVEL = _LOG_LEVEL


logging.info("環境変数による設定が終了しました")
