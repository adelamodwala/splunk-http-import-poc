# Kick-off
1. Start log generation app:
```
python3 log_generator.py
```
2. Edit `splunk_script.py` to use the correct host
3. Start Splunk locally. This will load the log scraping script `splunk_script.py` into the directory Splunk will look for eligible scripts.
```
docker compose up --build --force-recreate --no-deps
```
4. If script is not enabled in Splunk, follow instructions to add data source as Script
5. Watch the logs pile in :)

