

def display_results(data, group_label):
    current_group = None

    for row in data:
        if row[group_label] != current_group:
            current_group = row[group_label]
            print(f"\n {group_label.capitalize()}: {current_group}")
            print("-" * 40)

        print(f"   Candidate: {row['candidate_name']}")
        print(f"   Votes: {row['total_votes']}")
        print(f"   Percentage: {row['vote_percentage']}%\n")
