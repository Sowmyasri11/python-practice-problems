from collections import deque

ticket_queue = deque()
print(ticket_queue)

#people arrive to the queue
ticket_queue.append("John")
ticket_queue.append("Jane")
ticket_queue.append("Linda")

print(ticket_queue)

#people bought their tickets
print(ticket_queue.popleft())

print(ticket_queue.popleft())
print(ticket_queue.popleft())

#no people left in the queue

print(ticket_queue.popleft())



recent_files = deque(["core.py", "README.md", "__init__.py"], maxlen=3)

recent_files.appendleft("database.py")
print(recent_files)
recent_files.appendleft("requirements.txt")
print(recent_files)

