def is_year_leap(year: int) -> bool:
    if year % 4:
        return False
    else:
        return True