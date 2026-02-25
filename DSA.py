#stack - LIFO or FILO
#operations 
#push --> add an element to the top of the stack
#pop --> remove the top element from the stack and return it
#peek --> return the top element without removing it
#isEmpty --> check if the stack is empty
#size --> return the number of elements in the stack

#Push
#1) create empty list to represent the stack
#2)input element to be added to the stack
#3)add value to stack
#4)print stack

#pseudo code for push operation
#push(data):
#if (stack is full):
#    print("Stack overflow")
#else:
#    top = top + 1
#    stack[top] = data

#pop
#1)check if stack is empty , if empty print stack underflow
#2)if stack is not empty, remove and return the top element
#3)print stack
#peak operation
# stack = []

# while True:
#     print("\n1.Push\n2.Pop\n3.peek\n4.Display\n5.Exit")
#     choice = int(input("Enter the choice :"))
#     if choice == 1:
#         val = int(input("Enter value"))
#         stack.append(val)
#         print("pushed",val)
#     elif choice == 2:
#         if not stack :
#             print("Stack Empty")
#         else:
#             print("popped",stack.pop())
#     elif choice ==3:
#         if not stack:
#             print("Stack Empty")
#         else:
#             print("Top")
#     elif choice == 4:
#         print("stack :",stack)
#     else:
#         print("Invalid Choice")
#         break

# queue operation
# enqueue - add an item at rear
# dequeue - remove an item from 

# queue = []

# while True:
#     print("\n1.Enqueue\n2.Dequeue\n3.peek\n4.Display\n5.Exit")
#     choice = int(input("Enter the choice :"))
#     if choice == 1:
#         val = int(input("Enter value :"))
#         queue.append(val)
#         print("added",val)
#     elif choice == 2:
#         if not queue :
#             print("queue Empty")
#         else:
#             print("removed",queue.pop())
#     elif choice ==3:
#         if not queue:
#             print("queue Empty")
#         else:
#             print("Front:",queue[0])
#     elif choice == 4:
#         print("queue :",queue)
#     else:
#         print("Invalid Choice")
#         break
#Circular queue
#reuse empty spaces
#save money
# if front is free,rear can reuse it
# n= 3
# queue=[None]*3
# front = 0
# rear = 0

# #import 
# queue[rear]=10
# rear =[rear+1]%size
# [10,------]
# [10.20 ----]
# [10.20.30]
# important conditions
# queue is full when (rear+1)%size 

# pseudocode
# enqueue
# 1. If queue full + print "Queue Full"
# 2. If first element + set front = 0
# 3. Move rear circularly
# 4. Insert element

# dequeue
# 1. If queue empty -->print "queue Empty"
# 2. Remove front element 
# 3. If last element removed + reset front & rear 
# 4. Else move front circularly

# Display
# if empty + print message
# start from front 
# print until rear

# step by step logic
# enqueue 
# 1. check full condition 
# 2. set front if first insert 
# 3.move rear using ModuleNotFoundError
# 4.insert missing