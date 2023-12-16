# Gửi yêu cầu POST
response = requests.post("https://makequizee.000webhostapp.com/make_exam.php", json={
                                            "data": QuestList  # Gửi chuỗi JSON dưới dạng dữ liệu
                                        })
if response.status_code == 200:
    # Kiểm tra xem response có phải là JSON hay không
    try:
        json_data = response.json()
        # Nếu response là JSON, bạn có thể xử lý dữ liệu JSON ở đây
        print('Dữ liệu JSON:', json_data)
    except ValueError:
        # Nếu response không phải là JSON, bạn có thể xử lý dữ liệu text/plain ở đây
        print('Dữ liệu text/plain:', response.text)
else:
    print('Request thất bại. Mã trạng thái:', response.status_code)