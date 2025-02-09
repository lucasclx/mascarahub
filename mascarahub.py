import cv2
import numpy as np

# Carregar a imagem do mascote
mascote_path = 'mascote.png'
mascote = cv2.imread(mascote_path, cv2.IMREAD_UNCHANGED)

# Verificar se a imagem foi carregada corretamente
if mascote is None:
    print(f"Erro ao carregar a imagem: {mascote_path}")
    exit()

# Ajustar para um tamanho maior
altura_camera, largura_camera = 720, 1280  # Tamanho maior para melhor encaixe da foto
mascote = cv2.resize(mascote, (largura_camera, altura_camera))

# Remover o canal alfa, se presente
if mascote.shape[2] == 4:
    mascote = cv2.cvtColor(mascote, cv2.COLOR_BGRA2BGR)

# Inicializa a câmera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, largura_camera)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, altura_camera)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionar o frame para o tamanho do mascote
    frame = cv2.resize(frame, (largura_camera, altura_camera))

    # Criar uma máscara para identificar a área verde na imagem do mascote (em HSV)
    mascote_hsv = cv2.cvtColor(mascote, cv2.COLOR_BGR2HSV)
    lower_green = np.array([50, 100, 100])  # Limites inferiores para a cor verde
    upper_green = np.array([70, 255, 255])  # Limites superiores para a cor verde
    mascara_verde = cv2.inRange(mascote_hsv, lower_green, upper_green)

    # Aplicar a máscara para manter o frame da câmera apenas na área verde
    frame_mascarado = cv2.bitwise_and(frame, frame, mask=mascara_verde)

    # Inverter a máscara para mostrar a imagem do mascote fora da área verde
    mascara_invertida = cv2.bitwise_not(mascara_verde)
    mascote_somente = cv2.bitwise_and(mascote, mascote, mask=mascara_invertida)

    # Certificar-se de que o número de canais e as dimensões são iguais
    if mascote_somente.shape != frame_mascarado.shape:
        mascote_somente = cv2.resize(mascote_somente, (frame_mascarado.shape[1], frame_mascarado.shape[0]))

    # Combinar o mascote e o frame da câmera
    frame_final = cv2.add(frame_mascarado, mascote_somente)

    # Mostrar o frame final
    cv2.imshow('Mascote com câmera', frame_final)

    # Captura as teclas pressionadas
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Fecha a câmera
        break
    elif key == ord('f'):  # Salva a imagem atual
        cv2.imwrite('foto_mascote_com_camera.png', frame_final)
        print("Foto salva como 'foto_mascote_com_camera.png'")

# Liberar a câmera e fechar as janelas
cap.release()
cv2.destroyAllWindows()
