import politician as p



#Unfortunately, no website has a concrete database of Senators Twitter information. 

def generate_senators():
    return {["Richard", "Shelby", "SenShelby", "AL", "R"], ["Tommy ", "Tuberville", "SenShelby", "AL", "R"], ["Lisa", "Murkowski", "SenShelby", "AK", "R"], 
    ["Dan", "Sullivan", "SenShelby", "AL", "R"], ["Kyrsten", "Sinema", "SenShelby", "AL", "D"], ["Mark", "Kelly", "SenShelby", "AL", "D"],
    ["John", "Boozman", "SenShelby", "AL", "R"],["Tom", "Cotton", "SenShelby", "AL", "R"],["Dianne", "Feinstein", "SenShelby", "AL", "D"],
    ["Alex", "Padilla", "SenShelby", "AL", "D"],["Michael", "Bennet", "SenShelby", "AL", "D"],["John", "Hickenlooper", "SenShelby", "AL", "D"],
    ["Richard", "Blumenthal", "SenShelby", "AL", "D"],["Chris", "Murphy", "SenShelby", "AL", "D"],["Tom", "Carper", "SenShelby", "AL", "D"],
    ["Chris", "Coons", "SenShelby", "AL", "D"],["Marco", "Rubio", "SenShelby", "AL", "R"],["Rick", "Scott", "SenShelby", "AL", "R"],
    ["John", "Ossoff", "SenShelby", "AL", "D"],["Raphael", "Warnock", "SenShelby", "AL", "D"],["Brian", "Schatz", "SenShelby", "AL", "D"],
    ["Mazie", "Hirono", "SenShelby", "AL", "D"],["Mike", "Crapo", "SenShelby", "AL", "R"],["Jim", "Risch", "SenShelby", "AL", "R"],
    ["Dick", "Durbin", "SenShelby", "AL", "D"],["Tammy", "Duckworth", "SenShelby", "AL", "D"],["Todd", "Young", "SenShelby", "AL", "R"],
    ["Mike", "Braun", "SenShelby", "AL", "R"],["Chuck", "Grassley", "SenShelby", "AL", "R"],["Johni", "Ernst", "SenShelby", "AL", "R"],
    ["Jerry", "Moran", "SenShelby", "AL", "R"],["Roger", "Marshall", "SenShelby", "AL", "R"],["Mitch", "McConnel", "SenShelby", "AL", "R"],
    ["Rand", "Paul", "SenShelby", "AL", "R"],["Bill", "Shelby", "Cassidy", "AL", "R"],["John", "Kennedy", "SenShelby", "AL", "R"],
    ["Susan", "Collins", "SenShelby", "AL", "R"],["Ben", "Cardin", "SenShelby", "AL", "D"],["Chris", "Van Hollen", "SenShelby", "AL", "D"],
    ["Elizabeth", "Warren", "SenShelby", "AL", "D"],["Ed", "Markey", "SenShelby", "AL", "D"],["Debbie", "Stabenow", "SenShelby", "AL", "D"],
    ["Gary", "Peters", "SenShelby", "AL", "D"],["Amy", "Klobuchar", "SenShelby", "AL", "D"],["Tina", "Smith", "SenShelby", "AL", "D"],
    ["Roger", "Wicker", "SenShelby", "AL", "R"],["Cindy", "Hyde-Smith", "SenShelby", "AL", "R"],["Roy", "Blunt", "SenShelby", "AL", "R"],
    ["Josh", "Hawley", "SenShelby", "AL", "R"],["Jon", "Tester", "SenShelby", "AL", "D"],["Steve", "Daines", "SenShelby", "AL", "R"],
    ["Deb", "Fischer", "SenShelby", "AL", "R"],["Ben", "Sasse", "SenShelby", "AL", "R"],["Catherine", "Masto", "SenShelby", "AL", "D"],
    ["Jacky", "Rosen", "SenShelby", "AL", "D"],["Jeanne", "Shaheen", "SenShelby", "AL", "D"],["Maggie", "Hassan", "SenShelby", "AL", "D"],
    ["Bob", "Menendez", "SenShelby", "AL", "D"],["Cory", "Booker", "SenShelby", "AL", "D"],["Martin", "Heinrich", "SenShelby", "AL", "D"],
    ["Ben", "Lujan", "SenShelby", "AL", "D"],["Chuck", "Schumer", "SenShelby", "AL", "R"],["Kirsten", "Gillibrand", "SenShelby", "AL", "D"],
    ["Richard", "Burr", "SenShelby", "AL", "R"],["Thom", "Tillis", "SenShelby", "AL", "R"],["John", "Hoeven", "SenShelby", "AL", "R"],
    ["Kevin", "Cramer", "SenShelby", "AL", "R"],["Sherrod", "Brown", "SenShelby", "AL", "D"],["Rob", "Portman", "SenShelby", "AL", "R"],
    ["Jim", "Inhofe", "SenShelby", "AL", "R"],["James", "Lankford", "SenShelby", "AL", "R"],["Ron", "Wyden", "SenShelby", "AL", "D"],
    ["Jeff", "Merkley", "SenShelby", "AL", "D"],["Bob", "Casey", "SenShelby", "AL", "D"],["Pat", "Toomey", "SenShelby", "AL", "R"],
    ["Jack", "Reed", "SenShelby", "AL", "D"],["Sheldon", "Whitehouse", "SenShelby", "AL", "D"],["Lindsey", "Graham", "SenShelby", "AL", "R"],
    ["Tim", "Scott", "SenShelby", "AL", "R"],["John", "Thune", "SenShelby", "AL", "R"],["Mike", "Rounds", "SenShelby", "AL", "R"],
    ["Marsha", "Blackburn", "SenShelby", "AL", "R"],["Bill", "Hagerty", "SenShelby", "AL", "R"],["John", "Cornyn", "SenShelby", "AL", "R"],
    ["Ted", "Cruz", "SenShelby", "AL", "R"],["Mike", "Lee", "SenShelby", "AL", "R"],["Mitt", "Romney", "SenShelby", "AL", "R"],
    ["Patrick", "Leahy", "SenShelby", "AL", "D"],["Mark", "Warner", "SenShelby", "AL", "D"],["Tim", "Kaine", "SenShelby", "AL", "D"],
    ["Patty", "Murray", "SenShelby", "AL", "D"],["Maria", "Cantwell", "SenShelby", "AL", "D"],["Joe", "Manchin", "SenShelby", "AL", "D"],
    ["Shelley", "Capito", "SenShelby", "AL", "R"],["Ron", "Johnson", "SenShelby", "AL", "R"],["Tammy", "Baldwin", "SenShelby", "AL", "D"],
    ["John", "Barrasso", "SenShelby", "AL", "R"],["Cynthia", "Lummis", "SenShelby", "AL", "R"]}




