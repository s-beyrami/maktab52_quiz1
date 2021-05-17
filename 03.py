from typing import Generator, Iterator


def read():
    with open("test.txt") as f:
        temp = f.readline()
        # print(temp)
        templist = temp.split()
        # print(templist)
        for word in templist:
            temp = [char for char in word]
            for character in temp:
                if temp.count(character) > 1:
                    yield "".join(temp)
                    break

#
# def generator(n):
#  for i in range(n):
#  yield i ** 2
