arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(arr, n):
    # primeiramente precisamos setar valores iniciais e finais do array ou lista
    small = 0
    high = len(arr) - 1

    # logo em seguida um loop para enquanto que o valor menor for menor ou igual ao valor mais alto do array continuar iterando
    while small <= high:
        # pego o meio do array para começar a busca
        mid = (small + high) // 2
        # faço uma variavel de chute na posição do meio
        shot = arr[mid]

        # faço as verificações para saber se o chute está certo
        if shot == n:
            return mid
        # caso não esteja seto o meio para um valor menor ou maior dependendo do chute
        if shot > n:
            high = mid - 1
        else:
            small = mid + 1
    return None


print(binary_search(arr, 1))
