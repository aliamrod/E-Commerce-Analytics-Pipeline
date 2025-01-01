import pandas as pd 
import sqlite3 
# % cd /Users/aliamahama-rodriguez/project_dir

# Load CSV data onto workspace
orders = pd.read_csv("./data/orders.csv")
products = pd.read_csv("./data/products.csv")
customers = pd.read_csv("./data/customers.csv")

# Create SQLite database connection using SQLite3
conn = sqlite3.connect("ecommerce.db")


# Write the data to SQLite database
# Writes 'orders', 'products', and 'customers' DataFrame into SQLite tables. 
# Replaces table if already exists (`if_exists="replace"`).
# Does not include the DataFrame's index as a column in the table.
orders.to_sql("orders", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
customers.to_sql("customers", conn, if_exists="replace", index=False)

# Close connection
conn.close()

# Explorary analysis 
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the SQLite database
conn = sqlite3.connect('ecommerce.db')

# Load the data from SQLite into pandas DataFrames
# Fetch all records (rows) and all columns (*) from the respective tables in the SQLite database: `orders`, `products`, and `customers`.
orders = pd.read_sql('SELECT * FROM orders', conn)
products = pd.read_sql('SELECT * FROM products', conn)
customers = pd.read_sql('SELECT * FROM customers', conn)
conn.close()

# Preview data: inspect data with `.head()` and `.info()`.
#print(orders.head())
#print(products.head())
#print(customers.head())
#print(orders.info())
#print(products.info())
#print(customers.info())

# Clean and preprocess data
orders = orders.dropna()
products = products.dropna()
customers = customers.dropna()

#print(orders.describe())

# Count number of orders per status type
status_counts = orders['order_status'].value_counts()
print("order status counts: ")
print(status_counts)

status_proportions = orders['order_status'].value_counts(normalize=True)
print(status_proportions.values)


# Chi-Square Test
import scipy.stats as stats 
observed_counts = status_counts.values  # Observed frequencies
expected_counts = [len(orders) / len(status_counts)] * len(status_counts)  # Expected frequencies assuming uniform distribution

# Perform the Chi-Square test
chi2_stat, p_value = stats.chisquare(observed_counts, expected_counts)

# Display the test results
print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-value: {p_value}")

# Conclusion based on p-value
if p_value < 0.05:
    conclusion = "There is a significant difference in the distribution of order statuses (Completed, Pending, Cancelled)."
else:
    conclusion = "There is no significant difference in the distribution of order statuses (Completed, Pending, Cancelled)."

print("\nConclusion:")
print(conclusion)

# Add informative data//feature engineering
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders['days_since_order'] = (pd.to_datetime('today') - orders['order_date']).dt.days
orders['order_month'] = orders['order_date'].dt.month
print(orders.head())


## ML: Random Forest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Encoding categorical variables
orders['order_status_encoded'] = orders['order_status'].map({'Completed': 0, 'Pending': 1, 'Cancelled': 2})
orders = pd.get_dummies(orders, columns=['order_duration'], drop_first=True)

# Split data into features (X) and target (y)
X = orders[['days_since_order', 'order_month'] + [col for col in orders.columns if 'order_duration' in col]]
y = orders['order_status_encoded']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
