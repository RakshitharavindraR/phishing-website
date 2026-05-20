
def extract_features(url):
    features = {
        "url_length": len(url),
        "contains_https": 1 if "https" in url else 0,
        "contains_at": 1 if "@" in url else 0
    }
    return features
