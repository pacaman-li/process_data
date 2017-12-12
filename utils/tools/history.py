# -*- coding: utf-8 -*-

import os
# import sys
import getopt
import requests
# import yaml
import json

import config as conf
from utils.tools.call_help import historyHelp


def loadHistory(codes=[]):
    print("load history train data", codes)
    pass


def run(argv):
    try:
        opts, args = getopt.getopt(argv, "hl:")
    except getopt.GetoptError as e:
        print(e)
        historyHelp(2)

    for opt, arg in opts:
        if opt == '-h':
            historyHelp()
        elif opt == '-l':
            if arg == 'all':
                loadHistory()
            else:
                codes = arg.split(',')
                loadHistory(codes)

    historyHelp()
