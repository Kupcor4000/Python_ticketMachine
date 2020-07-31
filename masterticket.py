import sys
TICKET_PRICE = 10

def total_price(tickets):
    if tickets > tickets_remaining or tickets <= 0:
        raise ValueError("Ta liczba biletów nie jest dozwolona!")
    return tickets*TICKET_PRICE


tickets_remaining = 100  

while tickets_remaining != 0:
    #Output how many tickets are remaining using the tickets_remaining variable
    print("Tickets availbe: {}".format(tickets_remaining))
    print("")
    
    #personalize user experience
    #grab user name and welcome him
    name = input("What is your name dear user? ")
    print("Welcome in our shop {}!".format(name))
    
    #request a certain amount of tickets and type a total cost
    #bilety powinny się odejmywać od całości
    try:
        amount_of_tickets = int(input("How many tickets do you want to buy {}? ".format(name)))
        print("Całkowita cena z {} bilety wynosi {}".format(amount_of_tickets,total_price(amount_of_tickets)))
        solding = input("Do you want to continue buying {} tickets? Y/N ".format(amount_of_tickets)) #Y/N
        
        if solding.upper() == "Y": 
            tickets_remaining -= amount_of_tickets
            print("SOLD! Thank you for your purchasing Mr. {}".format(name))
        else:
            print("Thank you anyway, see you soon Mr. {}".format(name))
    except ValueError as err:   # aby nie przekraczał granicy (0, tickets_remaining)
        print("Niewykonalna operacja!")
        print("{}".format(err))
    else:
        print("Dziękujemy za zakupy {}!".format(name))
        
print("")
print("Wszystkie bilety zostały wyprzedane zapraszamy innym razem!")
        