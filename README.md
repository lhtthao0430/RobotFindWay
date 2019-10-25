# RobotFindWay
*Breadth_Fist_Search(e,s,f,n,m):
e: là ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 0 là có thể di chuyển vào, 1 là có chướng ngại vật.
s: tọa độ điểm xuất phát
f: tọa độ điểm cần đến
n,m: kích thướt ma trận e
Trả về
    + ma trận rỗng" nếu như k tìm được đường
    + ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 1 là ô thuộc đường đi cần tìm. 
*Two_Side_Search(e,s,f,n,m):
e: là ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 0 là có thể di chuyển vào, 1 là có chướng ngại vật.
s: tọa độ điểm xuất phát
f: tọa độ điểm cần đến
n,m: kích thướt ma trận e
Trả về
    + ma trận rỗng" nếu như k tìm được đường
    + ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 1 là ô thuộc đường đi cần tìm. 
*Depth_Fist_Search(e,s,f,n,m):
e: là ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 0 là có thể di chuyển vào, 1 là có chướng ngại vật.
s: tọa độ điểm xuất phát
f: tọa độ điểm cần đến
n,m: kích thướt ma trận e
Trả về
    + ma trận rỗng" nếu như k tìm được đường
    + ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 1 là ô thuộc đường đi cần tìm. 
*K_Place_Search(e,n,m,listPlace,s,f):
e: là ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 0 là có thể di chuyển vào, 1 là có chướng ngại vật.
n,m: kích thướt ma trận e
lishPlace: danh sách cách địa điểm cần đi qua các điểm này khác điểm xuất phát và kết thúc. 
s: tọa độ điểm xuất phát
f: tọa độ điểm cần đến
Trả về
    + ma trận rỗng" nếu như k tìm được đường
    + ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 1 là ô thuộc đường đi cần tìm.
*Moving_Search(e,s,f,n,m):
e: là ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 0 là có thể di chuyển vào, 1 là có chướng ngại vật.
s: tọa độ điểm xuất phát
f: tọa độ điểm cần đến
n,m: kích thướt ma trận e
Trả về
    + ma trận rỗng" nếu như k tìm được đường
    + ma trận (C+1)(N+1)*(M+1) trong đó với mỗi ma trận 0<=i<=C là một ma trận 2 chiều là trạng thái của bước i trong cách đi tốt nhất

