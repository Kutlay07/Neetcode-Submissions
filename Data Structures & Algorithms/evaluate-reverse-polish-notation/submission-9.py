class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        arr=tokens

        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                st.append(int(token))
            else:
                b = st.pop()
                a = st.pop()

                if token == "+":
                    st.append(a + b)
                elif token == "-":
                    st.append(a - b)
                elif token == "*":
                    st.append(a * b)
                else:
                    st.append(int(a / b))
        return st[-1]