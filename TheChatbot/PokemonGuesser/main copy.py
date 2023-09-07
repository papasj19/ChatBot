import os
import random
from random import randint, choice
from telebot import TeleBot
import pokebase as pb
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dataclasses import dataclass


@dataclass
class User:
    def __init__(self, newname):
        self.weatherScore = 0
        self.activityScore = 0
        self.otherScore = 0
        self.indifferenceScore = 0
        self.siblings = False
        self.name = newname


starter = "Lets Get Started. \n "
beginningSequence = starter + "This is a personality test to determine the right pokemon partner for your journey."
nameSequence = ".\n We will start by imagining you could be anywhere in the world, would you enjoy a warmer climate?"

idkHowButItCoversMyAss = [
    "How good of a teacher is Conrado?",
    "How much fun will it be in Japan?",
    "How cool is the Pokemon Cafe in Tokyo?"
]

weatherQuestions = [
    "Do you enjoy the sound of thunderstorms?",
    "Is watching thunderstorms enjoyable?",
    "How would you like to go for a walk in the rain?",
    "Do you enjoy sailing?",
    "How do you feel about being on an island?",
    "How do you feel about being on the open sea?",
    "Do you have the ability to drive your vehicle under intense rain conditions?",
    "If you made plans and it begins raining, do you continue?",
    "Do you agree that you are a strong swimmer?",
    "When completely surrounded by land do you feel like you are trapped?",
    "Are you afraid of heights?",
    "When traveling do you plan heavily for the weather?"
]

activityQuestions = [
    "Would you enjoy going skydiving",
    "Do you think a phone case is helpful?",
    "How much do you like going to the mountains",
    "Would you agree that your room is dirty?",
    "Would you agree that your computer screen is dirty?",
    "How much do you enjoy physical sports?",
    "Do you consider chess to be boring?",
    "Do you consider video games to be for nerds?",
    "Do you believe that reading is waste of time",
    "Do you enjoy training for marathons?",
    "Would you like to learn a new sport?",
    "Do you mind sweating?",
    "Is weightlifting a good use of your brain exercise?"
]

personalQuestions = [
    "Do you enjoy your siblings?",
    "How do you feel about confrontation?",
    "How often do you see your family?",
    "Would you consider doing an erasmus?"
]

questions_asked_text = []
answer_text = []
scored = []

MAX_QUESTIONS = 15
MAX_WEATHER = 4
MAX_PERSONAL = 2
MAX_ACTIVITIES = 8

new_user = User(" ")
asked_weather = []
asked_personal = []
asked_activity = []

marker = False
lastQuestion = 'weather'

waterType = ["squirtle", "psyduck", "poliwag", "tentacool", "slowpoke", "seel", "shellder", "krabby", "horsea", "goldeen", "staryu", "magikarp", "lapras", "wartortle", "blastoise", "golduck", "poliwhirl", "poliwrath", "tentacruel", "slowbro", "dewgong", "cloyster", "kingler"]
fireType = ["charmander", "vulpix", "growlithe", "ponyta", "moltres", "charmeleon", "charizard", "ninetales", "arcanine", "rapidash", "magmar"]
fightType = ["mankey", "machop", "primeape", "machoke", "machamp", "hitmonlee", "hitmonchan"]
grassType = ["bulbasaur", "oddish", "bellsprout", "exeggcute", "tangela", "ivysaur", "venusaur", "gloom", "vileplume", "weepinbell", "victreebel", "exeggutor"]
psychicType = ["abra", "drowzee", "kadabra", "alakazam", "hypno", "mr-mime"]
poisonType = ["koffing", "ekans", "arbok", "weedle", "grimer", "muk"]
ghostType = ["ghastly", "haunter", "gengar"]

analyzer = SentimentIntensityAnalyzer()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot('Hidden for safety')


def determine_weather_question(iters):
    option = randint(1, len(weatherQuestions))
    if option not in asked_weather:
        asked_weather.append(option)
        return weatherQuestions[option-1]
    else:
        if iters < 15:
            return determine_weather_question(iters+1)
        else:
            saveMe = randint(1, len(idkHowButItCoversMyAss))
            return idkHowButItCoversMyAss[saveMe-1]


def determine_activity_question(iters):
    option = randint(1, len(activityQuestions))
    if option not in asked_activity:
        asked_activity.append(option)
        return activityQuestions[option-1]
    else:
        if iters < 15:
            return determine_activity_question(iters+1)
        else:
            saveMe = randint(1, len(idkHowButItCoversMyAss))
            return idkHowButItCoversMyAss[saveMe-1]


