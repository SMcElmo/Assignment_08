#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# SMcElmurry, 2020-Mar-15, Added CD Object class, DataProcessing function class,
#                          functions to existing class, and main body code
#------------------------------------------#

# -- DATA -- #
file_name = 'cdInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __str__: Returns the CD object attributes as a comma separated by a string

    """
    # TODone Add Code to the CD class
    # -- Fields -- #
    # NONE

    # -- Constructor -- #
    def __init__(self, identification, album, artistName):
        # -- Attributes -- #
        self.__cd_id = identification
        self.__cd_title = album
        self.__cd_artist = artistName

#    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    @cd_id.setter
    def cd_id(self, value):
        if type(value) is not int:
            raise Exception("ID must be an integer")
        else:
            self.__cd_id = int(value)

    @property
    def cd_title(self):
        return self.__cd_title
    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = value

    @property
    def cd_artist(self):
        return self.__cd_artist
    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = value

    # -- Methods -- #
    def __str__(self):
        cdTraits = str(self.cd_id) + "," + self.cd_title +"," + self.cd_artist
        return cdTraits


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    """
    # TODone Add code to process data from a file
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of CD Objects.
        Reads the data from file identified by file_name into a 2D table
        (list of CDs). One line in the file represents one CD row in table.

        Args:
            file_name (string): name of file used to read the data from

        Raises:
            FileNotFoundError: If 'file_name' does not exist in local directory

        Returns:
            cdList (List): a list of CD object types
        """
        cdList = []
        def exception_Message(exError, exMessage):
            """Local function to handle different custom error messages.
            
            Args:
                exError (Exception): Exception raised when accessing file
                exMessage (Str): Custom message printed to user
                
            Returns:
                None.
            """
            print(exError.__class__, exError)
            print(exError.__doc__)
            print(exMessage)
        try:
            with open(file_name, "r") as objFile:
                for line in objFile:
                    data = line.strip().split(',')
                    objCD = CD(int(data[0]), data[1], data[2])
                    cdList.append(objCD)
            print("File " + file_name + " loaded.")
            return cdList
        except Exception as e:
            if userChoice == "l" and lstOfCDObjects:
                exception_Message(e, "Saved inventory does not exist. Current data not overwritten.")
            elif userChoice == "l":
                exception_Message(e, "Saved inventory does not exist, please add CDs to inventory.")
            else:
                exception_Message(e, "Inventory does not exist. No file loaded.")

    # TODone Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, cdList):
        """Function to write data from cdList to a .txt file.

        Args:
            file_name (Str): name of file used to read the data from.
            cdList (List of CD Objects): 2D data structure (list of CDs) that holds the data during runtime.

        Returns:
            None.
        """
        with open(file_name, "w") as objFile:
            for row in cdList:
                objFile.write(str(row) + '\n')
        print("File saved!")


class DataProcessing:
    """Processes data to and from file:

    properties:

    methods:
        add_CD(cdID, cdTitle, cdArtist, table): -> (List of CD objects)
        check_DupID(dupID, cdList): -> (Boolean)
        check_DupEntry(dupTitle, dupArtist, cdList): -> (Boolean)
    """
    # Functions linked to add/delete
    @staticmethod
    def add_CD(cdID, cdTitle, cdArtist, table):
        """Function that creates a CD object and adds it to the list (table)
        
        Args:
            cdID (int): ID to be added to lstTbl
            cdTitle (string): Album title to be added to lstTbl
            cdArtist (string): Album artist to be added to lstTble
            
        Raises:
            ValueError: If cdID is not an int type
            
        Returns:
            table (List): List of CD Objects
        """
        objCD = CD(cdID, cdTitle, cdArtist)
        doubleID = DataProcessing.check_DupID(cdID, table)
        repeatEntry = DataProcessing.check_DupEntry(cdTitle, cdArtist, table)
        if repeatEntry:
            print("Album and artist already in library.")
            return table
        elif doubleID:
            while True:
                try:
                    newID = int(input("Unique numeric ID required. \nTo add to library, enter a new ID: "))
                    break
                except Exception as e:
                    print(e.__class__, e)
                    print(e.__doc__)
                    print("Please enter a valid ID Number")
            return DataProcessing.add_CD(newID, cdTitle, cdArtist, table)
        else:
            table.append(objCD)
            return table

    @staticmethod
    def check_DupID(idToFind, cdList):
        """Function to check for duplicate IDs in lstOfCDObjects.

        Args:
            idToFind (int): CD ID to be checked.
            strChoice (str): last user-entered choice from menu

        Returns:
            idMatch (int): Returns list index of ID + 1 if found, 0 otherwise
        """
        idMatch = 0
        if not cdList:
            return 0
        intRowNr = -1
        for row in cdList:
            intRowNr += 1
            if row.cd_id == idToFind:
                idMatch = intRowNr + 1
                break
        return idMatch

    @staticmethod
    def check_DupEntry(dupTitle, dupArtist, cdList):
        """Function to check for duplicate entries in cdList.

        Args:
            dupTitle (string): CD Title to be checked.
            dupArtist (string): CD Artist to be checked.
            cdList (list): list of CD Objects to be parsed

        Returns:
            dupAlbumArtist (Boolean): True if the album/artist pairing exists in lstTbl.
        """
        dupAlbumArtist = False
        if not cdList:
            return dupAlbumArtist
        for entryRow in cdList:
            if entryRow.cd_title == dupTitle and entryRow.cd_artist == dupArtist:
                dupAlbumArtist = True
                break
        return dupAlbumArtist


# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    """Processes data to and from file:

    properties:

    methods:
        showMenu(): -> None
        menuSelect(): -> None
        show_inventory(table): -> None
        CD_Entry(): -> (int), (str), (str)
        yes_No(userYN): -> (str)
        value_Errors(newType, userPrompt, errorMessage): -> (int)
    """
    # TODone add code to show menu to user
    @staticmethod
    def showMenu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print("""
