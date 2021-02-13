import json
from GetBookInfo import run_Book_List
from CreateBook import run_Create_Book
from CreateCategory import run_Create_Category
from CreateAdmin import run_Create_Admin
from Login import run_Login
from SearchAutor import run_Search_Autor
from GetAutors import run_Autors
from SearchBook import run_Search_Book
from SearchCategory import run_Search_Category
from GetNumberview import run_Number_Viewed
from CreateAutor import run_Create_Autor
from GetCategories import run_Categories
from Exit import run_Exit
from Restart import run_Restart


class Main:
    exitprogramm = False

    while exitprogramm == False:

        print('What do you want to do?')
        print('Your Options are:')
        print('1. Search a Book')
        print('2. Search a Category')
        print('3. Search a Autor')
        print('4. Show all Categories')
        print('5. Show all Autors')
        print('6. Show all Books')
        print('7. Show Number of viewed Books/Categories')
        print('8. Log in as Admin')
        print('9. Create a Book(Needs Admin rights)')
        print('10. Create a Autor(Needs Admin rights)')
        print('11. Create a Category(Needs Admin rights)')
        print('12. Create a Admin(Needs Admin rights)')
        print('13. Exite the Programm')
        selection = input('Type the Number here: ')
        #selection = int(selection)
        #print(selection)
        exitbool = False
        if selection == '1':
            while exitbool == False:
                run_Search_Book()
                exitbool = run_Restart()
        elif selection == '2':
            while exitbool == False:
                run_Search_Category()
                exitbool = run_Restart()
        elif selection == '3':
            while exitbool == False:
                run_Search_Autor()
                exitbool = run_Restart()
        elif selection == '4':
            while exitbool == False:
                run_Categories()
                exitbool = run_Restart()
        elif selection == '5':
            while exitbool == False:
                run_Autors()
                exitbool = run_Restart()
        elif selection == '6':
            while exitbool == False:
                run_Book_List()
                exitbool = run_Restart()
        elif selection == '7':
            while exitbool == False:
                run_Number_Viewed()
                exitbool = run_Restart()
        elif selection == '8':
            run_Login()
        elif selection == '9':
            while exitbool == False:
                run_Create_Book()
                exitbool = run_Restart()
        elif selection == '10':
            while exitbool == False:
                run_Create_Autor()
                exitbool = run_Restart()
        elif selection == '11':
            while exitbool == False:
                run_Create_Category()
                exitbool = run_Restart()
        elif selection == '12':
            while exitbool == False:
                run_Create_Admin()
                exitbool = run_Restart()
        elif selection == '13':
            exitprogramm = run_Exit()
        
        else:
            print('Please type in a Number')
            run_Restart()



    #run_create_book()
    #run_Book_list()
    #run_create_Category()
    #run_Create_Admin()
    #run_Login()
    #run_Autor_Search()
    #run_Autors()
    #run_search_book()
    #run_search_Category()
    #run_Number_Viewed()
    #run_Create_Autor()