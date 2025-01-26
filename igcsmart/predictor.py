def predict(mock:str, study_hours:int, subject_interest:int, practice_paper_avg:str):
    # Define both grading systems
    brit_system = [str(i) for i in range(1, 10)]
    print(brit_system)
    letter_system = ["G", "F", "E", "D", "C", "B", "A", "A*"]

    system_used = 0
    # When 0 it is the brit system, when 1 it is the letter system

    # Declare Values For Later
    mock_val = None
    pp_val = None
    study_hours_var = None

    priority = [4, 2, 1, 3]
    ratio = [6, 1.5, 1, 1.5]

    result = []


    # Check which system is used, and assign values
    if mock:
        if mock in letter_system:
            mock_val = letter_system.index(mock)
            system_used = 1
        elif mock in brit_system: mock_val = brit_system.index(mock)
        else: return "ERROR: Invalid Input"

    if practice_paper_avg:
        if practice_paper_avg in letter_system: pp_val = letter_system.index(practice_paper_avg)
        elif practice_paper_avg in brit_system: pp_val = brit_system.index(practice_paper_avg)
        else: return "ERROR: Invalid Input"

    # Convert study hours into a numeric value

    if study_hours is not None:
        study_hours_var = study_hours

    if mock_val:
        result.append(mock_val*ratio[0])
    else:
        return "ERROR: Invalid Input"

    print(study_hours_var)
    if study_hours_var or study_hours_var == 0:
        result.append((study_hours_var/0.875)*ratio[1])
    else:
        return "ERROR: Invalid Input"


    if subject_interest:
        result.append(subject_interest*ratio[2])
    else:
        return "ERROR: Invalid Input"

    if pp_val is not None:
        result.append(subject_interest*ratio[3])
    else:
        return "ERROR: Invalid Input"

    # Calculate output + divide by accuracy threshold (2)

    total = sum(result)/len(result)/2
    try:
        return "Predicted Grade: " + str(brit_system[round(total) - 1]) + "/" + str(letter_system[round(total) - 1])
    except IndexError:
        return "Predicted Grade: 9/A*"


