#!/bin/bash
# Run overnight automation

cd /root/.openclaw/workspace/lesson-hub

echo "Starting Lesson Hub overnight automation..."
echo ""

python3 automation/pipeline.py --topic "p5.js basics" --lessons 5

echo ""
echo "Done! You can now view the results at:"
echo "  http://localhost:8080/teacher/"
