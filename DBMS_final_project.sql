CREATE DATABASE `HIGHLIGHT_musical_instrument_shop`;
SHOW DATABASES;
USE `HIGHLIGHT_musical_instrument_shop`;
CREATE TABLE PRODUCT
(
	Product_ID VARCHAR(30) NOT NULL,
    Class VARCHAR(20) NOT NULL,
	Brand VARCHAR(50) NOT NULL,
    Product_name VARCHAR(100) NOT NULL,
    Price INTEGER NOT NULL,
    Stock INTEGER NOT NULL,
    Release_date DATE NOT NULL,
    recommend boolean NOT NULL,
    is_used boolean NOT NULL,
    state TEXT NOT NULL,
	PRIMARY KEY (Product_ID)
);
describe product;
CREATE TABLE CUSTOMER
(
	Customer_account VARCHAR(20) NOT NULL,
    Pwd VARCHAR(20) NOT NULL,
	Customer_name VARCHAR(20) NOT NULL,
    Birthday DATE ,
    Address VARCHAR(100) NOT NULL,
    PhoneNo VARCHAR(15) NOT NULL,
    CouponPt INTEGER NOT NULL,
    Email VARCHAR(100),
	PRIMARY KEY (Customer_account)
);

CREATE TABLE ORDER_INFO
(
    OrderNo VARCHAR(100) NOT NULL,
    Customer_account VARCHAR(20) NOT NULL,
    Address VARCHAR(100) NOT NULL,
    Established_date DATE NOT NULL,
    completion_date DATE,
    State VARCHAR(10) NOT NULL,
    PaymentMethod VARCHAR(10) NOT NULL,
    IsPaid BOOLEAN NOT NULL,
    PRIMARY KEY (OrderNO),
    FOREIGN KEY (Customer_account) REFERENCES CUSTOMER(Customer_account) ON DELETE CASCADE
);

CREATE TABLE ORDER_OUTLINE
(
	OrderNo VARCHAR(100) NOT NULL,
    Product_id VARCHAR(30) NOT NULL,
    Amount INTEGER NOT NULL,
    Note VARCHAR(100),
	PRIMARY KEY (OrderNo,Product_ID),
    FOREIGN KEY (OrderNo) REFERENCES ORDER_INFO(OrderNo) ON DELETE CASCADE,
    FOREIGN KEY (Product_id) REFERENCES PRODUCT(Product_id) ON DELETE CASCADE
);


CREATE TABLE EMPLOYEE
(
    Employee_id VARCHAR(15) NOT NULL,
    Name VARCHAR(15) NOT NULL,
    ID_number VARCHAR(15) NOT NULL,
    Gender VARCHAR(1) ,
    Birthday DATE,
    PhoneNo VARCHAR(15),
    Salary INTEGER,
    PRIMARY KEY(Employee_id) 
);

CREATE TABLE CART
(
    Customer_account VARCHAR(20) NOT NULL,
    Product_id VARCHAR(30) NOT NULL,
    Amount INTEGER NOT NULL,
    PRIMARY KEY (Customer_account, Product_id),
    FOREIGN KEY (Customer_account) REFERENCES CUSTOMER(Customer_account) ON DELETE CASCADE,
    FOREIGN KEY (Product_id) REFERENCES PRODUCT(Product_ID) ON DELETE CASCADE
);

DROP table PRODUCT;
DROP table CUSTOMER;
DROP table ORDER_OUTLINE;
DROP table ORDER_INFO;
DROP table EMPLOYEE;
DROP table CART;

LOAD DATA INFILE 'D:/NCKUCSIE/grade3/grade3-2/DatabaseSystem/FinalProject/product.csv' INTO TABLE PRODUCT;

select * from employee;

select * from product;
select * from customer;
select * from cart;


