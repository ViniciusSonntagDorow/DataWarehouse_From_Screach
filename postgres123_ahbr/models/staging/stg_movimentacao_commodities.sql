-- source import

with source as (
    SELECT
        date,
        symbol,
        action,
        quantity
    FROM
        {{ source ('postgres123_ahbr','movimentacao_commodities') }}
),

-- renames/type changes/casts

renamed as (
    SELECT
        CAST(date as date) as movement_date,
        symbol,
        action,
        quantity
    FROM
        source
)

-- select * from

SELECT *
FROM renamed