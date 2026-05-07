#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌏 Global-Ready Data Cleaning Demo (SaaS Subscription Focus)
Target: US/EU Market
Scenario: Cleaning messy subscription data for a SaaS startup.
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_global_dirty_data(n_rows=100):
    """Generate messy SaaS subscription data"""
    np.random.seed(42)
    dates = [datetime(2026, 1, 1) + timedelta(days=i) for i in range(n_rows)]
    plans = ['Basic', 'Pro', 'Enterprise', 'Trial']
    regions = ['New York', 'London', 'Berlin', 'Tokyo', None] # Simulating missing data
    
    data = {
        'Date': dates,
        'Customer_ID': [f'CUST-{1000+i}' for i in range(n_rows)],
        'Plan': np.random.choice(plans, n_rows),
        'MRR': np.random.choice([9.99, 29.99, 99.99, 0.00], n_rows), # Monthly Recurring Revenue
        'Status': np.random.choice(['Active', 'Churned', 'Paused', None], n_rows), # Missing status
        'Region': np.random.choice(regions, n_rows)
    }
    
    df = pd.DataFrame(data)
    
    # Inject specific "messy" issues common in real world
    df.loc[10, 'MRR'] = -9.99  # Negative revenue (Error)
    df.loc[20, 'MRR'] = 99999.99 # Outlier
    df.loc[30, 'Status'] = 'unknown' # Inconsistent format
    
    return df

def clean_data_global(df):
    """Professional cleaning logic"""
    df_clean = df.copy()
    
    # 1. Handle Missing Values
    df_clean['Region'] = df_clean['Region'].fillna('Unknown')
    df_clean['Status'] = df_clean['Status'].fillna('Active') # Conservative approach
    
    # 2. Handle Outliers & Errors
    # Negative MRR -> 0
    df_clean.loc[df_clean['MRR'] < 0, 'MRR'] = 0
    # Extreme Outlier -> Cap at 99th percentile
    cap = df_clean['MRR'].quantile(0.99)
    df_clean.loc[df_clean['MRR'] > cap, 'MRR'] = cap
    
    # 3. Feature Engineering (The "Value Add")
    df_clean['Annual_Value'] = df_clean['MRR'] * 12
    
    return df_clean

def generate_html_report_global(df_dirty, df_clean, output_path):
    """Generate a clean, professional English HTML report"""
    total_mrr = df_clean['MRR'].sum()
    avg_mrr = df_clean['MRR'].mean()
    top_region = df_clean.groupby('Region')['MRR'].sum().idxmax()
    
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI Data Cleaning Demo - SaaS Metrics</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 40px; background: #f3f4f6; color: #1f2937; line-height: 1.6; }}
        .container {{ max-width: 900px; margin: 0 auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); }}
        h1 {{ color: #111827; font-size: 28px; border-bottom: 2px solid #3b82f6; padding-bottom: 15px; }}
        h2 {{ color: #374151; font-size: 20px; margin-top: 30px; }}
        .metric-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 20px 0; }}
        .metric-card {{ background: #eff6ff; padding: 20px; border-radius: 8px; text-align: center; border: 1px solid #dbeafe; }}
        .metric-value {{ font-size: 28px; font-weight: 700; color: #2563eb; }}
        .metric-label {{ font-size: 14px; color: #6b7280; margin-top: 5px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 14px; }}
        th {{ background: #f9fafb; text-align: left; padding: 12px; color: #374151; font-weight: 600; }}
        td {{ border-bottom: 1px solid #e5e7eb; padding: 12px; color: #4b5563; }}
        .badge {{ padding: 4px 8px; border-radius: 99px; font-size: 12px; font-weight: 600; }}
        .badge-dirty {{ background: #fee2e2; color: #991b1b; }}
        .badge-clean {{ background: #d1fae5; color: #065f46; }}
        .cta {{ margin-top: 40px; padding: 20px; background: #1f2937; color: white; border-radius: 8px; text-align: center; }}
        .cta a {{ color: #60a5fa; text-decoration: none; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Automated Data Cleaning Demo</h1>
        <p><strong>Scenario:</strong> SaaS Subscription Data Cleaning & Enrichment</p>
        <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        
        <h2>1. Key Metrics (Post-Cleaning)</h2>
        <div class="metric-grid">
            <div class="metric-card">
                <div class="metric-value">${total_mrr:,.2f}</div>
                <div class="metric-label">Total MRR</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">${avg_mrr:.2f}</div>
                <div class="metric-label">Avg MRR / User</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{top_region}</div>
                <div class="metric-label">Top Region</div>
            </div>
        </div>

        <h2>2. Transformation Logic</h2>
        <table>
            <tr><th>Issue Type</th><th>Before</th><th>After</th><th>Action Taken</th></tr>
            <tr>
                <td>Missing Values</td>
                <td><span class="badge badge-dirty">Nulls in 'Region'</span></td>
                <td><span class="badge badge-clean">Filled: 'Unknown'</span></td>
                <td>Imputation</td>
            </tr>
            <tr>
                <td>Data Errors</td>
                <td><span class="badge badge-dirty">Negative MRR</span></td>
                <td><span class="badge badge-clean">Corrected to $0</span></td>
                <td>Logic Check</td>
            </tr>
            <tr>
                <td>Outliers</td>
                <td><span class="badge badge-dirty">$99,999.99</span></td>
                <td><span class="badge badge-clean">Capped at 99th %ile</span></td>
                <td>Statistical Cap</td>
            </tr>
        </table>

        <h2>3. Data Preview (First 5 Rows)</h2>
        <table>
            {df_clean.head(5).to_html(index=False, border=0)}
        </table>

        <div class="cta">
            <h3>🚀 Ready to automate your data workflows?</h3>
            <p>I help SaaS founders and e-commerce brands turn messy data into actionable insights.</p>
            <p>Contact: <strong>xiaoyuer@example.com</strong> | <a href="#">View Portfolio</a></p>
        </div>
    </div>
</body>
</html>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    print("🌏 Generating Global Demo (SaaS Focus)...")
    df_dirty = generate_global_dirty_data(100)
    df_clean = clean_data_global(df_dirty)
    
    output_dir = os.path.expanduser("~/.openclaw/workspace/projects/data-cleaning-visualization/demo_output")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "saas_cleaning_demo.html")
    
    generate_html_report_global(df_dirty, df_clean, output_file)
    print(f"✅ Global Demo Generated: {output_file}")

if __name__ == "__main__":
    main()