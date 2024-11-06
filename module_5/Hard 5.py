import hashlib
import time


class User:
    def __init__(self, nickname, password, age):

        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
class  UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.curret_user = None

    def log_in(self, nickname, password):
        user = self.users.get(nickname)
        if not user:
            raise ValueError("Пользователь не найден.")
        if user.password != hashlib.sha256(password.encode()).hexdigest():
            raise ValueError("Неверный пароль.")

    def register(self, nickname, password, age):
        if nickname in self.users:
            print("Пользователь с таким ником уже существует.")
        elif nickname not in self.users:
            self.users[nickname] = User(nickname, password, age)
            self.curret_user = nickname
            print(f"Пользователь {nickname} успешно зарегистрирован.")
    def log_out(self, nickname):
        if nickname not in self.users:
            raise ValueError("Пользователь не найден.")
        self.curret_user = None
        print(f"Пользователь {nickname} успешно вышел из системы.")
    def add(self, *other):
        video = self.videos
        for i in other:
            if i.title.lower() not in video:
                self.videos.append(i)
            else:
                print("Видео с таким названием уже есть")


    def get_videos(self, find_word):
        list_video = []
        for i in self.videos:
            if find_word.lower() in i.title.lower():
                list_video.append(i.title)
        return print(f"Список видео по вашему запросу: {list_video}")
    def watch_video(self, nickname, name_video):
        user = self.users.get(nickname)
        if not self.curret_user:
            print("Для просмотра видео войдите в систему")

        else:
            for i in self.videos:
                if name_video == i.title:
                    if i.adult_mode and user.age < 18:
                        print(f"Доступ запрещен, пользователь не достиг совершенолетия")
                        break
                    print(f"Вы смотрите видео: {i.title}")
                    n = i.duration
                    while n > 0:
                        print(" Осталось секунд до конца видео: ", n)
                        n -= 1
                        time.sleep(n)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# # # Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video(None, 'Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video("vasya_pupkin", 'Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('urban_pythonist','Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.curret_user)
#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('urban_pythonist','Лучший язык программирования 2024 года!')