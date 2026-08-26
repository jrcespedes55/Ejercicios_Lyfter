import menu
import Data.data

def main():
    while(True):
        menu.show_menu()
        answer = menu.get_menu_option()
        students = Data.data.read_students("Data/students.csv")
        menu.run_menu(answer,students)
        if(answer == 0):
            break

if __name__ == "__main__":
    main()