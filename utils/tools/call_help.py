# -*- coding: utf-8 -*-

import sys

import config as conf


def baseHelp(exit_code=0, is_exit=True):
    print('python manager.py [OPTION]')
    print('--OPTION as [train|predict|result|history]')
    if is_exit:
        sys.exit(exit_code)


def trainHelp(exit_code=0):
    baseHelp(exit_code, is_exit=False)
    print('option train [OPTION]')
    print("-t train type [simple|conv|multi|rnn] define \"rnn\"")
    print('-c load train config file at dir("%s") or all' % conf.TYPE_CONF_DIR)
    print("-n train times")
    print("-m cache train data to memory")
    print("-s save train sess tensor to dir(\"%s\")" % conf.MODEL_SAVE_PATH)
    sys.exit(exit_code)


def predictHelp(exit_code=0):
    baseHelp(exit_code, is_exit=False)
    print('option predict [OPTION]')
    print('-c load train config file at dir("%s") or all' % conf.TYPE_CONF_DIR)
    sys.exit(exit_code)


def resultHelp(exit_code=0):
    baseHelp(exit_code, is_exit=False)
    print('option result [OPTION]')
    # print('-c load train info at dir("%s") or all' % conf.MODEL_SAVE_PATH)
    print("-a filter accuracy value, default value 0.3")
    print("-p filter possibility value from a stock, default 60, between(0, 100)")
    print("-s save filter result file name about quality stock")
    sys.exit(exit_code)


def historyHelp(exit_code=0):
    baseHelp(exit_code, is_exit=False)
    print('option history [OPTION]')
    print('-l load stock codes as "601348,000345" or all')
    sys.exit(exit_code)
