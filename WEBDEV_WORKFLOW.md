# WEB DEV TEAM WORKFLOW

tracker:
  kind: local
  queue_file: data/webdev_queue.json

polling:
  interval_ms: 10000
  max_concurrent_agents: 5

---

# WEB DEVELOPMENT TEAM - Curriculum to Production

This team specializes in converting curriculum pipeline outputs into deployed, production-ready website.

## TEAM STRUCTURE

### Team Lead: WebDevOrchestrator
- Coordinates all web dev agents
- Manages queue of curriculum updates
- Triggers builds and deploys

---

## PHASE 1: INTAKE (4 Agents)

### Agent 1.1: CurriculumWatcher
Monitor workspace/ for new curriculum outputs.
- Watch for new JSON files in workspace/
- Detect new lessons generated
- Trigger intake pipeline
- Output: {new_lessons[], last_checked}

### Agent 1.2: DataParser
Parse curriculum JSON into usable data.
- Read workspace/phase2, phase3 outputs
- Extract lesson components
- Normalize data structure
- Output: {parsed_lessons[], components{}}

### Agent 1.3: ContentExtractor
Extract content from parsed data.
- Pull objectives, materials, activities
- Extract assessment content
- Get standards alignment
- Output: {content_by_lesson{}}

### Agent 1.4: AssetCollector
Collect related assets.
- Find simulation code
- Gather images/icons
- Collect media files
- Output: {assets_by_lesson{}}

---

## PHASE 2: CONVERSION (5 Agents)

### Agent 2.1: PageBuilder
Build Astro/Next.js pages from curriculum.
- Generate lesson detail pages
- Create index pages
- Build navigation
- Output: {pages_generated[]}

### Agent 2.2: ComponentBuilder
Build reusable UI components.
- LessonCard
- NavBar
- SearchBar
- FilterPanel
- Output: {components[]}

### Agent 2.3: APIBuilder  
Create API endpoints for lessons.
- /api/lessons.json
- /api/lessons/[id].json
- /api/search.json
- Output: {endpoints[]}

### Agent 2.4: AssetProcessor
Process and optimize assets.
- Minify simulation code
- Optimize images
- Create responsive versions
- Output: {processed_assets[]}

### Agent 2.5: StyleIntegrator
Apply consistent styling.
- Match theme across pages
- Ensure accessibility
- Mobile responsive
- Output: {styled_pages[]}

---

## PHASE 3: INTEGRATION (4 Agents)

### Agent 3.1: LinkManager
Create internal links between pages.
- Cross-link lessons
- Connect related content
- Build breadcrumbs
- Output: {links_created[]}

### Agent 3.2: SearchIndexer
Build search index.
- Index all lesson content
- Create search functionality
- Optimize for fast search
- Output: {search_index{}}

### Agent 3.3: SEOManager
Handle SEO requirements.
- Generate meta tags
- Create sitemaps
- OpenGraph images
- Output: {seo_data{}}

### Agent 3.4: I18nManager
Prepare for internationalization.
- Extract translatable strings
- Setup i18n structure
- Prepare for translations
- Output: {i18n_ready}

---

## PHASE 4: TESTING (3 Agents)

### Agent 4.1: BuildTester
Test that site builds successfully.
- Run astro build / next build
- Check for errors
- Verify all pages generated
- Output: {build_success, errors[]}

### Agent 4.2: LinkTester
Test all internal links.
- Crawl all pages
- Find broken links
- Verify redirects
- Output: {broken_links[], status}

### Agent 4.3: PerformanceTester
Test site performance.
- Lighthouse scores
- Load times
- Bundle sizes
- Output: {performance_scores{}}

---

## PHASE 5: DEPLOYMENT (2 Agents)

### Agent 5.1: GitPusher
Commit and push changes.
- Stage all changes
- Create commit with curriculum update
- Tag version
- Push to remote
- Output: {commit_hash, files_changed[]}

### Agent 5.2: VercelDeployer
Deploy to Vercel.
- Trigger Vercel deploy
- Wait for build
- Verify live site
- Output: {deployment_url, status}

---

## AUTOMATION TRIGGERS

The Web Dev team activates when:

1. **New curriculum generated** - Pipeline completes a lesson
2. **Scheduled rebuild** - Daily/weekly sync
3. **Manual trigger** - User requests rebuild
4. **Content update** - User edits lesson data

---

## WORKFLOW

```
CURRICULUM PIPELINE COMPLETE
         ↓
  CurriculumWatcher detects new
         ↓
  DataParser + ContentExtractor
         ↓
  PageBuilder + ComponentBuilder
         ↓
  LinkManager + SearchIndexer
         ↓
  BuildTester + LinkTester
         ↓
  GitPusher + VercelDeployer
         ↓
  LIVE SITE UPDATED
```

---

## SUCCESS CRITERIA

- All new lessons appear on site within 5 minutes
- Build succeeds 100% of time
- No broken links
- Lighthouse score > 90
- All pages mobile responsive

---

## AGENT COUNT: 18

| Phase | Agents |
|-------|--------|
| Intake | 4 |
| Conversion | 5 |
| Integration | 4 |
| Testing | 3 |
| Deployment | 2 |
