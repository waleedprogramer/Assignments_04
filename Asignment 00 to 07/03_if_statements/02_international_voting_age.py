PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def voting_age():
    user_age = int(input("How old are you? "))
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturkbouipo where the voting age is {PETURKSBOUIPO_AGE} ")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}")

    if user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE} ") 

    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE} ")    


    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE} ") 
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}")       
        



if __name__ == '__main__':
    voting_age()