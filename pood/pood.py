import string

product = []  # полка продуктов
prices = []  # цена продуктов в магазине
basket = []  # корзина покупателя
pricebasket = []  # цены товаров в корзине
buy = []  # купленные товары покупателем
pricebuy = []  # цены покупак


def buyy():
    """Функция которая помещает товары из корзины в покупки и выдаёт чек"""
    print("Bill".center(20, "="))
    print("Product".ljust(8), "Hind")

    summ = 0
    for i in range(len(basket)):
        summ += int(pricebasket[i])
        buy.append(basket[i])
        pricebuy.append(pricebasket[i])
        print(f"{basket[i]} ---> {pricebasket[i]}$")

    basket.clear()
    pricebasket.clear()
    print()
    print(f"summ: {summ}$")
    print("".center(20, "="))


def summ():
    """Выдаёт общую сумму покупок"""
    summ = 0
    for i in pricebuy:
        summ += int(i)
    print(f"Общая сумма: {summ}")


def take():
    """Поместить из товаров магазина в корзину"""
    access = int(input("Введите количество: "))
    for i in range(access):
        product = input("-> Введите товар: ")
        if product in productss:
            basket.append(product)
            ind = productss.index(product)
            pricebasket.append(pricess[ind])
        else:
            print("Такого продукта нет!")
            continue


def sort():
    """Сортировка по ценам"""
    if len(buy) == 0:
        return "Ne hvataet"

    for i in range(len(buy) - 1):
        for i in range(len(buy) - 1):
            if pricebuy[i] > pricebuy[i + 1]:
                pricebuy[i], pricebuy[i + 1] = pricebuy[i + 1], pricebuy[i]
                buy[i], buy[i + 1] = buy[i + 1], buy[i]

    print("".center(70, "="))


def sortalpha():
    """Сортировка по алфавиту"""
    if len(buy) == 0:
        return "Ne hvataet"

    xlist = [i for i in zip(buy, pricebuy)]
    xlist = sorted(xlist)
    print(xlist)


def maxx():
    """Макс. цена в покупках"""
    id = pricebuy.index(max(pricebuy))
    print(buy[id], pricebuy[id])


def minn():
    """Мин. цена в покупках"""
    id = pricebuy.index(min(pricebuy))
    print(buy[id], pricebuy[id])


def get():
    """Получить продукт"""
    xproduct = str(input("Введите товар: "))

    id = buy.index(xproduct)

    print(buy[id], pricebuy[id])

    print("".center(70, "="))


def getproduct():
    """Посмотреть список товаров в магазине"""
    for i, j in zip(productss, pricess):
        print(f"{i} ---> {j}")


def help():
    """Посмотреть возможные функции"""

    print("-----> buy - поместить из корзины в покупки")
    print("-----> summ - посмотреть сумму покупок")
    print("-----> take - взять в корзину")
    print("-----> sort - сортировка по возрастанию")
    print("-----> sortalpha - сортировка по алфавиту")
    print("-----> max - посмотреть самый дорогой товар в покупках")
    print("-----> min посмотреть самый дешёвый товар в покупках")
    print("-----> get - посмотреть продукт в наличии")
    print("-----> getproduct - просмотреть список продуктов в магазине")


productss = ["apple", "orange", "pear", "banana", "grape", "fish", "sea", "pork"]  # Товары в магазине
pricess = [90, 120, 90, 130, 120, 430, 320, 350]  # Цены товаров в магазине


while True:
    """Магазин продуктов"""
    try:

        access = str(input("-----> Введите значение: "))

        if access == "new":
            inp = int(input("-----> Введите количество элементов: "))
            print("products".center(20, "="))

            for i in range(inp):
                xproduct = str(input("-----> Введите продукт: "))
                yprice = int(input("-----> Введите цену продукта: "))

                productss.append(xproduct)
                pricess.append(yprice)

            print("".center(20, "="))

        elif access == "exit":
            break
    except:
        pass


while True:
    """Покупатель"""
    try:
        print("Pood".center(70, "="))
        print(f"В корзине: \nтовар: {basket} цена: {pricebasket}")
        print(f"В покупках: \nтовар:{buy} цена: {pricebuy}")
        print("".center(70, "-"))

        access = input("---> Введите значение: ")

        if access == "take":
            take()

        elif access == "sort":
            sort()

        elif access == "max":
            maxx()

        elif access == "min":
            minn()

        elif access == "get":
            get()

        elif access == "getproducts":
            getproduct()

        elif access == "buy":
            buyy()

        elif access == "summ":
            summ()

        elif access == "sortalpha":
            sortalpha()

        elif access == "help":
            help()

    except:
        pass