------- MENU -------
[i] - View the inventory
[a] - Add a CD
[d] - Delete a CD
[l] - Load a saved file
[s] - Save the inventory to file
[x] - Exit the program""")

    # TODone add code to captures user's choice
    @staticmethod
    def menuSelect():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('What action would you like to take? ').lower().strip()
        print()
        return choice

    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)')
        for row in table:
            print('{}\t{} (by:{})'.format(row.cd_id, row.cd_title, row.cd_artist))
        print('======================================')

    # TODone add code to get CD data from user
    @staticmethod
    def CD_Entry():
        """Asks the user for information to add to their inventory

        Args:
            None

        Returns:
            intID (int): ID to be entered to CD Object
            strTitle (str): CD Title to be entered to CD Object
            strArtist (str): CD Artist to be entered to CD Object
        """
        intID = IO.value_Errors(int, "Enter an ID number: ", "Entry is not an integer value.")
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return intID, strTitle, stArtist

    #Miscellaneous Functions
    @staticmethod
    def yes_No(userYN):
        """Evaluates user's answer to a yes/no question. Asks again if answer is not yes(y) or no(n)

        Args:
            userYN (string): User's answer to a yes or no question

        Returns:
            (string) containing either 'y' or 'n'
        """
        while True:
            if userYN == "y" or userYN == "yes":
                return "y"
            elif userYN == "n" or userYN == "no":
                return "n"
            userYN = input("Please choose yes or no (y/n): ")

    @staticmethod
    def value_Errors(newType, userPrompt, errorMessage):
        """Checks if user input can be converted to the required data type.
        Displays errors to user if choice is invalid.

        Args:
            newType (data type): data type to convert user input to
            userPrompt (string): question to ask to user
            errorMessage (string): custom colloquial error message for user

        Raises:
            ValueError: if user input cannot be converted to declared data type

        Returns:
            Converted user value to new data type
        """
        while True:
            try:
                new_value = newType(input(userPrompt))
                return new_value
            except Exception as e:
                print(e.__class__, e)
                print(e.__doc__)
                print(errorMessage)


# -- Main Body of Script -- #
# TODone Add Code to the main body
# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.load_inventory(file_name)
if lstOfCDObjects:
    IO.show_inventory(lstOfCDObjects)
# Display menu to user
while True:
    IO.showMenu()
    userChoice = IO.menuSelect()

    # Display inventory to user
    if userChoice == "i":
        IO.show_inventory(lstOfCDObjects)
        continue

    # Add a CD to Inventory
    elif userChoice == "a":
        ID, Title, Artist = IO.CD_Entry()
        lstOfCDObjects = DataProcessing.add_CD(ID, Title, Artist, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue

    # Delete a CD from Inventory
    elif userChoice == "d":
        IO.show_inventory(lstOfCDObjects)
        intIDDel = IO.value_Errors(int, "Which ID would you like to deleted? ", "Please enter an integer value. ")
        blnCDRemoved = DataProcessing.check_DupID(intIDDel, lstOfCDObjects)
        if blnCDRemoved:
            del lstOfCDObjects[blnCDRemoved - 1]
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        IO.show_inventory(lstOfCDObjects)
        continue

    # Loads .txt File to Inventory
    elif userChoice == "l":
        if lstOfCDObjects:
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.', end=' ')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
            if IO.yes_No(strYesNo.lower()) == 'y':
                print('reloading...\n')
                lstOfCDObjects = FileIO.load_inventory(file_name)
                IO.show_inventory(lstOfCDObjects)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstOfCDObjects)
        else:
            FileIO.load_inventory(file_name)
        continue

    # Saves Current Inventory to .txt File
    elif userChoice == "s":
        FileIO.save_inventory(file_name, lstOfCDObjects)
        continue

    # Exits
    elif userChoice == 'x':
        break
    # Failsafe
    else:
        print("Random error")


