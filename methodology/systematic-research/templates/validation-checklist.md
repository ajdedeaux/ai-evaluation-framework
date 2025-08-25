# Validation Checklist

## Pre-Validation Setup
- [ ] Generated JSON ready for review
- [ ] Schema reference available (`/schemas/mattress.schema.json`)
- [ ] Validation agent prompt copied
- [ ] Repository standards documented

## Schema Compliance Check
- [ ] All required fields present
- [ ] Field types correct (numbers as numbers, strings as strings)
- [ ] Enum values valid (size, confidence levels)
- [ ] Null handling appropriate (null vs. empty string vs. 0)
- [ ] JSON structure matches schema exactly

## Evidence Quality Check
- [ ] Every technical claim has supporting evidence
- [ ] Evidence sources are accessible URLs  
- [ ] Confidence levels appropriate for source types
- [ ] Minimum source requirements met (2+ for critical specs)
- [ ] Customer-facing specs use High confidence sources only

## Technical Accuracy Check
- [ ] Layer thickness calculations reasonable
- [ ] Coil system specifications complete and logical
- [ ] Weight specifications appropriate for size and construction
- [ ] Warranty details complete and accurate
- [ ] Construction details match patent/official sources

## Repository Integration Check
- [ ] spec_uid follows naming convention
- [ ] File naming matches repository standards
- [ ] Brand folder structure appropriate
- [ ] SME insights actionable and accurate
- [ ] Ready for customer deployment

## Final Approval
- [ ] Overall validation status: APPROVED
- [ ] Customer deployment ready: YES
- [ ] Required fixes: None
- [ ] Ready for `/specs/` folder commit
