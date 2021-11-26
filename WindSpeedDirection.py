def wind_direction_degrees(u, v):
    radians = np.arctan2(u, v)
    degrees = radians/(2*np.pi)*360) - 180
    if degrees < 0: return degrees + 360
    else: return degrees

def wind_speed(u, v):
    return np.sqrt((u**2) + (v**2))
