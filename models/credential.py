from datetime import datetime


class Credential:
    def __init__(self, service: str, username: str, password: str, created_at: str = None):
        self.service = service.strip()
        self.username = username.strip()
        self.password = password
        self.created_at = created_at or self._current_timestamp()

    @staticmethod
    def _current_timestamp() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> dict:
        return {
            "service": self.service,
            "username": self.username,
            "password": self.password,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            service=data.get("service"),
            username=data.get("username"),
            password=data.get("password"),
            created_at=data.get("created_at")
        )

    def __repr__(self) -> str:
        return f"Credential(service='{self.service}', username='{self.username}')"
