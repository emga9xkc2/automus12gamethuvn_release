<b>1. Bấm chữ Code có nền xanh, phía trên => Download ZIP</b>

<b>2. Giải nén và chạy file setup_python.bat trong thư mục setup. Đợi cài xong khoảng 1 vài phút</b>

<b>3. Chạy file setup_tool.bat trong thư mục setup. Quay lại 1 bước. tìm file AUTO MU SS12 mở nó lên là được</b>

<b>4. Hướng dẫn sử dụng</b>

<b>5. Thông tin phiên bản</b>

- v2.4

  - Fix lỗi bị reset hàng loạt 1 lúc

- v2.3

  - Fix lỗi gom quái, khi bật chức năng gom quái vẫn reset bình thường, chỉ gom quái khi đứng đúng map đã cài auto
  - Sửa thời gian reset, nêú đang trong thời gian x2 master sẽ không reset

- v2.2

  - Thêm auto cộng point khi point sót lớn hơn 1000. Để sử dụng hãy khi thêm dấu + ở phần cài đặt. Ví dụ: -1+ 500+
  - Thêm hack khoảng cách 1 số skill từ 6 lên 8

- v2.1

  - Fix lỗi cộng điểm acc > 65k point

- v2.0

  - Tự nhấn ok khi bị disconnect hoặc khi có thông báo có người vào nhóm
  - Thêm tùy chọn tự động vào map stadium 30p khi bị pk map Dungeon và LostTower, tự sang bãi khác khi bãi định vào đã có > 1 người
  - Sửa lỗi auto buff HP khi đang ở trong thành

- v1.8

  - Thêm tùy chọn tự động vào phó bản exp khi bị pk map Dungeon và LostTower

- v1.6

  - Thêm chế độ auto chỉnh skill để ks, ví dụ map chính cài skill ruby, map thấp (lost7) cài mũi tên băng để ks

  * Để sử dụng chế độ auto trên, bấm Z cài đặt KỸ NĂNG (ô bên trái) là skill ruby, KỸ NĂNG 2 (ô bên phải phía dưới) là skill mũi tên băng, các class khác tương tự.

  - Thêm thông báo phiên bản mới khi có

- v1.5

  - Fix lỗi nhận diện sai tên nhân vật

- v1.3

  - Không phải tích lại auto reset khi tắt tool mở lại
  - Reset lần lượt từng acc, tránh disconnect

- v1.1

  - Quét clone xung quanh để auto pk
  - Bị ngắt kết nối sẽ thông báo về telegram
  - Khi bị pk + bị theo dõi thông báo về telegram
  - Khắc phục lỗi đang reset 1 acc bị ngắt kết nối cả dàn đứng chơi
  - Xóa nick bị ngắt kết nối trên giao diện, khi đăng nhập lại sẽ hiển thị lại
  - Bị pk ở lost7 sẽ tự về lost3 train tiếp, 1 lúc sau quay lại lost7
  - Khi train ở lost3 30s sẽ ở đầu map, 30s sẽ ở giữa map
  - Bị pk 7 lần liên tục ở map Karutan2 sẽ về ngẫu nhiên map bất kỳ đứng chơi
  - Bị pk lần 1. 5 phút quay lại bãi
  - Bị pk lần 2. 20 phút quay lại bãi
  - Bị pk lần 3. 40 phút quay lại bãi
  - Bị pk lần 4. 60 phút quay lại bãi
  - Quá 30 phút không bị pk tính số lần bị pk lại từ đầu

- v1.0

  - Lệnh telegram:
  - Để ra lại bãi, chat: rabai TenNV
  - Để ra lại bãi ở 1 tọa độ mới, chat: rabai TenNV,TenMap,X,Y
