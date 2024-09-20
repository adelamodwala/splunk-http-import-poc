import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
from datetime import datetime, timedelta
import json

class IntervalHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL and query parameters
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        print(query_params)

        # Check if the path is '/intervals'
        if parsed_url.path == '/intervals':
            # Get 'from' and 'to' parameters
            from_date = query_params.get('from', [''])[0]
            to_date = query_params.get('to', [''])[0]

            # Validate and parse the date strings
            try:
                from_datetime = datetime.fromisoformat(from_date.replace('Z', '+00:00'))
                to_datetime = datetime.fromisoformat(to_date.replace('Z', '+00:00'))
            except ValueError:
                self.send_error(400, "Invalid date format. Please use ISO 8601 format (e.g., '2023-04-15T12:30:45Z')")
                return

            # Ensure 'from' is earlier than 'to'
            if from_datetime >= to_datetime:
                self.send_error(400, "'from' date must be earlier than 'to' date")
                return

            # Generate intervals
            intervals = []
            current = to_datetime
            while current > from_datetime:
                intervals.append(current.isoformat() + 'Z')
                current -= timedelta(seconds=5)

            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(intervals).encode())
        else:
            self.send_error(404, "Not Found")

# Set up and run the server
PORT = 8080
with socketserver.TCPServer(("", PORT), IntervalHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()