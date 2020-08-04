import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_items(browser):
    browser.get(link)
    time.sleep(5)
    btn = browser.find_element_by_class_name('btn-add-to-basket')
    print("\nТекст кнопки: " + btn.text)
    assert len(btn.text) > 0, "Кнопка не найдена"
