import time
import duckdb

# Benchmark CSV read
start = time.perf_counter()
# df = duckdb.read_csv("fact_sales2.csv")
df = duckdb.read_parquet("fact_sales.parquet")
elapsed = time.perf_counter() - start
print(f"read_csv: {elapsed:.4f} seconds")

# Benchmark SQL query
start = time.perf_counter()


query1 = """

create table dim_product (
	product_id integer,
	product_name text,
	product_line text,
	price numeric(10,2)
);

insert into dim_product values
(1, 'Leather Wallet', 'Fashion accessories', 45.99),
(2, 'Bluetooth Earbuds', 'Electronic accessories', 89.50),
(3, 'Vitamin C Serum', 'Health and beauty', 25.75),
(4, 'Organic Green Tea', 'Food and beverages', 15.20),
(5, 'Yoga Mat', 'Sports and travel', 39.99),
(6, 'Wall Clock', 'Home and lifestyle', 29.90),
(7, 'Silk Scarf', 'Fashion accessories', 34.50),
(8, 'Wireless Charger', 'Electronic accessories', 22.00),
(9, 'Herbal Shampoo', 'Health and beauty', 18.45),
(10, 'Gourmet Coffee Beans', 'Food and beverages', 12.95),
(11, 'Hiking Backpack', 'Sports and travel', 65.00),
(12, 'Scented Candles Set', 'Home and lifestyle', 27.50),
(13, 'Sunglasses', 'Fashion accessories', 49.95),
(14, 'Smartwatch', 'Electronic accessories', 129.99),
(15, 'Face Moisturizer', 'Health and beauty', 21.10),
(16, 'Dark Chocolate Box', 'Food and beverages', 9.75),
(17, 'Resistance Bands', 'Sports and travel', 19.99),
(18, 'Ceramic Vase', 'Home and lifestyle', 33.40),
(19, 'Wool Beanie', 'Fashion accessories', 17.60),
(20, 'Power Bank 10000mAh', 'Electronic accessories', 38.80),
(21, 'Charm Bracelet', 'Fashion accessories', 22.75),
(22, 'USB-C Cable', 'Electronic accessories', 9.99),
(23, 'Aloe Vera Gel', 'Health and beauty', 14.30),
(24, 'Sparkling Water', 'Food and beverages', 3.50),
(25, 'Camping Tent', 'Sports and travel', 150.00),
(26, 'Throw Pillow', 'Home and lifestyle', 18.90),
(27, 'Leather Belt', 'Fashion accessories', 40.00),
(28, 'Noise Cancelling Headphones', 'Electronic accessories', 199.99),
(29, 'Lip Balm Set', 'Health and beauty', 12.00),
(30, 'Organic Honey', 'Food and beverages', 11.20),
(31, 'Running Shoes', 'Sports and travel', 75.00),
(32, 'Indoor Plant Pot', 'Home and lifestyle', 25.00),
(33, 'Fashion Sunglasses', 'Fashion accessories', 55.00),
(34, 'Tablet Stand', 'Electronic accessories', 29.99),
(35, 'Facial Cleanser', 'Health and beauty', 19.50),
(36, 'Granola Bars', 'Food and beverages', 6.40),
(37, 'Travel Pillow', 'Sports and travel', 15.00),
(38, 'Decorative Lamp', 'Home and lifestyle', 44.75),
(39, 'Silk Tie', 'Fashion accessories', 30.00),
(40, 'Portable Speaker', 'Electronic accessories', 59.99),
(41, 'Beaded Necklace', 'Fashion accessories', 27.50),
(42, 'Gaming Mouse', 'Electronic accessories', 49.99),
(43, 'Essential Oils Set', 'Health and beauty', 35.00),
(44, 'Protein Powder', 'Food and beverages', 45.25),
(45, 'Mountain Bike Helmet', 'Sports and travel', 85.00),
(46, 'Wooden Picture Frame', 'Home and lifestyle', 22.30),
(47, 'Canvas Tote Bag', 'Fashion accessories', 18.75),
(48, 'Laptop Sleeve', 'Electronic accessories', 24.50),
(49, 'Hand Cream', 'Health and beauty', 9.99),
(50, 'Organic Almonds', 'Food and beverages', 12.80),
(51, 'Fitness Tracker', 'Sports and travel', 79.95),
(52, 'Wall Art Poster', 'Home and lifestyle', 15.60),
(53, 'Stud Earrings', 'Fashion accessories', 16.40),
(54, 'Portable SSD', 'Electronic accessories', 89.99),
(55, 'Bath Bomb Set', 'Health and beauty', 22.00),
(56, 'Herbal Tea Mix', 'Food and beverages', 7.25),
(57, 'Trekking Poles', 'Sports and travel', 55.00),
(58, 'Cozy Blanket', 'Home and lifestyle', 38.50),
(59, 'Wool Socks', 'Fashion accessories', 13.90),
(60, 'Smart Home Hub', 'Electronic accessories', 99.99);


create table dim_branch (
	branch_id integer,
	branch_name text,
	branch_city text,
);

insert into dim_branch values 
	(1, 'Main Branch', 'Yangon'),
	(2, 'Second Branch', 'Naypyitaw'),
	(3, 'Third Branch', 'Mandalay');


create table fact_sales(
	invoice_id text,   
 	branch_id integer,
 	customer_id integer,
 	product_id  integer,
 	quantity integer,
 	date text,
 	time text,
 	payment integer,
 	rating numeric(10,2)
);
COPY fact_sales FROM 'fact_sales2.csv';


select 
	db.branch_city,
	sum( fs.quantity * dp.price) as total
from fact_sales fs
join dim_branch db on fs.branch_id = db.branch_id
join dim_product dp on fs.product_id = dp.product_id
group by db.branch_city;
"""

result = duckdb.sql(query1)
elapsed = time.perf_counter() - start
print(f"SQL query: {elapsed:.4f} seconds")

print(result)
print(len(df))