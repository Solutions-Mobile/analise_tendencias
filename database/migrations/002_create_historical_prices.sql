CREATE TABLE historical_prices (
    asset_id UUID NOT NULL,
    date DATE NOT NULL,

    open NUMERIC(18, 6) NOT NULL,
    high NUMERIC(18, 6) NOT NULL,
    low NUMERIC(18, 6) NOT NULL,
    close NUMERIC(18, 6) NOT NULL,
    average NUMERIC(18, 6) NOT NULL,

    trades INTEGER NOT NULL DEFAULT 0,
    quantity BIGINT NOT NULL DEFAULT 0,
    volume NUMERIC(20, 6) NOT NULL DEFAULT 0,

    CONSTRAINT pk_historical_prices
        PRIMARY KEY (asset_id, date),

    CONSTRAINT fk_historical_prices_asset
        FOREIGN KEY (asset_id)
        REFERENCES assets (asset_id)
);
