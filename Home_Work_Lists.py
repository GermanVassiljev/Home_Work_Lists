List=[]
while True:
    Ask_user=str(input("Желаете увидеть работу функции списков? Да \ Нет"))
    if Ask_user.lower()=="да":
        print("Вы можете выбрать следующие функции: ")
        print("1 - L.isdigit")# Состоит ли строка из цифр
        print("2 - L.isalpha")# Состоит ли строка из букв
        print("3 - L.ljust")# Делает длину строки и заменяет не достающие в конце
        print("4 - L.rjust")# Делает длину строки и заменяет не достающие в начале
        print("5 - L.title")# Делает первую букву большой, а остальными маленькими
        print("6 - L.istitle")# Начинаются ли слова в строке с заглавной буквы
        print("7 - L.upper")# Преобразование строки к верхнему регистру
        print("8 - L.lower")# Преобразование строки к нижнему регистру
        print("9 - L.swapcase")# Переводит символы нижнего регистра в верхний, а верхнего – в нижний
        print("10 - len(L)")# Длина строки
        Ask_list=int(input("Введите номер функции списка, которую хотите проверить: "))
        if Ask_list==1:
            print("Это функция нужна для проверки списка в виде цифр.")
            Ask_1_List=input("Впишите любую цифру или букву: ")
            List.append(Ask_1_List)
            print("Теперь данная функция скажет нам. Является ли ваш объект цифрой или буквой")
            if Ask_1_List.isdigit() == True:
                print("Вы написали цифру/цифры")
            else:
                print("Вы написали букву/буквы")
        elif Ask_list==2:
            print("Это функция нужна для проверки списка в виде букв.")
            Ask_2_List=input("Впишите любую цифру или букву: ")
            List.append(Ask_2_List)
            print("Теперь данная функция скажет нам. Является ли ваш объект цифрой или буквой")
            if Ask_2_List.isdigit() == False:
                print("Вы написали цифру/цифры")
            else:
                print("Вы написали букву/буквы")
        elif Ask_list==3:
            print("Это функция нужна для увеличения строки и замена не достающих на определённый символ в конце.")
            Ask_3_List_2=input("Впишите значение в список: ")
            Ask_3_List_3=int(input("Напишите длину желаемой строки: "))
            Ask_3_List_4=input("Впишите символ, который вы хотите вставить при необходимости: ")
            print(Ask_3_List_2.ljust(Ask_3_List_3,Ask_3_List_4))
        elif Ask_list==4:
            print("Это функция нужна для увеличения строки и замена не достающих на определённый символ с начало.")
            Ask_4_List_2=input("Впишите значение в список: ")
            Ask_4_List_3=int(input("Напишите длину строки: "))
            Ask_4_List_4=input("Впишите символ, который вы хотите вставить при необходимости: ")
            print(Ask_4_List_2.rjust(Ask_4_List_3,Ask_4_List_4))
        elif Ask_list==5:
            print("Данная функция делает первую букву с большой буквы, а все остальные маленькими.")
            Ask_5_List=input("Впишите слово: ")
            List.append(Ask_5_List)
            print(Ask_5_List.title())
        elif Ask_list==6:
            print("Это функция проверяет начинается ли слово с большой буквы.")
            Ask_6_List=input("Впишите слово: ")
            List.append(Ask_6_List)
            if Ask_6_List.istitle()==True:
                print("Слово начинается с большой буквы.")
            else:
                print("Слово не начинается с большой буквы.")
        elif Ask_list==7:
            print("Это функция делает всё больгыми буквами.")
            Ask_7_List=input("Впишите слово: ")
            List.append(Ask_7_List)
            print(Ask_7_List.upper())
        elif Ask_list==8:
            print("Это функция делает всё больгыми буквами.")
            Ask_8_List=input("Введите слово: ")
            List.append(Ask_8_List)
            print(Ask_8_List.upper())
        elif Ask_list==9:
            print("Это функция делает большие буквы маленькими, а маленькие в большие.")
            Ask_9_List=input("Введите слово.")
            List.append(Ask_9_List)
            print(Ask_9_List.swapcase())
        elif Ask_list==10:
            print("Это функция вычисляет длину строк списка.")
            Ask_10_List=input("Введите слово: ")
            List.append(Ask_10_List)
            print(len(Ask_10_List))
        List=[]
    else:
        break
        

