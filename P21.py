#Version test edit
import string
def noun():
    return input("Enter a noun: ")

def plnoun():
    return input("Enter a plural noun: ")

def verb():
    return input("Enter a present tense verb: ")

def verbing():
    return input("Enter an 'ing' verb: ")

def verbed():
    return input("Enter an 'ed' verb: ")

def adj():
    return input("Enter an adjective: ")

def name():
    return string.capwords(input("Enter a famous person\'s name: "))

def number():
    return str(input("Enter a number: "))

def adverb():
    return input("Enter an adverb: ")

def place():
    return input("Enter a city/town: ")

story =("March 7, in the year " + number() + ": It was still " + number() + " days before Patrick was \n"
    "due. I weighed about " + number() + " pounds and looked like I\'d swallowed \n" \
    "a " + noun() + ". I felt like it, too!  Bruce was " + adj() + ", but I think \n" \
    "he\'d had enough of me having to " + verb() + " all the time and get \n"  \
    "all " + adj() + " over " + adj() + " " + plnoun() + ".  One minute I\'d be " + adj() + " and the next \n"  \
    "I\'d be " + verbing() + " like a " + noun() + ". Bruce and I spent the day at the \n"  \
    + noun() + " museum in " + place().capitalize() + " and came home to relax - but then my water \n"  \
    "broke! Bruce grabbed our to-go " + noun() + " and off we went to " + noun().capitalize() + " " + noun().capitalize() + " \n"  \
    "Hospital. I was in labor for " + number() + " hours before the " + plnoun() + " brought \n"  \
    "in Dr. " + name() + ". I " + verbed() + " like there was no " + noun() + " but the baby wouldn\'t \n"  \
    + verb() + ".  There was obviously a "+ noun() + " and they said Patrick would have to be \n"  \
    + verbed() + " by " + adj() + "-section. And so he was. Bruce declined the chance to \n"  \
    + verb() + " the " + noun() + ", but was happy to hold Patrick as soon as he\'d been " + verbed() + ". \n"  \
    "Of course, everyone was " + adj() + " when they saw our " + adj() + ", " + adj() + ", " + noun() + " of \n"  \
    "joy. " + adverb().capitalize() + ", we were able to bring him home, strapped in his " + noun() + " in the \n"  \
    "back of our " + noun() + ". Over " + number() + " diapers and " + number() + " of years of school later \n"  \
    "he's still " + adj() + " and we love him " + adverb() + "!\n")


print ("\n\'It Could Have Happened That Way - Birth\'\n")

print (story)
