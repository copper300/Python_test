a = 1
# uses global because there is no local 'a'
def f():
    print("Inside f() : %d" % a)

# Variable 'a' is redefined as a local
def g():
    a = 2
    print("Inside g() : %d" % a)

# Use global keyword to modify global 'a'
def h():
    global a
    a = 3
    print("Inside h() : %d" % a)

# Global scope
print("global : %d" % a)
f()

print("global : %d" % a)
g()

print("global : %d" % a)
h()

print("global : %d" % a)

