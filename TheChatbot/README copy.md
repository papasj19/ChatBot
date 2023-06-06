# Knowledge Based Systems - Chatbot

by Spencer Johnson & Marc Escote & Jan Bellavista
on March-June, 2023

The following explanation is in conjunction with Knowledge Based Systems semester 2 project. The repository used for the project can be found [here](https://github.com/papasj19/ChatBot). This project was conceptualized from the popular Nintendo [Pokemon Game](https://mysterydungeon.pokemon.com/en-us/).

The idea for this chatbot came from the first part of the Pokemon mystery dungeon games. During this sequence the user is prompted through a series of questions and at the end they are given a playable character based upon how they answered the questions. As we keep track of how the users have responded we build them a score that is the metric used for the character calculation. 


## Included Software
     
* PokemonGuesser
    * Code: `main.py`
    * This document: `README.md`
    * PreLoaded Pokemon: `pok.txt`
    * Results of Recent Users: `Results.txt`

## System requirements

* [JetBrains PyCharm](https://www.jetbrains.com/pycharm/) 
* Libraries used:
    * [random](https://docs.python.org/3/library/random.html) 
    * [dataclasses](https://docs.python.org/3/library/dataclasses.html) 
    * [telebot](https://pypi.org/project/pyTelegramBotAPI/)
    * [vaderSentiment](https://pypi.org/project/vaderSentiment/)
    * [pokebase](https://pokeapi.co)
       
    
The project was developed and debugged largely using the platform pycharm.

There exists only one file related to the compilation of the project shown below:
```bash
PokemonGuesser/main.py
``` 
The user will only need the aforementioned software. There was only two command line tools installed. 

```bash
$ pip install vaderSentiment
```
```bash
$ pip install python-telegram-bot
```

## Questions to be asked

At the time of the this writing the questions are broken up into three different categories. Weather, Activity, and Personal questions are used randomly to try and obtain a rough image of the user we are interacting with.

## Limitations

* Random Questions 
    * Since the group decided to have the questions presented to the user randomly, to provide a more unique and diverse experience, sometimes the questions are structured weirdly or seem random, it is because they are.
     
* Based On Input Type
    * The program does not check to ensure that user has made sense when delivering a response. This in turn can allow for incorrect results as their response will be labeled as neutral

* Metric Scoring 
    *  The scoring is not the best algorithm in the world and the system could easily be optimized with more time 
     
* Differences Between Actual Games
    * Obviously we could not implement everything correctly in relation to the franchise and the lore. There existed parts (types, moves, etc) that had to be omitted in order to be able to deliver a working prototype.
    

## Contact

Spencer Johnson - spencerjames.johnson@students.salle.url.edu - GitHub:  [@papasj19](https://github.com/papasj19)

Marc Escoté marc.escote@students.salle.url.edu

Jan Bellavista - jan.bellavista@students.salle.url.edu

