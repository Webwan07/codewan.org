import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import info as io
import functions as ft
import pyperclip

st.set_page_config(page_title="Code Wan",
                   initial_sidebar_state='auto')

# Load the data from the file system if it exists, otherwise initialize an empty dictionary
try:
    with open("data.pkl", "rb") as f:
        data = pickle.load(f)
except FileNotFoundError:
    data = {}

with st.sidebar:
    selectedInfo = option_menu(
        menu_title=None,
        options=["About","Settings","Rate us"],
        default_index=0,
        icons=["info-square","gear","star-half"],
        styles={"nav-link-selected": {"background-color": "#8D72E1"}}
    )
    if selectedInfo == "About":
        st.markdown(f'''<p id="copyright">{io.aboutME}</p>''',
                unsafe_allow_html=True)
        
    elif selectedInfo == "Settings":
        selectedSettings = st.selectbox(" ",ft.settingsList)

        if selectedSettings == ft.settingsList[0]:
            st.info("This site is under development.")

        elif selectedSettings == ft.settingsList[1]:
            password = st.text_input(" ",placeholder="Key",type="password").lower()
            ft.extraSection(password)

    elif selectedInfo == "Rate us":
        ft.star_rating("Rate us")
        
    st.markdown(f'''<p style="text-align:center">© 2023 Josuan. All rights reserved.</p>''',
                unsafe_allow_html=True)


selected = option_menu(menu_title=None,
                       options=ft.optionList,
                       default_index=0,
                       orientation="horizontal",
                       icons=["file-earmark-code","plus-slash-minus"],
                       styles={"nav-link-selected": {"background-color": "#8D72E1"}})

if selected == ft.optionList[0]:
    for key,value in data.items():
        st.subheader(key)
        st.code(value[0],line_numbers=True)
        if st.button("Copy code",key=f"{key}_key"):
            pyperclip.copy(value[0])
        st.text(f"Programmed by: {value[1]}")
        st.write("---")

elif selected == ft.optionList[1]:
    selectBox = st.selectbox("Select",ft.selectBoxList)

    if selectBox == ft.selectBoxList[0]:
        with st.form(key="A"):
            addTitle = st.text_input(" ",placeholder="Title")
            addCode = st.text_area(" ",placeholder="Code")
            addAuthor = st.text_input(" ",placeholder="Author")

            if st.form_submit_button('Add'):
                if addTitle in data.keys():
                    st.error("Duplicate title found!")
                else:
                    st.success("Code uploaded!")
                    data.update({addTitle:[addCode,addAuthor]})
                    with open("data.pkl", "wb") as f:
                        pickle.dump(data, f)

    elif selectBox == ft.selectBoxList[1]:
        with st.form(key="B"):
            removeCode = st.text_input(" ",placeholder="Input code Title")

            if st.form_submit_button("Remove"):
                if removeCode not in data.keys():
                    st.error("There's no such title!")
                else:
                    st.success("Code removed!")
                    data.pop(removeCode, None)
                    with open("data.pkl", "wb") as f:
                        pickle.dump(data, f)

ft.hide_footer()