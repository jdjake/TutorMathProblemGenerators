import random

def get_income_tax(income, tax_bracket):
    total_tax = 0

    i = 1
    while income > tax_bracket[i][1]:
        total_tax += tax_bracket[i][0]*tax_bracket[i][1]
        i += 1

    total_tax += (income - tax_bracket[i-1][1])*tax_bracket[i][0]
    return total_tax

def obtain_answer(income_time, wage, deduction, EI_rate, CPP_rate, fed_tax, provincial_tax):
    gross_income = income_time*wage
    taxable_income = max(gross_income - deduction,0)
    EI_deduction = EI_rate*gross_income
    CPP_deduction = CPP_rate*gross_income

    fed_deduction = get_income_tax(taxable_income, fed_tax)
    provin_deduction = get_income_tax(taxable_income, provincial_tax)

    net_income = gross_income - EI_deduction - CPP_deduction - fed_deduction - provin_deduction
    return net_income / income_time

def gen_random_bracket(low_or_high):
    if low_or_high == "low":
        percentages = [0,0.01,0.05,0.1,0.15]
    else:
        percentages = [0,0.05,0.1,0.2,0.5]

    bracket = [
        [percentages[0], 1000*random.randint(0,5)],
        [percentages[1], 10000 + random.randint(-2,2)*1000],
        [percentages[2], 20000 + random.randint(-5,10)*1000],
        [percentages[3], 40000 + random.randint(-1,3)*5000],
        [percentages[4],300000]
    ]

    return bracket

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
businesses = (
    "Peanut Farm",
    "Clown College",
    "Coffee Flavored Toothpaste Factory",
    "Meme Factory",
    "4D Printing Factory",
    "Llama farm",
    "Spooky Ant Farm")
income_times = (
    ["weekly", 52],
    ["daily", 365],
    ["semi-Monthly", 24],
    ["monthly", 12],
    ["annually",1])

name = random.choice(names)
location = random.choice(locations)
business = random.choice(businesses)
income_time = random.choice(income_times)

annual_income = random.randint(1,10) * 22776
income = annual_income / income_time[1]
tax_exemption = annual_income / random.randint(5,10)
EI_rate = 0.01 + random.randint(1,10) * 1.0 / 2000
CPP_rate = 0.02 + random.randint(1,20) * 1.0 / 2000

fed_tax = gen_random_bracket("low")
provincial_tax = gen_random_bracket("high")

print("""
{fname} works at a {fbusiness} in {flocation}. They have {fexemption}
dollars worth of tax-exempt expenses annually, and get paid {fincome} dollars
{fincome_time}. Calculate the net income each pay period based on the
following tax information:

In {flocation}, citizens must pay:
    {fEI} percent of their gross income on EI
    {fCPP} percent of their gross income on CPP

In addition, citizen must pay federal and provincial tax
based on the following tax brackets:
    Federal Tax:
        {ffedper1} percent of taxable income above {ffedmin0} up to a max of {ffedmin1}
        {ffedper2} percent of taxable income between {ffedmin1} and {ffedmin2}
        {ffedper3} percent of taxable income between {ffedmin2} and {ffedmin3}
        {ffedper4} percent of taxable income between {ffedmin3} and {ffedmin4}
    Provincial Tax:
        {fprovper1} percent of taxable income above {fprovmin0} up to a max of {fprovmin1}
        {fprovper2} percent of taxable income between {fprovmin1} and {fprovmin2}
        {fprovper3} percent of taxable income between {fprovmin2} and {fprovmin3}
        {fprovper4} percent of taxable income between {fprovmin3} and {fprovmin4}""".format(
        fname=name,
        fbusiness=business,
        flocation=location,
        fexemption=tax_exemption,
        fincome=income,
        fincome_time=income_time[0],
        fEI = EI_rate*100,
        fCPP = CPP_rate*100,
        ffedper1 = int(fed_tax[1][0]*100),
        ffedper2 = int(fed_tax[2][0]*100),
        ffedper3 = int(fed_tax[3][0]*100),
        ffedper4 = int(fed_tax[4][0]*100),
        ffedmin0 = fed_tax[0][1],
        ffedmin1 = fed_tax[1][1],
        ffedmin2 = fed_tax[2][1],
        ffedmin3 = fed_tax[3][1],
        ffedmin4 = fed_tax[4][1],
        fprovper1 = int(provincial_tax[1][0]*100),
        fprovper2 = int(provincial_tax[2][0]*100),
        fprovper3 = int(provincial_tax[3][0]*100),
        fprovper4 = int(provincial_tax[4][0]*100),
        fprovmin0 = provincial_tax[0][1],
        fprovmin1 = provincial_tax[1][1],
        fprovmin2 = provincial_tax[2][1],
        fprovmin3 = provincial_tax[3][1],
        fprovmin4 = provincial_tax[4][1]
))

raw_input("Press ENTER to reveal answer:")

answer = obtain_answer(income_time[1], income, tax_exemption, EI_rate, CPP_rate, fed_tax, provincial_tax)

print("{fname} would earn {fanswer:.2f} dollars {fincome_time}".format(fname = name, fanswer = answer, fincome_time = income_time[0]))