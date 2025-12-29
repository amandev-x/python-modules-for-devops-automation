import os 

# Get environment variable
db_host = os.getenv('DB_HOST', 'localhost') # Default to 'localhost' if not set
db_port = os.getenv('DB_PORT', '5432')      # Default to '5432' if not set
api_key = os.environ.get('API_KEY')         # Will return None if not set

print(f"Database Host: {db_host}")
print(f"Database Port: {db_port}")
print(f"API Key: {api_key}")

# Set environment variable
os.environ['ENV'] = "production"
print(f"Environment: {os.environ['ENV']}")

# List all environment variables
for key, value in os.environ.items():
    print(f"{key}: {value}")