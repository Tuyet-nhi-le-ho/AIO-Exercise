import math
import random


def calc_regression_loss_function():

    num_samples = input('input number of samples(integer number) = ')
    if not num_samples.isnumeric():
        print('number of samples must be an integer number!')
        return
    loss_name = input('input loss name (MAE, MSE): ')
    final_loss = 0
    num_samples = int(num_samples)

    for i in range(num_samples):

        y = random.uniform(0, 10)
        y_hat = random.uniform(0, 10)
        if loss_name == 'MAE':
            calc_mae(y, y_hat)

        elif loss_name == 'MSE':
            loss = calc_mse(y, y_hat)
            final_loss += loss
        print(
            f"loss name: {loss_name}, sample:{i},predict: {y_hat}, target: {y}")
    final_loss /= num_samples
    if loss_name == 'RSME':
        final_loss = math.sqrt(final_loss)
    print(f"Final {loss_name} : {final_loss}")


def calc_mae(y, y_hat):
    return abs(y-y_hat)


def calc_mse(y, y_hat):
    return (y-y_hat)**2
