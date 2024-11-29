import os
import time
import pyautogui


def open_calculator():
    """
        Открывает приложение калькулятора в зависимости от операционной системы.
    """
    if os.name == 'nt':  # Windows
        os.system('start calc')
    elif os.name == 'posix':  # macOS или Linux
        os.system('open -a Calculator')
    else:
        raise Exception("Неизвестная операционная система")


def locate_and_click(button_image):
    """
        Находит и нажимает кнопку на экране калькулятора.
    """
    button_location = pyautogui.locateOnScreen(button_image, confidence=0.9)
    if button_location is not None:
        pyautogui.click(button_location)
        time.sleep(0.1)  # Пауза между нажатиями
    else:
        raise Exception(f"Кнопка {button_image} не найдена на экране.")


def calculate():
    """
        Выполняет операцию сложения (12 + 7) в калькуляторе.
    """
    time.sleep(1)
    locate_and_click('images/1.png')
    locate_and_click('images/2.png')
    locate_and_click('images/plus.png')
    locate_and_click('images/7.png')
    locate_and_click('images/equal.png')

    result = pyautogui.locateOnScreen('images/result.png', confidence=0.9)
    if result is None:
        raise Exception("Результат не совпадает с ожидаемым.")
    else:
        print("Результат совпадает с ожидаемым.")
        pyautogui.hotkey('alt', 'f4')  # Закрытие калькулятора


def main():
    """
        Главная функция, которая запускает калькулятор и выполняет сложение.
    """
    open_calculator()
    calculate()


if __name__ == "__main__":
    main()
