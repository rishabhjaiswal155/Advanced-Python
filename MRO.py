#MRO(Method Resolution Order)
#C3 Algorithm
#DLR(Depth First Left to Right)

class A:pass         #A.mro()=AO 
class B:pass         #B.mro()=BO 
class C:pass         #C.mro()=CO
class X(A,B):pass    #X.mro()=XABO
class Y(B,C):pass    #Y.mro()=YBCO
class P(X,Y,C):pass	 #P.mro()=P+Merge(X.mro(),Y.mro(),C.mro(),XYC)
print(P.mro())       #       =P+Merge(XABO,YBCO,CO,XYC)
					 #       =P+X+Merge(ABO,YBCO,CO,YC)
					 #       =P+X+A+Merge(BO,YBCO,CO,YC)
					 #		 =P+X+A+Y+Merge(BO,BCO,CO,C)
					 #       =P+X+A+Y+B+Merge(O,CO,CO,C)
					 #       =P+X+A+Y+B+C+Merge(O,O,O)
					 #       =P+X+A+Y+B+C+O