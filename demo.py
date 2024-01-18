import streamlit as st

st.title("Hello Streamlit")

st.header("Header")

st.subheader("Sub Header")

st.text("like this video and subscribe to the channel")

st.markdown("""
# h1 tag
## h2 tag
### h3 tag
""")

st.markdown("""
:moon:<br>
:sunglasses:<br>
:heart:
""",True)

st.markdown("""
**this is bold text**<br>
__this is italic text__
""",True)

st.write('Emon Hasan','is a','Data Scientist')

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')

st.write('# Emon Hasan is a Machine Learning Engineer')

st.write(st)

d = {
    'name':'emon',
    'language':'python',
    'expert':'Machine Learning'
}
st.write(d)
