		Skyscraper Puzzle Solving Using Domain Contraction Techniques
				By Vinay Detani (B18CSE061)
		Indian Institute of Technology, Jodhpur


	File Details : 
main.py			: It has main function that evoke the pygame app_class
app_class.py		: It contains the user interface parts like grids, numbers, clues and buttons
algorithmClass.py	: It contains the implementation of the algorithm's steps as mentioned in 
			  in the Project_report file.
buttonClass.py		: It has button's UI and click features.
settings.py		: It contains the basic setting of the game, like grid size, clues,
			  colors and dimensions that were used by app_class for creating the game.
Project_report.doc	: It is the report of the project and detailed explaination of the
			  algorithms according to the guildlines.


How to RUN it?

Run the  command  " python main.py " in the terminal 
If you haven't install the pygame : use " pip install pygame ", before running the game

RUN Button :  It will call a function that solve some part of the puzzle and details will
	      will be visible on the screen. Intially, each cell domain contains the all the N numbers
	      By clicking the RUN,button an operation will be performed over the domains and result
	      will be displayed on the grids.
	      Click it until you get the solution.

Reset Button : It will reset the puzzle to the original state

To change the puzzle/new puzzle: 
Add the puzzle in the settings.py file according to the other games already added.
Change the SIZE variable in settings.py.

Lastly, in app_class set the self.grid to the new gameboard that is added in settings.py file


For checking the intermediate calculations and steps : uncomments the print statements
in algorithm class. 




################################  THANK YOU  #############################################
 		    