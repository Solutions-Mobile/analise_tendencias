\set ON_ERROR_STOP on

BEGIN;

CREATE TEMP TABLE assets_import (
    asset_id   uuid,
    asset_type varchar(30),
    name       varchar(200),
    isin       varchar(20),
    symbol     varchar(20),
    valid_from date,
    valid_to   date
);

\copy assets_import (asset_id, asset_type, name, isin, symbol, valid_from, valid_to) FROM 'core/reference/assets.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', QUOTE '"', ENCODING 'UTF8');

INSERT INTO assets (
    asset_id,
    asset_type,
    name,
    isin,
    symbol,
    valid_from,
    valid_to
)
SELECT
    asset_id,
    asset_type,
    name,
    isin,
    symbol,
    valid_from,
    valid_to
FROM assets_import
ON CONFLICT (asset_id) DO UPDATE
SET
    asset_type = EXCLUDED.asset_type,
    name       = EXCLUDED.name,
    isin       = EXCLUDED.isin,
    symbol     = EXCLUDED.symbol,
    valid_from = EXCLUDED.valid_from,
    valid_to   = EXCLUDED.valid_to;

COMMIT;
