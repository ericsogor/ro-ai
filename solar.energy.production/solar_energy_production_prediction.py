
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
df_train=pd.read_csv('train.csv')
df_test=pd.read_csv('test.csv')

x_train=df_train.drop(columns=['energy_output'])
y_train=df_train['energy_output']

model=RandomForestRegressor(n_estimators=300,
                            random_state=42,
                            n_jobs=-1)
model.fit(x_train,y_train)
y_pred=model.predict(df_test)
print(y_pred)

submission=pd.DataFrame({
    'SampleID': df_test['SampleID'],
    'energy_output' : y_pred.round(2)
})
submission.to_csv('submission.csv', index=False)
