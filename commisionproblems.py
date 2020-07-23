import random

names = (
    "Matilda",
    "Millicent",
    "Cecil", 
    "Mortimer", 
    "Melvin",
    "Bernard", 
    "Hildegarde", 
    "Mabel", 
    "Rudolph", 
    "Humphrey", 
    "Stanley")
locations = (
    "Vancouver",
    "Wakanda", 
    "Tatooine", 
    "Antarctica", 
    "Precalculus-ville", 
    "Timbuctoo")
businesses = [
    ("Peanut Farm","Peanut"),
    ("Clown College","Clown"),
    ("Coffee Flavored Toothpaste Factory", "Roll of Toothpaste"),
    ("Meme Factory", "Meme"),
    ("4D Printing Factory", "4D Printer"),
    ("Llama farm", "Llama Milk Carton"),
    ("Spooky Ant Farm", "Ant Ghost"),
    ("Technology Factory", "Macintosh Apple Picker")]
income_times = (
    ["weekly", 52],
    ["daily", 365],
    ["semi-Monthly", 24],
    ["monthly", 12],
    ["annually",1])

name = random.choice(names)
location = random.choice(locations)
(business, item_name) = random.choice(businesses)
income_time = random.choice(income_times)

annual_income = random.randint(1,10) * 22776
income = annual_income / income_time[1]
commision_rate = random.randint(1,200)
sell1 = random.randint(1,100)
sell2 = random.randint(1,100)

income1 = income + commision_rate*sell1
income2 = income + commision_rate*sell2

print("""
{fname} works at a {fbusiness} in {flocation}. They get
paid {fincome_time}. In addition, they earn a commision each time
they sell a {fitem}. Suppose they earn {fincome1} dollars over one pay period
after selling {fsell1} {fitem}s, and {fincome2} dollars over another pay period
after selling {fsell2} {fitem}s. What is their annual gross income and how much
commision do they earn for selling each item?""".format(
        fname=name,
        fbusiness=business,
        fitem = item_name,
        flocation=location,
        fincome_time=income_time[0],
        fincome1=income1,
        fincome2=income2,
        fsell1=sell1,
        fsell2=sell2
))

raw_input("Press ENTER to reveal answer:")

answer = 100

print("{fname} earns {fanswer} dollars annually, and earns {fcommision} dollars for each item they sell".format(fname = name, fanswer = annual_income, fcommision = commision_rate))