def determine_option():
    if MAX_WEATHER == len(asked_weather):
        if MAX_ACTIVITIES == len(asked_activity) and MAX_PERSONAL != len(asked_personal):
            return 'personal'
        elif MAX_PERSONAL == len(asked_personal) and MAX_ACTIVITIES != len(asked_activity):
            return 'activity'
        elif MAX_PERSONAL != len(asked_personal) and MAX_ACTIVITIES != len(asked_activity):
            return choice(['activity', 'personal'])
        else:
            return 'full'
    elif MAX_ACTIVITIES == len(asked_activity):
        if MAX_WEATHER == len(asked_weather) and MAX_PERSONAL != len(asked_personal):
            return 'personal'
        elif MAX_PERSONAL == len(asked_personal) and MAX_WEATHER != len(asked_weather):
            return 'weather'
        elif MAX_PERSONAL != len(asked_personal) and MAX_WEATHER != len(asked_weather):
            return choice(['weather', 'personal'])
        else:
            return 'full'
    elif MAX_PERSONAL == len(asked_personal):
        if MAX_WEATHER == len(asked_weather) and MAX_ACTIVITIES != len(asked_activity):
            return 'activity'
        elif MAX_ACTIVITIES == len(asked_activity) and MAX_WEATHER != len(asked_weather):
            return 'weather'
        elif MAX_WEATHER != len(asked_weather) and MAX_ACTIVITIES != len(asked_activity):
            return choice(['activity', 'weather'])
        else:
            return 'full'
    else:
        return choice(['weather', 'activity', 'personal'])


def determine_personal_question():
    option = randint(1, len(personalQuestions))
    if option not in asked_personal:
        asked_personal.append(option)
        return personalQuestions[option-1]
    else:
        return determine_personal_question()


def determine_question_ask(score):
    menu_option = determine_option()
    print(menu_option)
    global marker
    global lastQuestion
    if not marker:
        marker = True
        score_score(score, 'weather')
        return determine_weather_question(0)
    else:
        if menu_option != 'full':
            if lastQuestion == 'weather':
                lastQuestion = menu_option
                score_score(score, 'weather')
                return determine_weather_question(0)
            elif lastQuestion == 'activity':
                lastQuestion = menu_option
                score_score(score, 'activity')
                return determine_activity_question(0)
            elif lastQuestion == 'personal':
                lastQuestion = menu_option
                score_score(score, 'personal')
                return determine_personal_question()
        elif lastQuestion == 'full':
            saveMe = randint(1, len(idkHowButItCoversMyAss))
            return idkHowButItCoversMyAss[saveMe-1]


def question_manager(message):
    num_q = len(asked_personal) + len(asked_activity) + len(asked_weather)
    if num_q < MAX_QUESTIONS-1:
        data_score = analyze_data(message.text.title())
        answer_text.append(message.text.title())
        print(data_score)
        question = determine_question_ask(data_score)
        showUserScore()
        questions_asked_text.append(question)
        sent_msg = bot.send_message(message.chat.id, question, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, question_manager)
    else:
        newMon = analyze_user()
        guy = pb.pokemon(newMon)
        reply_text = "Your pokemon partner has been found.\n Their name is: "
        second_part_text = "\n Here is a link to a picture of the pokemon you have been given " + guy.sprites.front_default
        dude = reply_text + guy.name + second_part_text
        writeInfoOut()
        bot.reply_to(message, dude)


def showUserScore():
    print("water " + str(new_user.weatherScore))
    print("physicality " + str(new_user.activityScore))
    print("radicality " + str(new_user.otherScore))
    print("indifferentiality " + str(new_user.indifferenceScore))


# type =1 is weather,
def score_score(score, type_sc):
    if score == 'neutral':
        new_user.indifferenceScore += 5
    if type_sc == 'weather':
        if score == 'positive':
            new_user.weatherScore += 10
        elif score == 'negative':
            new_user.weatherScore -= 10
    elif type_sc == 'activity':
        if score == 'positive':
            new_user.activityScore += 10
        elif score == 'negative':
            new_user.activityScore -= 10
    elif type_sc == 'personal':
        if score == 'positive':
            new_user.otherScore += 10
        elif score == 'negative':
            new_user.otherScore -= 10


# returns 1 if POSITIVE, -1 if NEGATIVE, and 0 if NEUTRAL
def analyze_data(new_data):
    vs = analyzer.polarity_scores(new_data)
    scored.append(vs)
    print(vs)
    if vs['pos'] > 0.4 or vs['compound'] >= 0.2:
        return 'positive'
    elif vs['neg'] > 0.4 or vs['compound'] <= -0.2:
        return 'negative'
    else:
        return 'neutral'


