import mysql.connector
import datetime
import time
connection=mysql.connector.connect(host='localhost',
								   port='3306',
								   user='root',
								   password='F74086250',
								   database='HIGHLIGHT_musical_instrument_shop')

cursor=connection.cursor()

cursor.execute('delete from CART;')
cursor.execute('delete from CUSTOMER;')
cursor.execute('delete from PRODUCT;')

P_table={'table_name':['PRODUCT'],'Product_ID':['A01','A02'],'Class':['電吉他','木吉他'],'Brand':['Fender','gibson'],'Product_name':['墨廠 Classic Player Jaguar Special CAR 電吉他','墨廠 Classic Player Jaguar Special CAR 電吉他'],'Price':['25000','30000'],'Stock':['5','8'],'Release_date':['2022-05-01','2022-06-01'],'recommend':['1','0'],'is_used':['0','1'],'state':['New','a little bit dirty'],'audition':['Fender_American_Performer_Telecaster.mp3','Bacchus_-_BJB-1M.mp3']}
for i in range(2):
	P_insert_command=f"insert into {P_table['table_name'][0]} VALUES ('{P_table['Product_ID'][i]}','{P_table['Class'][i]}','{P_table['Brand'][i]}','{P_table['Product_name'][i]}','{P_table['Price'][i]}','{P_table['Stock'][i]}','{P_table['Release_date'][i]}','{P_table['recommend'][i]}','{P_table['is_used'][i]}','{P_table['state'][i]}','{P_table['audition'][i]}');"
	cursor.execute(P_insert_command)

C_table={'table_name':['CUSTOMER'],'Customer_account':['F74086250','F74084737'],'Pwd':['aeiou95048','wx200010'],'Customer_name':['shang','fish'],'Birthday':['2000-07-03','2001-06-28'],'Address':['太子學舍','頂鑫'],'PhoneNo':['0912763795','0975238005'],'CouponPt':['0','0'],'Email':['f74086250@gs.ncku.edu.tw','f74084737@gs.ncku.edu.tw']}
for i in range(2):
	C_insert_command=f"insert into {C_table['table_name'][0]} VALUES ('{C_table['Customer_account'][i]}','{C_table['Pwd'][i]}','{C_table['Customer_name'][i]}','{C_table['Birthday'][i]}','{C_table['Address'][i]}','{C_table['PhoneNo'][i]}','{C_table['CouponPt'][i]}','{C_table['Email'][i]}');"
	cursor.execute(C_insert_command)

# CART_table={'table_name':['CART'],'Customer_account':['F74086250','F74084737'],'Product_id':['A01','A02'],'Amount':['3','5']}
# for i in range(2):
# 	CART_insert_command=f"insert into {CART_table['table_name'][0]} VALUES ('{CART_table['Customer_account'][1]}','{CART_table['Product_id'][i]}','{CART_table['Amount'][i]}');"
# 	cursor.execute(CART_insert_command)

# # 取出該用戶的購物車資料
# Customer_account="F74084737"
# select_from_cart_command=f"select * from cart WHERE Customer_account = '{Customer_account}';"
# cursor.execute(select_from_cart_command)
# cart_list=[]
# records=cursor.fetchall()
# for r in records:
# 	cart_list.append(list(r))
# print(cart_list)

# # 檢查購物車中是否有商品數量超過庫存
# Exceed_Stock = False
# for i in range(len(cart_list)):
# 	Product_id = cart_list[i][1]
# 	Amount = cart_list[i][2]
# 	select_command=f"SELECT STOCK FROM PRODUCT WHERE Product_id = '{Product_id}' "
# 	cursor.execute(select_command)
# 	records=cursor.fetchall()
# 	STOCK=int(list(records[0])[0])
# 	# 若有任一商品超過庫存，則報錯，拒絕訂單成立
# 	if(Amount > STOCK):
# 		Exceed_Stock = True
# 		print(f"編號{Product_id}的商品已超過庫存{STOCK}")
# 		break

# # 若商品數量皆不超過庫存，則代表該訂單可以成立：
# if(Exceed_Stock == False):

# 	Serial_no=0
# 	# 開始插入 Order_info 
# 	loc_dt = datetime.datetime.today() 
# 	loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
# 	OrderNo=Customer_account+"_"+loc_dt_format
# 	Serial_no+=1
# 	cursor.execute(f"select Address from CUSTOMER WHERE Customer_account = '{Customer_account}';")
# 	records=cursor.fetchall()
# 	Address=list(records[0])[0]

# 	Established_date=str(datetime.date.today())
# 	completion_date=str(datetime.date.today())
# 	State="訂單準備中"
# 	PaymentMethod="信用卡"
# 	IsPaid="0"
# 	insert_command='INSERT INTO '+ 'ORDER_INFO'+' VALUES'+f"('{OrderNo}','{Customer_account}','{Address}','{Established_date}','{completion_date}','{State}','{PaymentMethod}','{IsPaid}');"
# 	cursor.execute(insert_command)

