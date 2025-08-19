from modules.linear_algebra.errors import (
    InvalidMatrixDataError,
    InvalidMatrixShapeError,
)


class Matrix:
    def __init__(
        self,
        rows: int,
        cols: int,
        data: list[list[float]] | None = None,
        default_value: float = 0.0,
    ) -> None:
        if rows <= 0 or cols <= 0:
            raise InvalidMatrixShapeError(rows, cols)

        if data is not None:
            if (
                len(data) == 0
                or len(data) != rows
                or any(len(row) != cols for row in data)
            ):
                raise InvalidMatrixDataError(
                    data_rows=len(data),
                    data_cols=len(data[0]) if data else 0,
                    expected_rows=rows,
                    expected_cols=cols,
                )

        self.rows = rows
        self.cols = cols
        self.data = data or [[default_value] * cols for _ in range(rows)]

    def get(self, i: int, j: int) -> float:
        return self.data[i][j]

    def set(self, i: int, j: int, value: float) -> None:
        self.data[i][j] = value

    def transpose(self) -> "Matrix":
        return Matrix(
            rows=self.cols,
            cols=self.rows,
            data=[[self.get(i, j) for i in range(self.rows)] for j in range(self.cols)],
        )

    def multiply(self, other: "Matrix") -> "Matrix":
        if self.cols != other.rows:
            raise InvalidMatrixShapeError(self.rows, other.cols)

        result = Matrix(self.rows, other.cols, default_value=0.0)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.set(
                        i, j, result.get(i, j) + self.get(i, k) * other.get(k, j)
                    )
        return result

    def __str__(self) -> str:
        transposed = self.transpose()
        column_widths = [
            max([len(str(transposed.get(i, j))) for j in range(transposed.cols)])
            for i in range(transposed.rows)
        ]

        result_str = ""
        for i in range(self.rows):
            row_str: list[str] = []
            for j in range(self.cols):
                value = self.get(i, j)
                row_str.append(str(value) + " " * (column_widths[j] - len(str(value))))
            result_str += "| " + " | ".join(row_str) + " |\n"
        return result_str
