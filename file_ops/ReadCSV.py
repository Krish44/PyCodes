import csv

with open("C:\Drives_kp\Learning\PyCodes\PracticeFiles\sampleCSV.csv") as CSVfile:
    # CSV fil has contents ex: SA, AB Devilliers, 158
    readCSV = csv.reader(CSVfile, delimiter=',')

    # Create a list for every column value
    country = []
    player = []
    score = []
    # Read through CSV file
    for rows in readCSV:
        in_country = rows[0]
        in_player = rows[1]
        in_scores = rows[2]

        # Keep appending every column value to respective list
        country.append(in_country)
        player.append(in_player)
        score.append(in_scores)
    # Print all the list details
    print("List Player :",player)
    print("List Country:",country)
    print("List Scores :",score)

    try:
        ourPlayer = input("Which player you want to check? \n")
        # Search index of key in list for case insensitive
        # Using list comprehension. Geting index and searching in the original list.
        temp_player = [x.lower() for x in player]

        pldex = temp_player.index(ourPlayer.lower())
        o_player = player[pldex]
        o_country = country[pldex]
        o_score = score[pldex]
        print('\n',o_player, 'from', o_country, 'has high score of', o_score)

    except Exception as e:
      print(e)