import csv
all_the_female_players = set()
all_the_male_players = set()
all_countries = set()
class OlympicMedalData:
    def read_csv(self,file_path):
        data = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:
                parts = line.strip().split(',')
                medal_entry = {
                "year": int(parts[0]),
                "location": parts[1],
                "gold": {"name": parts[2], "country": parts[3]},
                "silver": {"name": parts[4], "country": parts[5]},
                "bronze": {"name": parts[6], "country": parts[7]}
            }
                data.append(medal_entry)
        return data
    def read_csv_doubles(self, file_path):
        data = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:
                parts = line.split(',')
                for part in range(len(parts)):
                    parts[part] = parts[part].replace('"',"")
                medal_entry = {
                    "year": int(parts[0]),
                    "location": parts[1],
                    "gold": {"name": [parts[2], parts[3]], "country": parts[4]},
                    "silver": {"name": [parts[5], parts[6]], "country": parts[7]},
                    "bronze": {"name": [parts[8], parts[9]], "country": parts[10]}
                    }
                data.append(medal_entry)
        return data
olympic_data = OlympicMedalData()
womens_singles_olympic_medals = olympic_data.read_csv('E:/MCA/MCA 3rd/python/ca/womens_singles_olympic_medals.csv')
mens_singles_olympic_medals = olympic_data.read_csv('E:/MCA/MCA 3rd/python/ca/mens_singles_olympic_medals.csv')
mens_doubles_olympic_medals = olympic_data.read_csv_doubles('E:/MCA/MCA 3rd/python/ca/mens_doubles_olympic_medals.csv')
womens_doubles_olympic_medals = olympic_data.read_csv_doubles('E:/MCA/MCA 3rd/python/ca/womens_doubles_olympic_medals.csv')
mixed_doubles_olympic_medals = olympic_data.read_csv_doubles('E:/MCA/MCA 3rd/python/ca/doubles_doubles_olympic_medals.csv')
def create_list():
    for entry in womens_singles_olympic_medals:
        all_the_female_players.add(entry["gold"]["name"])
        all_the_female_players.add(entry["silver"]["name"])
        all_the_female_players.add(entry["bronze"]["name"])
    for entry in womens_doubles_olympic_medals:
        all_the_female_players.add(entry["gold"]["name"][0])
        all_the_female_players.add(entry["gold"]["name"][1])
        all_the_female_players.add(entry["silver"]["name"][0])
        all_the_female_players.add(entry["silver"]["name"][1])
        all_the_female_players.add(entry["bronze"]["name"][0])
        all_the_female_players.add(entry["bronze"]["name"][1])
    for entry in mixed_doubles_olympic_medals:
        all_the_female_players.add(entry["gold"]["name"][1])
        all_the_female_players.add(entry["silver"]["name"][1])
        all_the_female_players.add(entry["bronze"]["name"][1])
    for entry in mens_singles_olympic_medals:
        all_the_male_players.add(entry["gold"]["name"])
        all_the_male_players.add(entry["silver"]["name"])
        all_the_male_players.add(entry["bronze"]["name"])
    for entry in mens_doubles_olympic_medals:
        all_the_male_players.add(entry["gold"]["name"][0])
        all_the_male_players.add(entry["gold"]["name"][1])
        all_the_male_players.add(entry["silver"]["name"][0])
        all_the_male_players.add(entry["silver"]["name"][1])
        all_the_male_players.add(entry["bronze"]["name"][0])
        all_the_male_players.add(entry["bronze"]["name"][1])
    for entry in mixed_doubles_olympic_medals:
        all_the_male_players.add(entry["gold"]["name"][0])
        all_the_male_players.add(entry["silver"]["name"][0])
        all_the_male_players.add(entry["bronze"]["name"][0])
    for entry in womens_singles_olympic_medals:
        all_countries.add(entry["gold"]["country"])
        all_countries.add(entry["silver"]["country"])
        all_countries.add(entry["bronze"]["country"])
    for entry in mens_singles_olympic_medals:
        all_countries.add(entry["gold"]["country"])
        all_countries.add(entry["silver"]["country"])
        all_countries.add(entry["bronze"]["country"])
    for entry in womens_doubles_olympic_medals:
        all_countries.add(entry["gold"]["country"])
        all_countries.add(entry["silver"]["country"])
        all_countries.add(entry["bronze"]["country"])
    for entry in mens_doubles_olympic_medals:
        all_countries.add(entry["gold"]["country"])
        all_countries.add(entry["silver"]["country"])
        all_countries.add(entry["bronze"]["country"])
    for entry in mixed_doubles_olympic_medals:
        all_countries.add(entry["gold"]["country"])
        all_countries.add(entry["silver"]["country"])
        all_countries.add(entry["bronze"]["country"])

