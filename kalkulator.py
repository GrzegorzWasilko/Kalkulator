#Moduł 4-zadanie 2-->> Kalkulator
#string zamiast int rzutowanie i co ?

import sys #do argv w przyszłości
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile-kalkulator.log")
#bsicConfic ustawiłem aby zwracał komunikaty od poziomu debug +data i godzina + plik txt
#----------------------------------------------------------------------
def calculator (arg1,arg2) :
    choice=input("wybierz działanie 1-dodawanie, 2- odejmowanie, 3- Mnożenie, 4- Dzielenie \n")
    if choice == 1: #Dodawanie
        result=arg1+arg2
        return result

    elif choice == 2: #Odejmowaie
        if arg2>arg1:
        #logging.info('wynik ponizej zera')
         exit(1) #upewnic sie czy to dobry wybór na błąd !
    elif arg2<=arg1:
        result=arg1-arg2
        return result

    elif choice == 3: #Mnożenie
        result=arg1*arg2
        return result

    elif choice == 4: #Dzielenie
        if arg2==0:     # warunek nie działa , dzieli przez zero
          logging.info("pamiętaj cholero, nie dziel przez 0")
          exit(1)
        elif arg2!=0:
            result=arg1/arg2
            return result
#__________________________________________________________________
if __name__== '__main__' :

    value_one=int(input('podaj pierwszą liczbę'))
    value_two=int(input('podaj drugą liczbę'))
    print('wprowadziłeś %d %d' % (value_one,value_two))
    response=calculator(value_one,value_two)
    print("wynik działania to %d" % response)