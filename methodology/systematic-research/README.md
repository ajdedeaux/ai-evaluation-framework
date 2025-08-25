# Systematic Mattress Research Protocol
**Streamlined Research-to-JSON Pipeline**

---

## Quick Start

**Goal**: Replace manual ChatGPT back-and-forth with systematic 20-minute research workflow.

**Input**: Brand + Collection + Retailer Variant  
**Output**: Complete, validated JSON specifications ready for `/specs/` folder

---

## How It Works

### The Problem We Solved
Your Purple Cool Touch research took 20+ ChatGPT exchanges over 2-3 hours to achieve comprehensive, evidence-backed specifications. This system automates that exact methodology into a repeatable workflow.

### The Solution
1. **Research Agent** executes systematic fact-gathering
2. **Validation Agent** ensures quality and schema compliance  
3. **Export Pipeline** generates ready-to-commit JSON files

---

## File Structure

```
docs/systematic-research/
├── README.md                    # This overview
├── research-protocol.md         # Detailed methodology 
├── prompts/
│   ├── research-agent.md       # Main research prompt
│   ├── validation-agent.md     # Quality control prompt
│   └── examples/
│       ├── purple-example.md   # Working example
│       └── research-log.md     # Sample research session
├── templates/
│   ├── research-input.md       # Input parameter template
│   ├── validation-checklist.md # Quality control checklist
│   └── export-format.md        # Output specification
└── workflows/
    ├── 20-minute-research.md   # Step-by-step workflow
    └── troubleshooting.md      # Common issues & fixes
```

---

## Workflows Available

### 1. Standard Research (20 minutes)
**Use for**: New mattress families, complete specifications
**Process**: Input → Research Agent → Validation Agent → Export
**Output**: Complete JSON specifications for `/specs/{brand}/`

### 2. Quick Validation (5 minutes)  
**Use for**: Verify existing specifications, update confidence levels
**Process**: Existing JSON → Validation Agent → Quality Report
**Output**: Validation report + recommended fixes

### 3. Batch Processing (45 minutes)
**Use for**: Multiple models in same collection  
**Process**: Collection parameters → Research Agent (loop) → Batch validation
**Output**: Full collection folder with all sizes/variants

---

## Integration with Your Repository

### Input Sources
- Uses your existing evidence standards from `/evidence/`
- Follows your JSON schema from `/schemas/mattress.schema.json`
- Maintains your confidence levels (High/Medium/Low)

### Output Integration
- Generates files for `/specs/{brand}/` following your naming convention
- Creates evidence entries compatible with your existing format
- Maintains your SME layer structure (hero_features, fit_personas, etc.)

### Quality Standards
- All outputs validate against your established schema
- Evidence chain follows your Purple Cool Touch methodology
- Customer-safe vs. technical appendix distinction maintained

---

## Success Metrics

| Metric | Target | Status |
|--------|--------|---------|
| Research Time | 20 min (vs 2-3 hours manual) | 🎯 |
| Schema Compliance | 100% validation pass | 🎯 |
| Evidence Quality | High-confidence sources only | 🎯 |
| Accuracy vs Manual | 95%+ specification match | 🎯 |

---

## Next Steps

1. **Review** → [`research-protocol.md`](research-protocol.md) for detailed methodology
2. **Try** → [`workflows/20-minute-research.md`](workflows/20-minute-research.md) with known mattress
3. **Customize** → [`prompts/research-agent.md`](prompts/research-agent.md) for your preferences  
4. **Scale** → Apply to new mattress families beyond Purple

---

## Files to Create

Copy these files into your repository:

```bash
# Create the directory structure
mkdir -p docs/systematic-research/prompts/examples
mkdir -p docs/systematic-research/templates  
mkdir -p docs/systematic-research/workflows

# Then copy each markdown file from the templates below
```

**Next**: See individual file templates in the sections below ⬇️
