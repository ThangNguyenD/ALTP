def cau_hoi(Question, Answer):
    print(Question)
    Choice= input("Nhập đáp án của bạn: ")
    while Choice not in ['A','B','C','D']:
        print("Câu Trả Lời Không Tồn Tại")
        Choice=input("Nhập Đáp Án Của Bạn: ") 
    if Choice == Answer:
        print("True")
    else:
        print("False")
cau_hoi("""1. Đế quốc đạt tới đỉnh cao về lãnh thổ của nó dưới thời nào?
A. Trajan
B. Nerva
C. Nero
D. Claudius""",'A')

cau_hoi("""2. Cách mạng Pháp bắt đầu từ nănm nào?
A. 1799
B. 1789
C. 1798
D. 1788""",'B')

cau_hoi("""3. Tốc độ ánh sáng là bao nhiêu?
A. ~300.000 km/s 
B. ~299.000 km/s
C. ~399.792 km/s
D. ~292.458 km/s""","A")

cau_hoi("""4. Tên khoa học của chó là gì?
A. Felis catus
B. Canis lupus familiaris
C. Equus caballus
D. Panthera leo""","B")

cau_hoi("""5. Ý nghĩa của từ viết tắt HTTP là gì?
A. Huge Text Transfer Protocol
B. High Tech Transfer Protocol
C. Hyper Text Transfer Protocol
D. Happy Text Transfer Protocol""","C")

cau_hoi("""6. Phi hành gia nào từng đặt chân lên mặt trăng
A. Edward Michael Fincke
B. Andrew Feustel
C. Harrison Hagan Schmitt
D. Oleg Kononenko""","C")

cau_hoi("""7.IPhone đầu tiên được phát hành vào năm nào?
A. 2004
B. 2007
C. 2010
D. 2013""","B")

cau_hoi("""8. Tổ chức nào sau đây không trực thuộc Liên Hợp Quốc
A. UNICEF
B. UNESCO
C. Interpol
D. WHO""","C")

cau_hoi("""9. William Shakespeare đã viết bao nhiêu vở kịch
A. 15
B. 50
C. 20
D. 39 ""","D")

cau_hoi("""10. Đâu là một trong hai người leo lên đỉnh Everest đầu tiên
A. Lino Lacedelli
B. George Everest
C. Achille Compagnoni
D. Edmund Hillary""", "D")