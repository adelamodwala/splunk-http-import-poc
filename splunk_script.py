from datetime import datetime, timedelta
import requests
import json

def get_intervals():
    now = datetime.utcnow()
    from_time = now - timedelta(seconds=10)
    
    params = {
        'from': from_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'to': now.strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    
    try:
        response = requests.get("http://192.168.50.129:8080/intervals", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def output_results(intervals):
    events = []
    for interval in intervals:
        events.append({
            "time": interval,
            "event": "UTC Interval"
        })
    return events

def run_script():
    try:
        intervals = get_intervals()
        events = output_results(intervals)
        print(json.dumps(events))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run_script()