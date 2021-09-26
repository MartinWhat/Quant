#-*- coding:utf-8 -*-
import jqdatasdk as jq
from jqdatasdk import *
from datetime import datetime, timedelta
import pandas as pd
import time
import numpy
import math
import requests



# aa 为你自己的帐号， bb 为你自己的密码
auth('17606619309','619309')
api = "https://sctapi.ftqq.com/SCT42234TWKI7KpDbOsx9xCQrzLeBVkSx.send"


def xuangu(context):
    q = jq.query(
            jq.valuation.code,
            jq.valuation.market_cap
        ).filter(
            jq.valuation.market_cap.between(20,30)
        ).order_by(
    jq.valuation.market_cap.asc()
    )
    giao = jq.run_query(q)
    print(giao)
    buylist = list(giao['code'])
    return buylist

'''
df=get_fundamentals(query(valuation))
print(df[:4])
'''