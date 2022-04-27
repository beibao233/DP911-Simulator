from DP911.Exceptions.Errors import OutOfRangeError


def set_range(rmin: int, data: int, rmax: int):
    if not (rmin <= data) and (data <= rmax):
        raise OutOfRangeError(rmin, rmax)
    else:
        return True
