# 09. Logical Operators in Python: and, or, not
# Used to combine conditional statements.

has_id = True
has_ticket = False
is_vip = True

print(f"has_id: {has_id} | has_ticket: {has_ticket} | is_vip: {is_vip}\n")

# 1. 'and' operator (True only if BOTH operands are True)
can_enter_general = has_id and has_ticket
print(f"can_enter_general (has_id and has_ticket): {can_enter_general}")

# 2. 'or' operator (True if AT LEAST ONE operand is True)
can_enter = has_ticket or is_vip
print(f"can_enter (has_ticket or is_vip)         : {can_enter}")

# 3. 'not' operator (Inverts the boolean value)
needs_ticket = not has_ticket
print(f"needs_ticket (not has_ticket)            : {needs_ticket}")
