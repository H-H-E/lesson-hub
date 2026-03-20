# Site Dev WORKFLOW

tracker:
  kind: local
  queue_file: data/site_queue.json

polling:
  interval_ms: 5000
  max_concurrent_agents: 5

workspace:
  root: workspace

agent:
  command: node automation/site_agent.js
  max_concurrent_agents: 5
  turn_timeout_ms: 120000

---

# FRONTEND DEVELOPMENT PIPELINE

## PHASE 1: DESIGN (5 Agents)

### Agent 1.1: UXResearcher
Research target users and their needs.
- Teachers (primary)
- Students (secondary)
- Parents
- Output: {personas[], user_journeys[], pain_points[]}

### Agent 1.2: InformationArchitect
Design site structure and navigation.
- Pages needed
- Navigation flow
- Content hierarchy
- Output: {pages[], navigation{}, sitemap}

### Agent 1.3: UIDesigner
Design visual system.
- Color palette
- Typography
- Spacing
- Components
- Output: {theme{}, components[], styles}

### Agent 1.4: ContentStrategist
Plan content for each page.
- Home page content
- Lesson pages
- About/FAQ
- Output: {content_by_page{}}

### Agent 1.5: SEOPlanner
Plan SEO and metadata.
- Keywords
- Meta descriptions
- Social sharing
- Output: {metadata{}, keywords[]}

## PHASE 2: BUILD (6 Agents)

### Agent 2.1: SetupAgent
Initialize project structure.
- package.json
- vite/astro config
- folder structure
- Output: {files_created[]}

### Agent 2.2: LayoutBuilder
Build main layout components.
- Header
- Footer
- Navigation
- Output: {components[]}

### Agent 2.3: PageBuilder
Build core pages.
- Home
- Lessons index
- Lesson detail
- Dashboard
- Output: {pages[]}

### Agent 2.4: ComponentBuilder
Build reusable components.
- LessonCard
- NavBar
- SearchBar
- Modal
- Output: {components[]}

### Agent 2.5: StyleBuilder
Implement styling system.
- CSS variables
- Global styles
- Component styles
- Output: {css_files[]}

### Agent 2.6: AssetBuilder
Create/process assets.
- Images
- Icons
- Fonts
- Output: {assets[]}

## PHASE 3: INTERACTIVE (4 Agents)

### Agent 3.1: SearchEngine
Build search functionality.
- Full-text search
- Filters
- Results display
- Output: {search_component{}}

### Agent 3.2: FilterEngine
Build lesson filtering.
- By grade
- By topic
- By status
- Output: {filter_component{}}

### Agent 3.3: DashboardBuilder
Build dashboard page.
- Real-time status
- Agent progress
- Pipeline stats
- Output: {dashboard_page}

### Agent 3.4: InteractivityBuilder
Add interactive features.
- Animations
- Transitions
- User interactions
- Output: {interactions[]}

## PHASE 4: TEST (3 Agents)

### Agent 4.1: LighthouseAuditor
Run Lighthouse audits.
- Performance
- Accessibility
- SEO
- Output: {scores{}, issues[]}

### Agent 4.2: BrowserTester
Test across browsers.
- Chrome
- Firefox
- Safari
- Output: {results{}}

### Agent 4.3: MobileTester
Test responsive design.
- Mobile
- Tablet
- Desktop
- Output: {breakpoints{}}

## PHASE 5: DEPLOY (2 Agents)

### Agent 5.1: BuildRunner
Build for production.
- Run build command
- Optimize assets
- Output: {build_output}

### Agent 5.2: DeployRunner
Deploy to Vercel.
- Vercel CLI
- Or Git integration
- Output: {deployment_url}

---

## STACK

- Framework: Astro (fast, static-first)
- Styling: CSS Variables + scoped styles
- Search: Client-side Fuse.js
- Icons: Lucide
- Fonts: Google Fonts (Space Grotesk, Inter)

## SUCCESS CRITERIA

- Lighthouse score > 90
- All pages load < 3s
- Mobile responsive
- Accessible (WCAG 2.1 AA)
- SEO optimized