def print_results_by_game():
    print("Enter the name of the game you want to the result of")
    print('''1. Men's Singles\n2. Women's Singles\n3. Men's Doubles\n4. Women's Doubles\n5. Mixed Doubles\n6. Go back\n7. Exit''')
    game = int(input())
    if game == 1:
        for years in mens_singles_olympic_medals:
            print(f"Year  -> {years['year']}  Location  -> {years['location']}")
            print(f"                    Name                   Winning Country")
            print(f"Gold:     {years['gold']['name']:^25}  {years['gold']['country']:^25}")
            print(f"Silver:   {years['silver']['name']:^25}  {years['silver']['country']:^25}")
            print(f"Bronze:   {years['bronze']['name']:^25}  {years['bronze']['country']:^25}\n")
    elif game == 2:
        for years in womens_singles_olympic_medals:
            print(f"Year  -> {years['year']}  Location  -> {years['location']}")
            print(f"                    Name                   Winning Country")
            print(f"Gold:     {years['gold']['name']:^25}  {years['gold']['country']:^25}")
            print(f"Silver:   {years['silver']['name']:^25}  {years['silver']['country']:^25}")
            print(f"Bronze:   {years['bronze']['name']:^25}  {years['bronze']['country']:^25}\n")
    elif game == 3:
        for years in mens_doubles_olympic_medals:
            print(f"Year  -> {years['year']}  Location  -> {years['location']}")
            print(f"                    Name                   Winning Country")
            print(f"Gold:     {years['gold']['name'][0]:^25}  {years['gold']['country']:^25}")
            print(f"          {years['gold']['name'][1]:^25}  {years['gold']['country']:^25}")
            print(f"Silver:   {years['silver']['name'][0]:^25}  {years['silver']['country']:^25}")
            print(f"          {years['silver']['name'][1]:^25}  {years['silver']['country']:^25}")
            print(f"Bronze:   {years['bronze']['name'][0]:^25}  {years['bronze']['country']:^25}")
            print(f"          {years['bronze']['name'][1]:^25}  {years['bronze']['country']:^25}\n")
    elif game == 4:
        for years in mens_doubles_olympic_medals:
            print(f"Year  -> {years['year']}  Location  -> {years['location']}")
            print(f"                    Name                   Winning Country")
            print(f"Gold:     {years['gold']['name'][0]:^25}  {years['gold']['country']:^25}")
            print(f"          {years['gold']['name'][1]:^25}  {years['gold']['country']:^25}")
            print(f"Silver:   {years['silver']['name'][0]:^25}  {years['silver']['country']:^25}")
            print(f"          {years['silver']['name'][1]:^25}  {years['silver']['country']:^25}")
            print(f"Bronze:   {years['bronze']['name'][0]:^25}  {years['bronze']['country']:^25}")
            print(f"          {years['bronze']['name'][1]:^25}  {years['bronze']['country']:^25}\n")
    elif game == 5:
        for years in mixed_doubles_olympic_medals:
            print(f"Year  -> {years['year']}  Location  -> {years['location']}")
            print(f"                    Name                   Winning Country")
            print(f"Gold:     {years['gold']['name'][0]:^25}  {years['gold']['country']:^25}")
            print(f"          {years['gold']['name'][1]:^25}  {years['gold']['country']:^25}")
            print(f"Silver:   {years['silver']['name'][0]:^25}  {years['silver']['country']:^25}")
            print(f"          {years['silver']['name'][1]:^25}  {years['silver']['country']:^25}")
            print(f"Bronze:   {years['bronze']['name'][0]:^25}  {years['bronze']['country']:^25}")
            print(f"          {years['bronze']['name'][1]:^25}  {years['bronze']['country']:^25}\n")
    elif game == 6:
        fun1()
    elif game == 7: 
        exit()
    fun1()
def check_medals_by_location(location, *args):
    gold = 0
    silver = 0
    bronze = 0
    for choices in args:
        for years in choices:
            if years['gold']['country'] == location:
                gold = gold + 1
            if years['silver']['country'] == location:
                silver = silver + 1
            if years['bronze']['country'] == location:
                bronze = bronze + 1
    return(gold,silver,bronze)
