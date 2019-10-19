*Breadth_Fist_Search(e,s,f,n,m):
e: là ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 0 là có thể di chuyển vào, 1 là có chướng ngại vật.
s: tọa độ điểm xuất phát
f: tọa độ điểm cần đến
n,m: kích thướt ma trận e
Trả về
    +"Can't find the way" nếu như k tìm được đường
    + ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 1 là ô thuộc đường đi cần tìm. 
Ý tưởng: Bắt đầu từ điểm xuất phát và lần lượt nhìn các điểm kề với điểm gốc. Sau đó, với điểm đỉnh trong số đó, thuật toán lại lần lượt nhìn trước các điểm kề với nó mà chưa được quan sát trước đó và lặp lại cho tới khi tìm được điểm đến. 
Thuật toán:
    B1:Chèn điểm xuất vào hàng đợi (đang hướng tới)
    B2:Lấy ra điểm đầu tiên trong hàng đợi và quan sát nó
        Nếu điểm này chính là điểm đích, dừng quá trình tìm kiếm và trả về kết quả.
        Nếu không phải thì chèn tất cả các điểm kề với điểm vừa thăm và có thể đi được nhưng chưa được quan sát trước đó vào hàng đợi.
    B3:Nếu hàng đợi là rỗng, thì tất cả các điểm có thể đến được đều đã được quan sát – dừng việc tìm kiếm và trả về "không thấy".
    B4:Nếu hàng đợi không rỗng thì quay về bước 2.
Đô phức tạp: O(N*M)
*Two_Side_Search(e,s,f,n,m):
e: là ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 0 là có thể di chuyển vào, 1 là có chướng ngại vật.
s: tọa độ điểm xuất phát
f: tọa độ điểm cần đến
n,m: kích thướt ma trận e
Trả về
    +"Can't find the way" nếu như k tìm được đường
    + ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 1 là ô thuộc đường đi cần tìm. 
Ý tưởng: Bắt đầu từ điểm xuất phát và điểm đến lần lượt nhìn các điểm kề với chúng . Sau đó, với điểm đỉnh trong số đó, thuật toán lại lần lượt nhìn trước các điểm kề với nó mà chưa được quan sát trước đó và lặp lại cho tới khi tìm được đường đi từ 2 điểm gặp nhau.
Thuật toán:
    B1:Chèn điểm xuất phát và kết thúc vào hàng đợi.
    B2:Lấy ra điểm đầu tiên trong hàng đợi và quan sát nó.Chèn tất cả các điểm kề với điểm vừa thăm và có thể đi được nhưng chưa được quan sát trước đó vào hàng đợi.
        Nếu có điểm kề với nó nhưng đi từ điểm bắt đầu khác nó ta trả về con đường.
    B3:Nếu hàng đợi là rỗng, thì tất cả các điểm có thể đến được đều đã được quan sát – dừng việc tìm kiếm và trả về "không thấy".
    B4:Nếu hàng đợi không rỗng thì quay về bước 2.
Đô phức tạp: O(N*M)
*Depth_Fist_Search(e,s,f,n,m):
e: là ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 0 là có thể di chuyển vào, 1 là có chướng ngại vật.
s: tọa độ điểm xuất phát
f: tọa độ điểm cần đến
n,m: kích thướt ma trận e
Trả về
    +"Can't find the way" nếu như k tìm được đường
    + ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 1 là ô thuộc đường đi cần tìm. 
Ý tưởng: khởi đầu tại điểm xuất phát và phát triển xa nhất có thể theo mỗi nhánh. Quá trình tìm kiếm được phát triển tới điểm đến cần tìm hoặc tới một nút không có con. Khi đó giải thuật quay lui về đỉnh vừa mới tìm kiếm ở bước trước.
Thuật toán:
    B1: Đẩy điểm xuất phát vào ngăn xếp
    B2: Xét điểm u cuối cùng trong hàng đợi và quan sát nó
        Nếu điểm này chính là điểm đích hoặc không tồn tại điểm v kề với u có thể đi được và v chưa thăm hoặc chi phí đến v lớn hơn chi phí đến u + 1 thì xóa điểm u khỏi ngăn xếp.
        Nếu tồn tại điểm v kề với u có thể đi được và v chưa thăm hoặc chi phí đến v lớn hơn chi phí đến u + 1
        ta gán chi phí v là chi phí u +1 và đẩy v vào cuối hàng đợi và chuyển đến bước 3.
    B3: Nếu ngăn xếp không rổng chuyển đến bước 2.\
    B4: Nếu điểm đến chưa xét ta trả "không tìm được" ngược lại trả về đường từ điểm xuất phát đến điểm đích.
