import yfinance as yf
import pandas as pd

def run_analysis():
    # Configuration
    initial_investment = 1_000_000
    scenarios = [
        ("1995-01-01", "2010-01-01"),
        ("2000-01-01", "2015-01-01"),
        ("2005-01-01", "2020-01-01"),
        ("2008-01-01", "2023-01-01")
    ]

    print(f"{'Start Date':<12} | {'End Date':<12} | {'Total Return Index':<20} | {'Final Value ($)':<20}")
    print("-" * 75)

    results = []

    for start_date, end_date in scenarios:
        # Fetch data with a buffer to ensure we capture trading days around Jan 1
        data = yf.download("SPY", start=pd.Timestamp(start_date) - pd.Timedelta(days=5), 
                           end=pd.Timestamp(end_date) + pd.Timedelta(days=5), progress=False)
        
        if data.empty:
            print(f"No data found for {start_date}")
            continue

        try:
            # Find closest trading days
            start_idx = data.index.searchsorted(pd.Timestamp(start_date))
            end_idx = data.index.searchsorted(pd.Timestamp(end_date))
            
            # Boundary checks
            if start_idx >= len(data): start_idx = len(data) - 1
            if end_idx >= len(data): end_idx = len(data) - 1
                
            # Use Adjusted Close to account for dividends/splits
            start_price = float(data.iloc[start_idx]['Adj Close'])
            end_price = float(data.iloc[end_idx]['Adj Close'])
            
            # Calculate metrics
            total_return_index = end_price / start_price
            final_value = initial_investment * total_return_index
            
            results.append({
                "Start": start_date,
                "Value": final_value
            })
            
            print(f"{start_date:<12} | {end_date:<12} | {total_return_index:<20.4f} | ${final_value:,.2f}")
            
        except Exception as e:
            print(f"Error processing {start_date}: {e}")

    # Identify Best and Worst
    if results:
        best = max(results, key=lambda x: x['Value'])
        worst = min(results, key=lambda x: x['Value'])
        print("\n--- PERFORMANCE SUMMARY ---")
        print(f"BEST PERFORMER:  Start: {best['Start']} | Final Value: ${best['Value']:,.2f}")
        print(f"WORST PERFORMER: Start: {worst['Start']} | Final Value: ${worst['Value']:,.2f}")

if __name__ == "__main__":
    run_analysis()
