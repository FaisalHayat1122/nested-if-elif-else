mood=input("Enter your mood(happy/sad/tired):").lower()
budget=iNt(input("Enter your budget(pkr):"))
weather=input("weather today?(sunny/rainy/cold):").lower()
company=input("Who are you with?(alone/friemd/family):").lower()


print("\n Planning Weakend \n")

if mood=="happy":
    if budget>1000:
        if weather =="sunny":
            if company == "friend":
                print("Dear {name},go for and outdoor movie:")
            else:
                print("watch b;ock Buster movie")
        else:
            print("Order pizza + netflix")
    else:
        print("Watch Comedy movie on mobile with snacks")
elif mood =="sad":
    if compamy == "alone":
        print("Watch motivational movie and order comfort food!")
    else:
        if budget > 500:
            print("Ice-Cream + feel good movie with loved one")
        else:
            print("Tea+old classic movie")
elif mood =="Tired":
    if weather =="cold":
        print("Sleep-early + light music!")
#    elifmood==tired:
        if budget >300:
            print("Fast-food + and watch comedy movie!")
    else:
        print("Relax with music or book!")
        
else:
    print("Mood not recognized, just relax and enjoy yourself!")