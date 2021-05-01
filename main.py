from Dao import Dao


def db_insert(mot, definition):
    dao = Dao()
    dao.insert(mot, definition)


if __name__ == '__main__':
    print('**********************************************')
    print('traitement en cours..')
    dico = {}
    with open('dico.txt', 'r', encoding="utf-8") as f:
        # content = [line.strip() for line in f]
        for line in f:
            if len(line.strip()) > 0:
                array_line = line.strip().split(' ', 1)
                if len(array_line) > 1:
                    # print(array_line[0]+' : '+array_line[1].strip())
                    dico[array_line[0]] = array_line[1].strip()

                    print('insertion mot : {}..'.format(array_line[0]))
                    db_insert(array_line[0], array_line[1].strip())

    print('**********************************************')
