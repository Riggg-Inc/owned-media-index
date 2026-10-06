"""Offline declared-evidence check, not a semantic or Workboard interceptor."""
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / 'schemas/scope-evidence.schema.json').read_text())

def validate(record):
    errors = []
    if not isinstance(record, dict):
        return ['record must be an object']
    for key in SCHEMA['required']:
        rule = SCHEMA['properties'][key]
        v = record.get(key)
        if key not in record:
            errors.append('missing: ' + key)
        elif rule.get('type') == 'string' and (not isinstance(v, str) or not v.strip()):
            errors.append('nonempty string required: ' + key)
        elif rule.get('type') == 'array' and (not isinstance(v, list) or any(not isinstance(i, str) for i in v)):
            errors.append('string array required: ' + key)
        elif 'const' in rule and (type(v) is not type(rule['const']) or v != rule['const']):
            errors.append('context/scope gate: ' + key)
        elif 'enum' in rule and v not in rule['enum']:
            errors.append('invalid stage')
    if set(record) - set(SCHEMA['properties']):
        errors.append('unknown fields')
    reg = json.loads((ROOT / 'docs-internal/intake-suppressions.json').read_text())
    if record.get('mechanism') not in reg['eligible_mechanisms']:
        errors.append('blocked or unclassified mechanism; return for context/watch')
    slug = str(record.get('slug', '')).lower().split('/')[-1].removesuffix('.md')
    if slug in reg['retired_slugs'] or slug in reg['superseded_slugs']:
        errors.append('retired/superseded slug')
    if set(record.get('related_card_ids', []) if isinstance(record.get('related_card_ids'), list) else []) & set(reg['suppressed_card_ids']):
        errors.append('retired/superseded card identifier')
    return errors

if __name__ == '__main__':
    try:
        errors = validate(json.loads(Path(sys.argv[1]).read_text()))
    except (IndexError, OSError, ValueError) as e:
        errors = [str(e)]
    print(json.dumps({'verdict': 'RETURN' if errors else 'PASS_DECLARED_SCOPE', 'errors': errors}))
    sys.exit(bool(errors))
