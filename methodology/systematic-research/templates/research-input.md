# Research Input Template

## Target Specification
```
Brand: [e.g., Purple, Tempur-Pedic, Saatva]
Collection: [e.g., RestorePlus, ProAdapt, Classic]
Retailer Variant: [e.g., Cool Touch, Breeze, Luxury Firm]
Sizes: [e.g., Queen, King, CalKing]
```

## Research Scope
- [ ] Complete technical specifications
- [ ] Coil counts and construction details
- [ ] Materials and layer construction
- [ ] Warranty and foundation requirements
- [ ] SME insights (hero features, personas, objections)

## Quality Requirements  
- [ ] High-confidence sources for customer-facing specifications
- [ ] Cross-validation for technical details (2+ sources)
- [ ] Evidence chain documentation
- [ ] Schema compliance validation

## Expected Output
- JSON file: `{collection}-{variant}-{height}-{size}.json`
- Location: `/specs/{brand}/`  
- Evidence: Sources documented with confidence levels
- Validation: Pass all quality gates before repository commit
