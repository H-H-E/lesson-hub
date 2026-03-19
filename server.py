#!/usr/bin/env python3
"""
Lesson Hub - Web Server
Serves student and teacher modes, hosts p5.js/three.js simulations
"""

import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PORT = 8080
BASE_DIR = Path(__file__).parent

class LessonHubHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # API endpoints
        if self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            status = {'automation_status': 'Ready', 'lessons_completed': 0, 'last_run': None}
            status_file = BASE_DIR / 'data' / 'status.json'
            if status_file.exists():
                try:
                    status = json.loads(status_file.read_text())
                except: pass
            
            self.wfile.write(json.dumps(status).encode())
            return
        
        if self.path == '/api/lessons':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            lessons_file = BASE_DIR / 'data' / 'lessons.json'
            if lessons_file.exists():
                data = json.loads(lessons_file.read_text())
            else:
                data = {'lessons': []}
            
            self.wfile.write(json.dumps(data).encode())
            return
        
        if self.path == '/api/lessons/<lesson_id>':
            # Get specific lesson
            lesson_id = self.path.split('/')[-1]
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            lessons_file = BASE_DIR / 'data' / 'lessons.json'
            if lessons_file.exists():
                data = json.loads(lessons_file.read_text())
                lesson = next((l for l in data.get('lessons', []) if l.get('id') == lesson_id), None)
            else:
                lesson = None
            
            self.wfile.write(json.dumps(lesson or {}).encode())
            return
        
        if self.path == '/api/teacher-script/<lesson_id>':
            # Get teacher script for lesson
            lesson_id = self.path.split('/')[-1]
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            script_file = BASE_DIR / 'scripts' / f'lesson_{lesson_id}_teacher.md'
            if script_file.exists():
                script = script_file.read_text()
            else:
                script = "# Script not yet generated\n\nRun overnight automation to generate."
            
            self.wfile.write(json.dumps({'script': script}).encode())
            return
        
        # Serve static files
        return SimpleHTTPRequestHandler.do_GET(self)
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

def run_server():
    # Ensure directories exist
    (BASE_DIR / 'data').mkdir(exist_ok=True)
    (BASE_DIR / 'scripts').mkdir(exist_ok=True)
    (BASE_DIR / 'public' / 'student').mkdir(exist_ok=True)
    (BASE_DIR / 'public' / 'teacher').mkdir(exist_ok=True)
    
    # Create default data files if they don't exist
    status_file = BASE_DIR / 'data' / 'status.json'
    if not status_file.exists():
        status_file.write_text(json.dumps({
            'automation_status': 'Ready',
            'lessons_completed': 0,
            'last_run': None
        }))
    
    lessons_file = BASE_DIR / 'data' / 'lessons.json'
    if not lessons_file.exists():
        lessons_file.write_text(json.dumps({'lessons': []}))
    
    os.chdir(BASE_DIR)
    server = HTTPServer(('', PORT), LessonHubHandler)
    print(f"🎓 Lesson Hub running at http://localhost:{PORT}")
    print(f"   Student Mode:  http://localhost:{PORT}/student/")
    print(f"   Teacher Mode:  http://localhost:{PORT}/teacher/")
    print(f"\nPress Ctrl+C to stop")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped")

if __name__ == '__main__':
    run_server()
