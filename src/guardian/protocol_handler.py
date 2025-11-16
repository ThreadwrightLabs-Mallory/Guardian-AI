"""
Guardian Protocol Handler

This module handles routing, interpretation, and management of behavioral and safety protocols
within the Guardian memory architecture. It supports layered protocol invocation, identity anchor
reinforcement, and values enforcement.

Author: Mallory
"""

import json
import os

class GuardianProtocolHandler:
    def __init__(self, memory_path="memory/parent.jsonl"):
        self.memory_path = memory_path
        self.protocols = self.load_protocols()

    def load_protocols(self):
        protocols = []
        if not os.path.exists(self.memory_path):
            print(f"[Warning] No memory file found at {self.memory_path}")
            return protocols

        with open(self.memory_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    protocol = json.loads(line.strip())
                    protocols.append(protocol)
                except json.JSONDecodeError:
                    print("[Error] Skipping malformed line.")
                    continue
        print(f"[Info] Loaded {len(protocols)} protocols from memory.")
        return protocols

    def get_protocol_by_name(self, name):
        for protocol in self.protocols:
            if protocol.get("name") == name:
                return protocol
        return None

    def get_protocols_by_type(self, ptype):
        return [p for p in self.protocols if p.get("type") == ptype]

    def execute_protocol(self, protocol_name):
        protocol = self.get_protocol_by_name(protocol_name)
        if protocol:
            print(f"[Execute] Protocol '{protocol_name}' found. Running instructions...")
            return protocol.get("instructions", "No instructions found.")
        return f"[Error] Protocol '{protocol_name}' not found."

# Example usage
if __name__ == "__main__":
    handler = GuardianProtocolHandler()
    print(handler.execute_protocol("anti_shame"))
