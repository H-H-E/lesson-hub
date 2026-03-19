# Curriculum Autopilot - GitHub Actions

This workflow runs the autonomous curriculum development.

## Option 1: Manual Run

Go to GitHub > Actions > Run Workflow

## Option 2: Scheduled (GitHub)

Enable in GitHub settings:
1. Repository Settings > Actions > General
2. Allow "Read and Write" permissions
3. Then workflow will run on schedule

## Schedule

Daily at 6 PM:
```yaml
on:
  schedule:
    - cron: '0 18 * * *'
```

## Manual Trigger

```bash
gh workflow run autopilot.yml -f hours=8
```

## Current Workflow File

See `.github/workflows/autopilot.yml`

---

## Local Alternative (Currently Running)

The autopilot can also run locally:

```bash
# Run for 8 hours
python3 automation/autopilot.py --hours 8

# Run in background
nohup python3 automation/autopilot.py --hours 8 > autopilot.log &
```

---

## What It Does

Each iteration:
1. Validates existing curriculum
2. Generates new content
3. Improves scaffolding
4. Adds new modules
5. Pushes to GitHub

---

*Setup Instructions*
