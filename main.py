from oktagon import Oktagon #Импортируем класс

def main(): #Создаем функцию 
    oktagon = Oktagon(8) #Добавляем объект
    oktagon.plo() #Используем все имеющиеся методы
    oktagon.per()
    oktagon.opis_okr()
    oktagon.vpis_okr()
    oktagon.pic()

if __name__ == '__main__': 
    main() 