def threat_level(prob):

    if prob < 0.3:
        return "LOW"

    elif prob < 0.6:
        return "MEDIUM"

    elif prob < 0.85:
        return "HIGH"

    else:
        return "CRITICAL"