def solution(phone_book):
    phone_book.sort()

    for x in range(len(phone_book) - 1):
        if phone_book[x] == phone_book[x + 1][:len(phone_book[x])]:
            return False
    return True