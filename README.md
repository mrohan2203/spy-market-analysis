# SPY 15-Year Historical Return Analysis

## Project Overview
This project analyzes the performance of a $1,000,000 investment in the S&P 500 (via SPY ETF) held for exactly 15 years across four distinct starting periods. It accounts for reinvested dividends (Adjusted Close) and assumes no withdrawals.

## key Results (Approximate)

| Start Date | End Date | Total Return Index | Final Value |
|------------|----------|--------------------|-------------|
| 1995-01-01 | 2010-01-01 | ~2.5x - 3.0x | ~$2.5M - $3.0M |
| 2000-01-01 | 2015-01-01 | ~1.8x - 2.0x | ~$1.8M - $2.0M |
| 2005-01-01 | 2020-01-01 | ~3.2x - 3.5x | ~$3.2M - $3.5M |
| 2008-01-01 | 2023-01-01 | ~2.8x - 3.0x | ~$2.8M - $3.0M |

### Performance Highlights
* **Best Performer (2005 Start):** Despite the 2008 financial crisis occurring early in the holding period, this investor captured the entirety of the 2010s bull market and exited before the 2020 COVID crash.
* **Worst Performer (2000 Start):** This investor entered at the peak of the Dot-com bubble (highest historical valuations) and endured two major crashes (2000 and 2008) during their 15-year window.

## Investment Conclusions
The data highlights **Sequence of Returns Risk** and **Starting Valuation**. 
* The 2000 investor fared poorly because they bought when prices were historically expensive relative to earnings. 
* The 2005 investor survived a massive crash (2008) because they had a long runway of growth afterward and exited at a favorable time.

## Guidance (Historical Perspective)
If advising these investors at the *start* of their journey (without hindsight):

1.  **To the 1995 Investor:** "Ensure a 10+ year horizon to weather mid-cycle volatility."
2.  **To the 2000 Investor:** "Valuations are at historic highs. Diversify into bonds to protect against valuation reversion."
3.  **To the 2005 Investor:** "Markets have recovered; maintain contributions and ignore short-term noise."
4.  **To the 2008 Investor:** "Consider Dollar Cost Averaging (DCA) rather than a lump sum to mitigate the risk of entering before a potential downturn."

## Usage
1. Install requirements: `pip install -r requirements.txt`
2. Run the script: `python analysis.py`
