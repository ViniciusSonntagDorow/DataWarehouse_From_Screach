-- source import

with source as (
    SELECT
        "Date",
        "Close",
        "Symbol"
    FROM
        "postgres123_ahbr"."public"."commodities"
),

-- renames/type changes/casts

renamed as (
    SELECT
        CAST("Date" as date) as date,
        "Close" as closing_data,
        "Symbol" as symbol
    FROM
        source
)

-- select * from

SELECT *
FROM renamed