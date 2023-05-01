def check_id(CNP):
    # Check if the input is the right length
    if len(CNP) != 13:
        return {"status": False, "error": "CNP has the wrong length"}

    # Check if the first digit and determine gender
    gender_digit = int(CNP[0])

    if not (1 <= gender_digit <= 9):
        return {"status": False, "error": "First digit is wrong"}

    if gender_digit in [1, 3, 5, 7]:
        gender = "male"
    elif gender_digit in [2, 4, 6, 8]:
        gender = "female"
    else:
        gender = "foreigner"

    # Extract the year, month, and day
    year = int(CNP[1:3])
    month = int(CNP[3:5])
    day = int(CNP[5:7])

    first_digit = int(CNP[0])
    if 1 <= first_digit <= 2:
        full_year = 1900 + year
    elif 3 <= first_digit <= 4:
        full_year = 1800 + year
    elif 5 <= first_digit <= 6:
        full_year = 2000 + year
    elif 7 <= first_digit <= 9:
        full_year = 1900 + year
    else:
        return {"status": False, "error": "First digit is wrong"}

    # Check if the date is valid
    import datetime

    try:
        birth_date = datetime.date(full_year, month, day)
    except ValueError:
        return {"status": False, "error": "Birthday doesn't exist/not valid date!"}

    # Determine the month
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    month_name = month_names[month - 1]

    # Look up the place of birth in the dictionary
    birth_place = CNP[7:9]
    dictionary = {
        "Alba": "01",
        "Arad": "02",
        "Arges": "03",
        "Bacau": "04",
        "Cluj": "12",
        "Constanta": "13",
        "Hunedoara": "20",
        "Ialomita": "21",
        "Bucuresti": "40",
        "Bucuresti S.1": "41",
        "Bucuresti S.2": "42",
        "Bucuresti S.3": "43",
        "Bucuresti S.4": "44",
        "Bucuresti S.5": "45",
        "Bucuresti S.6": "46",
    }
    if birth_place not in dictionary.values():
        return {"status": False, "error": "Birth place does not exist"}
    for place, code in dictionary.items():
        if code == birth_place:
            birth_place = place
            break

    # Calculate the control digit
    secret = "279146358279"
    total = 0
    for i in range(len(CNP) - 1):
        total += int(CNP[i]) * int(secret[i])

    if total % 11 == 10:
        control = 1
    else:
        control = total % 11

    if control != int(CNP[-1]):
        return {"status": False, "error": "Control digit is wrong"}

    # Return the results as a dictionary
    return {
        "status": True,
        "gender": gender,
        "year": full_year,
        "month": month_name,
        "day": day,
        "birth_date": birth_date,
        "birth_place": birth_place,
    }


# Print result
cnp = input("Scrie CNP : ")
result = check_id(cnp)
if result["status"]:
    print(f"Gender: {result['gender']}")
    print(f"Birth date: {result['birth_date']}")
    print(f"Birth place: {result['birth_place']}")
    print(f"CNP is valid")
else:
    print(result["error"])
