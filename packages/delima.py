print("Mabuhay, I am Justine Delima.")
user_choice = 0

while user_choice != 5:
    user_choice = int(input("Enter your choice: "))

    match user_choice:
        case 1:
            print('My birth month is February.')        
        case 2:
            print('My goal is to achieve my goal.')
        case 3:
            print('Comment mo bading')
        case 4:
            print('Ano pa')
        case 5:
            print('BYEEE bading wag kana bumalik.')
    