/data/data/com.shark.jizhang/databases/shark_account.db

表名 | 内容
---|---
account_detail | 账单明细
account_book | 账本列表


备忘sql：
```
.headers on
select * from account_detail limit 0,1;
record_id|client_id|server_id|account|year|month|day|week|date|date_s|ctime|remark|auto_tally|db_status|uid|cid|bid
1|aJmiJTnQrw8jAamMvAmcbd|BFek62LzxxEq7fCvAu4SnZ|33.0|2020|08|06|2020-31鍛▅1596725766000|1596725766|1597056349718|娲楀彂姘磡0|
3|Kh3xiqqrfLYCU84R7vMFBo|e102|1
sqlite> select sql from sqlite_master where type="table" and name="account_detail"; 
sql                                                                                 
CREATE TABLE account_detail (                                                       
    record_id  INTEGER PRIMARY KEY AUTOINCREMENT,                                   
    client_id TEXT,                                                                 
    server_id TEXT,                                                                 
    account REAL,                                                                   
    year TEXT,                                                                      
    month TEXT,                                                                     
    day TEXT,                                                                       
    week TEXT,                                                                      
    date INTEGER,                                                                   
    date_s INTEGER,                                                                 
    ctime INTEGER,                                                                  
    remark TEXT,                                                                    
    auto_tally INTEGER,                                                             
    db_status INTEGER,                                                              
    uid TEXT,                                                                       
    cid TEXT,                                                                       
    bid TEXT REFERENCES account_book (book_id) ON DELETE CASCADE,                   
    UNIQUE (                                                                        
        client_id,                                                                  
        server_id,                                                                  
        account,                                                                    
        uid,                                                                        
        cid,                                                                        
        bid                                                                         
    )                                                                               
```

```
POST /record/grant/service/sync/push/data/ HTTP/1.1
User-Agent: Mozilla/5.0 (Linux; Android 5.1.1; VOG-AL10 Build/HUAWEIVOG-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36/com.shark.jizhang/3.25.0
t: bBWCWXN9RzdeCmyghIf5l176095J9rI4RVKgVB0DKJlwaSaL1kpvKu/vd60+o/K3npY6AKLOah3ziaQcNYdE9FiEhQ/xeuCzpk5uFZ5JWsSzqt1NVFRP4AdYBkC6OyoaxAMyYTeXrDlZfE23VmhDlrP0LaN2qeY+Gh5vxcewQiyKg2YTkBaErUL0X2d0HQn5e4eOUNR+0azztTURETtbX+1HewIsyr9AxlvIad7r0WKu32jKAwLAb1WnjpkK8M4rzGPMsyOsWYwdVa/abZlQ4gV3h6QZXl2BUE+HVmjNlvaS3Wr8N5BGm7yYbm50AkA9M+kN2g6Qepw5FBjuV2JpDyc1SXalb4ErKbsCnqEe+uUwzbQ2NWsDL9QpFHUzBsCYBFQENTngfGlUCm2PHD9CFSAB6jPrVvyH1Y3IubGfv5QhVzu9MxihdtzJpx7MYwe5hYeC5QX0LA+HIO7unZsAlg==
Content-Type: application/x-www-form-urlencoded
Content-Length: 1552
Host: api.shayujizhang.com
Connection: close

sign=ec00a0&packageName=com.shark.jizhang&time=1596610233205&languages=zh&appVersionCode=160&deviceType=VOG-AL10&guest_id=fAEThmkcL8NDhX2qaRxdkQ&tally_data=%7B%22create_list%22%3A%5B%7B%22amount%22%3A22.0%2C%22amount_str%22%3A%2222%22%2C%22book_id%22%3A%221%22%2C%22book_name%22%3A%22DefaultTally%22%2C%22category_id%22%3A%22e100%22%2C%22category_name%22%3A%22%E9%A4%90%E9%A5%AE%22%2C%22category_type%22%3A0%2C%22client_id%22%3A%22sNTZM3Rejg7FynoxsykvEd%22%2C%22date%22%3A%222020%E5%B9%B408%E6%9C%8805%E6%97%A5%22%2C%22format_date%22%3A%222020-08-05%22%2C%22icon_name%22%3A%22e_catering%22%2C%22record_id%22%3A958%2C%22remark%22%3A%22test%22%2C%22sort_time%22%3A%222020-08-05%2014%3A43%3A48%22%2C%22uid%22%3A%22Kh3xiqqrfLYCU84R7vMFBo%22%7D%2C%7B%22amount%22%3A33.0%2C%22amount_str%22%3A%2233%22%2C%22book_id%22%3A%221%22%2C%22book_name%22%3A%22DefaultTally%22%2C%22category_id%22%3A%22e100%22%2C%22category_name%22%3A%22%E9%A4%90%E9%A5%AE%22%2C%22category_type%22%3A0%2C%22client_id%22%3A%22PTEPmXkft6mFWq7vHezdVk%22%2C%22date%22%3A%222020%E5%B9%B408%E6%9C%8805%E6%97%A5%22%2C%22format_date%22%3A%222020-08-05%22%2C%22icon_name%22%3A%22e_catering%22%2C%22record_id%22%3A959%2C%22remark%22%3A%22test%22%2C%22sort_time%22%3A%222020-08-05%2014%3A50%3A33%22%2C%22uid%22%3A%22Kh3xiqqrfLYCU84R7vMFBo%22%7D%5D%2C%22del_list%22%3A%5B%5D%2C%22update_list%22%3A%5B%5D%7D&appName=Tally&network=WIFI&androidId=41a48aa84cdc992a&operator=UNKNOWN&appVersion=3.25.0&imei=863064294886926&client=android&uid=Kh3xiqqrfLYCU84R7vMFBo&channel=aliapp&crack=1&deviceVersion=22
```

tally_data url解码：
```
{"create_list":[{"amount":22.0,"amount_str":"22","book_id":"1","book_name":"DefaultTally","category_id":"e100","category_name":"餐饮","category_type":0,"client_id":"sNTZM3Rejg7FynoxsykvEd","date":"2020年08月05日","format_date":"2020-08-05","icon_name":"e_catering","record_id":958,"remark":"test","sort_time":"2020-08-05 14:43:48","uid":"Kh3xiqqrfLYCU84R7vMFBo"},{"amount":33.0,"amount_str":"33","book_id":"1","book_name":"DefaultTally","category_id":"e100","category_name":"餐饮","category_type":0,"client_id":"PTEPmXkft6mFWq7vHezdVk","date":"2020年08月05日","format_date":"2020-08-05","icon_name":"e_catering","record_id":959,"remark":"test","sort_time":"2020-08-05 14:50:33","uid":"Kh3xiqqrfLYCU84R7vMFBo"}],"del_list":[],"update_list":[]}
```