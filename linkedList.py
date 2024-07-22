'''head = {
    "value": 11,
    "next": {
            "value": 12,
            "next": {
                    "value": 22,
                    "next": {
                        "value": 55,
                        "next": {
                                "value": 44,  """----------------> Tail"""
                                "next": None
                        }
                    }
            }
    }
}

print(head["next"]["next"]["value"])'''

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self,value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node

#     def pop(self):
#         if self.length ==0:
#             return None
#         temp = self.head
#         pre = self.head
#         while(temp.next):
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         return  temp.value

#     def prepend(self,value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length+=1
#         return True

#     def pop_first(self):
#         if self.length ==0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length-=1
#         if self.length ==1:
#             self.tail= None
#         return  temp
    
#     def get(self,index):
#         if index<0 or index>= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.index
#         return temp.value
    
#     def set_value(self,index,value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False



# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.print_list()
# print(my_linked_list.head.value)
# print(my_linked_list.tail.value)

# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# my_linked_list.prepend(1)
# my_linked_list.print_list()
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())


class Node:
    def __init__(self,value):
        self.value=value
        self.next =None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head = new_node
        self.tail =new_node
        self.length =1

    def print_list(self):
        temp =self.head
        while temp is not None:
            print(temp.value)
            temp= temp.next

    def append(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head =new_node
            self.tail =new_node
        else:
            self.tail.next = new_node
            self.tail =new_node
        self.length+=1
        return  True

    def pop(self):
        if self.length ==0:
            return None

        temp =self.head
        pre =self.head
        while temp.next is not None:
            pre =temp
            temp = temp.next
        self.tail =pre
        self.tail.next =None
        self.length-=1

        if self.length ==1:
            self.head =None
            self.tail =None
        return temp.value

    def preppend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head =new_node
            self.tail =new_node
        else:
            new_node.next=self.head
            self.head = new_node
        self.length+=1
        return True

    def popfirst(self):
        if self.length==0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length-=1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self,index):
        temp = self.head
        if index <0 or index>=self.length:
            return None
        else:
            for _ in range(index):
                temp = temp.next
            return temp.value


ll = LinkedList(0)
ll.append(3)
ll.append(8)
ll.append(10)
print(ll.get(2))


