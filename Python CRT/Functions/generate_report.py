db = {
    "geneA": "ATGT",  # 75%
    "geneB": "ATGC",  # 100%
    "geneC": "TTAC",  # 25%
    "geneD": "ATGG",  # 75%
    "geneE": "ATCC",  # 75%
    "geneF": "AGGC",  # 50%
    "geneG": "GTGC",  # 75%
    "geneH": "TTGC",  # 75%
    "geneI": "GGGG",  # 0%
    "geneJ": "ATGA"   # 75%
}

def generate_report(query: str, db: dict):
    for gene_id, sequence in db.items():
        # Compare each character in query with the corresponding character in the db sequence
        match_count = sum(1 for q, s in zip(query, sequence) if q == s)
        match_percentage = (match_count / len(query)) * 100

        # Determine match status
        if match_percentage >= 80:
            status = "Good match"
        elif match_percentage >= 50:
            status = "Moderate match"
        else:
            status = "Poor match"

        # Print formatted result
        print(f"ID: {gene_id} | Match: {int(match_percentage)}% | Status: {status}")

# Call the function with a sample query
generate_report("ATGC", db)
