from ..DTOs import HistoryDTO, MessageDTO


class HistoryRepository:
    """
    History repository
    """

    def __init__(self):
        self.__history = HistoryDTO(session="", messages=[])

    def get_history(self) -> HistoryDTO:
        """
        Public: get the history dtos
        """
        return self.__history

    def add_message(self, message: MessageDTO):
        """
        Public: add a message to the history
        """
        self.__history.messages.append(message)

    def clear_history(self):
        """
        Public: clear the history
        """
        self.__history = HistoryDTO(session="", messages=[])
