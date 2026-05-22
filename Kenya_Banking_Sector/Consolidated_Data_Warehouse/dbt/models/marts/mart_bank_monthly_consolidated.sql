/*
dbt mart model for consolidated banking sector analysis

Aggregates financial metrics across all 38+ licensed banks for
sector-wide analysis, peer comparison, and regulatory reporting.

Grain: One row per bank per month
*/

with bank_monthly_data as (
    select
        date_trunc('month', as_of_date)::date as month_end_date,
        bank_code,
        bank_name,
        banking_group,
        
        -- Balance sheet aggregates
        sum(total_assets) as total_assets,
        sum(total_liabilities) as total_liabilities,
        sum(shareholders_equity) as shareholders_equity,
        
        -- Asset quality
        sum(loan_portfolio_gross) as loan_portfolio_gross,
        sum(npl_amount) as npl_amount,
        (
            case
                when sum(loan_portfolio_gross) > 0
                then sum(npl_amount) / sum(loan_portfolio_gross) * 100
                else 0
            end
        ) as npl_ratio,
        
        sum(loan_loss_provisions) as loan_loss_provisions,
        
        -- Income statement
        sum(interest_income) as interest_income,
        sum(interest_expense) as interest_expense,
        sum(net_interest_income) as net_interest_income,
        sum(non_interest_income) as non_interest_income,
        sum(operating_expenses) as operating_expenses,
        sum(net_profit_before_tax) as net_profit_before_tax,
        sum(net_profit_after_tax) as net_profit_after_tax,
        
        -- Deposits and funding
        sum(total_deposits) as total_deposits,
        sum(customer_deposits) as customer_deposits,
        sum(interbank_funding) as interbank_funding,
        
        -- Capital
        sum(core_capital) as core_capital,
        sum(supplementary_capital) as supplementary_capital,
        
        -- Risk metrics
        max(capital_adequacy_ratio) as capital_adequacy_ratio,
        max(liquidity_coverage_ratio) as liquidity_coverage_ratio,
        max(net_stable_funding_ratio) as net_stable_funding_ratio,
        
        -- Customer metrics
        sum(active_customers) as active_customers,
        sum(active_borrowers) as active_borrowers
        
    from {{ ref('stg_bank_supervisory_data') }}
    
    group by
        date_trunc('month', as_of_date)::date,
        bank_code,
        bank_name,
        banking_group
)

select
    month_end_date,
    bank_code,
    bank_name,
    banking_group,
    
    -- Balance sheet (in millions KES)
    round(total_assets / 1000000, 2) as total_assets_millions,
    round(total_liabilities / 1000000, 2) as total_liabilities_millions,
    round(shareholders_equity / 1000000, 2) as equity_millions,
    
    -- Asset quality
    round(loan_portfolio_gross / 1000000, 2) as loan_portfolio_millions,
    round(npl_amount / 1000000, 2) as npl_millions,
    round(npl_ratio, 2) as npl_ratio_percent,
    round(loan_loss_provisions / 1000000, 2) as provisions_millions,
    round(
        case
            when npl_amount > 0 then loan_loss_provisions / npl_amount * 100
            else 0
        end,
        2
    ) as provision_coverage_ratio_percent,
    
    -- Income
    round(net_interest_income / 1000000, 2) as net_interest_income_millions,
    round(non_interest_income / 1000000, 2) as non_interest_income_millions,
    round(operating_expenses / 1000000, 2) as operating_expenses_millions,
    round(net_profit_after_tax / 1000000, 2) as net_profit_millions,
    
    -- Profitability ratios
    round(
        case
            when shareholders_equity > 0
            then net_profit_after_tax / shareholders_equity * 100
            else 0
        end,
        2
    ) as roe_percent,
    
    round(
        case
            when total_assets > 0
            then net_profit_after_tax / total_assets * 100
            else 0
        end,
        2
    ) as roa_percent,
    
    -- Efficiency
    round(
        case
            when (net_interest_income + non_interest_income) > 0
            then operating_expenses / (net_interest_income + non_interest_income) * 100
            else 0
        end,
        2
    ) as cost_to_income_ratio_percent,
    
    -- Funding
    round(total_deposits / 1000000, 2) as deposits_millions,
    round(
        case
            when total_assets > 0 then total_deposits / total_assets * 100
            else 0
        end,
        2
    ) as deposit_ratio_percent,
    
    -- Capital adequacy
    round(capital_adequacy_ratio, 2) as car_percent,
    round(
        case
            when total_assets > 0 then core_capital / total_assets * 100
            else 0
        end,
        2
    ) as tier1_ratio_percent,
    
    -- Liquidity
    round(liquidity_coverage_ratio, 2) as lcr_percent,
    round(net_stable_funding_ratio, 2) as nsfr_percent,
    
    -- Customer metrics
    active_customers,
    active_borrowers,
    
    -- Metadata
    current_timestamp as created_at
    
from bank_monthly_data

order by
    month_end_date desc,
    total_assets desc
