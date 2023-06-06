import time as t

class Library:

    def __init__(self, listofbooks, libraryname):
        self.name = libraryname
        self.listofbooks = listofbooks
        self.no_of_books = len(listofbooks)
        self.returned = "name"

    def printbooks(self):
        return f"List of books: {self.listofbooks}"

    @property
    def donatebook(self):
        return self.listofbooks

    @staticmethod
    def lendreturnbook(name, book, value, dictmain):
        namein = name
        bookin = book
        valuein = value

        def getfunc():

            if valuein == "get" and bookin not in dictmain:
                new = {f"{bookin}":f"{namein}"}
                dictmain.update(new)
                print(dictmain)
                return "Return book before due"
            elif valuein == "get" and bookin in dictmain:
                print(dictmain)
                return f"Sorry, {bookin} is assigned to {dictmain[bookin]}."

        def retfunc():
            if valuein == "ret" and bookin in dictmain:
                del dictmain[bookin]
                print(dictmain)
                return f"Thank you! visit again!"
            elif valuein == "ret" and bookin not in dictmain:
                print(dictmain)
                return f"Use the donate command to donate"

        def dnet():

            if valuein == "dnet":
                listofbooks.append(bookin)
            return "Thank you very much!"


        if valuein == "get":
            print(getfunc())
        elif value == "ret":
            print(retfunc())
        elif value == "dnet":
            print(dnet())
        elif value == "B":
            print(listofbooks)
        print(dictmain)

listofbooks = ["Dead poets society", "A thousand splendid suns", "Thinking Fast and slow", "Black Swan", "Hyperfocus",
               "Zarathustra", "God is dead"]

Oxford = Library(listofbooks, "Oxford")

dictmain = {}

def use(name, inp):
    name = name
    if len(inp)>2:
        value, book = inp.split(maxsplit=1)
        Oxford.lendreturnbook(name, book, value, dictmain)

        def filesave(bookin, namein, valuein, dictmain):
            timenow = t.ctime(t.time())
            with open("log.txt", "a") as f:
                f.write(f"\ntime: {timenow}\n{bookin}: {namein} {valuein}\n {dictmain}")

        filesave(book, name, value, dictmain)
    elif inp == "B":
        print(Oxford.printbooks())


if __name__ == '__main__':

    while True:
        name = input("Enter your name: ")
        inp = input(f"Type 'B' if you want to see all the list of books\n"
                    f"Type 'get' and with a space 'bookname' if you want a book\n"
                    f"Type 'ret' and with a space 'bookname' to return a book\n"
                    f"Type 'dnet' and with a space 'bookname' to donate a book\n"
                    f"Enter your input: ")
        use(name, inp)
