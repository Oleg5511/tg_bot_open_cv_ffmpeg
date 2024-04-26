import cv2

async def face_recognition(file_name: str, path: str) :
    # Загрузка изображения
    image = cv2.imread(f'{path}\{file_name}')
    # преобразуем изображение к оттенкам серого
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # инициализировать распознаватель лиц (каскад Хаара по умолчанию)
    # print(os.path("cascades/haarcascade_frontalface_default.xml"))
    face_cascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

    # обнаружение всех лиц на изображении
    faces = face_cascade.detectMultiScale(image_gray)
    if len(faces) == 0:
        return None

    return len(faces)


