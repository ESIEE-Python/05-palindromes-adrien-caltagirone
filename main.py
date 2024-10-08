"""Module"""
#### Fonction secondaire
import unicodedata

def ispalindrome(string) -> bool:
    """ Palindrome function """
    

    string = unicodedata.normalize('NFKD', string)
    string = string.lower().replace(" ","")

    if string == "":
        return True

    if len(string) == 1:
        return True

    if string[0] != string[-1]:
        return False

    return ispalindrome(string[1:-1])


#### Fonction principale


def main():
    """ Main """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
