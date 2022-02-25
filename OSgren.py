question = input("Finns det stöd för sporten?: ")
if question == "ja":                                                                                            
    question = input("Är det en sport?: ")
    if question == "ja":
        question = input("Kan ett flertal länder delta i sporten?: ")
        if question == "ja":
            question = input("Är det en vinter gren?: ")
            if question == "ja":
                question = input("Kan den spelas i OS vintermiljö?: ")
                if question == "ja":
                    print("Inför sporten")
                
                
                elif question == "nej":
                    print("Den är inte lämplig nog för Vinter OS")
            
        elif question == "nej":
            print("Den är inte utspridd nog")

    elif question == "nej":
        print("Det är ingen utövad sport")
elif question == "nej":
    print("Det finns inget stöd")   


