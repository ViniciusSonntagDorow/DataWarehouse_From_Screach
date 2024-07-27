with commodities as (
    SELECT
        date,
        closing_data,
        symbol
    FROM
        "postgres123_ahbr"."public"."stg_commodities"
),

movimentacao as (
    SELECT
        movement_date,
        symbol,
        action,
        quantity
    FROM
        "postgres123_ahbr"."public"."stg_movimentacao_commodities"
),

joined as (
    SELECT
        c.date,
        c.symbol,
        c.closing_data,
        m.action,
        m.quantity,
        (m.quantity * c.closing_data) as value,
        CASE
            WHEN m.action = 'sell' then (m.quantity * c.closing_data)
            ELSE -(m.quantity * c.closing_data)
        END as profit
    FROM
        commodities c
    INNER JOIN
        movimentacao m
    ON
        c.date = m.movement_date
        AND
        c.symbol = m.symbol
),

last_day as (
    SELECT max(date) as max_date
    FROM joined
),

filtered as(
    SELECT *
    FROM joined
    WHERE date = (SELECT max_date FROM last_day)
)

SELECT
    date,
    symbol,
    closing_data,
    action,
    value,
    profit
FROM
    filtered