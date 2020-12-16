
def test_add_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), f'Basket button not found'
