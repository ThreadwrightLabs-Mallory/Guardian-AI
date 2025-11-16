"""
Guardian Protocol Handler

This module handles routing, interpretation, and management of behavioral and safety protocols
within the Guardian memory architecture. It supports layered protocol invocation, identity anchor
reinforcement, and values enforcement.

Author: Mallory
"""

import json
import os

class ProtocolHandler:
    def __init__(self, memory_path=None):
        self.memory_path = memory_path or "memory/parent.jsonl"
        self.protocols = {}
        self.load_memory()

    def load_memory(self):
        if not os.path.exists(self.memory_path):
            print(f"No memory file found at {self.memory_path}")
            return

        with open(self.memory_path, 'r') as file:
            lines = file.readlines()
            self.protocols = [json.loads(line) for line in lines]
        print(f"Loaded {len(self.protocols)} protocols from memory.")

    def execute_protocol(self, protocol_name):
        for protocol in self.protocols:
            if protocol.get("name") == protocol_name:
                print(f"Executing protocol: {protocol_name}")
                return protocol.get("instructions", "No instructions found.")
        return f"Protocol '{protocol_name}' not found."

# Example usage
if __name__ == "__main__":
    handler = ProtocolHandler()
    print(handler.execute_protocol("anti_shame"))
