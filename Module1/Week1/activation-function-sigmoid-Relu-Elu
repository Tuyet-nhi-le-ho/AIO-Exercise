import math


def is_number(x):
    try:
        float(x)  # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


anpha = 0.01


def calc_activation_function():
    x = input('Input x= ')  # nhập giá trị x và kiểm tra x với hàm is_number
    if not is_number(x):
        print('x must be a number!')
        return

    # nhập tên activation function
    activation_func_name = input(
        'input activation function (sigmoid,Relu,Elu): ')
    x = float(x)  # convert x sang float type
    if activation_func_name not in ['sigmoid', 'Relu', 'Elu']:
        # kiểm tra tên activation function có hợp lệ không
        print(f"{activation_func_name} is not supported!")
        return

    if activation_func_name == 'sigmoid':
        result = sigmoid(x)
    elif activation_func_name == 'Relu':
        result = relu(x)
    elif activation_func_name == 'Elu':
        result = elu(x)
    print(f"{activation_func_name} : f({x}) = {result}")
    return result


def sigmoid(x):
    return 1/(1+math.e**(-x))


def relu(x):
    return x if x > 0 else 0


def elu(x):
    return x if x > 0 else anpha*((math.e**x)-1)
