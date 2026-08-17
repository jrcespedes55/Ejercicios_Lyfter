import menu

def main():
    while(True):
        menu.show_menu()
        answer = menu.get_menu_option()
        menu.run_menu(answer)
        if(answer == 0):
            break

if __name__ == "__main__":
    main()