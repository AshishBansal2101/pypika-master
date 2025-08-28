from pypika import Query, Table

# Define a table
customers = Table("customers")

# Build a query
q = Query.from_("customers").select("id").comment("Fetch all customer IDs")
print(q.get_sql())

# Print SQL
# customers = Table("customers").comment("Main table for customers")
# q = Query.from_(customers).select(customers.id)
# print(q.get_sql())

customers = Table("customers").comment("Main customers table")
orders = Table("orders").comment("Order history table")

q = Query.from_(customers).join(orders).on(customers.id==orders.customer_id).select(customers.id, orders.id)
print(q.get_sql())


# Create table comment
q = Query.create_table("users").columns(("id", "INT"), ("name", "VARCHAR(100)")).comment("Create users table if missing")
print(q.get_sql())

q = Query.drop_table("users").comment("Dropping users table for reset")
print(q.get_sql())

q = Query.drop_index("idx_users_name").comment("Removing unused index on name")
print(q.get_sql())

q = Query.drop_database("archive").if_exists().comment("Remove archive DB if it exists")
print(q.get_sql())

users = Table("users")

# Create an index with a comment
q = Query.create_index("idx_users_email") \
    .on(users) \
    .columns("email") \
    .comment("Index for fast lookup by email")
print(q.get_sql())

# Create a unique index with `IF NOT EXISTS` and where clause
q = Query.create_index("idx_active_users_email") \
    .on(users) \
    .columns("email") \
    .unique() \
    .if_not_exists() \
    .where(users.active == True) \
    .comment("Ensure unique emails for active users only")
print(q.get_sql())