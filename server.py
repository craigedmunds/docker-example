#!/usr/bin/env python3
import http.server
import socketserver
from datetime import datetime

class HelloWorldHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello World Docker Demo</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .timestamp {{ color: #666; font-size: 14px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🐳 Hello World from Docker!</h1>
                <p>This is a simple HTTP server running in an Alpine Linux container.</p>
                <p class="timestamp">Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</p>
                <p>Built and deployed with GitHub Actions! 🚀</p>
            </div>
        </body>
        </html>
        """
        
        self.wfile.write(html_content.encode())

if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), HelloWorldHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()