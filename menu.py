from lab2 import comparison_solver, comparison_system_solver, euclid_extended
import lab2
from lab1 import Caesar, given_var
import lab3

def Menu():
    exit = False
    while (not exit):
        print('------------------------------------------------------------------------------------------------')
        main_menu = int(input("Добро пожаловать! Куда пожелаете отправиться на этот раз? \n1) Первая лаба \n2) Вторая лаба \n3) Третья лаба \n4) Домой\n"))

        def first_lab():
            menu_option = int(input("Выскажите ваше волеизволение: \n1) Зашифровать текст (первая лаба), \n2) Расшифровать текст (первая ), \n3) Индивидуальный вариант текста, \n4) Выйти отсюда поскорее\n"))
            print()
            c = Caesar()
            if menu_option == 1: c.encryption()
            elif menu_option == 2: c.decryption()
            elif menu_option == 3: given_var()
            else: 
                return 0
        def second_lab():
            menu_option = int(input("Выскажите ваше волеизволение: \n1) Вычисление обратного элемента по модулю m,\
                            \n2) Решить сравнение вида:2 ax=b (mod m), \n3) Решить систему сравнений вида по модулю m: ax+y=b, cx+y=d,\
                            \n4) Расшифровать введённый текст, \n5) Индивидуальный вариант текста, \n6) Выйти отсюда поскорее\n"))
            print()
            # c = Caesar()
            if menu_option == 1: 
                lab2.inverse_element_interface()
                # c.encryption()
            elif menu_option == 2: 
                lab2.comparison_solver_interface()
            elif menu_option == 3: lab2.comparison_system_solver_interface()
            elif menu_option == 4: lab2.input_message_decryption()
            elif menu_option == 5: lab2.variant_case_decryption()
            
            else: 
                return 0
        def third_lab():
            menu_option = int(input("Выскажите ваше волеизволение: \n1) Рассчитать значение H_k/k для k=1,...,5, \n2) Построить график зависимости H_k/k от k, \n3) Выйти отсюда поскорее\n"))
            print()
            
            if menu_option == 1: lab3.entropy_lang_norm_interface()
            elif menu_option == 2: lab3.display_graphic()
            # elif menu_option == 3: given_var()
            else: 
                return 0
            
        if main_menu == 1: 
            main_menu = first_lab()
        elif main_menu == 2: 
            main_menu = second_lab()
        elif main_menu == 3: 
            main_menu = third_lab()
        else: break
        if main_menu == 0: break

Menu()
