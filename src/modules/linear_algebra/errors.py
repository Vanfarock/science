class InvalidMatrixShapeError(Exception):
    def __init__(self, rows: int, cols: int) -> None:
        self.message = f"Invalid matrix shape: {rows}x{cols}"
        super().__init__(self.message)


class InvalidMatrixDataError(Exception):
    def __init__(
        self, data_rows: int, data_cols: int, expected_rows: int, expected_cols: int
    ) -> None:
        self.message = f"Invalid matrix data: {data_rows}x{data_cols} (expected {expected_rows}x{expected_cols})"
        super().__init__(self.message)
