#!/bin/bash
# Auto-commit and push new lessons to GitHub

cd /root/.openclaw/workspace/lesson-hub

# Check for changes
if git diff --quiet && git diff --staged --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Add all changes (lessons, scripts)
git add -A

# Commit with timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
git commit -m "Lesson update: $TIMESTAMP"

# Push to GitHub
echo "Pushing to GitHub..."
git push origin master

echo "✅ Pushed to https://github.com/H-H-E/lesson-hub"
