# Knowledge Based Systems - Chatbot

by Spencer Johnson & Marc Escote & Jan Bellavista
on Friday 17th March, 2023

The following explanation is in conjunction with Knowledge Based Systems semester 2 project. The repository used for the project can be found [here](https://github.com/papasj19/ChatBot). This project was conceptualized from the popular Nintendo [Pokemon Game](https://mysterydungeon.pokemon.com/en-us/).

The idea for this chatbot came from the first part of the Pokemon mystery dungeon games. During this sequence the user is prompted through a series of questions and at the end they are given a playable character based upon how they answered the questions. As we keep track of how the users have responded we build them a score that is the metric used for the character calculation. 
     
* Presenting the Chosen Domain
    * PowerPoint: Presentation
    * Code: `main.py`
    * This document: `README.md`

## System requirements

* [JetBrains PyCharm](https://www.jetbrains.com/pycharm/) 
* Libraries used:
    * [nltk](https://www.nltk.org)  
    * [pandas](https://pandas.pydata.org)
    * [sklearn](https://scikit-learn.org/stable/index.html)
    * [scipy](https://scipy.org)
    
The project was developed and debugged largely using the platform pycharm.

There exists only one file related to the compilation of the project shown below:
```bash
Presenting_Domain/main.py
``` 
The user will only need the aforementioned software. There will be four libraries commented out at the top of the code(beneath the class declaration), if the users computer requests another library upon compilation, un-comment these lines and compile again, it should work. 

```python
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')
```

## Questions to be asked

At the time of the this writing the questions are broken up into four different categories. The first wants the user to input a number, the second type wants the user to input words, and the third and fourth ask the user for a letter(Y/N). The third and fourth types of questions needed to be placed in order to for sure that there is some sort of drastic enough difference that will allow for a clean calculation. The program uses a random number generator to decide which of the four categories to be used. As of now the submission will use 2 number, 5 word, and 6 Y/N(4 Weather and 4 Activity) questions in order to achieve a score. There is only two number questions programmed but there exist more word questions and Y/N questions. Again a random number generator is used to determine which of the questions is asked at each time.  

## Limitations

* Random Questions 
    * Since the group decided to have the questions presented to the user randomly, to provide a more unique and diverse experience, sometimes the questions are structured weirdly or seem random, it is because they are. In the original version, the questions were not checked for duplicates but this was fixed as there still was time before the deadline. 
     
* Based On Input Type
    * There exists different kind of questions and the program specifies what is would like to receive from the user based upon the question asked. As of now the program does not check the user input for wrong information or ensure that the information is allowed before moving forward. Since this is a proposal we assumed that the user would have full understanding of how the program would work and would not enter bad information. 

* Metric Scoring 
    *  The scoring is not the best algorithm in the world and the system could very well be flawed. As of now it is more of a demonstration as to what the group will do later with more options. At the the time of this writing the team got together to begin discussing the new metric equation and how to utilize it best.  
     
* Differences Between Actual Games
    * Obviously we could not implement everything correctly in relation to the franchise and the lore. There existed parts (types, moves, etc) that had to be omitted in order to be able to deliver a working prototype.  This could be fixed and become more realistic later once an external database of Pokémon is connected and allows for different uses without the team needing to program it manually. 
    

## Contact

Spencer Johnson - spencerjames.johnson@students.salle.url.edu - Social: [@papasj19](https://www.instagram.com/papasj19/) - GitHub:  [@papasj19](https://github.com/papasj19)

Marc Escoté marc.escote@students.salle.url.edu

Jan Bellavista - jan.bellavista@students.salle.url.edu

