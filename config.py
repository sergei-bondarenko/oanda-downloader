# Output csv file path, can be absolute or relative.
output = 'candles.csv'

# Server hostname:
#   "api-fxpractice.oanda.com" - a demo account.
#   "api-fxtrade.oanda.com" - a live accont.
hostname = 'api-fxpractice.oanda.com'

# Log into your account and go to "My Account" -> "My Services" -> 
# -> "Manage API Access" to get the token.
token = 'xxxxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxx'

# DateTime format which will be returned:
#  "UNIX" - "12345678" format (number of seconds since 1 Jan 1970).
#  "RFC3339" - "YYYY-MM-DDTHH:MM:SS" format.
datetime_format = 'RFC3339'

# A string containing the base currency and quote currency delimited
# by a "_".
instrument = 'EUR_USD'

# The Price component(s) to get candlestick data for. Can contain any
# combination of the characters "M" (midpoint candles), "B" (bid
# candles) and "A" (ask candles).
price = 'AB'

# Candlestick granularity:
#   S5,S10,S15,S30 - 5,10,15,30 second candlesticks, minute alignment.
#   M1,M2,M4,M5,M10,M15,M30 - 1,2,4,5,10,15,30 minute candlesticks,
#     hour alignment.
#   H1,H2,H3,H4,H6,H8,H12 - 1,2,3,4,6,8,12 hour candlesticks,
#     day alignment.
#   D - 1 day candlesticks, day alignment.
#   W - 1 week candlesticks, aligned to start of week.
#   M - 1 month candlesticks, aligned to first day of the month.
granularity = 'M1'

# A flag that controls whether the candlestick is "smoothed" or not.
# A smoothed candlestick uses the previous candle's close price as its
# open price, while an unsmoothed candlestick uses the first price
# from its time range as its open price. 
smooth = True

# The hour of the day (in the specified timezone) to use for
# granularities that have daily alignments. 
daily_alignment = 17

# The timezone to use for the daily_alignment parameter. Candlesticks
# with daily alignment will be aligned to the dailyAlignment hour
# within the alignmentTimezone. Note that the returned times will
# still be represented in UTC.
alignment_timezone = 'America/New_York'

# The day of the week used for granularities that have weekly
# alignment.
weekly_alignment = 'Friday'

# If both from_time and to_time specified, then all candles in this
# time range will be returned.
# In case only from_time or to_time is set then candles from this
# point to the respective end will be returned.
# If both variables are set to None then all candles will be
# downloaded.
# Values can be specified in a UNIX time format or human readable
# (RFC3339), e.g. "1234567890", "2009-01-31", "2019-02-17T20:00:00".
# The variables format does not have to be the same as specified in
# "datetime_format" variable.
from_time = '2019-01-01'
to_time = '2019-02-01'
