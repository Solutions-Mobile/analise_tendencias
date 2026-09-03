CREATE TABLE assets (
    asset_id UUID NOT NULL,
    asset_type VARCHAR(20) NOT NULL,
    name VARCHAR(120) NOT NULL,
    isin VARCHAR(12),
    symbol VARCHAR(20) NOT NULL,
    valid_from DATE NOT NULL,
    valid_to DATE,

    CONSTRAINT pk_assets
        PRIMARY KEY (asset_id),

    CONSTRAINT uq_assets_symbol
        UNIQUE (symbol),

    CONSTRAINT ck_assets_validity
        CHECK (
            valid_to IS NULL
            OR valid_to >= valid_from
        )
);
