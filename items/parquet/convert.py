import duckdb

con = duckdb.connect("my_sales.duckdb")

con.sql("SELECT * FROM sales").show()
