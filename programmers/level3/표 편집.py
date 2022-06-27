class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solution(n, k, cmd):
    stack = []

    head = Node(0)
    this = head
    select = head

    answer = ['O' for _ in range(n)]

    for x in range(1, n):
        this.right = Node(x, left=this)
        this = this.right
        if x == k:
            select = this

    for c in cmd:
        c = c.split()
        if c[0] == 'U':
            for _ in range(int(c[1])):
                if select.left is not None:
                    select = select.left
                else:
                    break
        elif c[0] == 'D':
            for _ in range(int(c[1])):
                if select.right is not None:
                    select = select.right
                else:
                    break
        elif c[0] == 'C':
            answer[select.value] = 'X'
            stack.append(select)

            if select.left is not None:
                select.left.right = select.right

            if select.right is not None:
                select.right.left = select.left

            if select.right is None :
                select = select.left
            else:
                select = select.right

        elif c[0] == 'Z':
            restorenode = stack.pop()
            answer[restorenode.value] = 'O'

            if restorenode.left is not None:
                restorenode.left.right = restorenode

            if restorenode.right is not None:
                restorenode.right.left = restorenode


    return ''.join(answer)