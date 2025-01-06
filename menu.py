from lab2 import comparison_solver, comparison_system_solver, euclid_extended
import lab2
from lab1 import Caesar, given_var
import lab3
import lab4
import lab5
import lab6
import lab7

def Menu():
    exit = False
    while (not exit):
        print('------------------------------------------------------------------------------------------------')
        main_menu = int(input("Добро пожаловать! Куда пожелаете отправиться на этот раз? \n1) Первая лаба \
                               \n2) Вторая лаба \
                               \n3) Третья лаба \
                              \n4) Четвёртая лаба \
                              \n5) Пятая лаба \
                              \n6) Шестая лаба \
                              \n7) Седьмая лаба \
                              \n8) Домой\n\n"))

        

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
            if menu_option == 1: 
                lab2.inverse_element_interface()
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
            else: 
                return 0
            
        def fourth_lab():
            exit_local = False
            p, q = lab4.p_q_input()
            while not exit_local:
                menu_option = int(input("Выберите опцию: \
                \n1. Автоматическая генерация ключей \
                \n2. Ввод открытых ключей вручную \
                \n3. Просмотр таблицы ключей \
                \n4. Шифрование сообщения \
                \n5. Расшифровка сообщения \
                \n6. Выйти\n"))
                print()
                print()

                if menu_option == 1: lab4.automatic_key_generation(p, q)
                elif menu_option == 2: lab4.open_keys_input(p, q)
                elif menu_option == 3: lab4.display_keys_table()
                elif menu_option == 4: lab4.encryption()
                elif menu_option == 5: lab4.decryption()
                else: 
                    exit_local = True

        def fifth_lab():
            menu_option = int(input("Выберите опцию: \
                \n1. Проведение факторизации числа 𝑛 методом пробного деления \
                \n2. Определение закрытого ключа \
                \n3. Расшифрование сообщения \
                \n4. Индивидуальный вариант расшифровки \
                \n5. Выйти\n"))
            if menu_option == 1:
                lab5.trial_division_interface()
            elif menu_option == 2:
                lab5.private_key_search_interface()
            elif menu_option == 3:
                lab5.decrypt_message_interface()
            elif menu_option == 4:
                lab5.induvidual_var()
            else: 
                return 0
            
        def sixth_lab():
            menu_option = int(input("Выберите опцию: \
                \n1. Проведение факторизации числа методом квадратичного решета \
                \n2. Проведение факторизации ро-методом \
                \n3. Индивидуальный вариант факторизации \
                \n4. Выйти\n"))
            if menu_option == 1:
                lab6.quadratic_sieve_fact_interface()
            elif menu_option == 2:
                lab6.rho_fact_interface()
            elif menu_option == 3:
                lab6.induvid_var()
            else:
                return 0

        def seventh_lab():
            menu_option = int(input("Выберите опцию: \
                \n1. Вычисление дискретного логарифма методом 'шаг младенца-шаг гиганта' \
                \n2. Выйти\n"))
            if menu_option == 1:
                lab7.babyStep_giantStep_interface()
            else: 
                return 0

        if main_menu == 1: 
            main_menu = first_lab()
        elif main_menu == 2: 
            main_menu = second_lab()
        elif main_menu == 3: 
            main_menu = third_lab()
        elif main_menu == 4: 
            main_menu = fourth_lab()
        elif main_menu == 5: 
            main_menu = fifth_lab()
        elif main_menu == 6: 
            main_menu = sixth_lab()
        elif main_menu == 7:
            main_menu = seventh_lab()
        else: 
            exit = True
        # if main_menu == 0: break

Menu()
