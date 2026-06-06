-- Drop existing tables if needed
DROP TABLE IF EXISTS superstore_orders;
DROP TABLE IF EXISTS ecommerce_events;
DROP TABLE IF EXISTS machines;
DROP TABLE IF EXISTS telemetry;
DROP TABLE IF EXISTS telemetry_features;
DROP TABLE IF EXISTS failures;
DROP TABLE IF EXISTS errors;
DROP TABLE IF EXISTS maintenance;
DROP TABLE IF EXISTS machine_features;

-- Superstore
CREATE TABLE superstore_orders (
    row_id INT,
    order_id TEXT,
    order_date TIMESTAMP,
    ship_date TIMESTAMP,
    ship_mode TEXT,
    customer_id TEXT,
    customer_name TEXT,
    segment TEXT,
    country TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    region TEXT,
    product_id TEXT,
    category TEXT,
    sub_category TEXT,
    product_name TEXT,
    sales NUMERIC,
    quantity INT,
    discount NUMERIC,
    profit NUMERIC,
    delivery_days INT,
    profit_margin NUMERIC
);

-- Ecommerce
CREATE TABLE ecommerce_events (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id BIGINT,
    category_id BIGINT,
    category_code TEXT,
    brand TEXT,
    price NUMERIC,
    user_id BIGINT,
    user_session TEXT
);

-- Azure tables
CREATE TABLE machines (
    machineid INT,
    model TEXT,
    age INT
);

CREATE TABLE telemetry (
    datetime TIMESTAMP,
    machineid INT,
    volt NUMERIC,
    rotate NUMERIC,
    pressure NUMERIC,
    vibration NUMERIC
);

CREATE TABLE telemetry_features (
    machineid INT,
    avg_volt NUMERIC,
    avg_rotate NUMERIC,
    avg_pressure NUMERIC,
    avg_vibration NUMERIC
);

CREATE TABLE failures (
    datetime TIMESTAMP,
    machineid INT,
    failure TEXT
);

CREATE TABLE errors (
    datetime TIMESTAMP,
    machineid INT,
    errorid TEXT
);

CREATE TABLE maintenance (
    datetime TIMESTAMP,
    machineid INT,
    comp TEXT
);

CREATE TABLE machine_features (
    machineid INT,
    avg_volt NUMERIC,
    avg_rotate NUMERIC,
    avg_pressure NUMERIC,
    avg_vibration NUMERIC,
    failure_count NUMERIC,
    maintenance_count NUMERIC,
    risk_score NUMERIC
);