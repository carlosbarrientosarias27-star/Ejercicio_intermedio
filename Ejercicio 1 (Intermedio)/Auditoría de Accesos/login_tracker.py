from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict


@dataclass
class LoginAttempt:
    username: str
    timestamp: datetime
    ip_address: str
    success: bool


class LoginTracker:
    def __init__(self):
        # Diccionario: username -> lista de intentos
        self.attempts: Dict[str, List[LoginAttempt]] = {}

    def register_attempt(self, username: str, ip_address: str, success: bool) -> None:
        """
        Registra un intento de login con timestamp automático.
        """
        attempt = LoginAttempt(
            username=username,
            timestamp=datetime.now(),
            ip_address=ip_address,
            success=success
        )

        if username not in self.attempts:
            self.attempts[username] = []

        self.attempts[username].append(attempt)

    def get_user_history(self, username: str) -> List[LoginAttempt]:
        """
        Devuelve el historial completo de intentos de un usuario.
        """
        return self.attempts.get(username, [])

    def get_consecutive_failures(self, username: str) -> int:
        """
        Devuelve la cantidad de intentos fallidos consecutivos
        (contando desde el intento más reciente hacia atrás).
        """
        history = self.attempts.get(username, [])
        count = 0

        for attempt in reversed(history):
            if attempt.success:
                break
            count += 1

        return count

    def has_exceeded_failed_attempts(self, username: str, threshold: int = 3) -> bool:
        """
        Indica si el usuario superó el número permitido de intentos fallidos consecutivos.
        """
        return self.get_consecutive_failures(username) >= threshold 
    

if __name__ == "__main__":
    tracker = LoginTracker()
    print("Módulo funcionando correctamente")
    

    tracker.register_attempt("juan", "192.168.1.10", False)
    tracker.register_attempt("juan", "192.168.1.10", False)
    tracker.register_attempt("juan", "192.168.1.10", True)
    tracker.register_attempt("juan", "192.168.1.11", False)
    tracker.register_attempt("juan", "192.168.1.11", False)
    tracker.register_attempt("juan", "192.168.1.11", False) 

    print("Historial:")
    for attempt in tracker.get_user_history("juan"):
        print(attempt)

    print("\nFallos consecutivos actuales:",
          tracker.get_consecutive_failures("juan"))

    print("¿Superó 3 intentos fallidos?",
          tracker.has_exceeded_failed_attempts("juan", threshold=3))