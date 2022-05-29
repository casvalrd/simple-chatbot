class bot:
    def database(self, act):
        if act == "read":
            path_source = open(r'wordlist.txt')
            try:
                read_file = path_source.read()
                split_word = read_file.splitlines()
                return split_word
            except IOError:
                print("Can't found your file location.")
            finally:
                path_source.close()

    def matching(self, word):
        db = self.database("read")

        for line in db:
            separate = line.split('|')
            if word == separate[0]:
                print(separate[1])

    def __init__(self):
        while True:
            user = input('>> ')

            if user == "exit":
                self.matching(user)
                break
            else:
                self.matching(user)


if __name__ == '__main__':
    bot()
    exit()
