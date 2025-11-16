import json

def load_protocols(filepath='data/guardian_protocols.jsonl'):
    protocols = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            protocols.append(json.loads(line.strip()))
    return protocols

def match_prompt(user_input, protocols):
    for item in protocols:
        if item['prompt'].lower() in user_input.lower():
            return item['completion']
    return None
