import streamlit as st

settingsList = ["Webite settings","Extras"]
optionList = ["Code","Add/Remove"]
selectBoxList = ["Add Code","Remove Code"]

def extraSection(password):
     if st.button("Open"):
        if password == "josuan":
            st.audio("http://drive.google.com/uc?export=view&id=1JJLFbeWLwomebiyUihNjlFJ5JrQYHgzU",format="audio/mp3")
        elif password == "kylle" or password == "ethel":
            st.write("---")
            st.image("http://drive.google.com/uc?export=view&id=1J0ixZXOKxKvqSm5bKww1LZx4ImHhHq9z")
            st.image("http://drive.google.com/uc?export=view&id=1JSxzaH-CYDrnm-x9DxftA2LPu6XroHUI")
            st.write("---")
        elif password == "emarie" or password == "cristy":
            st.write("---")
            st.image("http://drive.google.com/uc?export=view&id=1JbcsbbkNy4GiI4riVD78hYpQZBBIc607")
            st.image("http://drive.google.com/uc?export=view&id=1JYBfys0beZQ3GlSm_nwdkhDxUcFZnUc2")
            st.write("---")
        else:
            st.error("Wrong password!")

def star_rating(title, min_value=1,max_value=5,step=1):
    st.write(title)
    rating = st.slider("",min_value=min_value,max_value=max_value,step=step)
    stars = ""
    if st.button("Submit"):
        for i in range(1, max_value+1):
            if i <= rating:
                stars += "★"
            else:
                stars += "☆"
        if rating >= 3:
            st.success(f"Thank you so much! {stars}")
        else:
            st.info(f"Thank you! {stars}")
    return rating

def hide_footer():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style,unsafe_allow_html=True)