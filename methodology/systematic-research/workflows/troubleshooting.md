# Troubleshooting Guide

## Common Issues & Solutions

### Research Agent Problems

#### "Research taking too long / incomplete results"
**Problem**: Agent doesn't return comprehensive specifications
**Solution**: 
- Break request into smaller chunks (single model vs. collection)
- Provide more specific search parameters
- Reference successful examples (Purple Cool Touch)
- Add follow-up prompts for missing technical details

#### "Evidence sources are insufficient" 
**Problem**: Not enough sources or low confidence levels
**Solution**:
- Request minimum 2 sources for technical claims
- Specify High confidence requirement for customer specs
- Ask for patent research if construction details missing
- Cross-reference multiple retailer databases

#### "JSON structure doesn't match schema"
**Problem**: Generated JSON fails schema validation
**Solution**:
- Reference schema file explicitly in prompt
- Show example of correct JSON structure
- Specify exact key order requirements
- Emphasize null handling (not empty strings or 0)

### Validation Agent Problems  

#### "Validation keeps failing"
**Problem**: Generated specs don't pass quality gates
**Solution**:
- Address schema compliance issues first
- Improve evidence quality (more/better sources)
- Fix technical inconsistencies in specifications
- Ensure customer-safe vs. technical separation

#### "Evidence confidence levels wrong"
**Problem**: Sources marked with inappropriate confidence
**Solution**:
- Clarify confidence criteria in prompt
- High: Official brand, patents, verified exclusives
- Medium: Major retailer databases, industry specs
- Low: Forums, unverified (exclude from output)

## Getting Help

If systematic approach isn't working:
1. **Reference Purple Cool Touch**: Use as gold standard example
2. **Break down the problem**: Identify specific failure point
3. **Adjust prompt specificity**: More detailed requirements often help
4. **Quality over speed**: Better to take extra time for accuracy
5. **Iterate and improve**: Refine prompts based on results

The goal is to match your manual research quality while gaining speed and consistency.
