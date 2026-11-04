# stack_mullet.py

word = "MULLET"

print("=== PART 1: STACK ALGORITHM (LIFO) ===\n")

# Phase 1: PUSH
print("--- Phase 1: PUSH ---")
stack = []
for char in word:
    stack.append(char)
    print(f"Push {char:<5} | Current Stack: {stack}")

print("\n--- Phase 2: POP ---")
# Phase 2: POP
while len(stack) > 0:
    removed = stack.pop()  # LIFO: Remove from the top/end
    print(f"Pop {removed:<6} | Current Stack: {stack}")