import requests
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from io import BytesIO

# Загрузка изображения
url = 'https://i.pinimg.com/originals/7e/1b/fd/7e1bfd1191112533fe9872ef47398823.jpg'
response = requests.get(url)
img = Image.open(BytesIO(response.content))
# Изменение размера изображения
img = img.resize((200, 200))
# Преобразование изображения в черно-белый
img = img.convert('L')
# Cоздание объекта для рисования на изображении
draw = ImageDraw.Draw(img)
# Создание шрифта
font = ImageFont.truetype('arial.ttf', 20)
# Рисование текста
draw.text((10, 10), 'Милый котик!', font=font, fill='yellow')
# Визуализация изображения
plt.imshow(img, cmap='gray')
plt.show()





