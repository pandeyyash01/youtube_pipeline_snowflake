# 🎥 YouTube Video Stats to Snowflake Pipeline

This project is an **end-to-end data pipeline** that fetches real-time YouTube video statistics using the YouTube Data API and loads the data into a **Snowflake** data warehouse.

---

## 🚀 Tech Stack

- **Python** – scripting and orchestration
- **YouTube Data API v3** – for fetching video metrics
- **Pandas** – data manipulation
- **Snowflake Connector for Python** – data warehouse integration
- **CSV** – intermediate storage format

---

## 📁 Project Structure

youtube_pipeline_snowflake/
├── fetch_youtube_data.py
├── upload_to_snowflake.py
├── config.py
├── youtube_stats.csv
├── requirements.txt
└── README.md

---

## 🧠 What This Pipeline Does

1. Uses the **YouTube Data API** to pull metadata and statistics for a list of video IDs.
2. Extracts relevant fields like:
   - `video_id`, `title`, `channel_title`, `published_at`
   - `views`, `likes`, `comments`, `fetched_at`
3. Stores the results in a local `youtube_stats.csv` file.
4. Uploads the data into a **Snowflake table**, creating the table if it doesn’t exist.

---

## ⚙️ How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/youtube_pipeline_snowflake.git
cd youtube_pipeline_snowflake ---


## ****Install Required Packages****
pip install -r requirements.txt


**Create a config.py File**

YOUTUBE_API_KEY = "AIzaSyCI0jYWzs1JPQI6nbBVLqax5Na0HIbz3Ek"

SNOWFLAKE_USER = 'pandeyyash12'
SNOWFLAKE_PASSWORD = 'Yashrajpandey12'
SNOWFLAKE_ACCOUNT = 'xbwxvwh.ix28643'   # from your Snowflake URL
SNOWFLAKE_WAREHOUSE = 'COMPUTE_WH'
SNOWFLAKE_DATABASE = 'YOUTUBE_DB'
SNOWFLAKE_SCHEMA = 'PUBLIC'
SNOWFLAKE_TABLE = 'YOUTUBE_VIDEO_STATS'

**Run the Scripts**
python fetch_youtube_data.py
python upload_to_snowflake.py

**Use Cases**
- Monitor video performance metrics (views, likes, comments)
- Historical tracking of YouTube video stats
- Learn to integrate APIs with cloud data warehouses
- Hands-on experience for Data Engineering interviews

**🙌 Author**
Yashraj Pandey
Aspiring Data Engineer | Python, SQL, Snowflake
📧 pandeyyash042000@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/yashraj-pandey/

**🛡️ Disclaimer**
- This project is for learning and portfolio use only.
- Never expose API keys or credentials publicly.
- Use .gitignore to exclude sensitive files like config.py from GitHub
