# Importamos las librerías que vamos a utilizar

import requests
import pandas as pd
import json
import seaborn as sns

'''
PARA
    IMPORTAR

    LOS
DATOS

            DE 
        AEMET
'''

# ----------------------------------------------OPCION1----------------------------------------------

# -----------------------SACADO DE LA DOCUMENTACIÓN DE AEMET-----------------------
# url_2019_2023 = "https://opendata.aemet.es/opendata/sh/406a0614"
# querystring = {"<APYKEY>"}
# 
# headers = {
    # 'cache-control': "no-cache"
    # }
# 
# response = requests.request("GET", url_2019_2023, headers=headers, params=querystring)
# 
# print(response.text)

# df5=pd.DataFrame(response.json(requests.get("response")))


# ----------------------------------------------OPCION2----------------------------------------------

# -----------------------LA QUE HE UTILIZADO-----------------------

'''
PARA
        ESTA
    OPCION
            DESDE
                LA 
                        ACCESO GENERAL
        EN
    LA
            WEB
DE 
        AEMET
                CON
        TU APY 
        KEY
            
'''
# -----------------------DATOS RETIRO-----------------------

# response = requests.get("https://opendata.aemet.es/opendata/sh/9a0956fe")
# response2 =requests.get("https://opendata.aemet.es/opendata/sh/9850d26a")
# response3= requests.get("https://opendata.aemet.es/opendata/sh/bd4abe23")
# response4= requests.get("https://opendata.aemet.es/opendata/sh/7d30250e")
# response5= requests.get("https://opendata.aemet.es/opendata/sh/ff886457")
# response6= requests.get("https://opendata.aemet.es/opendata/sh/94548949")
# response7= requests.get("https://opendata.aemet.es/opendata/sh/9473e63b")
# response8= requests.get("https://opendata.aemet.es/opendata/sh/c649ce02")
# response9= requests.get("https://opendata.aemet.es/opendata/sh/07158db3")
# response10=requests.get("https://opendata.aemet.es/opendata/sh/fa53942f")
# response11=requests.get("https://opendata.aemet.es/opendata/sh/53dc5321")
# response12=requests.get("https://opendata.aemet.es/opendata/sh/3991914e")

# data = response.json()
# data2= response2.json()
# data3= response2.json()
# data4= response4.json()
# data5= response5.json()
# data6= response6.json()
# data7= response7.json()
# data8= response8.json()
# data9= response9.json()
# data10=response10.json()
# data11=response11.json()
# data12=response12.json()

# df_1964_1969 = pd.DataFrame(data)
# df_1969_1974 = pd.DataFrame(data2)
# df_1974_1979 = pd.DataFrame(data3)
# df_1979_1984 = pd.DataFrame(data4)
# df_1984_1989 = pd.DataFrame(data5)
# df_1989_1994 = pd.DataFrame(data6)
# df_1994_1999 = pd.DataFrame(data7)
# df_1999_2004 = pd.DataFrame(data8)
# df_2004_2009 = pd.DataFrame(data9)
# df_2009_2014 = pd.DataFrame(data10)
# df_2014_2019 = pd.DataFrame(data11)
# df_2019_2023 = pd.DataFrame(data12)

# -----------------------DATOS AEROPUERTO-----------------------

# response = requests.get("https://opendata.aemet.es/opendata/sh/6cda39a3")
# response2 =requests.get("https://opendata.aemet.es/opendata/sh/607efc85")
# response3= requests.get("https://opendata.aemet.es/opendata/sh/4ca9bdac")
# response4= requests.get("https://opendata.aemet.es/opendata/sh/2fb22c88")
# response5= requests.get("https://opendata.aemet.es/opendata/sh/3cd4c390")
# response6= requests.get("https://opendata.aemet.es/opendata/sh/650f00f8")
# response7= requests.get("https://opendata.aemet.es/opendata/sh/ba5d6132")
# response8= requests.get("https://opendata.aemet.es/opendata/sh/cd7960d9")
# response9= requests.get("https://opendata.aemet.es/opendata/sh/0a5bd63c")
# response10=requests.get("https://opendata.aemet.es/opendata/sh/ee9e1599")
# response11=requests.get("https://opendata.aemet.es/opendata/sh/607c21df")
# response12=requests.get("https://opendata.aemet.es/opendata/sh/f3b12a32")

