#!/bin/bash
# Autonomous curriculum development - runs on cron
# Add to crontab: 0 18 * * * /root/.openclaw/workspace/lesson-hub/run_autopilot.sh

cd /root/.openclaw/workspace/lesson-hub

echo "=========================================="
echo "🚀 Starting Autonomous Curriculum Development"
echo "Time: $(date)"
echo "=========================================="

# Run the autopilot
python3 automation/autopilot.py --hours 8

# Check if there were changes
if git diff --quiet; then
    echo "No changes to commit"
else
    echo "Committing changes..."
    git add -A
    git commit -m "Autopilot: Curriculum update $(date)"
    
    # Push
    echo "Pushing to GitHub..."
    gh auth status && git push https://x-access-token:$(gh auth token)@github.com/H-H-E/lesson-hub.git master
fi

echo "=========================================="
echo "✅ Done - $(date)"
echo "=========================================="
