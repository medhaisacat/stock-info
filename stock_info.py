# Instantiation
import sys
from pprint import pprint
import json
from nsetools import Nse
nse = Nse()

# Get top gainers
def get_gainers():
    pprint("Generating gainers...")
    gainers = []
    nse_gainers = nse.get_top_gainers()

    for nse_gainer in nse_gainers:
        gainer = {}
        gainer['Symbol'] = nse_gainer['symbol']
        gainer['LTP'] = nse_gainer['symbol']
        gainer['% change'] = nse_gainer['netPrice']
        gainer['Traded Qty'] = nse_gainer['tradedQuantity']
        gainer['Value (in Lakhs)'] = nse_gainer['turnoverInLakhs']
        gainer['Open'] = nse_gainer['openPrice']
        gainer['High'] = nse_gainer['highPrice']
        gainer['Low'] = nse_gainer['lowPrice']
        gainer['Prev. Close'] = nse_gainer['previousPrice']
        gainer['Latest Ex Date'] = nse_gainer['lastCorpAnnouncementDate']
        gainers.append(gainer)

    # Write gainers to JSON file
    with open('./gainers.json', 'w') as outfile:
        json.dump(gainers, outfile)
    
    pprint("Done")

    return gainers

# Get top losers
def get_losers():
    pprint("Generating losers...")
    losers = []
    nse_losers = nse.get_top_losers()

    for nse_loser in nse_losers:
        loser = {}
        loser['Symbol'] = nse_loser['symbol']
        loser['LTP'] = nse_loser['symbol']
        loser['% change'] = nse_loser['netPrice']
        loser['Traded Qty'] = nse_loser['tradedQuantity']
        loser['Value (in Lakhs)'] = nse_loser['turnoverInLakhs']
        loser['Open'] = nse_loser['openPrice']
        loser['High'] = nse_loser['highPrice']
        loser['Low'] = nse_loser['lowPrice']
        loser['Prev. Close'] = nse_loser['previousPrice']
        loser['Latest Ex Date'] = nse_loser['lastCorpAnnouncementDate']
        losers.append(loser)

    # Write losers to JSON file
    with open('./losers.json', 'w') as outfile:
        json.dump(losers, outfile)
    
    pprint("Done")
    
    return losers

# Check command line parameters 
match sys.argv[1]:
    case 'g':
        get_gainers()
    case 'l':
        get_losers()