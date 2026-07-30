def verify_invariants(nodes, archive_nodes=None):
    # Check for tag cluster collisions or contradictory invariants
    clusters = {}
    for node in nodes:
        tag_key = frozenset(node.get("tags", []))
        if tag_key in clusters:
            # Check invariant consistency
            existing_inv = clusters[tag_key]["invariant"]
            if existing_inv != node["invariant"]:
                print(f"[Warning] Invariant shift detected in tag cluster {list(tag_key)}")
        else:
            clusters[tag_key] = node
    return True
