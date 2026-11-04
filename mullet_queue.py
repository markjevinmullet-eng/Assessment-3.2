# queue_mullet.py

word = "MULLET"

print("=== PART 2: QUEUE ALGORITHM (FIFO) ===\n")

# Phase 1: ENQUEUE
print("--- Phase 1: ENQUEUE ---")
queue = []
for char in word:
    queue.append(char)
    print(f"Enqueue {char:<2} | Current Queue: {queue}")

print("\n--- Phase 2: DEQUEUE ---")
# Phase 2: DEQUEUE
while len(queue) > 0:
    removed = queue.pop(0)  # FIFO: Remove from the front
    print(f"Dequeue {removed:<2} | Current Queue: {queue}")