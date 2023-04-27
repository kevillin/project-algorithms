def study_schedule(permanence_period, target_time):
    counter = 0
    if not target_time:
        return None

    for enter, exit in permanence_period:
        if not enter or not exit or type(enter) == str or type(exit) == str:
            return None
        elif target_time >= enter and target_time <= exit:
            counter += 1
    return counter