# data = response.json()
# data2= response2.json()
# data3= response3.json()
# data4= response4.json()
# data5= response5.json()
# data6= response6.json()
# data7= response7.json()
# data8= response8.json()
# data9= response9.json()
# data10=response10.json()
# data11=response11.json()
# data12=response12.json()

# dfaeropuerto_1964_1969 = pd.DataFrame(data)
# dfaeropuerto_1969_1974 = pd.DataFrame(data2)
# dfaeropuerto_1974_1979 = pd.DataFrame(data3)
# dfaeropuerto_1979_1984 = pd.DataFrame(data4)
# dfaeropuerto_1984_1989 = pd.DataFrame(data5)
# dfaeropuerto_1989_1994 = pd.DataFrame(data6)
# dfaeropuerto_1994_1999 = pd.DataFrame(data7)
# dfaeropuerto_1999_2004 = pd.DataFrame(data8)
# dfaeropuerto_2004_2009 = pd.DataFrame(data9)
# dfaeropuerto_2009_2014 = pd.DataFrame(data10)
# dfaeropuerto_2014_2019 = pd.DataFrame(data11)
# dfaeropuerto_2019_2023 = pd.DataFrame(data12)

# -----------------------DATOS NAVACERRADA-----------------------

# response = requests.get("https://opendata.aemet.es/opendata/sh/7b14174e")
# response2 =requests.get("https://opendata.aemet.es/opendata/sh/202ff2cf")
# response3= requests.get("https://opendata.aemet.es/opendata/sh/7b15b941")
# response4= requests.get("https://opendata.aemet.es/opendata/sh/68cefa74")
# response5= requests.get("https://opendata.aemet.es/opendata/sh/c2a644e7")
# response6= requests.get("https://opendata.aemet.es/opendata/sh/409fd673")
# response7= requests.get("https://opendata.aemet.es/opendata/sh/86d0f835")
# response8= requests.get("https://opendata.aemet.es/opendata/sh/3ed17fa8")
# response9= requests.get("https://opendata.aemet.es/opendata/sh/68b5dc08")
# response10=requests.get("https://opendata.aemet.es/opendata/sh/3ab58e5f")
# response11=requests.get("https://opendata.aemet.es/opendata/sh/ddfed2df")
# response12=requests.get("https://opendata.aemet.es/opendata/sh/2a50c4bb")

# data = response.json()
# data2= response2.json()
# data3= response3.json()
# data4= response4.json()
# data5= response5.json()
# data6= response6.json()
# data7= response7.json()
# data8= response8.json()
# data9= response9.json()
# data10=response10.json()
# data11=response11.json()
# data12=response12.json()

# dfsomosierra_1964_1969 = pd.DataFrame(data)
# dfsomosierra_1969_1974 = pd.DataFrame(data2)
# dfsomosierra_1974_1979 = pd.DataFrame(data3)
# dfsomosierra_1979_1984 = pd.DataFrame(data4)
# dfsomosierra_1984_1989 = pd.DataFrame(data5)
# dfsomosierra_1989_1994 = pd.DataFrame(data6)
# dfsomosierra_1994_1999 = pd.DataFrame(data7)
# dfsomosierra_1999_2004 = pd.DataFrame(data8)
# dfsomosierra_2004_2009 = pd.DataFrame(data9)
# dfsomosierra_2009_2014 = pd.DataFrame(data10)
# dfsomosierra_2014_2019 = pd.DataFrame(data11)
# dfsomosierra_2019_2023 = pd.DataFrame(data12)

# ----------------------------------CONCATENAMOS LOS DIFERENTES DATAFRAMES----------------------------------------------
'''
df=pd.concat([df_2019_2023,df_2014_2019,df_2009_2014,df_2004_2009,df_1999_2004,df_1994_1999,df_1989_1994,df_1984_1989,df_1979_1984,df_1974_1979,df_1969_1974,df_1964_1969])
df=pd.concat([df,dfsomosierra_1964_1969,dfsomosierra_1969_1974,dfsomosierra_1974_1979,dfsomosierra_1979_1984,dfsomosierra_1984_1989,dfsomosierra_1989_1994,dfsomosierra_1994_1999,dfsomosierra_1999_2004,dfsomosierra_2004_2009,dfsomosierra_2009_2014,dfsomosierra_2014_2019,dfsomosierra_2019_2023])
'''

# PASAMOS EL DATAFRAME A UN CSV

# df.to_csv('data/temperaturas.csv', index=False)