/**
 * eNuminous README navigation transformer (2026-10-27).
 * Pure, deterministic, idempotent transformation; does not execute GitHub writes.
 * Usage: const rewrite = require('./tools/rewrite_readme_navigation.js');
 *        const {content, stats} = rewrite('EFMW', oldReadme);
 * Review output before writing and use the original file SHA to guard against conflicts.
 */
'use strict';
const lists = {
  animals: 'Tortoise Owl Octopus Gecko Hive Eagle Crab Shepherd Pulse Cat Fox Spider Raven Dolphin Ant Moth Shark Penguin Bat Hedgehog Crocodile Dragon Turtle Magpie Wolf Elephant Chameleon Jellyfish Beaver Mantis Bison Weasel Salmon Orca Mole Lynx Horse Termite Phoenix Cobra Whale Falcon Rhino Bonobo Axolotl Butterfly monster woodpecker Nightengale Chimera Circus Zoo-Monster'.split(' '),
  physics: 'Standard-Model-Reduction Higgs-Gauge-Lab EFMW-Physics-Lab Base888-Quantum-Geometry Quantum-Gravity QST Cosmology FieldSpace Cat-Physics Universe5 Music-of-the-Spheres Oroboros EFMW-Neutron-Star-Glitch-Resonance EFMW-Constants-Problem EFMW-108-Minute-Tests Ligo_EFMW_Search EFMW-Grid'.split(' '),
  formal: 'Monolithic-102-Zoo-Lean4 Monolithic-Zoo-Lean4 Monlithic_EFMW_102_Lean4 Aristotle-102-Monolithic-Lean Aristotle_EFMW_Lean Aristotle-165-Einsteinian-Tensors Einsteinian-156-Aristotle Monolithic_Zoo_Run MultiValuedClassicalAction-Lean4 Aristotle-eNuminous Aristotle-Ramtastic-Audit Aristotle-Agreement-and-Surprise-Global-Equalibrium-from-Local-Repair lean-worker Cadence-Zoo-Evidence Nightengale-Full-Zoo-Audit'.split(' '),
  editorial: 'papers docs medium Medium2 Medium3 Mathematics-and-Elite-Squad-Dynamics Research-Program Wrights-Law I-Have-Guts Extrauniversal-Warren-Report Harlequinn Alchemy-of-Emergence Universal-Cognitive-Attractor Emergentology aok'.split(' '),
  digital: 'Codex-888 accelerando-8192 Multiverse-Simulator Archimedes-Engine Archimedes-3D Archimedes-Field-Lab Coherence-Prediction-Engine OpenAI-math oph-lab Devs2.0 P-NP EFMW-Rule30 BackroomsProtocol-EFMW-Analysis Ramtastic Weaver_Os simself fieldcore DePIN meta-meme Borges-Library-CollapseOmega Avenue5 Verbinski-Protocol JEV-EFMW-Syncretic-Layer'.split(' '),
  core: 'EFMW EFMW-FULL EFMW-EXP-001 EFMW-Safety-001 Monolithic Monolithic_102_EFMW EFMW-Scientific-Claims EFMW_Post156_Zoo_Audit efmw-equation-review EFMW-CTX-001b EFMW-Lagrangian EFMW-Axioms'.split(' ')
};
const allPublic = new Set(Object.values(lists).flat().concat(['efmw-research-cache'])); // only names confirmed in public inventory
const named = {
 EFMW:['Monolithic_102_EFMW','Monolithic-102-Zoo-Lean4','EFMW_Post156_Zoo_Audit','papers','QST','EFMW-FULL'],
 Tortoise:['Monolithic-Zoo-Lean4','Monolithic-102-Zoo-Lean4','EFMW_Post156_Zoo_Audit','Owl','papers'],
 papers:['EFMW','Monolithic_102_EFMW','Research-Program','Cosmology','Quantum-Gravity','QST'],
 'Base888-Quantum-Geometry':['Quantum-Gravity','QST','Codex-888','EFMW','Standard-Model-Reduction'],
 'Quantum-Gravity':['QST','Base888-Quantum-Geometry','Standard-Model-Reduction','EFMW-Physics-Lab','papers'],
 QST:['Quantum-Gravity','Base888-Quantum-Geometry','Standard-Model-Reduction','EFMW-Lagrangian','papers'],
 'Standard-Model-Reduction':['Higgs-Gauge-Lab','EFMW-Physics-Lab','Base888-Quantum-Geometry','Quantum-Gravity','QST'],
 'Higgs-Gauge-Lab':['Standard-Model-Reduction','EFMW-Physics-Lab','Quantum-Gravity','QST'],
 'EFMW-Physics-Lab':['Higgs-Gauge-Lab','Standard-Model-Reduction','Quantum-Gravity','QST'],
 'Codex-888':['Base888-Quantum-Geometry','QST','accelerando-8192','EFMW'],
 Cosmology:['Oroboros','FieldSpace','EFMW-Lagrangian','Quantum-Gravity','papers'],
 'EFMW-Lagrangian':['Monolithic-102-Zoo-Lean4','Cosmology','EFMW','Quantum-Gravity'],
 'Monolithic-102-Zoo-Lean4':['Monolithic_102_EFMW','EFMW','Monolithic-Zoo-Lean4','EFMW_Post156_Zoo_Audit'],
 'Monolithic-Zoo-Lean4':['Tortoise','Monolithic-102-Zoo-Lean4','EFMW_Post156_Zoo_Audit','papers'],
 medium:['Medium2','Medium3','papers','Mathematics-and-Elite-Squad-Dynamics'],
 Medium2:['medium','Medium3','papers'], Medium3:['medium','Medium2','papers'],
 'Music-of-the-Spheres':['Cosmology','EFMW-Lagrangian','Oroboros','EFMW'],
 'Devs2.0':['EFMW-EXP-001','Coherence-Prediction-Engine','papers','EFMW'],
 'Aristotle-Ramtastic-Audit':['Ramtastic','Monolithic-Zoo-Lean4','EFMW_Post156_Zoo_Audit'],
 'Weaver_Os':['Monolithic-102-Zoo-Lean4','papers','EFMW'],
 'EFMW-Rule30':['P-NP','EFMW','papers'],
 'EFMW_Post156_Zoo_Audit':['Monolithic-Zoo-Lean4','Monolithic-102-Zoo-Lean4','Tortoise','EFMW']
};
function group(n) {
 if(lists.animals.includes(n)) return ['Zoo index and agents',lists.animals];
 if(lists.physics.includes(n)) return ['Fundamental physics, cosmology and quantum geometry',lists.physics];
 if(lists.formal.includes(n)) return ['Lean, proofs and independent audits',lists.formal];
 if(lists.editorial.includes(n)) return ['Papers, publications and creative work',lists.editorial];
 if(lists.digital.includes(n)) return ['Simulators, computation and experiments',lists.digital];
 if(lists.core.includes(n)) return ['Core EFMW and review',lists.core];
 return ['Other repositories',[n]];
}
function slug(s) {
 return s.replace(/\[([^\]]+)\]\([^)]+\)/g,'$1').replace(/<[^>]*>/g,'')
  .replace(/[\`*_~]/g,'').toLowerCase()
  .replace(/[^\p{L}\p{N}\s_-]/gu,'').trim().replace(/\s/g,'-');
}
function headings(s) {
 let fenced=false, found=[],seen=new Map();
 for(const line of s.split(/\r?\n/)) {
  if(/^\s*(```|~~~)/.test(line)) {fenced=!fenced; continue;}
  if(fenced) continue;
  const m=line.match(/^(#{1,5})\s+(.+?)(?:\s+#+)?\s*$/);
  if(!m) continue;
  const a=slug(m[2]);if(!a) continue;
  const count=seen.get(a)||0;seen.set(a,count+1);
  if(m[1].length>1) found.push({depth:m[1].length,label:m[2].replace(/[\`*]/g,'').replace(/\[([^\]]+)\]\([^)]+\)/g,'$1').replace(/<[^>]+>/g,'').replace(/[\[\]]/g,''),anchor:a+(count?'-'+count:'')});
 }
 return found;
}
module.exports = function rewriteReadme(name,original) {
 const earlier=original.match(/<!-- ENUMINOUS-NETWORK:START -->([\s\S]*?)<!-- ENUMINOUS-NETWORK:END -->/);
 const existing=original.match(/<!-- ENUMINOUS-UNIFIED-NAV:START -->([\s\S]*?)<!-- ENUMINOUS-UNIFIED-NAV:END -->/);
 const live=earlier?.[1]?.match(/\[Published page\]\((https?:\/\/[^)]+)\)/)?.[1] || existing?.[1]?.match(/\[Published site\]\((https?:\/\/[^)]+)\)/)?.[1];
 const webIndex=/\[index\.html\]\(https:\/\/github\.com\/enuminous\/[^)]+\/blob\/[^)]*\/index\.html\)/.test(earlier?.[1]||'') || (existing?.[1]||'').includes('[Web application](index.html)');
 let s=original.replace(/<!-- ENUMINOUS-UNIFIED-NAV:START -->[\s\S]*?<!-- ENUMINOUS-UNIFIED-NAV:END -->\s*/g,'')
   .replace(/<!-- ENUMINOUS-NETWORK:START -->[\s\S]*?<!-- ENUMINOUS-NETWORK:END -->\s*/g,'');
 if(!s.trim()) s='# '+name+'\n\n## Overview\n\nExplore this project and its counterparts using the navigation links above.\n';
 if(!/^#{1,2}\s+\S/m.test(s)) s='# '+name+'\n\n'+s.replace(/^\s+/,'');
 const hs=headings(s), chosen=hs.slice(0,80), [category,members]=group(name), ix=members.indexOf(name);
 const peerNames=[...(named[name]||[])];
 if(ix>=0&&members.length>1) for(const offset of [1,-1,2,-2])peerNames.push(members[(ix+members.length+offset)%members.length]);
 if(lists.animals.includes(name))peerNames.unshift('Tortoise','Monolithic-Zoo-Lean4','Monolithic-102-Zoo-Lean4');
 else if(lists.physics.includes(name))peerNames.push('EFMW','papers');
 else if(lists.formal.includes(name))peerNames.push('Monolithic_102_EFMW','EFMW');
 else if(lists.editorial.includes(name))peerNames.push('papers','EFMW');
 else peerNames.push('EFMW','papers');
 const peers=[...new Set(peerNames)].filter(n=>n!==name&&allPublic.has(n)).slice(0,9);
 const h1=(s.match(/^#\s+(.+)$/m)||[])[1];
 const toc=chosen.length?chosen.map(h=>' '.repeat(Math.max(0,Math.min(h.depth,4)-2)*2)+'- ['+h.label+'](#'+h.anchor+')').join('\n')
   :'- [Project overview](#'+slug(h1||name)+')';
 const nav=[
 '<!-- ENUMINOUS-UNIFIED-NAV:START -->','## Repository navigation','',
 '**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)','',
 '**This project:** [Repository home](https://github.com/enuminous/'+name+') · '+(name==='EFMW-Bounded-Test-1'?'[Public network index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md)':'[Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#'+slug(category)+')')+(live?' · [Published site]('+live+')':'')+(webIndex?' · [Web application](index.html)':''),'',
 '<details open>','<summary><strong>On this page</strong></summary>','',toc,chosen.length<hs.length?'\n- *Further headings are in the document below.*':'','',
 '</details>','',
 '**Related repositories:** '+peers.map(n=>'['+n+'](https://github.com/enuminous/'+n+')').join(' · '),'',
 '> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.',
 '<!-- ENUMINOUS-UNIFIED-NAV:END -->',''].join('\n');
 const head=s.match(/^#\s+.+$/m);
 const content=head?s.slice(0,head.index+head[0].length)+'\n\n'+nav+'\n'+s.slice(head.index+head[0].length).replace(/^\s*\n/,'\n') :nav+'\n'+s;
 return {content,stats:{oldLength:original.length,newLength:content.length,tocTotal:hs.length,tocListed:chosen.length,peers:peers.length,legacyBlockReplaced:!!earlier}};
};