def check_by_location():
    gold = 0
    silver = 0
    bronze = 0
    print('''Select select the type of game you want to check:\n1. Men's Single\n2. Women's Single\n3. Men's Double\n4. Women's Double\n5. Mixed Doubles\n6. All\n7. GO back\n8. Exit''')
    choice2 = int(input())
    print('''Enter the name of the country you want to check''')
    i = 1
    for country in all_countries:
        print(i, '. ',country)
        i = i + 1
    location = input()
    if choice2 == 1:
        list_of_medals = check_medals_by_location(location, mens_singles_olympic_medals)
    elif choice2 == 2:
        list_of_medals = check_medals_by_location(location, womens_singles_olympic_medals)
    elif choice2 == 3:
        list_of_medals = check_medals_by_location(location,mens_doubles_olympic_medals)
    elif choice2 == 4:
        list_of_medals = check_medals_by_location(location,womens_doubles_olympic_medals)
    elif choice2 == 5:
        list_of_medals = check_medals_by_location(location,mixed_doubles_olympic_medals)
    elif choice2 == 6:
        list_of_medals = check_medals_by_location(location,mens_singles_olympic_medals , womens_singles_olympic_medals ,
                                               mens_doubles_olympic_medals , womens_doubles_olympic_medals ,
                                               mixed_doubles_olympic_medals)
    elif choice2 == 7:
        fun1()
    elif choice2 == 8:
        exit()
    print(f"Country   ->    {location}")
    print("Total number of each type of medal: ")
    print(f"  Gold       Silver       Bronze  ")
    print(f"{list_of_medals[0]:^10} {list_of_medals[1]:^10} {list_of_medals[2]:^14}")
    fun1()
def check_medals_by_name(choice2, choice3, name):
    gold = 0
    silver = 0
    bronze = 0
    if choice2 == 1:
        if choice3 == 1:
            for years in mens_singles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
        elif choice3 == 2:
            for years in mens_doubles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
        elif choice3 == 3:
            for years in mixed_doubles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
        elif choice3 == 4:
            for years in mens_singles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
            for years in mens_doubles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
            for years in mixed_doubles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
    elif choice2 == 2:
        if choice3 == 1:
            for years in womens_singles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
        elif choice3 == 2:
            for years in womens_doubles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
        elif choice3 == 3:
            for years in mixed_doubles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
        elif choice3 == 4:
            for years in womens_singles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
            for years in womens_doubles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
            for years in mixed_doubles_olympic_medals:
                if years['gold']['name'] == name:
                    gold = gold + 1
                if years['silver']['name'] == name:
                    silver = silver + 1
                if years['bronze']['name'] == name:
                    bronze = bronze + 1
    return (gold, silver, bronze)
def check_by_name():
    print('''Enter the gender of the player:\n1. Male\n2. Female\n3. Go back\n4. Exit''')
    choice2 = int(input())
    if choice2 == 1:
        print('''Enter the name of the player''')
        i = 1
        for player in all_the_male_players:
            print(i, '. ',player)
            i = i + 1
        name = input()
        print('''Please select the type of the game:\n1. Men's Single\n2. Men's Double\n3. Mixed Double\n4. All''')
        choice3 = int(input())
        list_of_medals = check_medals_by_name(choice2, choice3, name)
        print(f"Name of the player  ->  {name}")
        print("Total number medals by the player: ")
        print(f"  Gold       Silver       Bronze  ")
        print(f"{list_of_medals[0]:^10} {list_of_medals[1]:^10} {list_of_medals[2]:^14}")
        fun1()
    elif choice2 == 2:
        print('''Enter the name of the player''')
        i = 1
        for player in all_the_female_players:
            print(i, '. ',player)
            i = i + 1
        name = input()
        print('''Please select the type of the game:\n1. Women's Single\n2. Women's Double\n3. Mixed Double\n4. All''')
        choice3 = int(input())
        list_of_medals = check_medals_by_name(choice2, choice3, name)
        print(f"Name of the player  ->  {name}")
        print("Total number medals by the player: ")
        print(f"  Gold       Silver       Bronze  ")
        print(f"{list_of_medals[0]:^10} {list_of_medals[1]:^10} {list_of_medals[2]:^14}")
        fun1()
    elif choice2 == 3:
        fun1()
    elif choice2 == 4:
        exit()
