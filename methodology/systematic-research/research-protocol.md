# Research Protocol - Detailed Methodology
**Based on your successful Purple Cool Touch research**

---

## Protocol Overview

This systematizes your proven ChatGPT research methodology into a repeatable process that maintains quality while eliminating manual back-and-forth.

### Your Original Process (Purple Cool Touch)
1. Initial product identification
2. Official specification gathering  
3. Third-party validation (GoodBed, Raymour & Flanigan)
4. Patent research for technical details
5. Evidence confidence scoring
6. Cross-model comparison and validation
7. SME insight integration
8. JSON generation and schema validation

### Systematic Version (Same Quality, 10x Speed)
All 8 steps above → Single automated research session with built-in validation

---

## Research Agent Methodology

### Phase 1: Official Source Gathering (5 minutes)
**Primary Sources (High Confidence)**
- Brand official website (Purple.com, etc.)
- Retailer exclusive pages (MattressFirm.com for variants)
- Official press releases and announcements
- Brand specification PDFs and datasheets

**Search Pattern:**
```
1. Brand homepage → Mattress section → Target collection
2. Retailer exclusive search → Variant confirmation  
3. Official spec downloads → PDF processing
4. Press release search → Launch details and unique features
```

### Phase 2: Technical Validation (5 minutes)
**Third-Party Verification (Medium Confidence)**
- GoodBed.com specification database
- Raymour & Flanigan product listings
- Major retailer spec confirmations
- Industry database cross-references

**Patent Research (High Confidence)**
- USPTO patent search for construction details
- Patent citations for technical architecture  
- Engineering specifications from patent disclosures

**Validation Rules:**
- Coil counts: Require 2+ source confirmation
- Technical specs: Official source + 1 verification minimum
- Weights/dimensions: Cross-check against multiple retailers

### Phase 3: Evidence Documentation (3 minutes)
**Source Confidence Scoring:**
- **High**: Official brand, patents, verified retailer exclusives
- **Medium**: Major retailer databases, industry specifications  
- **Low**: Forums, unverified sources (exclude from customer-safe)

**Evidence Chain Format:**
```json
"evidence": [
  {
    "source": "Purple Official",
    "url": "https://purple.com/mattresses/restore-plus",
    "claim": "3\" GelFlex Grid hybrid construction",
    "confidence": "High"
  },
  {
    "source": "GoodBed Database", 
    "url": "https://goodbed.com/...",
    "claim": "Queen coil count: 789",
    "confidence": "Medium"
  }
]
```

### Phase 4: SME Integration (2 minutes)
**Based on Technical Analysis:**
- Hero features from construction advantages
- Fit personas from comfort/support profile
- Common objections from material/feel characteristics  
- Positioning notes from competitive context

---

## Quality Gates

### Before JSON Generation
- ✅ All required schema fields have data or explicit null
- ✅ Every technical claim has evidence source
- ✅ Coil counts cross-validated (if available)
- ✅ Construction details match patent references
- ✅ Retailer variant exclusivity confirmed

### After JSON Generation  
- ✅ Schema validation passes (`mattress.schema.json`)
- ✅ Evidence confidence levels appropriate
- ✅ SME insights align with technical specifications
- ✅ Naming convention matches repository standards
- ✅ Customer-safe content verified (High confidence only)

---

## Output Specifications

### File Generation
**Naming**: `{collection}-{variant}-{height}-{size}.json`
**Location**: `/specs/{brand}/`
**Validation**: Must pass schema validation before commit

### Required Completeness
**Customer-Safe Fields (High Confidence Only):**
- profile_height_in
- grid_tech (if applicable)
- coil_system basics
- warranty details
- retailer information

**Technical Fields (Medium Confidence Acceptable):**
- Detailed coil counts
- Exact material compositions
- Weight specifications by size
- Advanced construction details

### Evidence Requirements
- Minimum 2 sources for technical specifications
- At least 1 High-confidence source for customer-facing claims
- Complete URL trail for fact verification
- Confidence level justification for each source

---

## Automation Implementation

### Research Agent Execution
```
INPUT: {brand: "Purple", collection: "RestorePlus", variant: "Cool Touch"}

PROCESS:
1. Execute Phase 1-4 research protocol
2. Generate evidence-backed JSON
3. Validate against quality gates
4. Return structured output

OUTPUT: Complete JSON + evidence report + confidence summary
```

### Integration with Your Repository  
- Follows your established schema exactly
- Uses your evidence confidence methodology  
- Maintains your SME insight structure
- Generates files in your naming convention

---

## Success Validation

### Against Your Purple Research
Compare automated output with your manually-researched Purple Cool Touch specifications:
- Technical accuracy: 95%+ match
- Evidence quality: Same source types and confidence levels
- Schema compliance: 100% validation
- Completeness: All fields populated appropriately

### Quality Metrics
- Research time: 20 minutes vs. 2-3 hours manual
- Consistency: Schema-enforced vs. human variable  
- Scalability: Multiple families vs. single family focus
- Accuracy: Maintained through systematic validation

---

This protocol captures your proven research methodology and makes it repeatable without losing the depth and accuracy you achieved with Purple Cool Touch.
