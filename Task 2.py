# -*- coding: utf-8 -*-
# Task 2
def contract_pricing(injection_date: str,
                     withdrawal_date: str,
                     rate,
                     volume,
                     max_vol,
                     storage_cost):
  injection_dt = pd.to_datetime(injection_date, dayfirst=True)
  withdrawal_dt = pd.to_datetime(withdrawal_date, dayfirst=True)
  price_buy = estimate_price(injection_dt)
  price_sell = estimate_price(withdrawal_dt)
  storage_months = (withdrawal_dt.year - injection_dt.year) * 12 + (withdrawal_dt.month - injection_dt.month)

  if volume > max_vol:
    volume = max_vol
  else:
    volume = volume

  cost = volume * rate * 2 + strorage_cost * storage_months

  return net_value = (price_sell - price_buy) * max_vol - cost



