import argparse
import json
import sys
from src.kernel.dag import verify_dag
from src.kernel.invariant import verify_invariants

def main():
    parser = argparse.ArgumentParser(description="Publishing OS Safety Kernel Validator")
    parser.add_argument("--input", required=True, help="Path to Master JSON")
    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        nodes = data.get("nodes", [])
        verify_dag(nodes)
        verify_invariants(nodes)
        print("[PASS] Safety Kernel: DAG topological consistency & invariant checks verified.")
        sys.exit(0)
    except Exception as e:
        print(f"[FAIL] Safety Kernel Violation: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
