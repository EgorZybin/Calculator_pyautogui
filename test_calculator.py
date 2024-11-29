from CalculatorScript import locate_and_click, open_calculator
import time


def test_locate_and_click():
    """
        Тест проверки наличия кнопки на экране.
    """
    button_images = [
        'images/1.png',
        'images/2.png',
        'images/plus.png',
        'images/7.png',
        'images/equal.png'
    ]

    try:
        for image in button_images:
            locate_and_click(image)
            time.sleep(1)
        print("Тест пройден: Все кнопки отработали")
    except Exception as e:
        print(f"Тест не пройден: {e}")


if __name__ == "__main__":
    open_calculator()
    time.sleep(1)
    test_locate_and_click()
