
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
            def highlight_greater(df):
                r = 'tomato'
            
            #  1st comparison
                m11 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 1'] > df['الطاقة القصوى بالكمية للمنتج 1']
                m12 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 1'] > df['الطاقة القصوى بالكمية للمنتج 1']
                m13 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 1'] > df['الطاقة القصوى بالكمية للمنتج 1']
                m14 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 1'] > df['الطاقة القصوى بالكمية للمنتج 1']
                
                m21 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 2'] > df['الطاقة القصوى بالكمية للمنتج 2']
                m22 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 2'] > df['الطاقة القصوى بالكمية للمنتج 2']
                m23 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 2'] > df['الطاقة القصوى بالكمية للمنتج 2']
                m24 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 2'] > df['الطاقة القصوى بالكمية للمنتج 2'] 
                
                m31 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 3'] > df['الطاقة القصوى بالكمية للمنتج 3']
                m32 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 3'] > df['الطاقة القصوى بالكمية للمنتج 3']
                m33 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 3'] > df['الطاقة القصوى بالكمية للمنتج 3']
                m34 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 3'] > df['الطاقة القصوى بالكمية للمنتج 3'] 
                
                m41 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 4'] > df['الطاقة القصوى بالكمية للمنتج 4']
                m42 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 4'] > df['الطاقة القصوى بالكمية للمنتج 4']
                m43 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 4'] > df['الطاقة القصوى بالكمية للمنتج 4']
                m44 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 4'] > df['الطاقة القصوى بالكمية للمنتج 4'] 
                
                m51 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 5'] > df['الطاقة القصوى بالكمية للمنتج 5']
                m52 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 5'] > df['الطاقة القصوى بالكمية للمنتج 5']
                m53 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 5'] > df['الطاقة القصوى بالكمية للمنتج 5']
                m54 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 5'] > df['الطاقة القصوى بالكمية للمنتج 5']
                
                m61 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 6'] > df['الطاقة القصوى بالكمية للمنتج 6']
                m62 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 6'] > df['الطاقة القصوى بالكمية للمنتج 6']
                m63 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 6'] > df['الطاقة القصوى بالكمية للمنتج 6']
                m64 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 6'] > df['الطاقة القصوى بالكمية للمنتج 6'] 
                
                m71 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 7'] > df['الطاقة القصوى بالكمية للمنتج 7']
                m72 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 7'] > df['الطاقة القصوى بالكمية للمنتج 7']
                m73 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 7'] > df['الطاقة القصوى بالكمية للمنتج 7']
                m74 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 7'] > df['الطاقة القصوى بالكمية للمنتج 7']
                
                m81 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 8'] > df['الطاقة القصوى بالكمية للمنتج 8']
                m82 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 8'] > df['الطاقة القصوى بالكمية للمنتج 8']
                m83 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 8'] > df['الطاقة القصوى بالكمية للمنتج 8']
                m84 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 8'] > df['الطاقة القصوى بالكمية للمنتج 8'] 
                
                m91 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 9'] > df['الطاقة القصوى بالكمية للمنتج 9']
                m92 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 9'] > df['الطاقة القصوى بالكمية للمنتج 9']
                m93 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 9'] > df['الطاقة القصوى بالكمية للمنتج 9']
                m94 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 9'] > df['الطاقة القصوى بالكمية للمنتج 9']  
                
                m101 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 10'] > df['الطاقة القصوى بالكمية للمنتج 10']
                m102 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 10'] > df['الطاقة القصوى بالكمية للمنتج 10']
                m103 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 10'] > df['الطاقة القصوى بالكمية للمنتج 10']
                m104 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 10'] > df['الطاقة القصوى بالكمية للمنتج 10']
                
                m111 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 11'] > df['الطاقة القصوى بالكمية للمنتج 11']
                m112 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 11'] > df['الطاقة القصوى بالكمية للمنتج 11']
                m113 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 11'] > df['الطاقة القصوى بالكمية للمنتج 11']
                m114 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 11'] > df['الطاقة القصوى بالكمية للمنتج 11']
                
                m121 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 12'] > df['الطاقة القصوى بالكمية للمنتج 12']
                m122 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 12'] > df['الطاقة القصوى بالكمية للمنتج 12']
                m123 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 12'] > df['الطاقة القصوى بالكمية للمنتج 12']
                m124 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 12'] > df['الطاقة القصوى بالكمية للمنتج 12']
                
                m131 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 13'] > df['الطاقة القصوى بالكمية للمنتج 13']
                m132 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 13'] > df['الطاقة القصوى بالكمية للمنتج 13']
                m133 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 13'] > df['الطاقة القصوى بالكمية للمنتج 13']
                m134 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 13'] > df['الطاقة القصوى بالكمية للمنتج 13']
                
                m141 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 14'] > df['الطاقة القصوى بالكمية للمنتج 14']
                m142 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 14'] > df['الطاقة القصوى بالكمية للمنتج 14']
                m143 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 14'] > df['الطاقة القصوى بالكمية للمنتج 14']
                m144 = df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 14'] > df['الطاقة القصوى بالكمية للمنتج 14']
                
                
                
                
                
                
                
                
                

            
            #******************************************************************************************************************
            #  2nd comparison price per item comparison 1
                first_number=df['متوسط سعر بيع الوحدة الواحدة للمنتج 1 د.ك ']*df['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 1']
                second_number=df['إجمالي المبيعات (د.ك) لعام 2017']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                a1= percent_diff <= -50 
                a2= percent_diff >= 50
            #  2nd comparison price per item comparison 2
                first_number=df['متوسط سعر بيع الوحدة الواحدة للمنتج 1 د.ك ']*df['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 1']
                second_number=df['إجمالي المبيعات (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                a3= percent_diff <= -50 
                a4= percent_diff >= 50
                
            #  2nd comparison price per item comparison 3
                first_number=df['متوسط سعر بيع الوحدة الواحدة للمنتج 1 د.ك ']*df['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 1']
                second_number=df['إجمالي المبيعات (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                a5= percent_diff <= -50 
                a6= percent_diff >= 50
                
            #  2nd comparison price per item comparison 4
                first_number=df['متوسط سعر بيع الوحدة الواحدة للمنتج 1 د.ك ']*df['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 1']
                second_number=df['إجمالي المبيعات (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                a7= percent_diff <= -50 
                a8= percent_diff >= 50
            #*********************************************************************************************************************    
            #  3rd (2017-2018)comparison price per item comparison 1
                first_number=df['قيمة أصـول المباني (د.ك) لعام 2017']
                second_number=df['قيمة أصـول المباني (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b1= percent_diff <= -50 
                b2= percent_diff >= 50
            #  3rd (2017-2018)comparison price per item comparison 2
                first_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2017']
                second_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b3= percent_diff <= -50 
                b4= percent_diff >= 50
            #  3rd (2017-2018)comparison price per item comparison 3    
                first_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2017']
                second_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b5= percent_diff <= -50 
                b6= percent_diff >= 50
            #  3rd (2017-2018)comparison price per item comparison 4
                first_number=df['قيمة أصـول أخرى (د.ك) لعام 2017']
                second_number=df['قيمة أصـول أخرى (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b7= percent_diff <= -50 
                b8= percent_diff >= 50
            #  3rd (2017-2018)comparison price per item comparison 5    
                first_number=df['إجمالي قيمة الأصول (د.ك) لعام 2017']
                second_number=df['إجمالي قيمة الأصول (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b9= percent_diff <= -50 
                b10= percent_diff >= 50
                
                
                
            #  3rd (2018-2019)comparison price per item comparison 1
                first_number=df['قيمة أصـول المباني (د.ك) لعام 2018']
                second_number=df['قيمة أصـول المباني (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b11= percent_diff <= -50 
                b12= percent_diff >= 50
            #  3rd (2018-2019)comparison price per item comparison 2
                first_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2018']
                second_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b13= percent_diff <= -50 
                b14= percent_diff >= 50
            #  3rd (2018-2019)comparison price per item comparison 3    
                first_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2018']
                second_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b15= percent_diff <= -50 
                b16= percent_diff >= 50
            #  3rd (2018-2019)comparison price per item comparison 4
                first_number=df['قيمة أصـول أخرى (د.ك) لعام 2018']
                second_number=df['قيمة أصـول أخرى (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b17= percent_diff <= -50 
                b18= percent_diff >= 50
            #  3rd (2018-2019)comparison price per item comparison 5    
                first_number=df['إجمالي قيمة الأصول (د.ك) لعام 2018']
                second_number=df['إجمالي قيمة الأصول (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b19= percent_diff <= -50 
                b20= percent_diff >= 50
                
                    
            #  3rd (2019-2020)comparison price per item comparison 1
                first_number=df['قيمة أصـول المباني (د.ك) لعام 2019']
                second_number=df['قيمة أصـول المباني (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b21= percent_diff <= -50 
                b22= percent_diff >= 50
            #  3rd (2019-2020)comparison price per item comparison 2
                first_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2019']
                second_number=df['قيمة أصـول آلات ومعدات (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b23= percent_diff <= -50 
                b24= percent_diff >= 50
            #  3rd (2019-2020)comparison price per item comparison 3    
                first_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2019']
                second_number=df['قيمة أصـول وسائل نقل (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b25= percent_diff <= -50 
                b26= percent_diff >= 50
            #  3rd (2019-2020)comparison price per item comparison 4
                first_number=df['قيمة أصـول أخرى (د.ك) لعام 2019']
                second_number=df['قيمة أصـول أخرى (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b27= percent_diff <= -50 
                b28= percent_diff >= 50
            #  3rd (2019-2020)comparison price per item comparison 5    
                first_number=df['إجمالي قيمة الأصول (د.ك) لعام 2019']
                second_number=df['إجمالي قيمة الأصول (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                b29= percent_diff <= -50 
                b30= percent_diff >= 50
            #**************************************************************************************************************************
                
            #  4th (2017-2018)comparison price per item comparison 1    
                first_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2017']
                second_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c1= percent_diff <= -50 
                c2= percent_diff >= 50
            #  4th (2017-2018)comparison price per item comparison 2
                first_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2017']
                second_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c3= percent_diff <= -50 
                c4= percent_diff >= 50
            #  4th (2017-2018)comparison price per item comparison 3
                first_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2017']
                second_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c5= percent_diff <= -50 
                c6= percent_diff >= 50
            #  4th (2017-2018)comparison price per item comparison 4
                first_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2017']
                second_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c7= percent_diff <= -50 
                c8= percent_diff >= 50
            #  4th (2017-2018)comparison price per item comparison 5
                first_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2017']
                second_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c9= percent_diff <= -50 
                c10= percent_diff >= 50
                
            #  4th (2018-2019)comparison price per item comparison 1    
                first_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2018']
                second_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c11= percent_diff <= -50 
                c12= percent_diff >= 50
            #  4th (2018-2019)comparison price per item comparison 2
                first_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2018']
                second_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c13= percent_diff <= -50 
                c14= percent_diff >= 50
            #  4th (2018-2019)comparison price per item comparison 3
                first_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2018']
                second_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c15= percent_diff <= -50 
                c16= percent_diff >= 50
            #  4th (2018-2019)comparison price per item comparison 4
                first_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2018']
                second_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c17= percent_diff <= -50 
                c18= percent_diff >= 50
            #  4th (2018-2019)comparison price per item comparison 5
                first_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2018']
                second_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c19= percent_diff <= -50 
                c20= percent_diff >= 50
            #  4th (2019-2020)comparison price per item comparison 1    
                first_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2019']
                second_number=df['قيمة الإنفاق على المباني (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c21= percent_diff <= -50 
                c22= percent_diff >= 50
            #  4th (2019-2020)comparison price per item comparison 2
                first_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2019']
                second_number=df['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c23= percent_diff <= -50 
                c24= percent_diff >= 50
            #  4th (2019-2020)comparison price per item comparison 3
                first_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2019']
                second_number=df['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c25= percent_diff <= -50 
                c26= percent_diff >= 50
            #  4th (2019-2020)comparison price per item comparison 4
                first_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2019']
                second_number=df['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c27= percent_diff <= -50 
                c28= percent_diff >= 50
            #  4th (2019-2020)comparison price per item comparison 5
                first_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2019']
                second_number=df['إجمالي قيمة الإنفاق (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                c29= percent_diff <= -50 
                c30= percent_diff >= 50
            #************************************************************************************************************************
                
            # 5th (2017-2018)comparison price per item comparison 1
                first_number=df['قيمة استهلاك كهرباء (د.ك) 2017']
                second_number=df['قيمة استهلاك كهرباء (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d1= percent_diff <= -50 
                d2= percent_diff >= 50
            # 5th (2017-2018)comparison price per item comparison 2
                first_number=df['قيمة استهلاك مياه عذبة (د.ك) 2017']
                second_number=df['قيمة استهلاك مياه عذبة (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d3= percent_diff <= -50 
                d4= percent_diff >= 50
            # 5th (2017-2018)comparison price per item comparison 3    
                first_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2017']
                second_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d5= percent_diff <= -50 
                d6= percent_diff >= 50
            # 5th (2017-2018)comparison price per item comparison 4    
                first_number=df['قيمة استهلاك بنزين (د.ك) 2017']
                second_number=df['قيمة استهلاك بنزين (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d7= percent_diff <= -50 
                d8= percent_diff >= 50
            # 5th (2017-2018)comparison price per item comparison 5        
                first_number=df['قيمة استهلاك ديزل (د.ك) 2017']
                second_number=df['قيمة استهلاك ديزل (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d9= percent_diff <= -50 
                d10= percent_diff >= 50
            # 5th (2017-2018)comparison price per item comparison 6     
                first_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2017']
                second_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d11= percent_diff <= -50 
                d12= percent_diff >= 50
            # 5th (2017-2018)comparison price per item comparison 7
                first_number=df['قيمة استهلاك منافع أخرى (د.ك) 2017']
                second_number=df['قيمة استهلاك منافع أخرى (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d13= percent_diff <= -50 
                d14= percent_diff >= 50
            # 5th (2017-2018)comparison price per item comparison 8
                first_number=df['الإجمالي (د.ك) لعام 2017']
                second_number=df['الإجمالي (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d15= percent_diff <= -50 
                d16= percent_diff >= 50
                
            # 5th (2018-2019)comparison price per item comparison 1
                first_number=df['قيمة استهلاك كهرباء (د.ك) 2018']
                second_number=df['قيمة استهلاك كهرباء (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d17= percent_diff <= -50 
                d18= percent_diff >= 50
            # 5th (2018-2019)comparison price per item comparison 2
                first_number=df['قيمة استهلاك مياه عذبة (د.ك) 2018']
                second_number=df['قيمة استهلاك مياه عذبة (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d19= percent_diff <= -50 
                d20= percent_diff >= 50
            # 5th (2018-2019)comparison price per item comparison 3    
                first_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2018']
                second_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d21= percent_diff <= -50 
                d22= percent_diff >= 50
            # 5th (2018-2019)comparison price per item comparison 4    
                first_number=df['قيمة استهلاك بنزين (د.ك) 2018']
                second_number=df['قيمة استهلاك بنزين (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d23= percent_diff <= -50 
                d24= percent_diff >= 50
            # 5th (2018-2019)comparison price per item comparison 5        
                first_number=df['قيمة استهلاك ديزل (د.ك) 2018']
                second_number=df['قيمة استهلاك ديزل (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d25= percent_diff <= -50 
                d26= percent_diff >= 50
            # 5th (2018-2019)comparison price per item comparison 6     
                first_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2018']
                second_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d27= percent_diff <= -50 
                d28= percent_diff >= 50
            # 5th (2018-2019)comparison price per item comparison 7
                first_number=df['قيمة استهلاك منافع أخرى (د.ك) 2018']
                second_number=df['قيمة استهلاك منافع أخرى (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d29= percent_diff <= -50 
                d30= percent_diff >= 50
            # 5th (2018-2019)comparison price per item comparison 8
                first_number=df['الإجمالي (د.ك) لعام 2018']
                second_number=df['الإجمالي (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d31= percent_diff <= -50 
                d32= percent_diff >= 50
                
                
            # 5th (2019-2020)comparison price per item comparison 1
                first_number=df['قيمة استهلاك كهرباء (د.ك) 2019']
                second_number=df['قيمة استهلاك كهرباء (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d33= percent_diff <= -50 
                d34= percent_diff >= 50
            # 5th (2019-2020)comparison price per item comparison 2
                first_number=df['قيمة استهلاك مياه عذبة (د.ك) 2019']
                second_number=df['قيمة استهلاك مياه عذبة (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d35= percent_diff <= -50 
                d36= percent_diff >= 50
            # 5th (2019-2020)comparison price per item comparison 3    
                first_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2019']
                second_number=df['قيمة استهلاك غاز طبيعي (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d37= percent_diff <= -50 
                d38= percent_diff >= 50
            # 5th (2019-2020)comparison price per item comparison 4    
                first_number=df['قيمة استهلاك بنزين (د.ك) 2019']
                second_number=df['قيمة استهلاك بنزين (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d39= percent_diff <= -50 
                d40= percent_diff >= 50
            # 5th (2019-2020)comparison price per item comparison 5        
                first_number=df['قيمة استهلاك ديزل (د.ك) 2019']
                second_number=df['قيمة استهلاك ديزل (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d41= percent_diff <= -50 
                d42= percent_diff >= 50
            # 5th (2019-2020)comparison price per item comparison 6     
                first_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2019']
                second_number=df['قيمة استهلاك زيوت وشحوم (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d43= percent_diff <= -50 
                d44= percent_diff >= 50
            # 5th (2019-2020)comparison price per item comparison 7
                first_number=df['قيمة استهلاك منافع أخرى (د.ك) 2019']
                second_number=df['قيمة استهلاك منافع أخرى (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d45= percent_diff <= -50 
                d46= percent_diff >= 50
            # 5th (2019-2020)comparison price per item comparison 8
                first_number=df['الإجمالي (د.ك) لعام 2019']
                second_number=df['الإجمالي (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                d47= percent_diff <= -50 
                d48= percent_diff >= 50
            #****************************************************************************************************************
            # 6th (2017-2018)comparison price per item comparison 1    
                first_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                e1= percent_diff <= -50 
                e2= percent_diff >= 50
            # 6th (2017-2018)comparison price per item comparison 2    
                first_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                e3= percent_diff <= -50 
                e4= percent_diff >= 50
                
            # 6th (2017-2018)comparison price per item comparison 3 
                first_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                e5= percent_diff <= -50 
                e6= percent_diff >= 50
                
            # 6th (2017-2018)comparison price per item comparison 4
                
                first_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                e7= percent_diff <= -50 
                e8= percent_diff >= 50
                
            # 6th (2017-2018)comparison price per item comparison 5    
                first_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                e9= percent_diff <= -50 
                e10= percent_diff >= 50
            # 6th (2017-2018)comparison price per item comparison 6    
                first_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                e11= percent_diff <= -50 
                e12= percent_diff >= 50
                
            # 6th (2017-2018)comparison price per item comparison 7  
                first_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                e13= percent_diff <= -50 
                e14= percent_diff >= 50
                
            # 6th (2017-2018)comparison price per item comparison 8    
                first_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2017']
                second_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
            
                e15= percent_diff <= -50 
                e16= percent_diff >= 50
            # 6th (2017-2018)comparison price per item comparison 9    
                first_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2017']
                second_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2018']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                e17= percent_diff <= -50 
                e18= percent_diff >= 50
            
            # 6th (2018-2019)comparison price per item comparison 1    
                first_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                ea1= percent_diff <= -50 
                ea2= percent_diff >= 50
            # 6th (2018-2019)comparison price per item comparison 2    
                first_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                ea3= percent_diff <= -50 
                ea4= percent_diff >= 50
                
            # 6th (2018-2019)comparison price per item comparison 3 
                first_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                ea5= percent_diff <= -50 
                ea6= percent_diff >= 50
                
            # 6th (2018-2019)comparison price per item comparison 4
                
                first_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                ea7= percent_diff <= -50 
                ea8= percent_diff >= 50
                
            # 6th (2018-2019)comparison price per item comparison 5    
                first_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                ea9= percent_diff <= -50 
                ea10= percent_diff >= 50
            # 6th (2018-2019)comparison price per item comparison 6    
                first_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                ea11= percent_diff <= -50 
                ea12= percent_diff >= 50
                
            # 6th (2018-2019)comparison price per item comparison 7  
                first_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                ea13= percent_diff <= -50 
                ea14= percent_diff >= 50
                
            # 6th (2018-2019)comparison price per item comparison 8    
                first_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2018']
                second_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
            
                ea15= percent_diff <= -50 
                ea16= percent_diff >= 50
            # 6th (2018-2019)comparison price per item comparison 9    
                first_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2018']
                second_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2019']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                ea17= percent_diff <= -50 
                ea18= percent_diff >= 50
            # 6th (2019-2020)comparison price per item comparison 1    
                first_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ الايجارات (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                eb1= percent_diff <= -50 
                eb2= percent_diff >= 50
            # 6th (2019-2020)comparison price per item comparison 2    
                first_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                eb3= percent_diff <= -50 
                eb4= percent_diff >= 50
                
            # 6th (2019-2020)comparison price per item comparison 3 
                first_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ تسويق وترويج (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                eb5= percent_diff <= -50 
                eb6= percent_diff >= 50
                
            # 6th (2019-2020)comparison price per item comparison 4
                
                first_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                eb7= percent_diff <= -50 
                eb8= percent_diff >= 50
                
            # 6th (2019-2020)comparison price per item comparison 5    
                first_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                eb9= percent_diff <= -50 
                eb10= percent_diff >= 50
            # 6th (2019-2020)comparison price per item comparison 6    
                first_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                eb11= percent_diff <= -50 
                eb12= percent_diff >= 50
                
            # 6th (2019-2020)comparison price per item comparison 7  
                first_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                eb13= percent_diff <= -50 
                eb14= percent_diff >= 50
                
            # 6th (2019-2020)comparison price per item comparison 8    
                first_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2019']
                second_number=df['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
            
                eb15= percent_diff <= -50 
                eb16= percent_diff >= 50
            # 6th (2019-2020)comparison price per item comparison 9    
                first_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2019']
                second_number=df['تكاليف المنشأة/الإجمالي (د.ك) لعام 2020']
                percent_diff = ((second_number - first_number)/first_number) * 100
                
                eb17= percent_diff <= -50 
                eb18= percent_diff >= 50    
                
            #***********************************************************************************************************************    
            # 7th (2017-2017) comparison
                ma1 = (df['صافي الأرباح السنوية (د.ك) لعام 2017'] >0) & (df['صافي الخسائر السنوية (د.ك) لعام 2017']>0)
                ma3 = (df['صافي الأرباح السنوية (د.ك) لعام 2017'] <0) & (df['صافي الخسائر السنوية (د.ك) لعام 2017']<0)
                ma4 = (df['صافي الأرباح السنوية (د.ك) لعام 2017'] <0) & (df['صافي الخسائر السنوية (د.ك) لعام 2017']>0)
                ma5 = (df['صافي الأرباح السنوية (د.ك) لعام 2017'] >0) & (df['صافي الخسائر السنوية (د.ك) لعام 2017']<0)
                ma2 = (df['صافي الأرباح السنوية (د.ك) لعام 2017'] == df['صافي الخسائر السنوية (د.ك) لعام 2017'])
            # 7th (2018-2018) comparison
                mb1 = (df['صافي الأرباح السنوية (د.ك) لعام 2018'] >0) & (df['صافي الخسائر السنوية (د.ك) لعام 2018']>0)
                mb3 = (df['صافي الأرباح السنوية (د.ك) لعام 2018'] <0) & (df['صافي الخسائر السنوية (د.ك) لعام 2018']<0)
                mb4 = (df['صافي الأرباح السنوية (د.ك) لعام 2018'] <0) & (df['صافي الخسائر السنوية (د.ك) لعام 2018']>0)
                mb5 = (df['صافي الأرباح السنوية (د.ك) لعام 2018'] >0) & (df['صافي الخسائر السنوية (د.ك) لعام 2018']<0)
                mb2 = (df['صافي الأرباح السنوية (د.ك) لعام 2018'] == df['صافي الخسائر السنوية (د.ك) لعام 2018'])    
            # 7th (2019-2019) comparison
                mc1 = (df['صافي الأرباح السنوية (د.ك) لعام 2019'] >0) & (df['صافي الخسائر السنوية (د.ك) لعام 2019']>0)
                mc3 = (df['صافي الأرباح السنوية (د.ك) لعام 2019'] <0) & (df['صافي الخسائر السنوية (د.ك) لعام 2019']<0)
                mc4 = (df['صافي الأرباح السنوية (د.ك) لعام 2019'] <0) & (df['صافي الخسائر السنوية (د.ك) لعام 2019']>0)
                mc5 = (df['صافي الأرباح السنوية (د.ك) لعام 2019'] >0) & (df['صافي الخسائر السنوية (د.ك) لعام 2019']<0)
                mc2 = (df['صافي الأرباح السنوية (د.ك) لعام 2019'] == df['صافي الخسائر السنوية (د.ك) لعام 2019'])    
                
            # 7th (2020-2020) comparison
                md1 = (df['صافي الأرباح السنوية (د.ك) لعام 2020'] >0) & (df['صافي الخسائر السنوية (د.ك) لعام 2020']>0)
                md3 = (df['صافي الأرباح السنوية (د.ك) لعام 2020'] <0) & (df['صافي الخسائر السنوية (د.ك) لعام 2020']<0)
                md4 = (df['صافي الأرباح السنوية (د.ك) لعام 2020'] <0) & (df['صافي الخسائر السنوية (د.ك) لعام 2020']>0)
                md5 = (df['صافي الأرباح السنوية (د.ك) لعام 2020'] >0) & (df['صافي الخسائر السنوية (د.ك) لعام 2020']<0)
                md2 = (df['صافي الأرباح السنوية (د.ك) لعام 2020'] == df['صافي الخسائر السنوية (د.ك) لعام 2020'])    
                
            #***********************************************************************************************************************    
            #***********************************************************************************************************************    
            #***********************************************************************************************************************    
            
                df1 = pd.DataFrame(' ', index=df.index, columns=df.columns)
                #rewrite values by boolean masks
                #1st comparison
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 1'] = np.where(m11, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 1'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 1'] = np.where(m12, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 1'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 1'] = np.where(m13, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 1'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 1'] = np.where(m14, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 1'])
                
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 2'] = np.where(m21, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 2'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 2'] = np.where(m22, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 2'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 2'] = np.where(m23, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 2'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 2'] = np.where(m24, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 2'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 3'] = np.where(m31, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 3'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 3'] = np.where(m32, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 3'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 3'] = np.where(m33, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 3'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 3'] = np.where(m34, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 3'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 4'] = np.where(m41, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 4'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 4'] = np.where(m42, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 4'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 4'] = np.where(m43, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 4'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 4'] = np.where(m44, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 4'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 5'] = np.where(m51, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 5'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 5'] = np.where(m52, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 5'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 5'] = np.where(m53, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 5'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 5'] = np.where(m54, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 5'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 6'] = np.where(m61, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 6'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 6'] = np.where(m62, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 6'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 6'] = np.where(m63, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 6'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 6'] = np.where(m64, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 6'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 7'] = np.where(m71, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 7'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 7'] = np.where(m72, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 7'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 7'] = np.where(m73, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 7'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 7'] = np.where(m74, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 7'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 8'] = np.where(m81, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 8'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 8'] = np.where(m82, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 8'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 8'] = np.where(m83, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 8'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 8'] = np.where(m84, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 8'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 9'] = np.where(m91, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 9'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 9'] = np.where(m92, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 9'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 9'] = np.where(m93, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 9'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 9'] = np.where(m94, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 9'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 10'] = np.where(m101, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 10'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 10'] = np.where(m102, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 10'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 10'] = np.where(m103, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 10'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 10'] = np.where(m104, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 10'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 11'] = np.where(m111, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 11'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 11'] = np.where(m112, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 11'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 11'] = np.where(m113, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 11'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 11'] = np.where(m114, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 11'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 12'] = np.where(m121, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 12'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 12'] = np.where(m122, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 12'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 12'] = np.where(m123, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 12'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 12'] = np.where(m124, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 12'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 13'] = np.where(m131, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 13'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 13'] = np.where(m132, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 13'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 13'] = np.where(m133, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 13'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 13'] = np.where(m134, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 13'])
                
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 14'] = np.where(m141, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2017 للمنتج 14'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 14'] = np.where(m142, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2018 للمنتج 14'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 14'] = np.where(m143, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2019 للمنتج 14'])
                df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 14'] = np.where(m144, 'background-color: {}'.format(r), df1['الطاقة الفعلية للمنتجات (الكمية) لعام 2020 للمنتج 14'])
                
                #2nd comparison
                df1['إجمالي المبيعات (د.ك) لعام 2017'] = np.where(a1, 'background-color: {}'.format(r), df1['إجمالي المبيعات (د.ك) لعام 2017'])
                df1['إجمالي المبيعات (د.ك) لعام 2017'] = np.where(a2, 'background-color: {}'.format(r), df1['إجمالي المبيعات (د.ك) لعام 2017'])
                
                df1['إجمالي المبيعات (د.ك) لعام 2018'] = np.where(a3, 'background-color: {}'.format(r), df1['إجمالي المبيعات (د.ك) لعام 2018'])
                df1['إجمالي المبيعات (د.ك) لعام 2018'] = np.where(a4, 'background-color: {}'.format(r), df1['إجمالي المبيعات (د.ك) لعام 2018'])
                
                df1['إجمالي المبيعات (د.ك) لعام 2019'] = np.where(a5, 'background-color: {}'.format(r), df1['إجمالي المبيعات (د.ك) لعام 2019'])
                df1['إجمالي المبيعات (د.ك) لعام 2019'] = np.where(a6, 'background-color: {}'.format(r), df1['إجمالي المبيعات (د.ك) لعام 2019'])
                
                df1['إجمالي المبيعات (د.ك) لعام 2020'] = np.where(a7, 'background-color: {}'.format(r), df1['إجمالي المبيعات (د.ك) لعام 2020'])
                df1['إجمالي المبيعات (د.ك) لعام 2020'] = np.where(a8, 'background-color: {}'.format(r), df1['إجمالي المبيعات (د.ك) لعام 2020'])
                
                #3rd comparison (2017-2018)
                df1['قيمة أصـول المباني (د.ك) لعام 2018'] = np.where(b1, 'background-color: {}'.format(r), df1['قيمة أصـول المباني (د.ك) لعام 2018'])
                df1['قيمة أصـول المباني (د.ك) لعام 2018'] = np.where(b2, 'background-color: {}'.format(r), df1['قيمة أصـول المباني (د.ك) لعام 2018'])
                
                df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2018'] = np.where(b3, 'background-color: {}'.format(r), df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2018'])
                df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2018'] = np.where(b4, 'background-color: {}'.format(r), df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2018'])
                
                df1['قيمة أصـول وسائل نقل (د.ك) لعام 2018'] = np.where(b5, 'background-color: {}'.format(r), df1['قيمة أصـول وسائل نقل (د.ك) لعام 2018'])
                df1['قيمة أصـول وسائل نقل (د.ك) لعام 2018'] = np.where(b6, 'background-color: {}'.format(r), df1['قيمة أصـول وسائل نقل (د.ك) لعام 2018'])
                
                df1['قيمة أصـول أخرى (د.ك) لعام 2018'] = np.where(b7, 'background-color: {}'.format(r), df1['قيمة أصـول أخرى (د.ك) لعام 2018'])
                df1['قيمة أصـول أخرى (د.ك) لعام 2018'] = np.where(b8, 'background-color: {}'.format(r), df1['قيمة أصـول أخرى (د.ك) لعام 2018'])
                
                df1['إجمالي قيمة الأصول (د.ك) لعام 2018'] = np.where(b9, 'background-color: {}'.format(r), df1['إجمالي قيمة الأصول (د.ك) لعام 2018'])
                df1['إجمالي قيمة الأصول (د.ك) لعام 2018'] = np.where(b10, 'background-color: {}'.format(r), df1['إجمالي قيمة الأصول (د.ك) لعام 2018'])
                
                #3rd comparison (2018-2019)
                df1['قيمة أصـول المباني (د.ك) لعام 2019'] = np.where(b11, 'background-color: {}'.format(r), df1['قيمة أصـول المباني (د.ك) لعام 2019'])
                df1['قيمة أصـول المباني (د.ك) لعام 2019'] = np.where(b12, 'background-color: {}'.format(r), df1['قيمة أصـول المباني (د.ك) لعام 2019'])
                
                df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2019'] = np.where(b13, 'background-color: {}'.format(r), df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2019'])
                df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2019'] = np.where(b14, 'background-color: {}'.format(r), df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2019'])
                
                df1['قيمة أصـول وسائل نقل (د.ك) لعام 2019'] = np.where(b15, 'background-color: {}'.format(r), df1['قيمة أصـول وسائل نقل (د.ك) لعام 2019'])
                df1['قيمة أصـول وسائل نقل (د.ك) لعام 2019'] = np.where(b16, 'background-color: {}'.format(r), df1['قيمة أصـول وسائل نقل (د.ك) لعام 2019'])
                
                df1['قيمة أصـول أخرى (د.ك) لعام 2019'] = np.where(b17, 'background-color: {}'.format(r), df1['قيمة أصـول أخرى (د.ك) لعام 2019'])
                df1['قيمة أصـول أخرى (د.ك) لعام 2019'] = np.where(b18, 'background-color: {}'.format(r), df1['قيمة أصـول أخرى (د.ك) لعام 2019'])
                
                df1['إجمالي قيمة الأصول (د.ك) لعام 2019'] = np.where(b19, 'background-color: {}'.format(r), df1['إجمالي قيمة الأصول (د.ك) لعام 2019'])
                df1['إجمالي قيمة الأصول (د.ك) لعام 2019'] = np.where(b20, 'background-color: {}'.format(r), df1['إجمالي قيمة الأصول (د.ك) لعام 2019'])
                
                #3rd comparison (2019-2020)
                df1['قيمة أصـول المباني (د.ك) لعام 2020'] = np.where(b21, 'background-color: {}'.format(r), df1['قيمة أصـول المباني (د.ك) لعام 2020'])
                df1['قيمة أصـول المباني (د.ك) لعام 2020'] = np.where(b22, 'background-color: {}'.format(r), df1['قيمة أصـول المباني (د.ك) لعام 2020'])
                
                df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2020'] = np.where(b23, 'background-color: {}'.format(r), df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2020'])
                df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2020'] = np.where(b24, 'background-color: {}'.format(r), df1['قيمة أصـول آلات ومعدات (د.ك) لعام 2020'])
                
                df1['قيمة أصـول وسائل نقل (د.ك) لعام 2020'] = np.where(b25, 'background-color: {}'.format(r), df1['قيمة أصـول وسائل نقل (د.ك) لعام 2020'])
                df1['قيمة أصـول وسائل نقل (د.ك) لعام 2020'] = np.where(b26, 'background-color: {}'.format(r), df1['قيمة أصـول وسائل نقل (د.ك) لعام 2020'])
                
                df1['قيمة أصـول أخرى (د.ك) لعام 2020'] = np.where(b27, 'background-color: {}'.format(r), df1['قيمة أصـول أخرى (د.ك) لعام 2020'])
                df1['قيمة أصـول أخرى (د.ك) لعام 2020'] = np.where(b28, 'background-color: {}'.format(r), df1['قيمة أصـول أخرى (د.ك) لعام 2020'])
                
                df1['إجمالي قيمة الأصول (د.ك) لعام 2020'] = np.where(b29, 'background-color: {}'.format(r), df1['إجمالي قيمة الأصول (د.ك) لعام 2020'])
                df1['إجمالي قيمة الأصول (د.ك) لعام 2020'] = np.where(b30, 'background-color: {}'.format(r), df1['إجمالي قيمة الأصول (د.ك) لعام 2020'])
                
                #4th comparison (2017-2018)
                
                df1['قيمة الإنفاق على المباني (د.ك) لعام 2018'] = np.where(c1, 'background-color: {}'.format(r), df1['قيمة الإنفاق على المباني (د.ك) لعام 2018'])
                df1['قيمة الإنفاق على المباني (د.ك) لعام 2018'] = np.where(c2, 'background-color: {}'.format(r), df1['قيمة الإنفاق على المباني (د.ك) لعام 2018'])
                
                df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2018'] = np.where(c3, 'background-color: {}'.format(r), df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2018'])
                df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2018'] = np.where(c4, 'background-color: {}'.format(r), df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2018'])
                
                df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2018'] = np.where(c5, 'background-color: {}'.format(r), df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2018'])
                df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2018'] = np.where(c6, 'background-color: {}'.format(r), df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2018'])
                
                df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2018'] = np.where(c7, 'background-color: {}'.format(r), df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2018'])
                df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2018'] = np.where(c8, 'background-color: {}'.format(r), df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2018'])
                
                df1['إجمالي قيمة الإنفاق (د.ك) لعام 2018'] = np.where(c9, 'background-color: {}'.format(r), df1['إجمالي قيمة الإنفاق (د.ك) لعام 2018'])
                df1['إجمالي قيمة الإنفاق (د.ك) لعام 2018'] = np.where(c10, 'background-color: {}'.format(r), df1['إجمالي قيمة الإنفاق (د.ك) لعام 2018'])
                #4th comparison (2018-2019)
                df1['قيمة الإنفاق على المباني (د.ك) لعام 2019'] = np.where(c11, 'background-color: {}'.format(r), df1['قيمة الإنفاق على المباني (د.ك) لعام 2019'])
                df1['قيمة الإنفاق على المباني (د.ك) لعام 2019'] = np.where(c12, 'background-color: {}'.format(r), df1['قيمة الإنفاق على المباني (د.ك) لعام 2019'])
                
                df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2019'] = np.where(c13, 'background-color: {}'.format(r), df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2019'])
                df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2019'] = np.where(c14, 'background-color: {}'.format(r), df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2019'])
                
                df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2019'] = np.where(c15, 'background-color: {}'.format(r), df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2019'])
                df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2019'] = np.where(c16, 'background-color: {}'.format(r), df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2019'])
                
                df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2019'] = np.where(c17, 'background-color: {}'.format(r), df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2019'])
                df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2019'] = np.where(c18, 'background-color: {}'.format(r), df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2019'])
                
                df1['إجمالي قيمة الإنفاق (د.ك) لعام 2019'] = np.where(c19, 'background-color: {}'.format(r), df1['إجمالي قيمة الإنفاق (د.ك) لعام 2019'])
                df1['إجمالي قيمة الإنفاق (د.ك) لعام 2019'] = np.where(c20, 'background-color: {}'.format(r), df1['إجمالي قيمة الإنفاق (د.ك) لعام 2019'])   
                #4th comparison (2019-2020)
                df1['قيمة الإنفاق على المباني (د.ك) لعام 2020'] = np.where(c21, 'background-color: {}'.format(r), df1['قيمة الإنفاق على المباني (د.ك) لعام 2020'])
                df1['قيمة الإنفاق على المباني (د.ك) لعام 2020'] = np.where(c22, 'background-color: {}'.format(r), df1['قيمة الإنفاق على المباني (د.ك) لعام 2020'])
                
                df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2020'] = np.where(c23, 'background-color: {}'.format(r), df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2020'])
                df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2020'] = np.where(c24, 'background-color: {}'.format(r), df1['قيمة الإنفاق على الآلات ومعدات (د.ك) لعام 2020'])
                
                df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2020'] = np.where(c25, 'background-color: {}'.format(r), df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2020'])
                df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2020'] = np.where(c26, 'background-color: {}'.format(r), df1['قيمة الإنفاق على وسائل النقل (د.ك) لعام 2020'])
                
                df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2020'] = np.where(c27, 'background-color: {}'.format(r), df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2020'])
                df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2020'] = np.where(c28, 'background-color: {}'.format(r), df1['إنفاقات أخرى لزيادة الإنتاج (د.ك) لعام 2020'])
                
                df1['إجمالي قيمة الإنفاق (د.ك) لعام 2020'] = np.where(c29, 'background-color: {}'.format(r), df1['إجمالي قيمة الإنفاق (د.ك) لعام 2020'])
                df1['إجمالي قيمة الإنفاق (د.ك) لعام 2020'] = np.where(c30, 'background-color: {}'.format(r), df1['إجمالي قيمة الإنفاق (د.ك) لعام 2020'])
                
                #5th comparison (2017-2018)
                
                df1['قيمة استهلاك كهرباء (د.ك) 2018'] = np.where(d1, 'background-color: {}'.format(r), df1['قيمة استهلاك كهرباء (د.ك) 2018'])
                df1['قيمة استهلاك كهرباء (د.ك) 2018'] = np.where(d2, 'background-color: {}'.format(r), df1['قيمة استهلاك كهرباء (د.ك) 2018'])
                
                df1['قيمة استهلاك مياه عذبة (د.ك) 2018'] = np.where(d3, 'background-color: {}'.format(r), df1['قيمة استهلاك مياه عذبة (د.ك) 2018'])
                df1['قيمة استهلاك مياه عذبة (د.ك) 2018'] = np.where(d4, 'background-color: {}'.format(r), df1['قيمة استهلاك مياه عذبة (د.ك) 2018'])
                
                df1['قيمة استهلاك غاز طبيعي (د.ك) 2018'] = np.where(d5, 'background-color: {}'.format(r), df1['قيمة استهلاك غاز طبيعي (د.ك) 2018'])
                df1['قيمة استهلاك غاز طبيعي (د.ك) 2018'] = np.where(d6, 'background-color: {}'.format(r), df1['قيمة استهلاك غاز طبيعي (د.ك) 2018'])
                
                df1['قيمة استهلاك بنزين (د.ك) 2018'] = np.where(d7, 'background-color: {}'.format(r), df1['قيمة استهلاك بنزين (د.ك) 2018'])
                df1['قيمة استهلاك بنزين (د.ك) 2018'] = np.where(d8, 'background-color: {}'.format(r), df1['قيمة استهلاك بنزين (د.ك) 2018'])
                
                df1['قيمة استهلاك ديزل (د.ك) 2018'] = np.where(d9, 'background-color: {}'.format(r), df1['قيمة استهلاك ديزل (د.ك) 2018'])
                df1['قيمة استهلاك ديزل (د.ك) 2018'] = np.where(d10, 'background-color: {}'.format(r), df1['قيمة استهلاك ديزل (د.ك) 2018'])
                
                df1['قيمة استهلاك زيوت وشحوم (د.ك) 2018'] = np.where(d11, 'background-color: {}'.format(r), df1['قيمة استهلاك زيوت وشحوم (د.ك) 2018'])
                df1['قيمة استهلاك زيوت وشحوم (د.ك) 2018'] = np.where(d12, 'background-color: {}'.format(r), df1['قيمة استهلاك زيوت وشحوم (د.ك) 2018'])
                
                df1['قيمة استهلاك منافع أخرى (د.ك) 2018'] = np.where(d13, 'background-color: {}'.format(r), df1['قيمة استهلاك منافع أخرى (د.ك) 2018'])
                df1['قيمة استهلاك منافع أخرى (د.ك) 2018'] = np.where(d14, 'background-color: {}'.format(r), df1['قيمة استهلاك منافع أخرى (د.ك) 2018'])
                
                df1['الإجمالي (د.ك) لعام 2018'] = np.where(d15, 'background-color: {}'.format(r), df1['الإجمالي (د.ك) لعام 2018'])
                df1['الإجمالي (د.ك) لعام 2018'] = np.where(d16, 'background-color: {}'.format(r), df1['الإجمالي (د.ك) لعام 2018'])
                
                df1['قيمة استهلاك كهرباء (د.ك) 2019'] = np.where(d17, 'background-color: {}'.format(r), df1['قيمة استهلاك كهرباء (د.ك) 2019'])
                df1['قيمة استهلاك كهرباء (د.ك) 2019'] = np.where(d18, 'background-color: {}'.format(r), df1['قيمة استهلاك كهرباء (د.ك) 2019'])
                
                df1['قيمة استهلاك مياه عذبة (د.ك) 2019'] = np.where(d19, 'background-color: {}'.format(r), df1['قيمة استهلاك مياه عذبة (د.ك) 2019'])
                df1['قيمة استهلاك مياه عذبة (د.ك) 2019'] = np.where(d20, 'background-color: {}'.format(r), df1['قيمة استهلاك مياه عذبة (د.ك) 2019'])
                
                df1['قيمة استهلاك غاز طبيعي (د.ك) 2019'] = np.where(d21, 'background-color: {}'.format(r), df1['قيمة استهلاك غاز طبيعي (د.ك) 2019'])
                df1['قيمة استهلاك غاز طبيعي (د.ك) 2019'] = np.where(d22, 'background-color: {}'.format(r), df1['قيمة استهلاك غاز طبيعي (د.ك) 2019'])
                
                df1['قيمة استهلاك بنزين (د.ك) 2019'] = np.where(d23, 'background-color: {}'.format(r), df1['قيمة استهلاك بنزين (د.ك) 2019'])
                df1['قيمة استهلاك بنزين (د.ك) 2019'] = np.where(d24, 'background-color: {}'.format(r), df1['قيمة استهلاك بنزين (د.ك) 2019'])
                
                df1['قيمة استهلاك ديزل (د.ك) 2019'] = np.where(d25, 'background-color: {}'.format(r), df1['قيمة استهلاك ديزل (د.ك) 2019'])
                df1['قيمة استهلاك ديزل (د.ك) 2019'] = np.where(d26, 'background-color: {}'.format(r), df1['قيمة استهلاك ديزل (د.ك) 2019'])
                
                df1['قيمة استهلاك زيوت وشحوم (د.ك) 2019'] = np.where(d27, 'background-color: {}'.format(r), df1['قيمة استهلاك زيوت وشحوم (د.ك) 2019'])
                df1['قيمة استهلاك زيوت وشحوم (د.ك) 2019'] = np.where(d28, 'background-color: {}'.format(r), df1['قيمة استهلاك زيوت وشحوم (د.ك) 2019'])
                
                df1['قيمة استهلاك منافع أخرى (د.ك) 2019'] = np.where(d29, 'background-color: {}'.format(r), df1['قيمة استهلاك منافع أخرى (د.ك) 2019'])
                df1['قيمة استهلاك منافع أخرى (د.ك) 2019'] = np.where(d30, 'background-color: {}'.format(r), df1['قيمة استهلاك منافع أخرى (د.ك) 2019'])
                
                df1['الإجمالي (د.ك) لعام 2019'] = np.where(d31, 'background-color: {}'.format(r), df1['الإجمالي (د.ك) لعام 2019'])
                df1['الإجمالي (د.ك) لعام 2019'] = np.where(d32, 'background-color: {}'.format(r), df1['الإجمالي (د.ك) لعام 2019'])
                
                df1['قيمة استهلاك كهرباء (د.ك) 2020'] = np.where(d33, 'background-color: {}'.format(r), df1['قيمة استهلاك كهرباء (د.ك) 2020'])
                df1['قيمة استهلاك كهرباء (د.ك) 2020'] = np.where(d34, 'background-color: {}'.format(r), df1['قيمة استهلاك كهرباء (د.ك) 2020'])
                
                df1['قيمة استهلاك مياه عذبة (د.ك) 2020'] = np.where(d35, 'background-color: {}'.format(r), df1['قيمة استهلاك مياه عذبة (د.ك) 2020'])
                df1['قيمة استهلاك مياه عذبة (د.ك) 2020'] = np.where(d36, 'background-color: {}'.format(r), df1['قيمة استهلاك مياه عذبة (د.ك) 2020'])
                
                df1['قيمة استهلاك غاز طبيعي (د.ك) 2020'] = np.where(d37, 'background-color: {}'.format(r), df1['قيمة استهلاك غاز طبيعي (د.ك) 2020'])
                df1['قيمة استهلاك غاز طبيعي (د.ك) 2020'] = np.where(d38, 'background-color: {}'.format(r), df1['قيمة استهلاك غاز طبيعي (د.ك) 2020'])
                
                df1['قيمة استهلاك بنزين (د.ك) 2020'] = np.where(d39, 'background-color: {}'.format(r), df1['قيمة استهلاك بنزين (د.ك) 2020'])
                df1['قيمة استهلاك بنزين (د.ك) 2020'] = np.where(d40, 'background-color: {}'.format(r), df1['قيمة استهلاك بنزين (د.ك) 2020'])
                
                df1['قيمة استهلاك ديزل (د.ك) 2020'] = np.where(d41, 'background-color: {}'.format(r), df1['قيمة استهلاك ديزل (د.ك) 2020'])
                df1['قيمة استهلاك ديزل (د.ك) 2020'] = np.where(d42, 'background-color: {}'.format(r), df1['قيمة استهلاك ديزل (د.ك) 2020'])
                
                df1['قيمة استهلاك زيوت وشحوم (د.ك) 2020'] = np.where(d43, 'background-color: {}'.format(r), df1['قيمة استهلاك زيوت وشحوم (د.ك) 2020'])
                df1['قيمة استهلاك زيوت وشحوم (د.ك) 2020'] = np.where(d44, 'background-color: {}'.format(r), df1['قيمة استهلاك زيوت وشحوم (د.ك) 2020'])
                
                df1['قيمة استهلاك منافع أخرى (د.ك) 2020'] = np.where(d45, 'background-color: {}'.format(r), df1['قيمة استهلاك منافع أخرى (د.ك) 2020'])
                df1['قيمة استهلاك منافع أخرى (د.ك) 2020'] = np.where(d46, 'background-color: {}'.format(r), df1['قيمة استهلاك منافع أخرى (د.ك) 2020'])
                
                df1['الإجمالي (د.ك) لعام 2020'] = np.where(d47, 'background-color: {}'.format(r), df1['الإجمالي (د.ك) لعام 2020'])
                df1['الإجمالي (د.ك) لعام 2020'] = np.where(d48, 'background-color: {}'.format(r), df1['الإجمالي (د.ك) لعام 2020'])
                
                #6th comparison (2017-2018)
                
                df1['تكاليف المنشأة/ الايجارات (د.ك) 2018'] = np.where(e1, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ الايجارات (د.ك) 2018'])
                df1['تكاليف المنشأة/ الايجارات (د.ك) 2018'] = np.where(e2, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ الايجارات (د.ك) 2018'])
                
                df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2018'] = np.where(e3, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2018'])
                df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2018'] = np.where(e4, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2018'])
                
                df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2018'] = np.where(e5, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2018'])
                df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2018'] = np.where(e6, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2018'])
                
                df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2018'] = np.where(e7, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2018'])
                df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2018'] = np.where(e8, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2018'])
                
                df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2018'] = np.where(e9, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2018'])
                df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2018'] = np.where(e10, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2018'])
                
                df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2018'] = np.where(e11, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2018'])
                df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2018'] = np.where(e12, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2018'])
                
                df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2018'] = np.where(e13, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2018'])
                df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2018'] = np.where(e14, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2018'])
                
                df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2018'] = np.where(e15, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2018'])
                df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2018'] = np.where(e16, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2018'])
                
                df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2018'] = np.where(e17, 'background-color: {}'.format(r), df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2018'])
                df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2018'] = np.where(e18, 'background-color: {}'.format(r), df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2018'])
                
                #6th comparison (2018-2019)
                df1['تكاليف المنشأة/ الايجارات (د.ك) 2019'] = np.where(ea1, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ الايجارات (د.ك) 2019'])
                df1['تكاليف المنشأة/ الايجارات (د.ك) 2019'] = np.where(ea2, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ الايجارات (د.ك) 2019'])
                
                df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2019'] = np.where(ea3, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2019'])
                df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2019'] = np.where(ea4, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2019'])
                
                df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2019'] = np.where(ea5, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2019'])
                df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2019'] = np.where(ea6, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2019'])
                
                df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2019'] = np.where(ea7, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2019'])
                df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2019'] = np.where(ea8, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2019'])
                
                df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2019'] = np.where(ea9, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2019'])
                df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2019'] = np.where(ea10, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2019'])
                
                df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2019'] = np.where(ea11, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2019'])
                df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2019'] = np.where(ea12, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2019'])
                
                df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2019'] = np.where(ea13, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2019'])
                df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2019'] = np.where(ea14, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2019'])
                
                df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2019'] = np.where(ea15, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2019'])
                df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2019'] = np.where(ea16, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2019'])
                
                df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2019'] = np.where(ea17, 'background-color: {}'.format(r), df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2019'])
                df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2019'] = np.where(ea18, 'background-color: {}'.format(r), df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2019'])
                
                #6th comparison (2019-2020)
                df1['تكاليف المنشأة/ الايجارات (د.ك) 2020'] = np.where(eb1, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ الايجارات (د.ك) 2020'])
                df1['تكاليف المنشأة/ الايجارات (د.ك) 2020'] = np.where(eb2, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ الايجارات (د.ك) 2020'])
                
                df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2020'] = np.where(eb3, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2020'])
                df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2020'] = np.where(eb4, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ صيانة وقطع غيار (د.ك) 2020'])
                
                df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2020'] = np.where(eb5, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2020'])
                df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2020'] = np.where(eb6, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تسويق وترويج (د.ك) 2020'])
                
                df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2020'] = np.where(eb7, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2020'])
                df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2020'] = np.where(eb8, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة وطنية (د.ك) 2020'])
                
                df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2020'] = np.where(eb9, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2020'])
                df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2020'] = np.where(eb10, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تدريب عمالة أخرى (د.ك) 2020'])
                
                df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2020'] = np.where(eb11, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2020'])
                df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2020'] = np.where(eb12, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ دراسات وبحوث (د.ك) 2020'])
                
                df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2020'] = np.where(eb13, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2020'])
                df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2020'] = np.where(eb14, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ مصاريف إدارية (د.ك) 2020'])
                
                df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2020'] = np.where(eb15, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2020'])
                df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2020'] = np.where(eb16, 'background-color: {}'.format(r), df1['تكاليف المنشأة/ تكاليف أخرى (د.ك) 2020'])
                
                df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2020'] = np.where(eb17, 'background-color: {}'.format(r), df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2020'])
                df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2020'] = np.where(eb18, 'background-color: {}'.format(r), df1['تكاليف المنشأة/الإجمالي (د.ك) لعام 2020'])
                #7th comparison
                df1['صافي الأرباح السنوية (د.ك) لعام 2017'] = np.where(ma1, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2017'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2017'] = np.where(ma1, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2017'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2017'] = np.where(ma2, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2017'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2017'] = np.where(ma2, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2017'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2017'] = np.where(ma3, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2017'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2017'] = np.where(ma3, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2017'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2017'] = np.where(ma4, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2017'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2017'] = np.where(ma4, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2017'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2017'] = np.where(ma5, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2017'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2017'] = np.where(ma5, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2017'])
                
                df1['صافي الأرباح السنوية (د.ك) لعام 2018'] = np.where(mb1, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2018'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2018'] = np.where(mb1, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2018'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2018'] = np.where(mb2, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2018'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2018'] = np.where(mb2, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2018'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2018'] = np.where(mb3, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2018'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2018'] = np.where(mb3, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2018'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2018'] = np.where(mb4, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2018'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2018'] = np.where(mb4, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2018'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2018'] = np.where(mb5, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2018'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2018'] = np.where(mb5, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2018'])
                
                df1['صافي الأرباح السنوية (د.ك) لعام 2019'] = np.where(mc1, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2019'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2019'] = np.where(mc1, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2019'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2019'] = np.where(mc2, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2019'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2019'] = np.where(mc2, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2019'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2019'] = np.where(mc3, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2019'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2019'] = np.where(mc3, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2019'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2019'] = np.where(mc4, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2019'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2019'] = np.where(mc4, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2019'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2019'] = np.where(mc5, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2019'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2019'] = np.where(mc5, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2019'])
                
                df1['صافي الأرباح السنوية (د.ك) لعام 2020'] = np.where(md1, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2020'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2020'] = np.where(md1, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2020'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2020'] = np.where(md2, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2020'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2020'] = np.where(md2, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2020'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2020'] = np.where(md3, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2020'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2020'] = np.where(md3, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2020'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2020'] = np.where(md4, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2020'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2020'] = np.where(md4, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2020'])
                df1['صافي الأرباح السنوية (د.ك) لعام 2020'] = np.where(md5, 'background-color: {}'.format(r), df1['صافي الأرباح السنوية (د.ك) لعام 2020'])
                df1['صافي الخسائر السنوية (د.ك) لعام 2020'] = np.where(md5, 'background-color: {}'.format(r), df1['صافي الخسائر السنوية (د.ك) لعام 2020'])
                
                
                
                
                return df1
            
            
            
            
            da=df.style.apply(highlight_greater, axis =None)
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
        
        
