import cv2
import mediapipe as mp
import pyautogui
import time

# Mediapipe el tanıma için gerekli ayarlar
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# El tanıma fonksiyonu
def detect_hands(frame):
    hands = mp_hands.Hands(min_detection_confidence=0.7)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    return results

# Ses kontrol fonksiyonu
def toggle_mute():
    pyautogui.press('volumemute')

# Video akışını başlat
cap = cv2.VideoCapture(0)

# Önceki durum
prev_mute_state = False

# Başlangıç zamanı
start_time = time.time()
timeout_duration = 15  # 15 saniye

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Kamera açılmadı.")
        break

    # El tanıma
    results = detect_hands(frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # İşaret parmağı ve orta parmak koordinatlarını al
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Koordinatları al
            x1, y1 = int(index_finger_tip.x * frame.shape[1]), int(index_finger_tip.y * frame.shape[0])
            x2, y2 = int(middle_finger_tip.x * frame.shape[1]), int(middle_finger_tip.y * frame.shape[0])

            # Parmakların birleşip birleşmediğini kontrol et
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            if distance < 30:  # Parmağın birleştiğini anlamak için eşik değeri
                current_mute_state = True
            else:
                current_mute_state = False

            # Ses durumu değişikliği
            if current_mute_state and not prev_mute_state:
                toggle_mute()
                print("Ses kapatıldı.")
            prev_mute_state = current_mute_state

            # Elin üzerindeki noktaları çiz
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Görüntüyü göster
    cv2.imshow("Kamera", frame)

    
    
    if cv2.waitKey(5) & 0xFF == 27:  # 'Esc' tuşuna basarak çıkış
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
