import operator


tareas = {}

def nombre_tarea():
    a = input("")
    return a

def valor():
    while True:
        try:
            b = int(input())
            return b
        except ValueError:
            print("No admitido")

def main():
    while input("Desea agregar una tarea: presione A") == "A":
        print("introduzca una tarea: ")
        tarea = name()
        print("Valor epistemico para la tarea: ")
        valor = valor()
        tareas[tarea] = valor
    cx = sorted(tareas.items(), key=operator.itemgetter(1), reverse=True)
    print("Orden:  {} ".format(cx))

    for a in cx:
        print("primero has: {}".format(a))
        while input("Has realizado esta tarea Si/no") == "no":
            print("La siguiente tarea ha realizar es " + a)

        


if __name__ == "__main__":
    main()

    