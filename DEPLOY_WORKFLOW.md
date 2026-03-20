# Vercel Deployment Pipeline WORKFLOW

tracker:
  kind: local
  queue_file: data/deploy_queue.json

polling:
  interval_ms: 5000
  max_concurrent_agents: 5

workspace:
  root: workspace

agent:
  command: python3 automation/deploy_agent.py
  max_concurrent_agents: 5
  max_retry_backoff_ms: 120000

---

# DEPLOYMENT PIPELINE - Agent System

This pipeline generates and deploys the lesson-hub website to Vercel using multiple specialized agents.

## PHASE 1: ANALYZE (3 Agents)

### Agent 1.1: StructureAnalyzer
Analyze current repo structure and identify what's needed for deployment.
- Check index.html exists
- Check docs/ structure
- Check public/ folders
- Identify missing files
- Output: {structure{}, missing[], recommendations[]}

### Agent 1.2: DependencyChecker
Check what's needed for Vercel deployment.
- Node.js requirements
- Static file serving
- Routing needs
- Output: {dependencies[], node_version, build_needed}

### Agent 1.3: ConfigGenerator
Generate necessary Vercel config files.
- vercel.json
- package.json
- _redirects or rewrites
- Output: {files_generated[], config{}}

## PHASE 2: BUILD (5 Agents)

### Agent 2.1: IndexPageBuilder
Build main landing page (index.html).
- Hero section
- Navigation
- Featured lessons
- Call to action
- Output: {file: "index.html", size}

### Agent 2.2: DashboardBuilder
Build pipeline dashboard.
- Real-time status
- Agent progress
- Score displays
- Output: {file: "dashboard.html"}

### Agent 2.3: DocsOrganizer
Organize lesson docs for web.
- Generate doc index
- Create navigation
- Add search functionality
- Output: {index_file, categories[]}

### Agent 2.4: PublicAssetsBuilder
Build public/ directories.
- student view
- teacher view
- static assets
- Output: {files[], structure}

### Agent 2.5: APIBuilder
Build simple API for lessons.
- JSON endpoints
- Search functionality
- Filtering
- Output: {endpoints[], api_files[]}

## PHASE 3: CONFIGURE (3 Agents)

### Agent 3.1: VercelConfigWriter
Write vercel.json.
- Build command
- Output directory
- Routing rules
- Output: {valid, config{}}

### Agent 3.2: PackageConfigWriter
Write package.json.
- Dependencies
- Scripts
- Engines
- Output: {valid, package{}}

### Agent 3.3: EnvConfigWriter
Write environment configs.
- .env.example
- Configuration
- Output: {env_vars[]}

## PHASE 4: DEPLOY (2 Agents)

### Agent 4.1: GitCommitter
Commit all changes.
- Stage files
- Commit with message
- Tag version
- Output: {commit_hash, files_committed[]}

### Agent 4.2: VercelDeployer
Deploy to Vercel.
- Link to Vercel
- Deploy command
- Verify deployment
- Output: {deployment_url, status}

---

## SCORING

| Phase | Max | Pass |
|-------|-----|------|
| Analyze | 30 | 20 |
| Build | 50 | 35 |
| Configure | 30 | 20 |
| Deploy | 20 | 15 |
| TOTAL | 130 | 90 |

---

## OUTPUT

For each deployment:
```
workspace/deploy/
├── analysis/     # Phase 1 outputs
├── build/       # Phase 2 outputs  
├── config/      # Phase 3 outputs
└── deploy/      # Phase 4 outputs
```

---

## SUCCESS CRITERIA

Deployment is complete when:
1. All phases pass scoring
2. index.html serves correctly
3. Dashboard loads
4. Docs are navigable
5. Vercel deployment succeeds
