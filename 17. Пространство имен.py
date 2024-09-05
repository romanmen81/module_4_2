def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function() # Вызовем inner_function внутри test_function

test_function() # Вызовем test_function

"""
inner_function() # Это вызовет ошибку, так как inner_function недоступна за пределами test_function

"""
