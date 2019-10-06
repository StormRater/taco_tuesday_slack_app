from lib.block.input_block import InputBlock
from lib.domain.label import Label
from lib.domain.taco import Taco


class TacoBlock(InputBlock):
    def __init__(self, taco_type: str, taco: Taco):
        super().__init__(label=self._create_label(taco),
                         initial_value='0',
                         block_id=self.generate_block_id(taco_type),
                         action_id=self.generate_action_id(taco_type))
        self.taco = taco

    @staticmethod
    def _create_label(taco: Taco) -> Label:
        return Label('{} ({})'.format(taco.taco_type, taco.get_price_string())).get_label()

    @staticmethod
    def generate_block_id(taco_type: str) -> str:
        return f'{taco_type}_blockId'

    @staticmethod
    def degenerate_block_id(taco_type: str) -> str:
        return taco_type.replace('_blockId', '')

    @staticmethod
    def generate_action_id(taco_type: str) -> str:
        return f'{taco_type}_actionId'

    @staticmethod
    def degenerate_action_id(action_id: str) -> str:
        return action_id.replace('_actionId', '')

    @staticmethod
    def action_id_to_block_id(action_id: str) -> str:
        return action_id.replace('_actionId', '_blockId')

    @staticmethod
    def block_id_to_action_id(block_id: str) -> str:
        return block_id.replace('_blockId', '_actionId')