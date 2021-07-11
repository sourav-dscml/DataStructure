
# you can use this to sort strings too
def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break

def bubble_sort_key(elements,key=None):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j][key] > elements[j+1][key]:
                tmp = elements[j][key]
                elements[j][key] = elements[j+1][key]
                elements[j+1][key] = tmp
                swapped = True

        if not swapped:
            break



if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3,4,2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    # bubble_sort(elements)
    # print(elements)
    bubble_sort_key(elements, key='transaction_amount')
    print(elements)
    