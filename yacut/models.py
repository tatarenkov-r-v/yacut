from datetime import datetime, UTC

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(128), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now(UTC))

    def to_dict(self):
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp,
        )

    # Добавляем в модель метод-десериализатор.
    # На вход метод принимает словарь data, полученный из JSON в запросе.
    def from_dict(self, data):
        # Для каждого поля модели, которое можно заполнить...
        for field in ['original', 'short']:
            # ...выполняется проверка — есть ли ключ с таким же именем в словаре:
            if field in data:
                # Если есть, добавляем значение из словаря
                # в соответствующее поле объекта модели:
                setattr(self, field, data[field])