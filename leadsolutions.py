input_data = {
    "company_size": "1000+ employees",
    "budget": "More than $100,000",
    "industry": "Healthcare",
    "urgency": "Immediate"
}

score_map = {
    "company_size": {
        "1-50 employees": 10,
        "51-200 employees": 20,
        "201-1000 employees": 30,
        "1000+ employees": 40
    },
    "budget": {
        "Less than $10,000": 10,
        "$10,000 - $50,000": 20,
        "$50,001 - $100,000": 30,
        "More than $100,000": 40
    },
    "industry": {
        "Technology": 20,
        "Finance": 15,
        "Healthcare": 25,
        "Retail": 10,
        "Other": 5
    },
    "urgency": {
        "Immediate": 40,
        "Short-term": 30,
        "Medium-term": 20,
        "Long-term": 10
    }
}

lead_score = sum(score_map[key][value] for key, value in input_data.items())
return {"lead_score": lead_score}
