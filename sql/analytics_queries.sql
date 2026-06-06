-- Superstore analytics queries 

-- Total sales and profit
SELECT
    ROUND(SUM(sales)::numeric, 2) AS total_sales,
    ROUND(SUM(profit)::numeric, 2) AS total_profit
FROM superstore_orders;


-- Top 10 states by revenue
SELECT
    state,
    ROUND(SUM(sales)::numeric, 2) AS revenue
FROM superstore_orders
GROUP BY state
ORDER BY revenue DESC
LIMIT 10;


-- Most profitable categories
SELECT
    category,
    ROUND(SUM(profit)::numeric, 2) AS profit
FROM superstore_orders
GROUP BY category
ORDER BY profit DESC;


-- Shipping performance
SELECT
    ship_mode,
    ROUND(AVG(delivery_days)::numeric, 2) AS avg_delivery_days
FROM superstore_orders
GROUP BY ship_mode
ORDER BY avg_delivery_days;



-- Ecommerce Analytics 
-- Funnel event counts
SELECT
    event_type,
    COUNT(*) AS total_events
FROM ecommerce_events
GROUP BY event_type
ORDER BY total_events DESC;


-- Top brands by interactions
SELECT
    brand,
    COUNT(*) AS interactions
FROM ecommerce_events
WHERE brand IS NOT NULL
GROUP BY brand
ORDER BY interactions DESC
LIMIT 10;



-- Azure Operations Analytics
-- Failure counts
SELECT
    failure,
    COUNT(*) AS total_failures
FROM failures
GROUP BY failure
ORDER BY total_failures DESC;


-- Machine telemetry metrics
SELECT
    machineid,
    ROUND(avg_vibration::numeric, 2) AS avg_vibration,
    ROUND(avg_pressure::numeric, 2) AS avg_pressure
FROM telemetry
ORDER BY avg_vibration DESC;

-- Machine risk metrics
SELECT
    machineid,
    ROUND(avg_vibration::numeric, 2) AS avg_vibration,
    ROUND(avg_pressure::numeric, 2) AS avg_pressure,
    ROUND(risk_score::numeric, 2) AS risk_score
FROM machine_features
ORDER BY risk_score DESC;