class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        arr=tokens

        for i in range(len(arr)):
            if arr[i]=="+" or arr[i]=="-" or arr[i]=="*" or arr[i]=="/":
                if st:
                    b=int(st.pop())
                    a=int(st.pop())

                    if arr[i]=="+":
                        st.append(a+b)
                    if arr[i]=="*":
                        st.append(a*b)
                    if arr[i]=="-":
                        st.append(a-b)
                    if arr[i]=="/":
                        st.append(int(a/b))
            else:
                st.append(arr[i])
        return int(st.pop())