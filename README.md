# MyPortfolio
This Repo aims at how I construct my portfolio in Iran Stock Market based on my quantitive analysis.

Every Point that I found is worth sharing i will add it to repo.

-----

## Structure
```bash
MyPortfolio
├── MyData                          # All Data needed for analysis
│   ├── ISM                         # Data for Iran Stock Market (which is empty to decrease repo size)
│   ├── forexFactory                # Data from forex Factory site
│   ├── crypto                      # Crypto data
│   ├── oil                         # oil data
│   ├── read.py                     # read the downloaded data in standard format
│   └── download.py                 # download data needed
│
├── analysis                        # main analysis module
│   ├── indicator                   # module to add indicator based analysis
│   │ ├── indicator                 # module to add indicator based analysis
│   │ ├── indicator_filter.py       # base class for indicator filters
│   │ ├── small_data_filter.py      # filter datas which have small amount of data for analysis
│   │ ├── adx_filter.py             # filter datas based on adx indicator
│   │ ├── ichi_filter.py            # filter datas based on ichi moku cload indicator
│   │ └── sma_filter.py             # filter datas based on multiple smas
│   │
│   ├── pattern                     # module to specify the pattern that found in a time  
│   │ └── pattern.py                # pattern recognization with help of Nonparametric kernel regression
│   │
│   ├── dependence                  # module to specify the relation between a stock and other retruns like indexes or oil price
│   │ └── regression.py             # linear regression 
│   │
│   └── tree                        # module for analysis with tree things
│     └── randomForest.py
│
├── chart                           # module for creating charts
│   ├── pattern.py
│   └── randomForest.py
│
├── scrapers                        # module for scraping sites
│   └── forexFactory.py             # www.forexfactory.com
│
├── strategy                        # My market strategy based on the analysis module
│   └── strategy1                   # A Simple Strategy for iran stock market
│   ├── strategy2                   # A RF strategy

```