def check_medals_by_year(year, *args):
    print(f"Year -> {year}")
    for choices in args:
        if (choices == womens_singles_olympic_medals):
            print("Women's single game information")
            for years in choices:
                if years['year'] == year:
                    print(f"                 Player name                 Player's country")
                    print(f"Gold:     {years['gold']['name']:^25}   {years['gold']['country']:^25}")
                    print(f"Silver:   {years['silver']['name']:^25}   {years['silver']['country']:^25}")
                    print(f"Bronze:   {years['bronze']['name']:^25}   {years['bronze']['country']:^25}\n")
        elif (choices == womens_doubles_olympic_medals):
            print("Women's double game information")
            for years in choices:
                if years['year'] == year:
                    print(f"                 Player name                 Player's country")
                    print(f"Gold:     {years['gold']['name'][0]:^25}   {years['gold']['country']:^25}")
                    print(f"          {years['gold']['name'][1]:^25}   {years['gold']['country']:^25}")
                    print(f"Silver:   {years['silver']['name'][0]:^25}   {years['silver']['country']:^25}")
                    print(f"          {years['silver']['name'][1]:^25}   {years['silver']['country']:^25}")
                    print(f"Bronze:   {years['bronze']['name'][0]:^25}   {years['bronze']['country']:^25}")
                    print(f"          {years['bronze']['name'][1]:^25}   {years['bronze']['country']:^25}\n")
        elif (choices == mens_singles_olympic_medals):
            print("Men's single game information")
            for years in choices:
                if years['year'] == year:
                    print(f"                 Player name                 Player's country")
                    print(f"Gold:     {years['gold']['name']:^25}   {years['gold']['country']:^25}")
                    print(f"Silver:   {years['silver']['name']:^25}   {years['silver']['country']:^25}")
                    print(f"Bronze:   {years['bronze']['name']:^25}   {years['bronze']['country']:^25}\n")
        elif (choices == mens_doubles_olympic_medals):
            print("Men's double game information")
            for years in choices:
                if years['year'] ==year:
                    print(f"                 Player name                 Player's country")
                    print(f"Gold:     {years['gold']['name'][0]:^25}   {years['gold']['country']:^25}")
                    print(f"          {years['gold']['name'][1]:^25}   {years['gold']['country']:^25}")
                    print(f"Silver:   {years['silver']['name'][0]:^25}   {years['silver']['country']:^25}")
                    print(f"          {years['silver']['name'][1]:^25}   {years['silver']['country']:^25}")
                    print(f"Bronze:   {years['bronze']['name'][0]:^25}   {years['bronze']['country']:^25}")
                    print(f"          {years['bronze']['name'][1]:^25}   {years['bronze']['country']:^25}\n")
        elif (choices == mixed_doubles_olympic_medals):
            print("Mixed double game information")
            for years in choices:
                if years['year'] == year:
                    print(f"                 Player name                 Player's country")
                    print(f"Gold:     {years['gold']['name'][0]:^25}   {years['gold']['country']:^25}")
                    print(f"          {years['gold']['name'][1]:^25}   {years['gold']['country']:^25}")
                    print(f"Silver:   {years['silver']['name'][0]:^25}   {years['silver']['country']:^25}")
                    print(f"          {years['silver']['name'][1]:^25}   {years['silver']['country']:^25}")
                    print(f"Bronze:   {years['bronze']['name'][0]:^25}   {years['bronze']['country']:^25}")
                    print(f"          {years['bronze']['name'][0]:^25}   {years['bronze']['country']:^25}\n")
def check_by_year():
    print('''Enter the year of the Olympics you want to check the medals record''')
    year = int(input())
    print('''Select the type of game you want to check:\n1. Men's Single\n2. Women's Single\n3. Men's Double\n4. Women's Double\n5. Mixed Doubles\n6. All\n7. Go back\n8. Exit''')
    choice2 = int(input())
    if (choice2 == 1):
        check_medals_by_year(year, mens_singles_olympic_medals)
        fun1()
    elif (choice2 == 2):
        check_medals_by_year(year, womens_singles_olympic_medals)
        fun1()
    elif (choice2 == 3):
        check_medals_by_year(year, mens_doubles_olympic_medals)
        fun1()
    elif (choice2 == 4):
        check_medals_by_year(year, womens_doubles_olympic_medals)
        fun1()
    elif (choice2 == 5):
        check_medals_by_year(year, mixed_doubles_olympic_medals)
        fun1()
    elif choice2 == 6:
        check_medals_by_year(year, mens_singles_olympic_medals , womens_singles_olympic_medals ,
                                               mens_doubles_olympic_medals , womens_doubles_olympic_medals ,
                                               mixed_doubles_olympic_medals)
        fun1()
    elif choice2 == 7:
        fun1()
    elif choice2 == 8:
        exit()
def exit():
    print("--------------Thanku for using The Dashboard--------------")
create_list()
print('''--------------------Welcome to the Olympic Badminton Medalists Dashboard--------------------''')
def fun1():
    print('''Select one of the following''')
    print('''1. Info about medals by the type of game\n2. Info about medals by name of the player \n3. Info about medals by year\n4. Info on the basis of the winning country\n5. Exit''')
    choicee = int(input())
    if (choicee == 1):
        print_results_by_game()
    elif (choicee == 2):
        check_by_name()
    elif (choicee == 3):
        check_by_year()
    elif (choicee == 4):
        check_by_location()
    else:
        exit()
fun1()