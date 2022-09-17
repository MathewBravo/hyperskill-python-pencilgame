import random


def assign_current_player(player: str) -> str:
    if player == "John":
        return "Jack"
    else:
        return "John"


def turn(player: str, pencils: []):
    pickup = 0
    if player == "John":
        print(player + "'s turn!")
        pickup = input()
        while not validate_pickup_count(pickup):
            pickup = input()
    else:
        print(player + "'s turn:")
        if not len(pencils) == 1 and (len(pencils) - 1) % 4 == 0:
            pickup = random.randint(1,3)
            print(pickup)
        elif len(pencils) == 4:
            pickup = 3
            print("3")
        elif len(pencils) == 3:
            pickup = 2
            print("2")
        elif len(pencils) == 2 or len(pencils) == 1:
            pickup = 1
            print(pickup)
        else:
            pickup = int((len(pencils) - 1) % 4)
            print(pickup)
    for i in range(0, int(pickup)):
        pencils.pop()
    if len(pencils) > 0:
        print(*pencils, sep="")


def validate_pickup_count(pickup) -> bool:
    try:
        int(pickup)
        pickup = int(pickup)
        if not pickup > 0 or not pickup <= 3:
            print("Possible values: '1', '2' or '3'")
            return False
        elif pickup > len(pencil_display):
            print("Too many pencils were taken")
            return False
        else:
            return True
    except ValueError:
        print("Possible values: '1', '2' or '3'")
        return False


def validate_pencil_count(userinput) -> bool:
    try:
        int(userinput)
        userinput = int(userinput)
        if not userinput > 0:
            print("The number of pencils should be positive")
            return False
        return True
    except ValueError:
        print("The number of pencils should be numeric")
        return False


def validate_player_name(playername) -> bool:
    if playername == "John" or playername == "Jack":
        return True
    else:
        print("Choose between 'John' and 'Jack'")
        return False


if __name__ == '__main__':
    pencil = "|"
    print("How many pencils would you like to use:")
    count_validation = False
    while not count_validation:
        pencil_count = input()
        count_validation = validate_pencil_count(pencil_count)
    pencil_display = []
    for i in range(0, int(pencil_count)):
        pencil_display.append(pencil)
    print("Who will be the first (John, Jack):")
    player_validation = False
    player = "John"
    computer = "Jack"
    while not player_validation:
        current_player = input()
        player_validation = validate_player_name(current_player)
    print(*pencil_display, sep="")
    while len(pencil_display) > 0:
        turn(current_player, pencil_display)
        current_player = assign_current_player(current_player)
    if len(pencil_display) == 0:
        print(current_player + " won!")