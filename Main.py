import json
from GetBookInfo import run_Book_list
from CreateBook import run_create_book
from CreateCategory import run_create_Category
from CreateAdmin import run_Create_Admin
from Login import run_Login
from AutorSearch import run_Autor_Search
from GetAutors import run_Autors
from SearchBook import run_search_book
from SearchCategory import run_search_Category
from GetNumberview import run_Number_Viewed
from CreateAutor import run_Create_Autor
from GetCategories import run_categories
from Exit import run_Exit
from Restart import run_restart
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
    selection = int(selection)
    #print(selection)
    if selection == 1:
        run_search_book()
        run_restart()
    if selection == 2:
        run_search_Category()
        run_restart()
    if selection == 3:
        run_Autor_Search()
        run_restart()
    if selection == 4:
        run_categories()
        run_restart()
    if selection == 5:
        run_Autors()
        run_restart()
    if selection == 6:
        run_Book_list()
        run_restart()
    if selection == 7:
        run_Number_Viewed()
        run_restart()
    if selection == 8:
        run_Login()
        run_restart()
    if selection == 9:
        run_create_book()
        run_restart()
    if selection == 10:
        run_Create_Autor()
        run_restart()
    if selection == 11:
        run_create_Category()
        run_restart()
    if selection == 12:
        run_Create_Admin()
        run_restart()
    if selection == 13:
        exitprogramm = run_Exit()
        


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