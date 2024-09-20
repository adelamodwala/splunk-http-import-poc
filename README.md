# Kick-off
1. Start log generation app:
```
python3 log_generator.py
```

2. Start Splunk locally. This will load the log scraping script `splunk_script.py` into the directory Splunk will look for scripts.
```
docker compose up --build --force-recreate --no-deps
```

3. If script is not enabled in Splunk, follow instructions to add data source as Script
4. Watch the logs pile in :)

