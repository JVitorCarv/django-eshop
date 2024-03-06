def parse_posint(value, default=1, max_value=100) -> int:
    try:
        value = int(value)
        if value <= 0:
            return default
        return min(value, max_value)
    except ValueError:
        return default
