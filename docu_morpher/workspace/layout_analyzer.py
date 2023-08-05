from typing import List, Tuple

class LayoutAnalyzer:
    def __init__(self, layout_data: List[Tuple[float, float, float, float]]):
        self.layout_data = layout_data

    def analyze_layout(self) -> List[Tuple[int, int]]:
        analyzed_layout_data = []
        for layout in self.layout_data:
            x0, y0, x1, y1 = layout
            width = int(x1 - x0)
            height = int(y1 - y0)
            analyzed_layout_data.append((width, height))
        return analyzed_layout_data
