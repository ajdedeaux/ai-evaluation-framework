# AI Evaluation Framework — From vibes to verification

This repo gives you a **straightforward way to tell if AI content is safe to ship**.  
It sets the rules for what “good” looks like, requires a source for every claim, and runs automatic checks before anything merges.

**How it works in one line:**  
Contract (the shape/rules) → Trusted Sources (High/Medium) → Evidence (a receipt for every fact) → Automatic Checks → Readiness Score → Ship.

---

## Who this is for
Teams that want AI-generated content to be **consistent, traceable, and deployment-ready** (sales sheets, product specs, FAQs, policies, etc.).

## What you get
- **Method:** plain-English playbook and roles.
- **Templates:** JSON schema (the contract), source registry (what counts as High/Medium), prompt examples.
- **Checks:** small scripts and a GitHub check that pass/fail your files automatically.
- **Examples:** a sample “spec” you can test in minutes.

---

## Quickstart (no command line)
1. Open this repo in **GitHub Desktop**.
2. Make sure the workflow file is here:  
   **`.github/workflows/validate-specs.yml`** (this is what runs the checks on pull requests).
3. Create a folder for sample content:  
   **`specs/mattress/tempur-pedic/proadapt/`**
4. Copy the sample:  
   **`examples/specimen_output.json` → `specs/mattress/tempur-pedic/proadapt/proadapt-soft-12-queen.json`**
5. In GitHub Desktop:
   - Create a new branch (e.g., `setup-ci`), **Commit** your change, then **Push**.
   - Click **Create Pull Request**.  
   GitHub will run the checks automatically. Green = good to merge; red = fix what it tells you.

> Think of these checks like spell-check for facts and structure. They verify the file shape, count your High/Medium sources, and compute a readiness score.

---

## Quickstart (optional, with command line)
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate_json.py specs contracts/schema.example.json
python scripts/check_evidence.py specs contracts/source_registry.example.yml
python scripts/score_readiness.py specs --min-score 85
