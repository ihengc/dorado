"""
@project:   dorado
@author:    ihc
@description:
"""
from .streams import MessageServer


class Application(MessageServer):

    def __init__(self, app_name, config):
        self.app_name = app_name
        self._config = config
        super().__init__(self._config.HOST, self._config.PORT)

    def start(self):
        self.serve_forever()



if __name__ == '__main__':
    from .config import ProcedureConfig

    app = Application('dorado_v_0_0_1', ProcedureConfig)
    app.serve_forever()
