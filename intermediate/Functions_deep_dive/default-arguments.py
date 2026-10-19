def alert_threshold(failed_count, threshold=3):
    return failed_count >= threshold

alert_threshold(4)       # uses threshold=3
alert_threshold(4, 5)    # overrides to threshold=5