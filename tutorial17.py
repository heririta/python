#17. Optional Parameters

def func(x) : 
    print(x)
/
func('hello')

#def func2(x, text) : 
def func2(x, text = '2') : 
    print(x)
    if(text == '1') : 
        print('text is 1')
    else : 
        print('text it not 1')

func2('heri','1')
func2('3')
func2('3','1')
