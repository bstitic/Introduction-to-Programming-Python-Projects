## Labyrinth game (Pythonia's Master)

##### My third project in Python (this one was particularly fun!). This OOP project focused on: class and objects (design, creation and usage), lists, multidimensional lists, functions (searching and sorting), I/O (eg. to read .txt files of maps) and string manipulation.

##### This project was about a labyrinth game with 3 different available maps. The player, who could control one of two hero characters, had the task of reaching key points of the map called "domination points" ("puntos de dominación") before the enemies did (the snakes). Also, if the player's character was touched by a snake this meant game over. There were 3 types of items, which could be either used by the player or the enemy snakes.

##### In this project, the user could play using the arrow keys of the keyboard to move the hero around on an animated GUI. 

##### There were key aspects of the game to consider during development such as, for example, having to wait for 3 seconds upon reaching an already claimed "domination point" (this was applicable to both snakes and the player). Also, the enemy snakes had to be somewhat intelligent so they were supposed to go after the hero character (to win immediately), items or a "domination point" (depending on what was closer). 

##### The game also had an internal coordinate system which varied depending on the case. For instance, for walls, "domination points" and items, a coordinate system was used which was based on the squares defined by the internal grid used to create the GUI. On the other hand, for snakes and heroes, since movement should be more fluid a coordinate system based on pixels was used instead. During project development, all elements were considered to internally occupy an area of 32x32 pixels.

##### For the development of this project, we were given several files. There were 3 maps (.txt files), 3 items (.gif files), several .gif files for the hero characters, several .gif files for the snakes, a .gif file for the background of the squares of the grid used to create the GUI, a .gif file for walls and 2 .py files. In these files, classes were defined for the characters, items and "domination points". However, I created my own classes with their own methods for all of these cases as well as some additional classes (walls, points, internal timer).   

##### Another file we were given was escenario.py, in which a class called "Escenario" was defined that is related to the GUI. It graphically represents the current stage of the game, lets the GUI be updated as needed and allows for fluid gameplay with the arrow keys. 

##### The description of this class ("Escenario") can be found in the HTML file in this folder, which we were given as well. For its part, the PDF file in this folder contains the entire project description (it is quite detailed).

##### Similarly to the previous projects, I haven't included the other files we were given here since I didn't develop them.

##### Finally, the report posted here includes some of the main challenges I faced during project development and how I solved them. Also, there were various aspects which we were free to design (like character speed). Two aspects that I designed and which I discussed in my report included, for example, dialogue and random map initialization using a list.