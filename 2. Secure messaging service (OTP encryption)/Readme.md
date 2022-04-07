## Secure messaging service (OTP encryption)

##### My second project in Python. This project focused on: functions, strings, lists, multidimensional lists and functions (sorting and searching). 

##### This project used the One-Time Pad technique for encryption, which is described in the PDF file on pages 1, 2 and 3. The objectives were to send encrypted messages to our classmates, receive and decrypt messages, show messages on the GUI (based on date) and also filter messages on the screen (the filter also needed to consider email addresses).

##### For developing this project, we were given two .py files: mensajeria.py and msgGUI.py. The first one, mensajeria.py, allowed for interaction with the server which managed the secure service. In particular, this file consisted of different functions. Regarding the second file (msgGUI.py), this one allowed for the program to be managed through the GUI. In particular, in this file a class named "Application" was defined with several methods. For example, these methods could change the aspect of the GUI, retrieve information from the GUI such as button information (user input) or show alerts to the user.

##### Examples of the GUI are shown in the PDF file on page 5 (Figure 1), page 6 (Figure 2) and page 7 (Figure 3). Also, the functions and methods of the previous files are described on pages 3-6.  

##### We were also given two .gif files of icons for the interface. These icons, as well as mensajeria.py and msgGUI.py, are not included in this folder since I did not develop them.   

##### Finally, the report I've included here focuses on the aspects I found challenging + how I solved them as well as extra aspects I included in my project. For instance, I had alerts for whenever the user exceeded the maximum number of emails that could be sent each day (50) and when the message to send had more than 45 characters (maximum length of the secret password for encryption).   