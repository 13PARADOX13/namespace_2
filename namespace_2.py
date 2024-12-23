def test_function():
    def inner_function():
        x = 'Я в области видимости функции test_function'
        print(x)
        return x
    inner_function()

test_function()
inner_function()