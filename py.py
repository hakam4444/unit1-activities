"""
Enter your home state: NY
Enter your home city: West Henrietta
Enter your street name: Dutchess Rd.
Enter your zip code: 14583
Enter your house number: 1347

Your mailing address is:
1347 Dutchess Rd.
West Henrietta , NY 14583


"""
state = input("Enter your home state: ")
city = input("Enter your home city: ")
street = str(input("Enter your street name: "))
zip = input("Enter your zip code: ")
house = input("Enter your house number: ")
print("your maling address is: \n "+ house + " " + 
    street + "\n" + city + " , " + state + " " + zip)