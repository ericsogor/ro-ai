import pandas as pd

df_test=pd.read_csv('test.csv')

def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = celsius_temp * 9/5 + 32
    return round(fahrenheit_temp, 2)


df_test['temperature_f'] = df_test['temperature_c'].apply(celsius_to_fahrenheit)


submission=pd.DataFrame({
    'SampleID' : df_test['SampleID'],
    'temperature_f': df_test['temperature_f']
})

submission.to_csv('submission.csv',index=False)



