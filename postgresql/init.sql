CREATE TABLE public.money_control (
    lender VARCHAR (50) NOT NULL,
    borrower VARCHAR (50) NOT NULL,
    amount NUMERIC (5, 2) NOT NULL
);

COPY public.money_control (lender, borrower, amount) FROM '/docker-entrypoint-initdb.d/default_data.csv' CSV HEADER;