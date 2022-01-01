
import streamlit as st
# Eda packages

import pandas as pd
import numpy as np

#Data viz packages

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

#function

def main():
    
    title_container1 = st.container()
    col1, col2 ,  = st.columns([6,12])
    from PIL import Image
    image = Image.open('static/asia.jpeg')
    with title_container1:
        with col1:
            st.image(image, width=200)
        with col2:
            st.markdown('<h1 style="color: purple;">ASIA Consulting</h1>',
                           unsafe_allow_html=True)
    
    st.subheader('Public Authority For Industry - Validity System For submitted Questionnaire')
    
    st.sidebar.image("static/ind.jpeg", use_column_width=True)
    activites = ["About","Validity System"]
    choice =st.sidebar.selectbox("Select Activity",activites)
    
    def get_df(file):
      # get extension and read file
      extension = file.name.split('.')[1]
      if extension.upper() == 'CSV':
        df = pd.read_csv(file)
      elif extension.upper() == 'XLSX':
        df = pd.read_excel(file)
      
      return df
    file = st.file_uploader("Upload file", type=['csv' 
                                             ,'xlsx'])
    if not file:
        st.write("Upload a .csv or .xlsx file to get started")
        return
      
    df = get_df(file)
    
    st.write("**Data has been loaded Successfully**")
    
    
    
    if choice == "About":
        
        from PIL import Image
        image = Image.open('static/PAI.jpeg')

        st.image(image, caption='Public Autority for Industry',width=600)
        st.text('© ASIA Consulting 2022')
    
    elif choice == "Validity System":
       
        if st.checkbox('Show Raw Data'):
            st.subheader('Raw Data')
            st.write(df)
            
        if st.checkbox('click here for Data validation'): 
            title_container1 = st.container()
            col1, col2 ,  = st.columns([6,12])
            from PIL import Image
            image = Image.open('static/val.png')
            with title_container1:
            
                with col2:
                    st.image(image, width=200, caption='Validating Data')
            st.subheader("Data After Validation")
            def highlight(df):
    
                r = "background-color : pink "
                y = "background-color : #f95f5f "
                o = "background-color : #5fba7d "
                w = "background-color : yellow "
                n = "background-color : orange "
                df1 = pd.DataFrame(" ", index = df.index, columns = df.columns)
            #2017    
                if (df['الطاقة القصوى بالكمية للمنتج 1'] <= df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 1']).any() :
                    df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 1'] = r
                else :
                     pass 
                    
            #2018        
                if (df['الطاقة القصوى بالكمية للمنتج 1'] <= df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 1']).any() :
                    df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 1'] = r
                else :
                     pass
            
        #2019        
                if (df['الطاقة القصوى بالكمية للمنتج 1'] <= df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 1']).any() :
                    df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 1'] = r
                else :
                     pass
            #2020        
                if (df['الطاقة القصوى بالكمية للمنتج 1'] <= df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 1']).any() :
                    df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 1'] = r
                else :
                     pass
                    
            #2017 price per item comparison
                first_number=df['متوسط سعر بيع الوحدة الواحدة للمنتج 1 د.ك ']*df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 1']
                second_number=df['إجمالي المبيعات (د.ك) لعام 2017']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إجمالي المبيعات (د.ك) لعام 2017']=w
                if (percent_diff > 50).any():
                    df1['إجمالي المبيعات (د.ك) لعام 2017']=w
                else :
                     pass
            #2018 price per item comparison
                first_number=df['متوسط سعر بيع الوحدة الواحدة للمنتج 1 د.ك ']*df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 1']
                second_number=df['إجمالي المبيعات (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
        
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إجمالي المبيعات (د.ك) لعام 2018']=w
                if (percent_diff > 50).any():
                    df1['إجمالي المبيعات (د.ك) لعام 2018']=w
                else :
                     pass
            
            #2019 price per item comparison
                first_number=df['متوسط سعر بيع الوحدة الواحدة للمنتج 1 د.ك ']*df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 1']
                second_number=df['إجمالي المبيعات (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إجمالي المبيعات (د.ك) لعام 2019']=w
                if (percent_diff > 50).any():
                    df1['إجمالي المبيعات (د.ك) لعام 2019']=w
                else :
                     pass
    
            #2020 price per item comparison
                first_number=df['متوسط سعر بيع الوحدة الواحدة للمنتج 1 د.ك ']*df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 1']
                second_number=df['إجمالي المبيعات (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إجمالي المبيعات (د.ك) لعام 2020']=w
                if (percent_diff > 50).any():
                    df1['إجمالي المبيعات (د.ك) لعام 2020']=w
                else :
                     pass
            
            #2017-2018(1) price per item comparison
                first_number=df['قيمة أصـول المباني (د.ك) لعام 2017']
                second_number=df['قيمة أصـول المباني (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول المباني (د.ك) لعام 2018']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول المباني (د.ك) لعام 2018']=o
                else:
                     pass
            #2017-2018(2) price per item comparison
                first_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2017']
                second_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2018']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2018']=o
                else:
                     pass
            #2017-2018(3) price per item comparison
                first_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2017']
                second_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول وسائل نقل (د.ك) لعام 2018']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول وسائل نقل (د.ك) لعام 2018']=o
                else:
                     pass
                    
            #2017-2018(4) price per item comparison
                first_number=df['قيمة أصـول أخرى (د.ك) لعام 2017']
                second_number=df['قيمة أصـول أخرى (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول أخرى (د.ك) لعام 2018']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول أخرى (د.ك) لعام 2018']=o
                else:
                     pass
            
            #2017-2018(5) price per item comparison
                first_number=df['إجمالي قيمة الأصول (د.ك) لعام 2017']
                second_number=df['إجمالي قيمة الأصول (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إجمالي قيمة الأصول (د.ك) لعام 2018']=o
                if (percent_diff > 50).any():
                    df1['إجمالي قيمة الأصول (د.ك) لعام 2018']=o
                else:
                     pass
            #2018-2019(1) price per item comparison
                first_number=df['قيمة أصـول المباني (د.ك) لعام 2018']
                second_number=df['قيمة أصـول المباني (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول المباني (د.ك) لعام 2019']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول المباني (د.ك) لعام 2019']=o
                else:
                     pass
            #2018-2019(2) price per item comparison
                first_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2018']
                second_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2019']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2019']=o
                else:
                     pass
            #2018-2019(3) price per item comparison
                first_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2018']
                second_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول وسائل نقل (د.ك) لعام 2019']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول وسائل نقل (د.ك) لعام 2019']=o
                else:
                     pass
                    
            #2018-2019(4) price per item comparison
                first_number=df['قيمة أصـول أخرى (د.ك) لعام 2018']
                second_number=df['قيمة أصـول أخرى (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول أخرى (د.ك) لعام 2019']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول أخرى (د.ك) لعام 2019']=o
                else:
                     pass
                    
            #2018-2019(5) price per item comparison
                first_number=df['إجمالي قيمة الأصول (د.ك) لعام 2018']
                second_number=df['إجمالي قيمة الأصول (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إجمالي قيمة الأصول (د.ك) لعام 2019']=o
                if (percent_diff > 50).any():
                    df1['إجمالي قيمة الأصول (د.ك) لعام 2019']=o
                else:
                     pass
            #2019-2020(1) price per item comparison
                first_number=df['قيمة أصـول المباني (د.ك) لعام 2019']
                second_number=df['قيمة أصـول المباني (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول المباني (د.ك) لعام 2020']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول المباني (د.ك) لعام 2020']=o
                else:
                     pass
            #2019-2020(2) price per item comparison
                first_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2019']
                second_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2020']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2020']=o
                else:
                     pass
            #2019-2020(3) price per item comparison
                first_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2019']
                second_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول وسائل نقل (د.ك) لعام 2020']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول وسائل نقل (د.ك) لعام 2020']=o
                else:
                     pass
                    
            #2019-2020(4) price per item comparison
                first_number=df['قيمة أصـول أخرى (د.ك) لعام 2019']
                second_number=df['قيمة أصـول أخرى (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة أصـول أخرى (د.ك) لعام 2020']=o
                if (percent_diff > 50).any():
                    df1['قيمة أصـول أخرى (د.ك) لعام 2020']=o
                else:
                     pass
                    
            #2019-2020(5) price per item comparison
                first_number=df['إجمالي قيمة الأصول (د.ك) لعام 2019']
                second_number=df['إجمالي قيمة الأصول (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إجمالي قيمة الأصول (د.ك) لعام 2020']=o
                if (percent_diff > 50).any():
                    df1['إجمالي قيمة الأصول (د.ك) لعام 2020']=o
                else:
                     pass
                    
            #2nd iteration for year
            
            #2017-2018(1) price per item comparison
                first_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2017']
                second_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة الإنفاق على المباني (د.ك) لعام 2018']=n
                if (percent_diff > 50).any():
                    df1['قيمة الإنفاق على المباني (د.ك) لعام 2018']=n
                else:
                     pass
            #2017-2018(2) price per item comparison
                first_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2017']
                second_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2018']=n
                if (percent_diff > 50).any():
                    df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2018']=n
                else:
                     pass
            #2017-2018(3) price per item comparison
                first_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2017']
                second_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2018']=n
                if (percent_diff > 50).any():
                    df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2018']=n
                else:
                     pass
                    
            #2017-2018(4) price per item comparison
                first_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2017']
                second_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2018']=n
                if (percent_diff > 50).any():
                    df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2018']=n
                else:
                     pass
                    
            #2017-2018(5) price per item comparison
                first_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2017']
                second_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إجمالي قيمة الإنفاق (د.ك) لعام 2018']=n
                if (percent_diff > 50).any():
                    df1['إجمالي قيمة الإنفاق (د.ك) لعام 2018']=n
                else:
                     pass
            #2018-2019(1) price per item comparison
                first_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2018']
                second_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة الإنفاق على المباني (د.ك) لعام 2019']=n
                if (percent_diff > 50).any():
                    df1['قيمة الإنفاق على المباني (د.ك) لعام 2019']=n
                else:
                     pass
            #2018-2019(2) price per item comparison
                first_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2018']
                second_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2019']=n
                if (percent_diff > 50).any():
                    df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2019']=n
                else:
                     pass
            #2018-2019(3) price per item comparison
                first_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2018']
                second_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2019']=n
                if (percent_diff > 50).any():
                    df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2019']=n
                else:
                     pass
                    
            #2018-2019(4) price per item comparison
                first_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2018']
                second_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2019']=n
                if (percent_diff > 50).any():
                    df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2019']=n
                else:
                     pass
                    
            #2018-2019(5) price per item comparison
                first_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2018']
                second_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إجمالي قيمة الإنفاق (د.ك) لعام 2019']=n
                if (percent_diff > 50).any():
                    df1['إجمالي قيمة الإنفاق (د.ك) لعام 2019']=n
                else:
                     pass
            
            #2019-2020(1) price per item comparison
                first_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2019']
                second_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة الإنفاق على المباني (د.ك) لعام 2020']=n
                if (percent_diff > 50).any():
                    df1['قيمة الإنفاق على المباني (د.ك) لعام 2020']=n
                else:
                     pass
            #2019-2020(2) price per item comparison
                first_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2019']
                second_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2020']=n
                if (percent_diff > 50).any():
                    df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2020']=n
                else:
                     pass
            #2019-2020(3) price per item comparison
                first_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2019']
                second_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2020']=n
                if (percent_diff > 50).any():
                    df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2020']=n
                else:
                     pass
                    
            #2019-2020(4) price per item comparison
                first_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2019']
                second_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2020']=n
                if (percent_diff > 50).any():
                    df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2020']=n
                else:
                     pass
                    
            #2019-2020(5) price per item comparison
                first_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2019']
                second_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['إجمالي قيمة الإنفاق (د.ك) لعام 2020']=n
                if (percent_diff > 50).any():
                    df1['إجمالي قيمة الإنفاق (د.ك) لعام 2020']=n
                else:
                     pass
            
            # 3rd iteration
            
            #2017-2018(1) price per item comparison
                first_number=df['قيمة استهلاك كهرباء (د.ك) 2017']
                second_number=df['قيمة استهلاك كهرباء (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك كهرباء (د.ك) 2018']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك كهرباء (د.ك) 2018']=y
                else:
                     pass
            #2017-2018(2) price per item comparison
                first_number=df['قيمة استهلاك مياه عذبة (د.ك) 2017']
                second_number=df['قيمة استهلاك مياه عذبة (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك مياه عذبة (د.ك) 2018']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك مياه عذبة (د.ك) 2018']=y
                else:
                     pass
            #2017-2018(3) price per item comparison
                first_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2017']
                second_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك غاز طبيعي (د.ك) 2018']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك غاز طبيعي (د.ك) 2018']=y
                else:
                     pass
                    
            #2017-2018(4) price per item comparison
                first_number=df['قيمة استهلاك بنزين (د.ك) 2017']
                second_number=df['قيمة استهلاك بنزين (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك بنزين (د.ك) 2018']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك بنزين (د.ك) 2018']=y
                else:
                     pass
                    
            #2017-2018(5) price per item comparison
                first_number=df['قيمة استهلاك ديزل (د.ك) 2017']
                second_number=df['قيمة استهلاك ديزل (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك ديزل (د.ك) 2018']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك ديزل (د.ك) 2018']=y
                else:
                     pass
            #2017-2018(6) price per item comparison
                first_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2017']
                second_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك زيوت وشحوم (د.ك) 2018']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك زيوت وشحوم (د.ك) 2018']=y
                else:
                     pass
            #2017-2018(7) price per item comparison
                first_number=df['قيمة استهلاك منافع أخرى (د.ك) 2017']
                second_number=df['قيمة استهلاك منافع أخرى (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك منافع أخرى (د.ك) 2018']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك منافع أخرى (د.ك) 2018']=y
                else:
                     pass
            #2017-2018(8) price per item comparison
                first_number=df['الإجمالي (د.ك) لعام 2017']
                second_number=df['الإجمالي (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['الإجمالي (د.ك) لعام 2018']=y
                if (percent_diff > 50).any():
                    df1['الإجمالي (د.ك) لعام 2018']=y
                else:
                     pass
            
            #2018-2019(1) price per item comparison
                first_number=df['قيمة استهلاك كهرباء (د.ك) 2018']
                second_number=df['قيمة استهلاك كهرباء (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك كهرباء (د.ك) 2019']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك كهرباء (د.ك) 2019']=y
                else:
                     pass
            #2018-2019(2) price per item comparison
                first_number=df['قيمة استهلاك مياه عذبة (د.ك) 2018']
                second_number=df['قيمة استهلاك مياه عذبة (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك مياه عذبة (د.ك) 2019']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك مياه عذبة (د.ك) 2019']=y
                else:
                     pass
            #2018-2019(3) price per item comparison
                first_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2018']
                second_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك غاز طبيعي (د.ك) 2019']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك غاز طبيعي (د.ك) 2019']=y
                else:
                     pass
                    
            #2018-2019(4) price per item comparison
                first_number=df['قيمة استهلاك بنزين (د.ك) 2018']
                second_number=df['قيمة استهلاك بنزين (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك بنزين (د.ك) 2019']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك بنزين (د.ك) 2019']=y
                else:
                     pass
                    
            #2018-2019(5) price per item comparison
                first_number=df['قيمة استهلاك ديزل (د.ك) 2018']
                second_number=df['قيمة استهلاك ديزل (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك ديزل (د.ك) 2019']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك ديزل (د.ك) 2019']=y
                else:
                     pass
            #2018-2019(6) price per item comparison
                first_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2018']
                second_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك زيوت وشحوم (د.ك) 2019']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك زيوت وشحوم (د.ك) 2019']=y
                else:
                     pass
            #2018-2019(7) price per item comparison
                first_number=df['قيمة استهلاك منافع أخرى (د.ك) 2018']
                second_number=df['قيمة استهلاك منافع أخرى (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك منافع أخرى (د.ك) 2019']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك منافع أخرى (د.ك) 2019']=y
                else:
                     pass
            #2018-2019(8) price per item comparison
                first_number=df['الإجمالي (د.ك) لعام 2018']
                second_number=df['الإجمالي (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['الإجمالي (د.ك) لعام 2019']=y
                if (percent_diff > 50).any():
                    df1['الإجمالي (د.ك) لعام 2019']=y
                else:
                     pass
            
            #2019-2020(1) price per item comparison
                first_number=df['قيمة استهلاك كهرباء (د.ك) 2019']
                second_number=df['قيمة استهلاك كهرباء (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك كهرباء (د.ك) 2020']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك كهرباء (د.ك) 2020']=y
                else:
                     pass
            #2019-2020(2) price per item comparison
                first_number=df['قيمة استهلاك مياه عذبة (د.ك) 2019']
                second_number=df['قيمة استهلاك مياه عذبة (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك مياه عذبة (د.ك) 2020']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك مياه عذبة (د.ك) 2020']=y
                else:
                     pass
            #2019-2020(3) price per item comparison
                first_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2019']
                second_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك غاز طبيعي (د.ك) 2020']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك غاز طبيعي (د.ك) 2020']=y
                else:
                     pass
                    
            #2019-2020(4) price per item comparison
                first_number=df['قيمة استهلاك بنزين (د.ك) 2019']
                second_number=df['قيمة استهلاك بنزين (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك بنزين (د.ك) 2020']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك بنزين (د.ك) 2020']=y
                else:
                     pass
                    
            #2019-2020(5) price per item comparison
                first_number=df['قيمة استهلاك ديزل (د.ك) 2019']
                second_number=df['قيمة استهلاك ديزل (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك ديزل (د.ك) 2020']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك ديزل (د.ك) 2020']=y
                else:
                     pass
            #2019-2020(6) price per item comparison
                first_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2019']
                second_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك زيوت وشحوم (د.ك) 2020']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك زيوت وشحوم (د.ك) 2020']=y
                else:
                     pass
            #2019-2020(7) price per item comparison
                first_number=df['قيمة استهلاك منافع أخرى (د.ك) 2019']
                second_number=df['قيمة استهلاك منافع أخرى (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['قيمة استهلاك منافع أخرى (د.ك) 2020']=y
                if (percent_diff > 50).any():
                    df1['قيمة استهلاك منافع أخرى (د.ك) 2020']=y
                else:
                     pass
            #2019-2020(8) price per item comparison
                first_number=df['الإجمالي (د.ك) لعام 2019']
                second_number=df['الإجمالي (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['الإجمالي (د.ك) لعام 2020']=y
                if (percent_diff > 50).any():
                    df1['الإجمالي (د.ك) لعام 2020']=y
                else:
                     pass        
            #4th iteration
            
            #2017-2018(1) price per item comparison
                first_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ الايجارات (د.ك) 2018']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ الايجارات (د.ك) 2018']=o
                else:
                     pass
            #2017-2018(2) price per item comparison
                first_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2018']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2018']=o
                else:
                     pass
            #2017-2018(3) price per item comparison
                first_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2018']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2018']=o
                else:
                     pass
                    
            #2017-2018(4) price per item comparison
                first_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2018']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2018']=o
                else:
                     pass
                    
            #2017-2018(5) price per item comparison
                first_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2018']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2018']=o
                else:
                     pass
            #2017-2018(6) price per item comparison
                first_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2018']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2018']=o
                else:
                     pass
            #2017-2018(7) price per item comparison
                first_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2018']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2018']=o
                else:
                     pass
            #2017-2018(8) price per item comparison
                first_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2018']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2018']=o
                else:
                     pass
            #2017-2018(9) price per item comparison
                first_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2017']
                second_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2018']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2018']=o
                else:
                     pass
            #2018-2019(1) price per item comparison
                first_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ الايجارات (د.ك) 2019']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ الايجارات (د.ك) 2019']=o
                else:
                     pass
            #2018-2019(2) price per item comparison
                first_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2019']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2019']=o
                else:
                     pass
            #2018-2019(3) price per item comparison
                first_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2019']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2019']=o
                else:
                     pass
                    
            #2018-2019(4) price per item comparison
                first_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2019']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2019']=o
                else:
                     pass
                    
            #2018-2019(5) price per item comparison
                first_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2019']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2019']=o
                else:
                     pass
            #2018-2019(6) price per item comparison
                first_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2019']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2019']=o
                else:
                     pass
            #2018-2019(7) price per item comparison
                first_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2019']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2019']=o
                else:
                     pass
            #2018-2019(8) price per item comparison
                first_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2019']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2019']=o
                else:
                     pass
            #2018-2019(9) price per item comparison
                first_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2018']
                second_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2019']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2019']=o
                else:
                     pass    
            #2019-2020(1) price per item comparison
                first_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ الايجارات (د.ك) 2020']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ الايجارات (د.ك) 2020']=o
                else:
                     pass
            #2019-2020(2) price per item comparison
                first_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2020']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2020']=o
                else:
                     pass
            #2019-2020(3) price per item comparison
                first_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2020']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2020']=o
                else:
                     pass
                    
            #2019-2020(4) price per item comparison
                first_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2020']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2020']=o
                else:
                     pass
                    
            #2019-2020(5) price per item comparison
                first_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2020']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2020']=o
                else:
                     pass
            #2019-2020(6) price per item comparison
                first_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2020']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2020']=o
                else:
                     pass
            #2019-2020(7) price per item comparison
                first_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2020']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2020']=o
                else:
                     pass
            #2019-2020(8) price per item comparison
                first_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2020']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2020']=o
                else:
                     pass
            #2019-2020(9) price per item comparison
                first_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2019']
                second_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                if (percent_diff <= 50).any():
                     pass
                if (percent_diff < -50).any():
                    df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2020']=o
                if (percent_diff > 50).any():
                    df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2020']=o
                else:
                     pass    
            
            # column comaprison
            #2017
                if (df['صافي الأرباح السنوية (د.ك) لعام 2017'] > 0).any():    
                    if (df['صافي الخسائر السنوية (د.ك) لعام 2017'] > 0).any():
                        df1[['صافي الخسائر السنوية (د.ك) لعام 2017','صافي الأرباح السنوية (د.ك) لعام 2017']] = r
                else:
                     pass
            
            #2018
                if (df['صافي الأرباح السنوية (د.ك) لعام 2018'] > 0).any():    
                    if (df['صافي الخسائر السنوية (د.ك) لعام 2018'] > 0).any():
                        df1[['صافي الخسائر السنوية (د.ك) لعام 2018','صافي الأرباح السنوية (د.ك) لعام 2018']] = r
                else:
                     pass
            #2019
                if (df['صافي الأرباح السنوية (د.ك) لعام 2019'] > 0).any():    
                    if (df['صافي الخسائر السنوية (د.ك) لعام 2019'] > 0).any():
                        df1[['صافي الخسائر السنوية (د.ك) لعام 2019','صافي الأرباح السنوية (د.ك) لعام 2019']] = r
                else:
                     pass
            
            #2020
                if (df['صافي الأرباح السنوية (د.ك) لعام 2020'] > 0).any():    
                    if (df['صافي الخسائر السنوية (د.ك) لعام 2020'] > 0).any():
                        df1[['صافي الخسائر السنوية (د.ك) لعام 2020','صافي الأرباح السنوية (د.ك) لعام 2020']] = r
                else:
                     pass
            
        
        
            
                
                
                
                
                
                
                
                
                
                
                
                
                
                return df1
            
            da=df.style.apply(highlight, axis =None)
            st.dataframe(da)
        
            import base64
            import io
            towrite = io.BytesIO()
            downloaded_file = da.to_excel(towrite, encoding='utf-8', index=False, header=True) # write to BytesIO buffer
            towrite.seek(0)  # reset pointer
            b64 = base64.b64encode(towrite.read()).decode() 
            linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="validation_result.xlsx">Download excel file</a>'
            st.markdown(linko, unsafe_allow_html=True)
            st.text(" ")
            st.text(" ")
            st.text(" ")
            st.text(" ")
            
            st.text(" ")
            st.text(" ")
            st.text(" ")
            st.text('© ASIA Consulting 2022')
                
        
            
            
            
                
            
        
        

    


        
        

if __name__=='__main__':
    main()
        
        