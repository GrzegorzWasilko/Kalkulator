#Moduł 4-zadanie 2-->> Kalkulator
#string zamiast int rzutowanie i co ?

import sys #do argv w przyszłości
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile-kalkulator.log")
#bsicConfic ustawiłem aby zwracał komunikaty od poziomu debug +data i godzina + plik txt (zapis do pliku nie na ekran)
#----------------------------------------------------------------------
def calculator (arg1,arg2) :
    choice=input("wybierz działanie 1-dodawanie, 2- odejmowanie, 3- Mnożenie, 4- Dzielenie \n")
    if choice =='1': #Dodawanie
        result=arg1+arg2
        print(type(result))#typ result to int
        return result

    elif choice =='2': #Odejmowaie
        if arg2>arg1:
         print('wynik ponizej zera')    #logging.info nie działa :((
         #exit(1) #upewnic sie czy to dobry wybór na błąd !
        elif arg2<=arg1:
            result=arg1-arg2
            return result

    elif choice =='3': #Mnożenie
        result=arg1*arg2
        return result

    elif choice =='4': #Dzielenie
        if arg2==0:   
          logging.info("pamiętaj cholero, nie dziel przez 0")#komunikat pojawi sie w notatniku
          exit(1)   #rasie Value Error  wychodzi z programu bez błedu
        elif arg2!=0:
            result=arg1/arg2
            return result
#__________________________________________________________________
if __name__== '__main__' :

    value_one=int(input('podaj pierwszą liczbę'))
    value_two=int(input('podaj drugą liczbę'))
    print('wprowadziłeś %d %d' % (value_one,value_two))
    response=calculator(int(value_one),int(value_two))#działa i bez rzutowania 
    print("wynik działania to %s" % response)