select * from order_info;
select * from order_outline;
ALTER TABLE PRODUCT ADD audition VARCHAR(100);
INSERT INTO product (Product_ID, Class, Brand, Product_name, Price, Stock, Release_date, recommend, is_used, state, audition) VALUES
('A01', '電吉他', 'Fender', '墨廠 Fender Classic Player Jaguar Special CAR 電吉他', 12000, 10, '2022-06-01', 1, 0, '狀況良好1', 'Fender_American_Performer_Telecaster.mp3'),
('G01', '電吉他', 'Fender', 'Fender American Performer Telecaster', 30000, 2, '2022-05-01', 1, 1, 'Fender_American_Performer_Telecaster.mp3', 'Fender_American_Performer_Telecaster.mp3'),
('G02', '電吉他', 'Epiphone', 'Les Paul Standard 50S', 21000, 4, '2022-03-02', 0, 0, '全新', 'Les_Paul_Standard_50S_2.mp3'),
('G03', '木吉他', 'Cort', 'Cort L100F 可插電民謠吉他', 12800, 9, '2022-04-06', 1, 0, '全新', 'CortL100F.mp3'),
('G04', '貝斯', 'Bacchus', 'Bacchus / BJB-1M 日系電貝斯', 12200, 2, '2022-04-26', 0, 1, '全新', 'Bacchus-_BJB-1M.mp3'),
('K01', 'MIDI鍵盤', 'Novation', 'Novation Launchkey 61 MK3 控制鍵盤', 10800, 0, '2021-11-26', 0, 0, '全新', '');
UPDATE product
SET Price=12000
WHERE Product_ID='A01';

UPDATE product
SET state='全琴九成新，線路狀況良好，弦距已有給專業技師調整'
WHERE Product_ID='G01';
INSERT INTO product (Product_ID, Class, Brand, Product_name, Price, Stock, Release_date, recommend, is_used, state, audition) VALUES
('A01', '電吉他', 'Fender', '墨廠 Fender Classic Player Jaguar Special CAR 電吉他', 12000, 10, '2022-06-01', 1, 0, '狀況良好1', 'Fender_American_Performer_Telecaster.mp3'),
('G01', '電吉他', 'Fender', 'Fender American Performer Telecaster', 7500, 10, '2022-05-01', 1, 1, '全琴九成新，線路狀況良好，弦距已有給專業技師調整', 'Fender_American_Performer_Telecaster.mp3'),
('G02', '電吉他', 'Epiphone', 'Les Paul Standard 50S', 21000, 10, '2022-03-02', 0, 0, '全新', 'Les_Paul_Standard_50S_2.mp3'),
('G03', '木吉他', 'Cort', 'Cort L100F 可插電民謠吉他', 12800, 10, '2022-04-06', 1, 0, '全新', 'CortL100F.mp3'),
('G04', '貝斯', 'Bacchus', 'Bacchus / BJB-1M 日系電貝斯', 12200, 10, '2022-04-26', 0, 1, '全新', 'Bacchus-_BJB-1M.mp3'),
('K01', 'MIDI鍵盤', 'Novation', 'Novation Launchkey 61 MK3 控制鍵盤', 10800, 10, '2021-11-26', 0, 0, '全新', '');
update PRODUCT set audition='Cort_L100F.mp3' where Product_ID='G03';

INSERT INTO customer (Customer_account, Pwd, Customer_name, Birthday, Address, PhoneNo, CouponPt, Email) VALUES
('charles', '1234', '竇賢祐', '2000-11-09', '台南市東區大學路1號光復二舍', '1999', 0, 'f74084012@gs.ncku.edu.tw'),
('shang', 'aeiou95048', '莊上緣', '2000-06-03', '台南市東區勝利路太子學舍743', '65304', 0, 'f74086250@gmail.com'),
('wx200010', 'ww2234136', '余紹桓', '2001-02-16', '高雄市三民區鼎大路666號', '1922', 0, 'wx200010@gmail.com');



INSERT INTO employee (Employee_id, Name, ID_number, Gender, Birthday, PhoneNo, Salary) VALUES
('01', '竇賢祐', 'F74084012', 'M', '2000-11-09', '1999', 10000),
('02', '莊上緣', 'F74086250', 'M', '2000-07-03', '65304', 20000),
('03', '余紹桓', 'F74084737', 'M', '2001-02-16', '1922', 300000);



