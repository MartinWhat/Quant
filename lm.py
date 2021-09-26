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


#获取市值
df=jq.get_fundamentals(query(valuation.code,valuation.market_cap).filter(valuation.market_cap.between(20,30)).order_by(valuation.market_cap.asc()))
print(df[:10])
