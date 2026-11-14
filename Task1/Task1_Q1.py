# Q1 - Electricity Subsidy Eligibility

def subsidy_separate(units, ration_card, age_over_80):
    results = []
    if units <= 100:
        results.append("Full subsidy")
    if 101 <= units <= 200 and ration_card:
        results.append("Partial subsidy")
    if units > 200 and age_over_80:
        results.append("Subsidy under senior-citizen exception")
    if not results:
        results.append("No subsidy")
    return results

def subsidy_elif(units, ration_card, age_over_80):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        return "No subsidy"
    else:
        if age_over_80:
            return "Subsidy under senior-citizen exception"
        return "No subsidy"

# Eight households, including the boundaries 100, 101 and 200.
households = [
    (80, False, False), (100, True, False),
    (101, True, False), (101, False, False),
    (150, False, False), (200, True, False),
    (201, False, False), (250, False, True)
]
for h in households:
    print(h, "=>", subsidy_separate(*h), "|", subsidy_elif(*h))
