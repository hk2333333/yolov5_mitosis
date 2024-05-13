import os
import sys

if __name__ == '__main__':
    train_path = 'train_img'
    test_path = 'test_img'

    train_items = os.listdir(train_path)
    test_items = os.listdir(test_path)

    train_indices = []
    test_indices = []

    for train_item in train_items:
        train_index = train_item.split('.png')[0]
        train_indices.append(train_index)

    for test_item in test_items:
        test_index = test_item.split('.png')[0]
        test_indices.append(test_index)

    train_file_name = 'train.txt'
    test_file_name = 'test.txt'

    with open(train_file_name, 'w') as file:
        for train_index in train_indices:
            file.write(train_index + "\n")

    with open(test_file_name, 'w') as file:
        for test_index in test_indices:
            file.write(test_index + "\n")

    print(f"{train_file_name} has created!!!")
    print(f'{test_file_name} has created!!!')
