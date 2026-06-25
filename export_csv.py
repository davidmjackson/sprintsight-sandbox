# SSSB-3 add export to CSV
def export_csv(rows):
    return "\n".join(",".join(map(str, r)) for r in rows)
