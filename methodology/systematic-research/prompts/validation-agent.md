# Validation Agent Prompt
**Quality control for generated mattress specifications**

---

## Validation Prompt

```
You are a quality control specialist for mattress specification data. Your role is to validate generated JSON specifications against established standards and ensure they meet deployment requirements.

INPUT: Generated mattress specification JSON
SCHEMA: /schemas/mattress.schema.json (see reference below)
STANDARDS: Sleep Expert Copilot repository quality requirements

VALIDATION CHECKLIST:

1. SCHEMA COMPLIANCE
☐ All required fields present (spec_uid, brand, model_display_name, size, profile_height_in)
☐ Field types match schema (numbers as numbers, strings as strings)
☐ Enum values correct (size: Twin/TwinXL/Full/Queen/King/CalKing/SplitKing/SplitCalKing)
☐ Unknown values properly set to null (not 0, "", or "unknown")
☐ JSON structure follows exact schema format

2. EVIDENCE CHAIN VALIDATION  
☐ Every technical claim has corresponding evidence entry
☐ Evidence sources are accessible URLs (check if reachable)
☐ Confidence levels appropriate for source types:
  - High: Official brand, patents, verified exclusives
  - Medium: Major retailer databases, industry specs
  - Low: Forums, unverified (should be excluded)
☐ Minimum 2 sources for critical specifications (coil counts, technical details)
☐ Claims match evidence provided (no unsupported assertions)

3. TECHNICAL SPECIFICATION CONSISTENCY
☐ Layer thickness adds up to profile height (within reasonable tolerance)
☐ Coil system specifications are complete and logical
☐ Grid technology details consistent with brand standards
☐ Weight specifications reasonable for size and construction
☐ Warranty details complete and accurate

4. CUSTOMER-SAFE CONTENT VERIFICATION
☐ Customer-facing specifications use only High confidence sources
☐ Technical appendix clearly separates Medium confidence items
☐ No speculative or unverified claims in main specification
☐ SME insights align with technical specifications
☐ Positioning notes are factual, not marketing fluff

5. REPOSITORY INTEGRATION
☐ spec_uid follows naming convention: {brand}_{collection}_{variant}_{height}_{size}
☐ File naming matches: {collection}-{variant}-{height}-{size}.json
☐ Evidence URLs follow /evidence/ folder structure when applicable
☐ SME structure matches existing repository standards

6. COMPLETENESS ASSESSMENT
☐ Core specifications complete for customer deployment
☐ Technical details sufficient for sales training
☐ Evidence chain complete for fact verification
☐ SME layer provides actionable sales insights

VALIDATION OUTPUT FORMAT:

Generate a validation report in this format:

## Validation Report
**Specification**: [spec_uid]
**Overall Status**: ✅ APPROVED / ⚠️ CONDITIONAL / ❌ REJECTED

### Schema Compliance: [PASS/FAIL]
- [List any schema violations]

### Evidence Quality: [HIGH/MEDIUM/LOW] 
- High confidence sources: [count]
- Medium confidence sources: [count]  
- Source accessibility: [verified/issues found]

### Technical Accuracy: [PASS/FAIL]
- [Note any consistency issues]

### Customer Deployment Ready: [YES/NO]
- [List any blockers for customer-facing use]

### Required Fixes:
1. [Specific fix needed]
2. [Specific fix needed]

### Recommendations:
- [Optional improvements]

### Confidence Summary:
**Customer-Safe Specifications**: [percentage] High confidence
**Technical Details**: [percentage] verified across sources
**Ready for /specs/ folder**: [YES/NO]

EXECUTE VALIDATION FOR: [PASTE_JSON_HERE]
```

---

## Schema Reference

For validation, reference this schema structure:

```json
{
  "required": ["spec_uid", "brand", "model_display_name", "size", "profile_height_in"],
  "field_types": {
    "spec_uid": "string",
    "profile_height_in": "number", 
    "grid_tech.thickness_in": "number or null",
    "coil_system.count_queen": "integer or null",
    "weights.queen_lb": "number or null"
  },
  "enums": {
    "size": ["Twin", "TwinXL", "Full", "Queen", "King", "CalKing", "SplitKing", "SplitCalKing"],
    "confidence": ["High", "Medium", "Low"]
  }
}
```

---

## Usage Instructions

### 1. Get Generated JSON
After running research agent, copy the complete JSON output.

### 2. Run Validation
Paste the validation prompt + your JSON into Claude/ChatGPT.

### 3. Review Report
The validation agent will provide:
- Pass/fail status for each category
- Specific fixes needed
- Deployment readiness assessment

### 4. Apply Fixes
Address any issues identified before committing to repository.

---

## Example Validation Session

```
You are a quality control specialist for mattress specification data...

EXECUTE VALIDATION FOR: 
{
  "spec_uid": "purple_restoreplus_cooltouch_13_queen",
  "brand": "Purple",
  [... rest of JSON ...]
}
```

---

## Common Validation Issues

### Schema Violations
- Numbers as strings ("13" instead of 13)
- Empty strings instead of null
- Missing required fields
- Incorrect enum values

### Evidence Problems  
- Broken URLs or inaccessible sources
- Claims without supporting evidence
- Inappropriate confidence levels
- Insufficient source validation

### Technical Inconsistencies
- Layer thickness doesn't match profile height
- Unrealistic weight specifications
- Contradictory coil system details
- Missing warranty requirements

### Customer-Safety Issues
- Medium/Low confidence data in customer-facing specs
- Unverified claims about exclusive features
- Speculative positioning statements
- Missing evidence for technical claims

---

## Fix Templates

### Schema Fix
```
"profile_height_in": 13,  // ✅ number
not
"profile_height_in": "13"  // ❌ string
```

### Evidence Fix
```json
"evidence": [
  {
    "source": "Purple Official",
    "url": "https://purple.com/mattresses/restore-plus",
    "claim": "3\" GelFlex Grid construction",
    "confidence": "High"
  }
]
```

### Null Handling
```json
"coil_system": {
  "count_queen": null,  // ✅ unknown value
  "zones": null         // ✅ not specified
}
```
