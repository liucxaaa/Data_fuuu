class ListNode:
    def __init__(self):
        self.val = None
        self.next = None
class Linked_list:
    def __init__(self):#创建头节点
        self.node = ListNode()
    def create(self,x):#插入操作
        q = self.node
        for i in range(len(x)):
            p = ListNode()
            p.val = x[i]
            q.next = p
            q = p
    def add(self,x,p):#增加单个元素到p的后面
        p1 = ListNode()
        temp = self.node
        while(temp.next):
            if temp.val == p:
                p1.val = x
                p1.next = temp.next
                temp.next = p1
                return
            else:
                temp = temp.next
    def pop(self,x):#删除操作
        p = self.node
        if x == p.val:
            self.node = self.node.next
            return
        while(p.next):
            if p.next.val == x:
                p.next = p.next.next
                return
            else:
                p= p.next
    def get_size(self,x):#得到线性表的长度
        p  =self.node
        num = 1
        while(p.next):
            p = p.next
            num+=1
        return num
    def GetNo(self,x):#得到线性表中第一个值为x的序号
        temp = self.node
        num = 0
        while(temp.next):
            num +=1
            if temp.val == x:
                return num
            temp = temp.next
        if temp.val == x:
            return num+1
    def Getitem(self,x):#得到x的位置的值
        temp = self.node
        num = 0
        while(temp.next):
            num+=1
            if num == x:
                return temp.val
            temp = temp.next
        if num == x-1:
            return temp.val
    def SetElem(self,x,e):#把x的位置的值该为e
        temp = self.node
        num = 0
        while(temp.next):
            num+=1
            if num == x:
                temp.val = e
            temp = temp.next
        if num == x-1:
            temp.val = e
    def display(self):#展示所有元素
        temp = self.node.next
        while(temp.next):
            print(temp.val)
            temp = temp.next
        print(temp.val)
list1 = [1,2,3,4,5,6,7]
tt = Linked_list()
tt.create(list1)
tt.display()
# print(tt.Getitem(7))
# tt.add(2,4)
# tt.display()
# tt.pop(3)
# tt.display()
