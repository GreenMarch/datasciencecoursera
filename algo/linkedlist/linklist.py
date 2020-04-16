class ListNode():  # 初始化 构造函数
    def __init__(self, value):
        self.value = value
        self.next = None


def Creatlist(n):
    if n <= 0:
        return False
    if n == 1:
        return ListNode(1)  # 只有一个节点
    else:
        root = ListNode(1)
        tmp = root
        for i in range(2, n + 1):  # 一个一个的增加节点
            tmp.next = ListNode(i)
            tmp = tmp.next
    return root  # 返回根节点


def printlist(head):  # 打印链表 （遍历）
    p = head
    while p != None:
        print(p.value)
        p = p.next


def listlen(head):  # 链表长度
    c = 0
    p = head
    while p != None:
        c = c + 1
        p = p.next
    return c


def insert(head, n):  # 在n的前面插入元素
    if n < 1 or n > listlen(head):
        return

    p = head
    for i in range(1, n - 1):  # 循环四次到达 5  （只能一个一个节点的移动 range不包含n-1）
        p = p.next
    a = input("Enter a value:")
    t = ListNode(value=a)
    t.next = p.next
    p.next = t
    return head


def dellist(head, n):  # 删除链表
    if n < 1 or n > listlen(head):
        return head
    elif n is 1:
        head = head.next  # 删除头
    else:
        p = head
        for i in range(1, n - 1):
            p = p.next  # 循环到达 2次
        q = p.next
        p.next = q.next  # 把5放在3的后面
    return head


def main():
    print("Create a linklist")
    head = Creatlist(7)
    printlist(head)
    print
    print
    "___________________________"

    n1 = input("Enter the index to insert")
    n1 = int(n1)
    insert(head, n1)
    printlist(head)
    print()
    print("___________________________")

    n2 = input("Enter the index to delete")
    n2 = int(n2)
    dellist(head, n2)
    printlist(head)


if __name__ == '__main__':  main()  # 主函数调用