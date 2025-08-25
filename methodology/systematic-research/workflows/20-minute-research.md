# 20-Minute Research Workflow
**Complete mattress family research in one session**

---

## Overview

This workflow takes you from research target to validated JSON specifications in 20 minutes, replacing the 2-3 hour manual ChatGPT process you used for Purple Cool Touch.

**Time Breakdown:**
- Setup: 2 minutes
- Research execution: 15 minutes  
- Validation & export: 3 minutes

---

## Step-by-Step Process

### Step 1: Setup (2 minutes)

**Define Research Target:**
```
Brand: [e.g., Purple]
Collection: [e.g., RestorePlus] 
Retailer Variant: [e.g., Cool Touch]
Sizes to Research: [e.g., Queen, King]
```

**Prepare Workspace:**
- Open Claude.ai or ChatGPT
- Have your repository open: `/specs/{brand}/` folder
- Copy research agent prompt from `/docs/systematic-research/prompts/research-agent.md`

### Step 2: Execute Research (15 minutes)

**2A. Launch Research Agent (2 minutes)**

Copy and customize the research prompt:
```
You are a systematic mattress research specialist executing a proven research protocol...

Execute systematic research for:
- Brand: Purple
- Collection: RestorePlus
- Retailer Variant: Cool Touch
- Sizes: Queen
```

Paste into Claude/ChatGPT and run.

**2B. Monitor Progress (8 minutes)**

The agent will work through:
- ✅ Official source gathering (Purple.com, MattressFirm.com)
- ✅ Technical validation (GoodBed, Raymour & Flanigan) 
- ✅ Patent research (USPTO construction details)
- ✅ Evidence documentation (source URLs, confidence levels)
- ✅ SME analysis (hero features, personas, objections)

**2C. Initial Review (5 minutes)**

Check the generated JSON for:
- Complete specification structure
- Evidence sources with URLs
- Reasonable technical specifications  
- SME insights that make sense

### Step 3: Validation & Export (3 minutes)

**3A. Run Validation Agent (2 minutes)**

Copy validation prompt from `/docs/systematic-research/prompts/validation-agent.md`:
```
You are a quality control specialist for mattress specification data...

EXECUTE VALIDATION FOR: [PASTE_GENERATED_JSON]
```

**3B. Review Validation Report (1 minute)**

Check for:
- ✅ Schema compliance: PASS
- ✅ Evidence quality: HIGH/MEDIUM  
- ✅ Customer deployment ready: YES
- ✅ Required fixes: None

**3C. Export to Repository (30 seconds)**

If validation passes:
1. Save JSON as `{collection}-{variant}-{height}-{size}.json`  
2. Place in `/specs/{brand}/` folder
3. Commit to repository

---

## Quality Checkpoints

### After Research Agent
- [ ] JSON structure follows your schema
- [ ] Evidence array has multiple sources
- [ ] Technical specifications look reasonable
- [ ] SME insights are actionable

### After Validation Agent  
- [ ] Schema compliance: 100%
- [ ] Evidence quality: High confidence for customer specs
- [ ] No technical inconsistencies
- [ ] Ready for customer deployment

### Before Repository Commit
- [ ] File naming matches convention
- [ ] JSON validates against schema
- [ ] Evidence URLs are accessible
- [ ] Fits with existing brand folder structure

---

## Example Session

### Input
```
Target: Purple RestorePlus Cool Touch Queen
Expected Output: purple_restoreplus_cooltouch_13_queen.json
```

### Research Agent Output (10 minutes)
```json
{
  "spec_uid": "purple_restoreplus_cooltouch_13_queen",
  "brand": "Purple",
  "collection": "RestorePlus",
  "retailer_variant": "Cool Touch",
  "model_display_name": "Purple RestorePlus Cool Touch 13\" Hybrid — Queen",
  "size": "Queen",
  "profile_height_in": 13,
  "grid_tech": { "type": "GelFlex Grid", "thickness_in": 3 },
  [... complete specification ...]
  "evidence": [
    {
      "source": "Purple Official",
      "url": "https://purple.com/mattresses/restore-plus",
      "claim": "3\" GelFlex Grid construction",
      "confidence": "High"
    }
  ]
}
```

### Validation Report (2 minutes)
```
## Validation Report
**Specification**: purple_restoreplus_cooltouch_13_queen
**Overall Status**: ✅ APPROVED

### Schema Compliance: PASS
### Evidence Quality: HIGH
- High confidence sources: 4
- Medium confidence sources: 2
### Customer Deployment Ready: YES
```

### Repository Export (30 seconds)
```
File: /specs/purple/restoreplus-cooltouch-13-queen.json
Status: Ready for commit ✅
```

---

## Troubleshooting

### If Research Takes Longer Than 15 Minutes
- Break into smaller chunks (single model vs. collection)
- Focus on Queen size first, expand later
- Use specific follow-up prompts for missing details

### If Validation Fails
- Address schema compliance issues first
- Improve evidence quality (more sources, better confidence)
- Fix technical inconsistencies
- Re-run validation agent

### If Output Quality Is Lower Than Expected
- Reference your Purple Cool Touch examples
- Request more detailed evidence documentation
- Ask for additional patent research
- Specify higher quality standards in prompts

---

## Success Metrics

### Time Targets
- Research setup: ≤ 2 minutes
- Agent execution: ≤ 15 minutes  
- Validation & export: ≤ 3 minutes
- **Total: 20 minutes vs. 2-3 hours manual**

### Quality Targets
- Schema compliance: 100%
- Evidence quality: High confidence for customer specs
- Technical accuracy: Match manual research standards
- Completeness: All required fields populated

### Consistency Targets  
- File naming: Perfect match to convention
- JSON structure: Identical to existing specifications
- Evidence format: Same as Purple Cool Touch examples
- SME insights: Actionable and accurate

---

This workflow gives you the same depth and quality as your manual Purple research, but in a fraction of the time and with systematic consistency.
