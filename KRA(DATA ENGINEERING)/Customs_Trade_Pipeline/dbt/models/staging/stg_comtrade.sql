with source as (
    select * from {{ source('customs_raw', 'raw_un_comtrade_benchmarks') }}
),
renamed as (
    select
        hs_code::varchar as hs_code, -- Explicit cast to varchar
        commodity,
        origin_country,
        year,
        volume_tons,
        declared_value_m_kes,
        duty_collected_m_kes,
        risk_score
    from source
)
select * from renamed
