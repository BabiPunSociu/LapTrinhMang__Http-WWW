# Cách comment: ctrl + 1
# --------------------------------------------------------------------------------------

# Học thư viện socket
#import socket



# # Lấy tên máy
# tenMay = socket.gethostname()
# print("Tên máy: %s"%tenMay)

# # Lấy địa chỉ ip
# ip_ = socket.gethostbyname(tenMay)
# print("Địa chỉ ip: %s"%ip_)

# # Lấy tên miền, bí danh và tất cả ip
# infor_ = socket.gethostbyname_ex('www.google.com')
# print("gethostbyname_ex: ",infor_)

# # Lấy dns, bí danh, tất cả ip
# host_addr = socket.gethostbyaddr('74.125.24.91')
# print("Địa chỉ host: ",host_addr)

# # Lấy fully qualified (tên miền đầy đủ)
# # tên miền có dạng hostname.domain.tld
# # ví dụ
# # mail.yahoo.com
# # www.wordpress.org
# fully_qualified = socket.getfqdn("www.google.com")
# print("fully qualified: %s"%fully_qualified)

# # Lấy thông tin đầy đủ từ fully qualified
# a = socket.getaddrinfo("www.google.com", None, 0, socket.SOCK_STREAM)
# #print(*a)

# # in list ip cắt từ a
# ips_ = []
# for x in a:
#     ips_.append(x[-1][0])
# print("Địa chỉ IP:")
# print(*ips_,sep="\n")

# --------------------------------------------------------------------------------------

# Python packet
# • Hai packet thường sử dụng
    # • urllib
    # • requests
# • Request and Response
    # • Client: khởi tạo HTTP section – mở kết nối TCP đến HTTP server và 
    # gửi request
    # • Server: gửi phản hồi

################ Thư viện urllib ################################

# urlopen:
    
# import thư viện
# from urllib.request import urlopen


# Tạo request
# res = urlopen("https://facebook.com")
# print(res)
# Một số thuộc tính và phương thức của đối tượng response
# read() readlines() url status
# # Đọc toàn bộ dưới dạng byte
# a= res.read()
# print(a)

# # Đọc từng dòng
# a = res.readlines()
# print(a[:10])

# # HTTP response status:
# # Các mã return (ví dụ: 200 Success, 404 Not found, ...)
# # Các mã: https://viblo.asia/p/cung-tim-hieu-ve-http-response-status-codes-RnB5p6wdZPG
# print(res.status)

# # URL đầy đủ
# print(res.url)

# • getheaders()
#print(res.getheaders())
# • Xử lý lỗi
# • import urllib.error
# • try ... except urrllib.error.HTTPError as e

###############################################


# Tùy biến request



# 1. Thêm các header vào request trước khi gửi đi
# • Tạo đối tượng request và gửi bằng urlopen()
# • Tạo đối tượng request
# • Thêm các header vào đối tượng request
# • Gửi các đối tượng request bằng urlopen

# # • Ví dụ
# from urllib.request import urlopen
# from urllib.request import Request
# req = Request("http://www.debian.org")
# #Thêm header: 
# req.add_header('accept-language', 'vi')
# #Gửi: 
# response = urlopen(req)
# print(req.header_items())


# Nén/mã hóa:
    # Các chuẩn nén đăng ký với IANA
    # gzip, compress, deflate và identity

# • Header Accept-Encoding
# • Client gửi request yêu cầu nén/mã hóa trong header: Accept-Encoding
# • Server chọn phương pháp nén mà nó hỗ trợ
# • Server nén/mã nội dung message và gửi về cho client
# • Ví dụ:
#     # nén: gzip
# from urllib.request import urlopen
# from urllib.request import Request
# #Tạo request: 
# req = Request("https://facebook.com")
# #Thêm header: 
# req.add_header('Accept-Encoding','gzip')
# #Gửi: 
# response = urlopen(req)
# #Kiểm tra header: 
# print("Kiểu nén:",response.getheader('Content-Encoding'))
# print("Header có nén:",req.header_items())
# print(response.read())
#     # giải nén:
# print("\nGiải nén\n")
# import gzip
# content = gzip.decompress(response.read())
# # content.splitlines()[:5]
# print(content)


###############################################
   # Cookie
