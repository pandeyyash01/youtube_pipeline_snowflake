# fetch_youtube_data.py

import requests
import pandas as pd
from datetime import datetime
from config import YOUTUBE_API_KEY

# 🎯 List of YouTube video IDs you want to track
VIDEO_IDS = [
    'dQw4w9WgXcQ',  # Example video ID (Rick Astley)
    # Add more video IDs here
]

def fetch_video_data(video_id):
    url = 'https://www.googleapis.com/youtube/v3/videos'
    params = {
        'part': 'snippet,statistics',
        'id': video_id,
        'key': YOUTUBE_API_KEY
    }

    response = requests.get(url, params=params).json()

    if not response.get('items'):
        print(f"❌ No data found for video ID: {video_id}")
        return None

    item = response['items'][0]
    stats = item['statistics']
    snippet = item['snippet']

    return {
        'video_id': video_id,
        'title': snippet['title'],
        'channel_title': snippet['channelTitle'],
        'published_at': snippet['publishedAt'],
        'views': int(stats.get('viewCount', 0)),
        'likes': int(stats.get('likeCount', 0)),
        'comments': int(stats.get('commentCount', 0)),
        'fetched_at': datetime.utcnow()
    }

def main():
    print("Script started...") 
    results = []

    for vid in VIDEO_IDS:
        data = fetch_video_data(vid)
        if data:
            results.append(data)

    df = pd.DataFrame(results)

    # Save as CSV (for Snowflake upload)
    df.to_csv('youtube_stats.csv', index=False)
    print("✅ YouTube stats saved to youtube_stats.csv")

if __name__ == '__main__':
    main()
