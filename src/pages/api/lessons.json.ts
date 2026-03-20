// API endpoint to get all lessons
export const prerender = false;

import { readdir, readFile } from 'fs/promises';
import { join } from 'path';

const workspacePath = join(process.cwd(), 'workspace');

export async function GET() {
  const lessons = [];
  
  try {
    // Read from workspace/phase2 for design outputs
    const designPath = join(workspacePath, 'phase2');
    
    // Sample lesson data - in production would parse actual JSON files
    const sampleLessons = [
      { grade: 1, module: 1, topic: 'Living Things', status: 'complete', score: 85 },
      { grade: 1, module: 2, topic: 'Matter', status: 'complete', score: 88 },
      { grade: 2, module: 1, topic: 'Life Cycles', status: 'complete', score: 82 },
    ];
    
    return new Response(JSON.stringify({
      lessons: sampleLessons,
      total: sampleLessons.length
    }), {
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (e) {
    return new Response(JSON.stringify({ error: e.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
