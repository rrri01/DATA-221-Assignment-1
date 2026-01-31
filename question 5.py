def circle_area_coverage(radius_of_circle_1, radius_of_circle_2):
    # i am choosing to not accept 0 as a value because that means there is no circle
    if radius_of_circle_1 <= 0 or radius_of_circle_1 % 1 != 0: # checks if it is negative or 0
        print("The radius must be a positive integer.")
        return None # exits out of the function
    if radius_of_circle_2 <= 0 or radius_of_circle_2 % 1 != 0: # checks if it is negative or 0
        print("The radius must be a positive integer.")
        return None # exits out of the function

    area_of_circle_1 = radius_of_circle_1**2 * 3.14
    area_of_circle_2 = radius_of_circle_2**2 * 3.14

    if area_of_circle_1 > area_of_circle_2:
        percentage_covered = (area_of_circle_2/area_of_circle_1)*100
    if area_of_circle_2 > area_of_circle_1:
        percentage_covered = (area_of_circle_1/area_of_circle_2)*100

    if area_of_circle_1 == area_of_circle_2:
        percentage_covered = 100
    return(f"{percentage_covered}%")

# call the function and print the result, i just used some random test numbers
print(circle_area_coverage(2, 1))

