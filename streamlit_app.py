import streamlit
import pandas

streamlit.title("My wifes new hotel")
streamlit.header("Breakfast Menu")
streamlit.text("idly")
streamlit.text("dosa")
streamlit.text("vada")
streamlit.text('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')
streamlit.text('\N{mechanical arm}')
streamlit.header('\N{call me hand} Find the list below')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))


streamlit.dataframe(my_fruit_list)
