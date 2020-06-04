import pandas as pd 
dataset=pd.read_csv('1_51.csv') 

feature_columns=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39','p40','p41','p42','p43','p44','p45','p46','p47','p48','p49','p50','p51']
              
X=dataset[feature_columns].values
y=dataset['disease'].values
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder() 
y=le.fit_transform(y) 
from sklearn.model_selection import train_test_split 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.04,random_state= 0) 

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier 
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train,y_train) 
y_pred=classifier.predict(X_train) 
accuracy=(metrics.accuracy_score(y_pred,y_train)*100)
print("Accuracy of our model is equal : "+str(round(accuracy,2))+'%.') 

dataset=pd.read_csv('51_101.csv') 
feature_columns=['p51','p52','p53','p54','p55','p56','p57','p58','p59','p60','p61','p62','p63','p64','p65','p66','p67','p68','p69','p70','p71','p72','p73','p74','p75','p76','p77','p78','p79','p80','p81','p82','p83','p84','p85','p86','p87','p88','p89','p90','p91','p92','p93','p94','p95','p96','p97','p98','p99','p100','p101']
              
X=dataset[feature_columns].values
y=dataset['disease'].values
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder() 
y=le.fit_transform(y) 
from sklearn.model_selection import train_test_split 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.04,random_state= 0) 

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier 
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train,y_train) 
y_pred=classifier.predict(X_train) 
accuracy=(metrics.accuracy_score(y_pred,y_train)*100)
print("Accuracy of our model is equal : "+str(round(accuracy,2))+'%.') 


dataset=pd.read_csv('101_201.csv')


feature_columns=['p101','p102','p103','p104','p105','p106','p107','p108','p109','p110','p111','p112','p113','p114','p115','p116','p117','p118','p119','p120','p121','p122','p123','p124','p125','p126','p127','p128','p129','p130','p131','p132','p133','p134','p135','p136','p137','p138','p139','p140','p141','p142','p143','p144','p145','p146','p147','p148','p149','p150','p151','p152','p153','p154','p155','p156','p157','p158','p159','p160','p161','p162','p163','p164','p165','p166','p167','p168','p169','p170','p171','p172','p173','p174','p175','p176','p177','p178','p179','p180','p181','p182','p183','p184','p185','p186','p187','p188','p189','p190','p191','p192','p193','p194','p195','p196','p197','p198','p199','p200','p201']
              
X=dataset[feature_columns].values
y=dataset['disease'].values
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder() 
y=le.fit_transform(y) 
from sklearn.model_selection import train_test_split 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.04,random_state= 0) 

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier 
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train,y_train) 
y_pred=classifier.predict(X_train) 
accuracy=(metrics.accuracy_score(y_pred,y_train)*100)
print("Accuracy of our model is equal : "+str(round(accuracy,2))+'%.') 

dataset=pd.read_csv('201_401.csv')

feature_columns=[ 'p201','p202','p203','p204','p205','p206','p207','p208','p209','p210','p211','p212','p213','p214','p215','p216','p217','p218','p219','p220','p221','p222','p223','p224','p225','p226','p227','p228','p229','p230','p231','p232','p233','p234','p235','p236','p237','p238','p239','p240','p241','p242','p243','p244','p245','p246','p247','p248','p249','p250','p251','p252','p253','p254','p255','p256','p257','p258','p259','p260','p261','p262','p263','p264','p265','p266','p267','p268','p269','p270','p271','p272','p273','p274','p275','p276','p277','p278','p279','p280','p281','p282','p283','p284','p285','p286','p287','p288','p289','p290','p291','p292','p293','p294','p295','p296','p297','p298','p299','p300',
                'p301','p302','p303','p304','p305','p306','p307','p308','p309','p310','p311','p312','p313','p314','p315','p316','p317','p318','p319','p320','p231','p322','p323','p324','p325','p326','p327','p328','p329','p330','p331','p332','p333','p334','p335','p336','p337','p338','p339','p340','p341','p342','p343','p344','p345','p346','p347','p348','p349','p350','p351','p352','p353','p354','p355','p356','p357','p358','p359','p360','p361','p362','p363','p364','p365','p366','p367','p368','p369','p370','p371','p372','p373','p374','p375','p376','p377','p378','p379','p380','p381','p382','p383','p384','p385','p386','p387','p388','p389','p390','p391','p392','p393','p394','p395','p396','p397','p398','p399','p400','p401']
X=dataset[feature_columns].values
y=dataset['disease'].values
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder() 
y=le.fit_transform(y) 
from sklearn.model_selection import train_test_split 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.04,random_state= 0) 

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier 
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train,y_train) 
y_pred=classifier.predict(X_train) 
accuracy=(metrics.accuracy_score(y_pred,y_train)*100)
print("Accuracy of our model is equal : "+str(round(accuracy,2))+'%.') 


