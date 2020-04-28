"""
2. Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.
"""
from collections import Counter
import sys
sys.setrecursionlimit(1999999)


class MyNode:
    def __init__(self, value, letter="", left=None, right=None):
        self.letter = letter
        self.value = value
        self.left = left
        self.right = right

    def merge(self, secondNode):
        outputNode = MyNode(value=self.value + secondNode.value, left=self, right=secondNode, letter="")
        self.value = 0
        secondNode.value = 0
        return outputNode

    def search(self, char, path=""):
        if self.letter == char:
            return 1, path
        if self.left is not None:
            res = self.left.search(char, path+"0")
            if res[0] == 1:
                return res
        if self.right is not None:
            res = self.right.search(char, path+"1")
            if res[0] == 1:
                return res
        return path


if __name__ == "__main__":
    # S = "beep boop beer!"
    S = str(input("Введите любую строку для кодирования по методу Хоффмана: "))

    #Если в введенной строке есть только одна разновидность символа, то нужно добавить вторую
    if len(set(S)) == 1:
        S += chr(ord(S[0])-1)

    cntr = Counter(S)
    least_common = cntr.most_common()
    least_common.reverse()
    least_common = [MyNode(value=i[1], letter=i[0]) for i in least_common]

    while len(least_common) > 1:
        left = least_common.pop(0)
        right = least_common.pop(0)
        mergedNode = left.merge(right)
        insert_pos = 0
        for i in range(len(least_common)):
            if mergedNode.value > least_common[i].value:
                insert_pos = i + 1
        least_common.insert(insert_pos, mergedNode)

    alphabet = {}
    for letter in set(S):
        alphabet[letter] = least_common[0].search(letter)[1]

    output = " ".join([alphabet[i] for i in S])
    print("Закодированная строка: %s" % output)
    print("Коды символов:", alphabet)

    """
    Таки закодировал :) Про раскодирование в задании ни слова
    """