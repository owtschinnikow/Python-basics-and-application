with open('dataset_24465_4.txt') as file, open('dataset_revers.txt', 'w') as revers:
    for line in file:
        revers.write(line)
    reversed(revers)