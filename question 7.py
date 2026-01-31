#NOT DONE YET

def time_conversion(seconds):
    if seconds < 0 :
        print("Please enter a positive number.")
        return None
    hours = seconds//3600
    minutes = (seconds%3600)//60
    seconds_left = (seconds%3600)%60

    am_or_pm = hours//12
    # this variable shows how many times it's been 12 hrs to help caluclate if it's  AM or PM

    time_of_day = 0

    if am_or_pm % 2 == 0:
        time_of_day = "AM"
    if am_or_pm % 2 == 1:
        time_of_day = "PM"

    return f"{hours} {minutes} {seconds_left} {time_of_day}"
    print(hours, minutes, seconds_left, time_of_day)

# call and print the function, i just put a random number
print(time_conversion(19067)) # expected output: 5 17 47 AM
