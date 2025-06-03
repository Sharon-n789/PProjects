# Coffee Machine
## About 
 ### It is a vending coffee machine that gives various coffee as per requirement.

---

 Menu consists of different coffees:-
 1. Latte - $2.5
2. Expresso - $1.5
3. Cappucino - $3

A person can order a coffee type by giving the input as the name of the coffee.

If there is enough resources then the machine will process the coffee.

After that it will ask for money and the person has to put the amount, if sufficient amount of money given then machine will deliver the needed coffee.

If cash is not enough, machine will refund the money.

---
## Coding Details

### It consists of 4 files
###  1. `main.py`
### 2. `menu.py`
### 3. `coffee_maker.py`
### 4. `money_machine.py`

---

Each file has specific work: -
 1. `main.py`

       It consists of entire workflow of the machine, giving of input and calling of methods for coffee making and money insertion also.
2. `menu.py`

      It consists of the menu of the coffee, what resources needed to make a particular coffee type.
3. `coffee_maker.py`

    It checks for the resources, if sufficient present then makes the particular coffe type.

    It also has the report about the resources. These can be checked by typing "Report" in the input.
4. `money_maker.py`

      The calculation of amount and the storing of amount takes place here. The machine checks the amount given by the person for the particular order and gives the change amount for it also. 

      If the given amount by the person is not sufficient then it gives output as "Sorry that's not enough money, Money refunded."

      Report about the total amount collected can also be seen by the machine by writing input as "Report".

---

Try and Enjoy the Virtual Coffee Machine!!