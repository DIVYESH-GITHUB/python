# Create a Controller class to connect the GUI and the model
from functools import partial
ERROR_MSG = 'ERROR'

class Controller:
    """PyCalc's Controller."""
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate.convert_bits_to_bytes(expression=self._view.getDisplayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.getDisplayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.getDisplayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['bits_to_bytes'].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)



# pyqt code for bits to bytes conversion
