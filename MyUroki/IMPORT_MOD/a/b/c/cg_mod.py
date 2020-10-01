print("*"*10, "cg_mod init!", "*"*10)
y=10
#import a.b.b_mod as b_mod
from .. import b_mod
print(b_mod.v)