# 	# 開始對每件商品插入 ORDER
# 	for i in range(len(cart_list)): #Customer_account,Product_id,Amount
# 		Product_id = cart_list[i][1]
# 		Amount = cart_list[i][2]
# 		Note = "no"
# 		insert_command='INSERT INTO '+'ORDER_OUTLINE'+' VALUES '+f"('{OrderNo}','{Product_id}','{Amount}','{Note}');"
# 		cursor.execute(insert_command)
# 		# 開始更新商品庫存

# 		# 取得目前商品的STOCK
# 		select_command=f"SELECT STOCK FROM PRODUCT WHERE Product_id = '{Product_id}' "
# 		cursor.execute(select_command)
# 		records=cursor.fetchall()
# 		STOCK=int(list(records[0])[0])

# 		# 減少商品庫存
# 		update_command=f"UPDATE PRODUCT SET STOCK = {STOCK-Amount} WHERE Product_ID = '{Product_id}'"
# 		cursor.execute(update_command)

# 	# 清空該用戶的購物車資料
# 	delete_command = f"DELETE FROM CART WHERE Customer_account = '{Customer_account}';"
# 	cursor.execute(delete_command)





















# table_name='ORDER_INFO'
# OrderNo='001'
# Customer_account='F74086250'
# Address='太子學舍536'
# Established_date='2022-05-01'
# completion_date='2022-06-01'
# State='訂單確認中'
# PaymentMethod='信用卡'
# IsPaid='0'
# attribute_list=[]
# cursor.execute("delete from "+table_name+";")
# attribute_list.append(OrderNo)
# attribute_list.append(Customer_account)
# attribute_list.append(Address)
# attribute_list.append(Established_date)
# attribute_list.append(completion_date)
# attribute_list.append(State)
# attribute_list.append(PaymentMethod)
# attribute_list.append(IsPaid)
# insert_command='INSERT INTO '+table_name+' VALUES'+f"('{OrderNo}','{Customer_account}','{Address}','{Established_date}','{completion_date}','{State}','{PaymentMethod}','{IsPaid}');"
# cursor.execute(insert_command)
# attribute_list[0]+="001"
# insert_command1='INSERT INTO '+table_name+' VALUES'+f"('{attribute_list[0]}','{attribute_list[1]}','{attribute_list[2]}','{attribute_list[3]}','{attribute_list[4]}','{attribute_list[5]}','{attribute_list[6]}','{attribute_list[7]}');"
# cursor.execute(insert_command1)
# attribute_list[0]+="001"
# insert_command1='INSERT INTO '+table_name+' VALUES'+f"('{attribute_list[0]}','{attribute_list[1]}','{attribute_list[2]}','{attribute_list[3]}','{attribute_list[4]}','{attribute_list[5]}','{attribute_list[6]}','{attribute_list[7]}');"
# cursor.execute(insert_command1)
# attribute_list[0]+="001"
# insert_command1='INSERT INTO '+table_name+' VALUES'+f"('{attribute_list[0]}','{attribute_list[1]}','{attribute_list[2]}','{attribute_list[3]}','{attribute_list[4]}','{attribute_list[5]}','{attribute_list[6]}','{attribute_list[7]}');"
# cursor.execute(insert_command1)
# attribute_list[0]+="001"
# insert_command1='INSERT INTO '+table_name+' VALUES'+f"('{attribute_list[0]}','{attribute_list[1]}','{attribute_list[2]}','{attribute_list[3]}','{attribute_list[4]}','{attribute_list[5]}','{attribute_list[6]}','{attribute_list[7]}');"
# cursor.execute(insert_command1)

# # select_all="select * from "+table_name
# # cursor.execute(select_all)
# select_command=f"select Customer_account from {table_name} where OrderNo = \'001\';"
# print(select_command)
# cursor.execute(select_command)
# records=cursor.fetchall()
# for r in records:
# 	print(r)

# #delete_command='DELETE FROM '+table_name+' WHERE OrderNo='+f"'{attribute_list[0]}';"
# #print(delete_command)
# # cursor.execute(delete_command)

# updata_command=f"update {table_name}\nset Customer_account=\'F74084737\'\nwhere OrderNo =\'001\';"
# cursor.execute(updata_command)

# product_insert_commamd="insert into product values ('01','電吉他','alpha','電擊他','25000','15','2022-05-01','1','1','良好');"
# print(product_insert_commamd)
# cursor.execute(product_insert_commamd)

# ORDER_OUTLINE='ORDER_OUTLINE'
# OrderNo='001'
# Product_id='01'
# Amount='5'
# Note='小辣不切'
# insert_command='INSERT INTO '+ORDER_OUTLINE+' VALUES '+f"('{OrderNo}','{Product_id}','{Amount}','{Note}');"
# print(insert_command)
# cursor.execute(insert_command)

cursor.close()
connection.commit()
connection.close()