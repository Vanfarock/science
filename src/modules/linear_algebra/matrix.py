from typing import TypeVar

from modules.linear_algebra.errors import (
    InvalidMatrixDataError,
    InvalidMatrixShapeError,
)

T = TypeVar("T")


class Matrix[T]:
    def __init__(
        self,
        rows: int,
        cols: int,
        data: list[list[T | None]] | None = None,
        default_value: T | None = None,
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

    def get(self, i: int, j: int) -> T | None:
        return self.data[i][j]

    def transpose(self) -> "Matrix[T]":
        return Matrix(
            rows=self.cols,
            cols=self.rows,
            data=[[self.get(i, j) for i in range(self.rows)] for j in range(self.cols)],
        )

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
