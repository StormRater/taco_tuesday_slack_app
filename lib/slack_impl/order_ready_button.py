from lib.slack_impl.employee_ready_button import EmployeeReadyButton
from lib.slack_impl.ready_button import ReadyButton


class OrderReadyButton(ReadyButton):
    PREFIX = 'OrderSubmit'

    def __init__(self):
        super().__init__(ready_text='Submit', not_ready_text='Submit', prefix=self.PREFIX)

    @staticmethod
    def get_ready():
        return all(EmployeeReadyButton.ReadyEmployees.values())

    @classmethod
    def is_order_button_action_id(cls, action_id: str):
        return action_id == cls._get_action_id(cls.PREFIX)

    @staticmethod
    def get():
        return OrderReadyButton().get_button()

    def get_button(self):
        self.ready = self.get_ready()

        return super().get_button()
