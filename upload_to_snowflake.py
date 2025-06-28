print("🧪 File is executing...")
import pandas as pd
import snowflake.connector
from config import (
    SNOWFLAKE_USER,
    SNOWFLAKE_PASSWORD,
    SNOWFLAKE_ACCOUNT,
    SNOWFLAKE_WAREHOUSE,
    SNOWFLAKE_DATABASE,
    SNOWFLAKE_SCHEMA,
    SNOWFLAKE_TABLE
)

print("🚀 Script started: uploading to Snowflake...")

try:
    df = pd.read_csv("youtube_stats.csv")
    print("📄 Loaded CSV with", len(df), "rows")
except Exception as e:
    print("❌ Failed to load CSV:", e)

try:
    conn = snowflake.connector.connect(
        
    user='pandeyyash12',
    password='Yashrajpandey12',
    account='zq00431.ap-southeast-1',
    warehouse='COMPUTE_WH',
    database='YOUTUBE_DB',
    schema='PUBLIC'
    
    )
    cs = conn.cursor()
    print("🔗 Connected to Snowflake")
except Exception as e:
    print("❌ Snowflake connection failed:", e)

try:
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {SNOWFLAKE_TABLE} (
        video_id STRING,
        title STRING,
        channel_title STRING,
        published_at STRING,
        views NUMBER,
        likes NUMBER,
        comments NUMBER,
        fetched_at TIMESTAMP
    );
    """
    cs.execute(create_table_sql)
    print("✅ Table checked/created")

    for i, row in df.iterrows():
        insert_sql = f"""
        INSERT INTO {SNOWFLAKE_TABLE} (
            video_id, title, channel_title, published_at,
            views, likes, comments, fetched_at
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cs.execute(insert_sql, tuple(row))
    print("✅ Data uploaded to Snowflake")

except Exception as e:
    print("❌ Failed during table creation or insert:", e)

try:
    cs.close()
    conn.close()
    print("🔒 Snowflake connection closed")
except:
    pass
