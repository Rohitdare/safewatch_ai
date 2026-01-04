def compute_severity(
    detection_count: int,
    avg_confidence: float
):
    """
    Decide severity based on persistence and confidence.
    """

    if detection_count >= 4 and avg_confidence >= 0.6:
        return "HIGH"

    if detection_count >= 3:
        return "MEDIUM"

    return "LOW"
