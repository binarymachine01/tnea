from difflib import SequenceMatcher


def calculate_match(name1, name2):
    # Use SequenceMatcher to calculate similarity
    similarity_ratio = SequenceMatcher(None, name1, name2).ratio()
    match_percentage = round(similarity_ratio * 100, 2)

    # Determine the matched substring
    matcher = SequenceMatcher(None, name1, name2)
    matched_blocks = matcher.get_matching_blocks()
    matched_string = ''.join([name1[block.a:block.a + block.size] for block in matched_blocks])

    # Return match percentage and matched string
    return match_percentage, matched_string


# Inputs
name1 = "R K S"
name2 = "Rakesh Kumar Singh"

# Calculate match
match_percentage, matched_string = calculate_match(name1, name2)

# Output result
print(f"Matched String: {matched_string}")
print(f"Match Percentage: {match_percentage}%")