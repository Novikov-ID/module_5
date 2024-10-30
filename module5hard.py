import time


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        password_hash = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                print(f'Пользователь {self.current_user.nickname} вошел в систему')
                return
            else:
                print(f'Неверный логин или пароль')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *new_videos):
        for new_video in new_videos:
            if not any(video.title == new_video.title for video in self.videos):
                self.videos.append(new_video)

    def get_videos(self, keyword):
        found_videos = []
        for video in self.videos:
            if keyword.lower() in video.title.lower():
                found_videos.append(video)
        return found_videos

    def watch_video(self, title):
        if not self.current_user:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for i in range(video.duration):
                    time.sleep(1)
                    j = i + 1
                    print(j, end=' ')
                    video.time_now += 1

                video.time_now = 0
                print('Конец видео')


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other: 'User'):
        return self.nickname == other.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title

    def __eq__(self, other: 'Video'):
        return self.title == other.title


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