Độ phức tạp: O((N*M)^2)
*K_Place_Search(e,n,m,listPlace,s,f):
e: là ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 0 là có thể di chuyển vào, 1 là có chướng ngại vật.
n,m: kích thướt ma trận e
lishPlace: danh sách cách địa điểm cần đi qua các điểm này khác điểm xuất phát và kết thúc. 
s: tọa độ điểm xuất phát
f: tọa độ điểm cần đến
Trả về
    +"Can't find the way" nếu như k tìm được đường
    + ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 1 là ô thuộc đường đi cần tìm.
Ý tưởng: Bắt đầu từ điểm xuất phát và lần lượt nhìn các điểm kề với điểm gốc. Sau đó, với điểm đỉnh trong số đó, thuật toán lại lần lượt nhìn trước các điểm kề với nó mà chưa được quan sát trước đó và lặp lại cho tới khi tìm được điểm đến. 
Thuật toán:
    B1:Chèn điểm xuất vào hàng đợi (đang hướng tới)
    B2:Lấy ra điểm đầu tiên trong hàng đợi và quan sát nó
        Nếu điểm này chính là điểm đích và đi qua các điểm cần đến, dừng quá trình tìm kiếm và trả về kết quả.
        Nếu không phải thì chèn tất cả các điểm kề với điểm vừa thăm và có thể đi được nhưng chưa được quan sát trước đó vào hàng đợi. 
            Nếu điểm đó là điểm cần đi qua thì đánh dấu trạng thái đã đi qua điểm đó.
    B3:Nếu hàng đợi là rỗng, thì tất cả các điểm có thể đến được đều đã được quan sát – dừng việc tìm kiếm và trả về "không thấy".
    B4:Nếu hàng đợi không rỗng thì quay về bước 2.
Đô phức tạp: O(N*M*2^K)
*Moving_Search(e,s,f,n,m):
e: là ma trận (N+1)*(M+1) chứa 0 và 1 trong đó 0 là có thể di chuyển vào, 1 là có chướng ngại vật.
s: tọa độ điểm xuất phát
f: tọa độ điểm cần đến
n,m: kích thướt ma trận e
Trả về
    +"Can't find the way" nếu như k tìm được đường
    + ma trận (C+1)(N+1)*(M+1) trong đó với mỗi ma trận 0<=i<=C là một ma trận 2 chiều là trạng thái của bước i trong cách đi tốt nhất
Ý tưởng: Bắt đầu từ điểm xuất phát và lần lượt nhìn các điểm kề với điểm gốc. Sau đó, với điểm đỉnh trong số đó, thuật toán lại lần lượt nhìn trước các điểm kề với nó mà chưa được quan sát trước đó và lặp lại cho tới khi tìm được điểm đến. 
Thuật toán:
    B1:Chèn điểm xuất vào hàng đợi (đang hướng tới)
    B2:Lấy ra điểm đầu tiên trong hàng đợi và quan sát nó
        Nếu điểm này chính là điểm đích, dừng quá trình tìm kiếm và trả về kết quả.
        Nếu không phải thì chèn tất cả các điểm kề với điểm vừa thăm và có thể đi được nhưng chưa được quan sát trước đó vào hàng đợi.
    B3:Nếu hàng đợi là rỗng, thì tất cả các điểm có thể đến được đều đã được quan sát – dừng việc tìm kiếm và trả về "không thấy".
    B4:Nếu hàng đợi không rỗng thì quay về bước 2.
Đô phức tạp: O(N*M*2)
