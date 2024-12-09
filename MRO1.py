#MRO Example

class D:pass       #D.mro()=DO
class E:pass       #E.mro()=EO
class F:pass       #F.mro()=FO
class B(D,E):pass  #B.mro()=BDEO
class C(D,F):pass  #C.mro()=CDFO
class A(B,C):pass  #A.mro()=A+Merge(B.mro(),C.mro(),BC)
print(A.mro())     #       =A+Merge(BDEO,CDFO,BC)
				   #       =A+B+Merge(DEO,CDFO,C)
				   #       =A+B+C+Merge(DEO,DFO)
				   #       =A+B+C+D+Merge(EO,FO)
				   #       =A+B+C+D+E+Merge(O,FO)
				   #       =A+B+C+D+E+F+Merge(O,O)
				   #	   =A+B+C+D+E+F+O
	