def analyze_user():
    maxType = findMaxUserScore()
    maxNum = checkMaxByType(maxType)
    val = checkPosOrNeg(maxType)
    indSc = lookIndiffScore()
    if indSc != 'high':
        return providePokemon(maxType, val)
    else:
        return random.choice(ghostType)


def providePokemon(typey, val):
    print(typey)
    if typey == 'weather':
        if val == 'yes':
            return random.choice(waterType)
        elif val == 'no':
            return random.choice(fireType)
    elif typey == 'activity':
        if val == 'yes':
            return random.choice(fightType)
        elif val == 'no':
            return random.choice(psychicType)
    elif typey == 'other':
        if val == 'yes':
            return random.choice(poisonType)
        elif val == 'no':
            return random.choice(grassType)
    else:
        return "eevee"


def lookIndiffScore():
    if new_user.indifferenceScore <= 15:
        return 'low'
    elif new_user.indifferenceScore <= 35:
        return 'medium'
    else:
        return 'high'


def checkMaxByType(typeU):
    if typeU == 'weather':
        return new_user.weatherScore
    elif typeU == 'activity':
        return new_user.activityScore
    elif typeU == 'other':
        return new_user.otherScore


def checkPosOrNeg(typeU):
    if typeU == 'weather':
        if new_user.weatherScore > 0:
            return 'yes'
        else:
            return 'no'
    elif typeU == 'activity':
        if new_user.activityScore > 0:
            return 'yes'
        else:
            return 'no'
    if typeU == 'other':
        if new_user.otherScore > 0:
            return 'yes'
        else:
            return 'no'


def findMaxUserScore():
    myMax = max(abs(new_user.weatherScore), abs(new_user.activityScore))
    myMax2 = max(abs(new_user.otherScore), abs(new_user.indifferenceScore))
    final = max(myMax, myMax2)
    print(final)
    if final == abs(new_user.weatherScore):
        return 'weather'
    elif final == abs(new_user.otherScore):
        return 'other'
    elif final == abs(new_user.activityScore):
        return 'activity'
    elif final == abs(new_user.indifferenceScore):
        return 'indifference'
    else:
        return 'none'


def loadPokemon():
    allPokemon = pb.generation('kanto')
    return allPokemon


def writeInfoOut():
    iter = 0
    f = open("results.txt", "a")
    f.write("\n\nThe Following information has been added:\n")
    var = "name: " + new_user.name + "   scores: weather->" + str(new_user.weatherScore) + ";act->" + str(new_user.activityScore) + ";oth->" + str(new_user.otherScore) + ";indf-> " + str(new_user.indifferenceScore)
    f.write(var)
    for ques in questions_asked_text:
        f.write("\nquestions asked: " + ques + " answer: " + answer_text[iter] + "\nwith score: " + str(scored[iter]))
        iter += 1


def writePokemon():
    f = open("pok.txt", "a")
    f.write("water: ")
    for dude in waterType:
        f.write(dude + ", ")
    f.write("\nfire: ")
    for dude in fireType:
        f.write(dude + ", ")
    f.write("\nfight: ")
    for dude in fightType:
        f.write(dude + ", ")
    f.write("\ngrass: ")
    for dude in grassType:
        f.write(dude + ", ")
    f.write("\npsychic: ")
    for dude in psychicType:
        f.write(dude + ", ")


def initializeProg():
    asked_weather.clear()
    asked_personal.clear()
    asked_activity.clear()
    new_user.activityScore = 0
    new_user.otherScore = 0
    new_user.weatherScore = 0
    new_user.indifferenceScore = 0
    marker = False
    #loadPokemonFromWeb()
    #writePokemon()


@bot.message_handler(commands=['start', 'hello', 'begin'])
def send_welcome(message):
    initializeProg()
    bot.reply_to(message, beginningSequence)
    user_input = f"Please begin by telling me your name"
    sent_msg = bot.send_message(message.chat.id, user_input, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, begin_questions)


def begin_questions(message):
    nameUser = message.text.title()
    text = "Nice to speak with you " + nameUser + nameSequence
    new_user.name = nameUser
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, question_manager)


def loadPokemonFromWeb():
    gen_resource = pb.generation(1)
    for mon in gen_resource.pokemon_species:
        guy = pb.pokemon(mon.name)
        if str(guy.types[0].type) == 'grass':
            grassType.append(guy.name)
        elif str(guy.types[0].type) == 'water':
            waterType.append(guy.name)
        elif str(guy.types[0].type) == 'fire':
            fireType.append(guy.name)
        elif str(guy.types[0].type) == 'fighting':
            fightType.append(guy.name)
        elif str(guy.types[0].type) == 'psychic':
            psychicType.append(guy.name)


bot.infinity_polling()
