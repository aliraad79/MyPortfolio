# MyPortfolio
This Repo aims at how I construct my portfolio in Iran Stock Market based on my quantitive analysis.

Every Point that I found is worth sharing i will add it to repo.

-----

## Structure
```bash
MyPortfolio
├── MyData                          # All Data needed for analysis
│   ├── ISM                         # Data for Iran Stock Market (which is empty to decrease repo size)
│   └── download.py                 # download data needed
├── analysis                        # main analysis module
│   ├── indicator                   # module to add indicator based analysis
│   │ ├── indicator                 # module to add indicator based analysis
│   │ ├── indicator_filter.py       # base class for indicator filters
│   │ ├── small_data_filter.py      # filter datas which have small amount of data for analysis
│   │ ├── adx_filter.py             # filter datas based on adx indicator
│   │ ├── ichi_filter.py            # filter datas based on ichi moku cload indicator
│   │ └── sma_filter.py             # filter datas based on multiple smas
│   └── pattern                     # module to specify the pattern that found in a time  
│     └── pattern.py                # pattern recognization with help of Nonparametric kernel regression
├── chart                           # module for creating charts
│   ├── pattern.py                  # chart the pattern
│   ├── indicator_filter.py         # base class for indicator filters
│   ├── small_data_filter.py        # filter datas which have small amount of data for analysis
│   ├── adx_filter.py               # filter datas based on adx indicator
│   ├── ichi_filter.py              # filter datas based on ichi moku cload indicator
│   └── sma_filter.py               # filter datas based on multiple smas
├── scrapers                        # module for scraping sites
│   ├── forexFactory.py             # www.forexfactory.com

```