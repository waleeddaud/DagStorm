from sqlalchemy import create_engine
SUPABASE_URI = "postgresql://postgres:7BMQuyzeMqsmiT9o@vkowbwjkhnsixksljrji.supabase.co:5432/postgres"

engine = create_engine(SUPABASE_URI)

try:
    with engine.connect() as conn:
        print("Connection successful")
except Exception as e:
    print(f"Error: {e}")
