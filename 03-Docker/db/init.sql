CREATE TABLE users (
    id    SERIAL PRIMARY KEY,
    name  TEXT NOT NULL,
    email TEXT
);

CREATE TABLE products (
    id    SERIAL PRIMARY KEY,
    name  TEXT NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

CREATE TABLE orders (
    id         SERIAL PRIMARY KEY,
    user_id    INT,
    total      NUMERIC(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE order_items (
    id         SERIAL PRIMARY KEY,
    order_id   INT NOT NULL REFERENCES orders(id),
    product_id INT NOT NULL REFERENCES products(id),
    qty        INT NOT NULL
);

CREATE TABLE order_audit (
    id          SERIAL PRIMARY KEY,
    order_id    INT NOT NULL,
    payload     JSONB,
    received_at TIMESTAMP DEFAULT now()
);

INSERT INTO users (name, email) VALUES
    ('Ana Torres',   'ana@example.com'),
    ('Luis Pérez',   'luis@example.com'),
    ('Marta Ruiz',   'marta@example.com'),
    ('Luis P.',      'luis@example.com'),
    ('Sin Correo',   NULL),
    ('Carlos Vega',  'carlos@example.com');

INSERT INTO products (name, price) VALUES
    ('Teclado', 50.00),
    ('Mouse',   20.00),
    ('Monitor', 200.00),
    ('Cable',   5.00);

INSERT INTO orders (user_id, total) VALUES
    (1, 70.00),
    (1, 200.00),
    (2, 45.00),
    (3, 10.00),
    (99, 50.00),
    (4, 0.00),
    (2, 100.00);

INSERT INTO order_items (order_id, product_id, qty) VALUES
    (1, 1, 1), (1, 2, 1),
    (2, 3, 1),
    (3, 2, 1), (3, 4, 1),
    (4, 4, 2),
    (5, 1, 1),
    (7, 2, 5);
