from fastapi import FastAPI, HTTPException
import cv2
import numpy as np
import requests
import uuid

appDet = FastAPI()
@appDet.get("/detect/grade3")
def read_file():
        ###Utworzenie ID
        task_id = str(uuid.uuid4())
        ### wczytywanie zdjecia
        image = cv2.imread("src/peds4.jpg")

        ### Właczenie HOG - narzedzia umożliwiajacego detekcje ludzi
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        ### Algorytm do wykrywania
        (rects, weights) = hog.detectMultiScale(
            image,
            winStride=(6, 6), ### Odpowiada za dokładność, niższa wartość - wieksza dokładność, wolniejsze działanie
            padding=(8, 8), ### Pomaga w wykrywaniu obiektów blisko krawedzi
            scale=1.1 ### Skala zmniejszenia obrazu, im blizej 1 tym dokladniejsze ale wolniejsze
        )
        count = len(rects)
        ### Usuwanie zmiennej, żeby nie zapychac pamieci i zawieszac programu
        del image
        ### Wyswietlanie wyniku
        return {
            "ID: ": task_id,
            "People detected: ": count}
###Url do zdjecia peds2 ?image_url=https://bi.im-g.pl/im/e3/e5/19/z27154403IH,Piesi-korzystajacy-z-telefonow-na-pasach-beda-kara.jpg
### Url do zdjecia peds4 ?image_url=https://i0.wp.com/theedinburghreporter.co.uk/wp-content/uploads/2022/12/image-2.jpg?fit=1200%2C900&ssl=1
@appDet.get("/detect/grade4")
def detect_from_url(image_url: str):
    #Utworzenie ID
    task_id = str(uuid.uuid4())

    #Pozyskiwanie url od użytkownika
    try:
        response = requests.get(image_url, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        raise HTTPException(status_code=400, detail="Failed to download image")

    # Przekształcanie otrzymanego url na plik który może być odczytany przez opencv
    np_arr = np.frombuffer(response.content, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    ### Wywalanie bledu jeśli ktoś przesłał url innego rodzaju niz zdjecie
    if image is None:
        raise HTTPException(status_code=400, detail="Invalid image format")

    ### Użycie hog do detekcji
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    ### Detekcja w taki sam sposób jak w poprzednim przypadku
    rects, weights = hog.detectMultiScale(
        image,
        winStride=(6, 6),
        padding=(8, 8),
        scale=1.1
    )

    count = len(rects)
    ### Usuwanie zmiennej, żeby nie zapychac pamieci i zawieszac programu
    del image
    ###Wynik
    return {
        "ID": task_id,
        "image_url": image_url,
        "people_detected": count
    }