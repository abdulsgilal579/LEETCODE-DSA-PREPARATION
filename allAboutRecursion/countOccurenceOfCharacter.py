string = "bananaaaaaa"
character = "a"


def countOccurence(string, character):
    def counting(index):
        if index == 0:
            if string[index] == character:
                return 1
            return 0
        if string[index] == character:
            return 1 + counting(index - 1)
        return 0 + counting(index - 1)

    return counting(len(string) - 1)


print(countOccurence(string=string, character=character))
