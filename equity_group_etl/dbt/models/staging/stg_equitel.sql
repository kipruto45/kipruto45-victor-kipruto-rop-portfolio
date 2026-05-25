with source as (
    select * from {{ source('equity_raw', 'raw_equitel_subscribers') }}
),
renamed as (
    select
        period,
        subscribers,
        operator
    from source
)
select * from renamed
