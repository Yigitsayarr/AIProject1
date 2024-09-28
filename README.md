El Tabanlı Ses Kontrol Uygulaması
Bu proje, bir kamera aracılığıyla el hareketlerini algılayarak bilgisayarın sesini kontrol etmeye yönelik bir uygulamadır. Uygulama, işaret parmağı ve orta parmak arasındaki mesafeye bakarak sesi açma veya kapama işlevini yerine getirir.

Özellikler
El Tanıma: Mediapipe kütüphanesi kullanılarak gerçek zamanlı el tanıma.
Ses Kontrolü: Parmakların birleşip birleşmediğine göre sesi açma veya kapama.
Kullanıcı Dostu Arayüz: Video akışı penceresi ile kullanıcı etkileşimi.
Gerekli Kütüphaneler
Proje için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

opencv-python
mediapipe
pyautogui

Bu kütüphaneleri yüklemek için terminalde aşağıdaki komutu çalıştırabilirsiniz:
pip install opencv-python mediapipe pyautogui
Kullanım

Uygulamayı başlatmak için aşağıdaki komutu çalıştırın:
python your_script_name.py
Uygulama açıldığında, kameranızın önünde elinizi hareket ettirin.

İşaret parmağınız ve orta parmağınız arasında mesafe 30 pikselden az olduğunda, sesiniz kapatılır veya açılır.

Uygulamadan çıkmak için 'Esc' tuşuna basın.

Kod Açıklaması
detect_hands(frame): Görüntü çerçevesinde elleri algılar ve sonuçları döndürür.
toggle_mute(): Ses durumunu değiştirir.
Ana döngü, video akışını başlatır, el tanıma işlemini gerçekleştirir ve ses kontrolünü yapar.
Gereksinimler
Python 3.x
Bir webcam
Notlar
Ses kontrolü sadece belirli durumlarda çalışır, bu nedenle uygulamayı kullanırken el hareketlerinizi dikkatli bir şekilde yapmalısınız.
Projeyi geliştirirken, daha fazla el hareketi tanıma özelliği eklemeyi düşünebilirsiniz.
